from support import APITestCase


class LearningProgressTests(APITestCase):
    def progress(self):
        response = self.client.get("/progress")
        self.assertEqual(response.status_code, 200)
        return {row["skill"]: row for row in response.json()["progress"]}

    def test_later_strength_counts_as_an_improvement(self):
        self.save_analysis(skill_gaps="Python", gap_severity="medium", sentiment="NEGATIVE")
        self.save_analysis(strengths="Python", gap_severity="low", sentiment="POSITIVE")
        python = self.progress()["Python"]
        self.assertEqual(python["attempts"], 2)
        self.assertEqual(python["severity_history"], ["medium", "low"])
        self.assertEqual(python["sentiment_history"], ["NEGATIVE", "POSITIVE"])
        self.assertEqual(python["progress_percentage"], 90)
        self.assertEqual(python["improvement"], 30)
        self.assertEqual(python["status"], "Improving")

    def test_strength_only_history_is_not_missing(self):
        self.save_analysis(strengths="SQL", gap_severity="low", sentiment="POSITIVE")
        sql = self.progress()["SQL"]
        self.assertEqual(sql["attempts"], 1)
        self.assertEqual(sql["latest_severity"], "low")
        self.assertEqual(sql["status"], "Stable")

    def test_possible_gap_is_a_medium_observation(self):
        self.save_analysis(possible_gaps="Python", gap_severity="low", sentiment="NEUTRAL")
        python = self.progress()["Python"]
        self.assertEqual(python["latest_severity"], "medium")
        self.assertEqual(python["progress_percentage"], 60)

    def test_confirmed_gap_scoring_is_preserved(self):
        self.save_analysis(skill_gaps="Python", gap_severity="high", sentiment="NEGATIVE")
        self.save_analysis(skill_gaps="Python", gap_severity="medium", sentiment="NEGATIVE")
        python = self.progress()["Python"]
        self.assertEqual(python["severity_history"], ["high", "medium"])
        self.assertEqual(python["improvement"], 30)

    def test_each_skill_is_counted_once_per_feedback_with_gap_precedence(self):
        self.save_analysis(skill_gaps="Python, Python", possible_gaps="Python, SQL",
                           strengths="Python, SQL", gap_severity="high", sentiment="NEGATIVE")
        rows = self.progress()
        self.assertEqual(rows["Python"]["attempts"], 1)
        self.assertEqual(rows["Python"]["latest_severity"], "high")
        self.assertEqual(rows["SQL"]["attempts"], 1)
        self.assertEqual(rows["SQL"]["latest_severity"], "medium")

    def test_unrelated_strength_does_not_improve_another_skill(self):
        self.save_analysis(skill_gaps="Python", gap_severity="high", sentiment="NEGATIVE")
        self.save_analysis(strengths="SQL", gap_severity="low", sentiment="POSITIVE")
        rows = self.progress()
        self.assertEqual(rows["Python"]["improvement"], 0)
        self.assertEqual(rows["Python"]["attempts"], 1)
        self.assertEqual(rows["SQL"]["latest_severity"], "low")

    def test_empty_skill_fields_do_not_create_phantom_skills(self):
        self.save_analysis(skill_gaps=" , ", possible_gaps=None, strengths="", gap_severity="low")
        self.assertEqual(self.progress(), {})

    def test_another_skills_high_severity_does_not_override_a_strength(self):
        self.save_analysis(skill_gaps="Python", strengths="SQL", gap_severity="high", sentiment="NEGATIVE")
        rows = self.progress()
        self.assertEqual(rows["Python"]["latest_severity"], "high")
        self.assertEqual(rows["SQL"]["latest_severity"], "low")
