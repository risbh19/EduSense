# EduSense

## NLP-Based Adaptive Learning Path Recommendation System

EduSense is an academic prototype that turns written student feedback into sentiment results, identified Computer Science skills, skill-gap categories and ranked learning resources. A React interface presents the results, saved analysis history and a severity-based progress view.

The recommendations adapt to the topics and sentiment found in the feedback. The displayed learning path uses four fixed study stages; it does not generate a prerequisite graph or a personalised timetable.

## How it works

```text
Student feedback
    |
    +--> DistilBERT sentiment prediction
    +--> spaCy keyword and topic extraction
             |
             v
    Skill matching against the 18-skill catalogue
             |
             v
    Confirmed gaps / possible gaps / strengths
             |
             v
    MiniLM embeddings + cosine similarity of resource titles
             |
             v
    Ranked resources + learning summary + frontend study stages
```

1. **Sentiment:** `distilbert-base-uncased-finetuned-sst-2-english` predicts positive or negative sentiment. The backend rounds confidence to four decimal places and relabels predictions below `0.65` as `NEUTRAL`. Sentiment inference uses the first 512 characters.
2. **Topics:** spaCy `en_core_web_sm` extracts nouns, proper nouns and noun chunks. Skills are matched through direct keyword/phrase matching with plural support, followed by a fallback that requires at least two keyword hits from the extracted terms.
3. **Skill gaps:** every matched skill receives the sentiment of the whole feedback.

| Sentiment | Skill category |
| --- | --- |
| `NEGATIVE` | Confirmed skill gap |
| `NEUTRAL` | Possible gap |
| `POSITIVE` | Strength |

Overall severity is `high` for at least three confirmed gaps, `medium` for one or two confirmed gaps, and `low` when there are none.

4. **Recommendations:** Sentence-Transformers `all-MiniLM-L6-v2` embeds the feedback and each resource title. Cosine similarity ranks the four resources configured for each selected skill. Resources for strengths are returned in `strengths_feedback`.
5. **Learning path:** when confirmed gaps exist, the frontend displays Understand the Basics, Learn Through Videos, Read & Revise, and Practice Problems, with the identified focus skills.

## Features and technology

- Dashboard, Analyze Feedback, Learning Progress and History views, with light/dark themes.
- Single-feedback analysis with SQLite persistence.
- Batch feedback analysis for up to 50 items per request; batch results are returned without saving them.
- Sentiment confidence, confirmed gaps, possible gaps, strengths and resource links.
- Saved feedback history with expandable analysis details.
- Dashboard statistics and progress indicators derived from stored analyses.
- Curated catalogue of 18 Computer Science skills and 72 resources.

| Layer | Technology |
| --- | --- |
| Backend | Python, FastAPI, Uvicorn |
| Storage | SQLAlchemy and SQLite |
| Sentiment | Hugging Face Transformers and DistilBERT |
| Topic extraction | spaCy and configured keywords |
| Resource ranking | Sentence-Transformers and MiniLM |
| Frontend | React 19, Vite 8 and axios |
| Evaluation | Jupyter/Kaggle notebook, Coursera reviews, VADER and TextBlob |

## Project structure

```text
EduSense/
|-- Readme.md
|-- backend/
|   |-- main.py                 # API routes and persistence workflow
|   |-- database.py             # Engine, sessions and declarative base
|   |-- models.py               # FeedbackAnalysis table
|   |-- sentiment.py            # DistilBERT inference
|   |-- topic_extractor.py      # spaCy extraction and skill matching
|   |-- skill_gap.py            # Gap categories and severity
|   |-- recommender.py          # Resource-title similarity ranking
|   |-- skills_db.py            # Skills, keywords and resource links
|   `-- requirements.txt
|-- frontend/
|   |-- package.json
|   |-- package-lock.json
|   |-- vite.config.js
|   `-- src/
|       |-- App.jsx
|       |-- App.css
|       `-- components/
|           |-- FeedbackInput.jsx
|           |-- ResultCard.jsx
|           |-- SkillGapCard.jsx
|           |-- RecommendationList.jsx
|           |-- LearningPath.jsx
|           `-- History.jsx
`-- notebook/
    `-- edusense-nlp-skill-gap-detection.ipynb
```

The database and raw evaluation CSV are not included in the current GitHub source tree. The backend creates `edusense.db` and its table when it starts. Its relative database path is resolved from the directory where the backend is launched.

## Local setup

Use Python 3.10 or 3.11 for the pinned backend packages. The locked Vite package requires Node.js `^20.19.0 || >=22.12.0`; Node.js 22.12 or later satisfies this requirement. Model downloads and package installation require an internet connection.

### 1. Clone the repository

```bash
git clone https://github.com/risbh19/EduSense.git
cd EduSense
```

### 2. Set up the backend

From the repository root:

```bash
cd backend
python -m venv .venv
```

Activate the environment using the command for your shell:

```powershell
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
```

```bash
# macOS or Linux
source .venv/bin/activate
```

Install the dependencies and the spaCy model:

```bash
python -m pip install -r requirements.txt
python -m pip install sqlalchemy==2.0.29
python -m spacy download en_core_web_sm
```

SQLAlchemy is imported by the application but is currently missing from `backend/requirements.txt`, so the separate installation command above is required.

Start the server **from inside the `backend` directory**:

```bash
python main.py
```

- API: http://localhost:8000
- Interactive API documentation: http://localhost:8000/docs

DistilBERT and MiniLM load lazily on their first use. The initial analysis may take longer while downloading and loading their weights. The root endpoint confirms that the API is reachable; it is not a model-readiness check.

### 3. Set up the frontend

Open another terminal and, from the repository root, run:

```bash
cd frontend
npm ci
npm run dev
```

Open the address printed by Vite, normally http://localhost:5173. The frontend calls the API at the fixed address `http://localhost:8000`, so keep the backend running on port 8000.

## API endpoints

| Method | Path | Behaviour |
| --- | --- | --- |
| `GET` | `/` | API message, version and endpoint list |
| `POST` | `/analyze` | Analyse one feedback text, save its summary, return results and ranked resources |
| `POST` | `/analyze/batch` | Analyse 1-50 feedback strings and return per-item summaries or errors; does not save results |
| `GET` | `/history` | Return saved analyses ordered by timestamp, newest first |
| `GET` | `/progress` | Return per-skill progress derived from confirmed-gap records |
| `GET` | `/stats` | Return saved analysis count, gap occurrences, unique gap skills and learning-path counter |
| `GET` | `/skills` | Return supported skill names and their count |

### Single analysis

Send this JSON body to `POST /analyze` using the interactive API documentation or an HTTP client:

```json
{
  "text": "I am still confused by recursion and its base cases. I need a clearer explanation."
}
```

The response contains `sentiment`, `topics`, `skill_gaps`, `possible_gaps`, `strengths`, `gap_severity`, `recommendations`, `strengths_feedback` and `overall_message`. Scores and detected topics depend on the input and model output; they are not fixed values.

The endpoint trims whitespace and rejects empty input or fewer than five characters with HTTP 400. The frontend limits feedback entry to 500 characters. The API itself has no upper feedback-length limit.

### Batch analysis

Send this JSON body to `POST /analyze/batch`:

```json
{
  "feedbacks": [
    "Recursion base cases are confusing.",
    "I enjoyed learning SQL joins."
  ]
}
```

The response has `total` and `results`. Each successful item includes its index, a feedback preview, sentiment label, skill categories, severity and summary. Empty items produce a per-item error. An empty list or more than 50 entries returns HTTP 400.

Batch processing has its own inference path and does not apply the single endpoint's five-character validation. It does not insert history rows or update database-derived dashboard/progress statistics.

## Storage and progress behaviour

Successful single analyses are stored in the `feedback_analysis` table. Its fields are `id`, `feedback`, `sentiment`, `sentiment_confidence`, `topics`, `skill_gaps`, `possible_gaps`, `strengths`, `gap_severity`, `overall_message` and `created_at`. Skill lists are stored as comma-separated text. Ranked resource lists are not persisted.

The current progress implementation:

- Reads saved rows in ascending ID order and includes only rows with confirmed skill gaps.
- Maps the overall feedback severity to `high = 30`, `medium = 60`, and `low = 90`.
- Applies that same severity to each confirmed skill in the feedback.
- Compares the first and latest mapped scores to display Improving, Stable or Needs Attention.
- Ignores later positive/strength feedback and neutral/possible-gap feedback when building skill history.

A normal low-severity result has no confirmed gaps, so it does not contribute a low-severity observation to the current progress calculation. The percentages are severity-based indicators, not measured mastery or learning gains.

Dashboard gap counts and unique-skill counts also use confirmed gaps only. The `learning_paths` statistic equals the total number of saved analyses; it is not a count of independently saved learning plans. All database records are shared because the current schema has no student accounts or student identifiers.

## Supported skills

Each skill has configured keywords and four learning resources.

| Difficulty | Skills |
| --- | --- |
| Beginner | Arrays, Linked Lists, Sorting, OOP, SQL, Python, Web Dev, Stacks and Queues |
| Intermediate | Trees, Recursion, DSA, DBMS, Operating Systems, Computer Networks, ML Basics, Hashing |
| Advanced | Graphs, Dynamic Programming |

Resources include videos and articles from sources such as CodeWithHarry, Apna College, CodeHelp, Abdul Bari and GeeksforGeeks. Ranking uses resource titles; it does not inspect the full resource content or verify link availability.

## Notebook evaluation

See [the repository notebook](notebook/edusense-nlp-skill-gap-detection.ipynb) or [the Kaggle notebook](https://www.kaggle.com/code/rixbh19/edusense-nlp-skill-gap-detection).

The saved notebook overview reports 140,320 Coursera reviews and 1,835 course identifiers. Keyword-based course filtering retains 47,888 reviews; this filter can include false positives and should not be treated as a manually verified CS-only dataset. A 300-review selection is described as balanced in the notebook, but its saved class counts are unequal.

Ratings 1-2, 3 and 4-5 are mapped to negative, neutral and positive sentiment respectively. On the common 100-review evaluation:

| Model | Accuracy |
| --- | --- |
| DistilBERT with the neutral confidence rule | 77% |
| VADER | 62% |
| TextBlob | 62% |

DistilBERT records 88.37% on the separate positive/negative-only subset of 86 reviews. That score has a different denominator from the three-class comparison. Only one of 14 neutral reviews is classified correctly. The topic experiment matches at least one skill in 19 of 100 reviews; this is coverage, not topic accuracy.

These are saved notebook results, not evidence of recommendation quality or improved learning outcomes. The notebook uses a Kaggle dataset path and additional evaluation packages; running it locally requires the review CSV, an adjusted dataset path and its notebook dependencies.

## Current limitations and future work

- The sentiment model was trained for positive/negative classification; neutral labels come from a confidence rule and have weak coverage in the saved evaluation.
- One sentiment is applied to every skill in a feedback message, so mixed opinions are not separated per topic.
- Topic matching is restricted to the configured vocabulary and can match overlapping skills.
- The four learning stages are fixed; there is no prerequisite reasoning, completion tracking or scheduling.
- Batch results are not persisted, and later strengths do not update the progress history.
- There are no user accounts, private per-student histories, authentication or API rate limits. CORS allows all origins, and the frontend API address is hard-coded.
- A sentiment-processing error can be returned as a neutral fallback with an error field. Other failures may return HTTP 500.
- The current repository contains no automated test suite. Module demonstration blocks and saved notebook outputs do not constitute full integration coverage.

Future work includes per-skill sentiment, broader topic extraction, prerequisite-aware plans, user accounts, batch persistence, progress that accounts for strengths and possible gaps, dependency-list completion, automated tests and labelled evaluations of recommendation relevance and learning outcomes.
