from support import APITestCase


class BatchAnalysisTests(APITestCase):
    def test_batch_results_are_saved_in_history_and_stats(self):
        texts = ["I struggle with Python loops", "Python functions confuse me"]
        response = self.client.post("/analyze/batch", json={"feedbacks": texts})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["total"], 2)
        self.assertEqual([row["sentiment"] for row in response.json()["results"]],
                         ["NEGATIVE", "NEGATIVE"])
        history = self.client.get("/history").json()
        self.assertEqual(history["total"], 2)
        self.assertCountEqual([row["feedback"] for row in history["history"]], texts)
        self.assertEqual(self.client.get("/stats").json()["total_analyses"], 2)

    def test_invalid_entries_do_not_run_inference_or_write_history(self):
        response = self.client.post("/analyze/batch", json={
            "feedbacks": ["   ", "bad", "  I struggle with Python  "],
        })
        results = response.json()["results"]
        self.assertEqual(results[0], {"index": 0, "error": "Empty feedback"})
        self.assertIn("too short", results[1]["error"])
        self.assertEqual(results[2]["index"], 2)
        self.assertEqual(self.detect.call_count, 1)
        history = self.client.get("/history").json()
        self.assertEqual(history["total"], 1)
        self.assertEqual(history["history"][0]["feedback"], "I struggle with Python")

    def test_one_failed_analysis_does_not_discard_later_successes(self):
        self.detect.side_effect = [RuntimeError("Synthetic inference failure"), self.gap_result]
        response = self.client.post("/analyze/batch", json={
            "feedbacks": ["First synthetic feedback", "Second synthetic feedback"],
        })
        results = response.json()["results"]
        self.assertIn("error", results[0])
        self.assertNotIn("error", results[1])
        self.assertEqual(self.client.get("/history").json()["total"], 1)

    def test_preview_is_truncated_but_full_feedback_is_saved(self):
        text = "Python loops " * 12
        response = self.client.post("/analyze/batch", json={"feedbacks": [text]})
        self.assertEqual(response.json()["results"][0]["text"], text.strip()[:100] + "...")
        self.assertEqual(self.client.get("/history").json()["history"][0]["feedback"], text.strip())

    def test_existing_batch_limits_and_single_analysis_still_work(self):
        for feedbacks in [[], ["Valid feedback"] * 51]:
            with self.subTest(size=len(feedbacks)):
                self.assertEqual(self.client.post("/analyze/batch", json={"feedbacks": feedbacks}).status_code, 400)
        response = self.client.post("/analyze", json={"text": "I struggle with Python"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.client.get("/history").json()["total"], 1)
