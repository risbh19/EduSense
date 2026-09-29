# EduSense 🎓

### NLP-Based Adaptive Learning Path Recommendation System

EduSense is an **NLP-powered personalized learning system** that analyzes student feedback, detects sentiment and skill gaps, and recommends relevant learning resources for each gap.

It turns unstructured student feedback into **actionable learning insights** using transformer-based sentiment analysis, keyword-based topic extraction, semantic similarity ranking, and a curated skills-resource knowledge base. Every analysis is stored in a database, so the app can also show **history, statistics and per-skill progress** over time.

---

## 🚀 Demo

> **Enter student feedback → Analyze sentiment → Detect skill gaps → Rank learning resources → Track progress**

### 🔗 Kaggle Notebook

👉 **[EduSense — NLP Skill Gap Detection](https://www.kaggle.com/code/rixbh19/edusense-nlp-skill-gap-detection)**

The notebook (also available in this repo under `notebook/`) demonstrates the NLP pipeline and compares sentiment models on Coursera course reviews.

### 💡 Example

**Input:**

```text
I really struggled with recursion and dynamic programming.
Base cases make no sense to me.
```

**Analysis:**

- **Sentiment:** `NEGATIVE` (very high confidence)
- **Detected Skill Gaps:** `Recursion`, `Dynamic Programming`
- **Recommended Resources:** Abdul Bari, Apna College, GeeksforGeeks (ranked by semantic relevance)

---

## 🧠 How It Works

```text
                    Student Feedback
                           │
                           ▼
                 ┌───────────────────┐
                 │ Sentiment Analysis│
                 │    DistilBERT     │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │ Topic Extraction  │
                 │ spaCy + keywords  │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │ Skill Gap         │
                 │ Detection         │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │ Semantic Resource │
                 │ Ranking (MiniLM)  │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │ SQLite storage →  │
                 │ history, progress │
                 └───────────────────┘
```

---

## ✨ Key Features

- 🎭 **Sentiment analysis** using DistilBERT (with a NEUTRAL band for low-confidence predictions)
- 🔍 **Topic extraction** using spaCy plus a curated keyword database
- 🧠 **Skill gap detection** into confirmed gaps, possible gaps and strengths, with gap severity
- 📚 **Resource recommendation** ranked by semantic similarity (Sentence Transformers)
- 🗄️ **Persistent storage** of every analysis with SQLite + SQLAlchemy
- 📈 **Progress tracking** per skill (improving / stable / needs attention)
- 📊 **Dashboard statistics** and analysis history
- 📦 **Batch feedback analysis** (up to 50 entries per request)
- ⚡ **REST API** using FastAPI with auto-generated Swagger docs
- 🌐 **React + Vite frontend** with dashboard, history and learning path views, plus dark mode
- 🗂️ Curated database of **18 Computer Science skills** with **72 learning resources**

---

## 🛠️ Tech Stack

| Layer | Technology |
| --- | --- |
| Language | Python 3, JavaScript |
| Sentiment Analysis | DistilBERT (`distilbert-base-uncased-finetuned-sst-2-english`) via Hugging Face Transformers |
| Topic Extraction | spaCy (`en_core_web_sm`) |
| Semantic Similarity | Sentence Transformers (`all-MiniLM-L6-v2`) |
| Backend API | FastAPI + Uvicorn |
| Database | SQLite + SQLAlchemy |
| Frontend | React + Vite + Axios |
| Notebook Dataset | Coursera Course Reviews (Kaggle) |

---

## 📁 Project Structure

```text
EduSense/
│
├── backend/
│   ├── main.py               # FastAPI app and all routes
│   ├── database.py           # SQLAlchemy engine, session, Base
│   ├── models.py             # FeedbackAnalysis table
│   ├── sentiment.py          # DistilBERT sentiment analysis
│   ├── topic_extractor.py    # spaCy topic extraction + skill matching
│   ├── skill_gap.py          # Skill gap detection logic
│   ├── recommender.py        # Semantic resource ranking (MiniLM)
│   ├── skills_db.py          # 18 skills, keywords and resources
│   └── requirements.txt
│
├── frontend/
│   ├── package.json
│   ├── vite.config.js
│   └── src/
│       ├── App.jsx           # Layout, dashboard, navigation
│       ├── App.css
│       └── components/
│           ├── FeedbackInput.jsx
│           ├── ResultCard.jsx
│           ├── SkillGapCard.jsx
│           ├── RecommendationList.jsx
│           ├── LearningPath.jsx
│           └── History.jsx
│
├── notebook/
│   └── edusense-nlp-skill-gap-detection.ipynb   # Kaggle evaluation notebook
│
├── .gitignore
└── README.md
```

> The SQLite file `edusense.db` is **not** committed. It is created automatically on the first run of the backend.

---

## ⚙️ Setup & Installation

**Prerequisites:** Python 3.10+ and Node.js 18+.

### 1. Clone the repository

```bash
git clone https://github.com/risbh19/EduSense.git
cd EduSense
```

### 2. Backend setup

```bash
cd backend
python -m venv venv
```

Activate the virtual environment:

```bash
# Windows (PowerShell / CMD)
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

Install dependencies and the spaCy model:

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

Start the backend (run this **from inside the `backend/` folder**):

```bash
python main.py
```

- API: `http://localhost:8000`
- Swagger docs: `http://localhost:8000/docs`

The first request downloads the DistilBERT and MiniLM models from Hugging Face, so it can take a while and needs an internet connection.

### 3. Frontend setup

Open a new terminal:

```bash
cd frontend
npm install
npm run dev
```

Frontend: `http://localhost:5173`

> The frontend currently calls the backend at `http://localhost:8000`, so keep the backend on port 8000.

---

## 📡 API Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/` | API health check and endpoint list |
| `POST` | `/analyze` | Analyze one feedback text, save it, return gaps and recommendations |
| `POST` | `/analyze/batch` | Analyze up to 50 feedback texts in one request |
| `GET` | `/history` | All saved analyses, newest first |
| `GET` | `/progress` | Per-skill progress derived from saved analyses |
| `GET` | `/stats` | Dashboard totals (analyses, skill gaps, unique skills) |
| `GET` | `/skills` | All supported skills |

### Sample request

`POST /analyze`

```json
{
  "text": "I really struggled with recursion and dynamic programming"
}
```

### Sample response (shortened)

```json
{
  "sentiment": {
    "label": "NEGATIVE",
    "score": 0.9997,
    "interpretation": "It looks like you're struggling here. Let's find resources to help."
  },
  "topics": {
    "matched_skills": ["Recursion", "Dynamic Programming"]
  },
  "skill_gaps": ["Recursion", "Dynamic Programming"],
  "possible_gaps": [],
  "strengths": [],
  "gap_severity": "medium",
  "recommendations": [
    {
      "skill": "Recursion",
      "gap_type": "confirmed",
      "difficulty": "intermediate",
      "resources": [
        {
          "title": "Recursion in Programming - Apna College",
          "url": "https://www.youtube.com/watch?v=sE0-oFXCZFE",
          "type": "video",
          "relevance_score": 0.6852
        }
      ],
      "message": "You seem to be struggling with Recursion. ..."
    }
  ],
  "strengths_feedback": [],
  "overall_message": "We found 2 skill gap(s): Recursion, Dynamic Programming. ..."
}
```

---

## 🔬 Model Components

### 1. Sentiment analysis

`distilbert-base-uncased-finetuned-sst-2-english` classifies feedback as positive or negative. Predictions with confidence below 0.65 are relabelled **NEUTRAL**.

### 2. Topic extraction

spaCy extracts nouns, proper nouns and noun chunks. Skills are then matched against the skills database in two passes: a direct whole-word keyword match (with plural support), then a lemma-based match that needs at least two keyword hits.

### 3. Skill gap detection

Matched skills are labelled using the sentiment of the whole feedback:

| Sentiment | Result |
| --- | --- |
| Negative | **Confirmed skill gap** |
| Neutral | **Possible gap** |
| Positive | **Strength** |

Gap severity is `high` for 3 or more confirmed gaps, `medium` for 1 or 2, and `low` otherwise.

### 4. Resource recommendation

`all-MiniLM-L6-v2` embeds the feedback text and each resource title. Resources for a skill are ranked by cosine similarity.

### 5. Progress tracking

Each saved analysis records severity per skill. `/progress` maps severity to a score (high = 30, medium = 60, low = 90) and compares the first and latest score to label each skill **Improving**, **Stable** or **Needs Attention**.

---

## 🗄️ Skills Database

EduSense currently covers **18 Computer Science skills** across three difficulty levels.

| Difficulty | Skills |
| --- | --- |
| Beginner | Arrays, Linked Lists, Sorting, OOP, SQL, Python, Web Dev, Stacks and Queues |
| Intermediate | Trees, Recursion, DSA, DBMS, Operating Systems, Computer Networks, ML Basics, Hashing |
| Advanced | Graphs, Dynamic Programming |

Each skill has a keyword list for matching and **4 curated learning resources** (videos and articles).

---

## 📊 Evaluation (from the notebook)

The notebook evaluates sentiment models on a 100-review sample of Coursera course reviews (3-class: positive / neutral / negative):

| Model | Accuracy |
| --- | --- |
| **DistilBERT** | **77%** |
| VADER | 62% |
| TextBlob | 62% |

DistilBERT reaches about 88% accuracy on positive/negative samples only. The notebook runs on Kaggle (its dataset path is `/kaggle/input/...`), so open it there or change the path to run locally.

---

## ⚠️ Current Limitations

Being upfront about what the system does not do yet:

- **Keyword-based skill matching.** On the notebook sample only 19 of 100 reviews matched any skill, so coverage is low.
- **Sentiment applies to the whole feedback.** A mixed sentence such as "I love Python but OOP confuses me" is not split per skill.
- **NEUTRAL detection is weak.** The SST-2 model was not trained for neutral text.
- **No user accounts.** History and progress are shared across all users of one database.
- **Small knowledge base.** 18 skills and 72 resources, with no prerequisite relationships between skills.
- **Hard-coded API URL** in the frontend and open CORS settings, so it is meant for local use for now.

---

## 🗺️ Roadmap

- [ ] Embedding-based skill extraction and aspect-level (per-skill) sentiment
- [ ] Prerequisite graph for ordered learning paths
- [ ] Labelled evaluation set with F1 for skill-gap detection and NDCG for recommendations
- [ ] User accounts and per-user progress
- [ ] Environment-based API URL, tests, Docker, CI and deployment

---

## 🤝 Contributing

Issues and pull requests are welcome.

## 👤 Author

**Rishabh** — [@risbh19](https://github.com/risbh19)
