# EduSense 🎓

### NLP-Based Adaptive Learning Path Recommendation System

EduSense is an **NLP-powered personalized learning system** that analyzes student feedback, identifies sentiment and skill gaps, and recommends relevant learning resources based on the student's learning needs.

The system converts unstructured student feedback into **actionable learning insights** using transformer-based NLP, topic extraction, semantic similarity, and a curated skills-resource knowledge base.

---

## 🚀 Demo

> **Enter student feedback → Analyze sentiment → Detect skill gaps → Rank learning resources → Build a personalized learning path**

### 🔗 Kaggle Notebook

👉 **[EduSense — NLP Skill Gap Detection](https://www.kaggle.com/code/rixbh19/edusense-nlp-skill-gap-detection)**

The Kaggle notebook demonstrates the NLP pipeline, skill-gap detection workflow, evaluation, and recommendation methodology.

### 💡 Example

**Input:**

```text
I really struggled with recursion and dynamic programming.
Base cases make no sense to me.
```

**Analysis:**

- **Sentiment:** `NEGATIVE` — 99.97% confidence
- **Detected Skill Gaps:** `Recursion`, `Dynamic Programming`
- **Recommended Resources:** Abdul Bari, Apna College, GeeksforGeeks

EduSense transforms qualitative student feedback into **personalized and actionable learning recommendations**.

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
                 │      spaCy        │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │  Skill Gap        │
                 │    Detection      │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │ Semantic Resource │
                 │     Ranking       │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │ Personalized      │
                 │ Learning Path     │
                 └───────────────────┘
```

---

## ✨ Key Features

- 🎭 **Sentiment Analysis** using DistilBERT
- 🔍 **NLP-based Topic Extraction** using spaCy
- 🧠 **Automatic Skill Gap Detection**
- 📚 **Personalized Resource Recommendation**
- 🔗 **Semantic Similarity Ranking** using Sentence Transformers
- 📊 **Skill Gap Severity Classification**
- ⚡ **REST API** using FastAPI
- 🌐 **Interactive Frontend** using React + Vite
- 📦 **Batch Feedback Analysis**
- 🗂️ Curated database of **18 Computer Science skills**
- 🎯 Learning resources mapped to individual skills

---

## 🛠️ Tech Stack

| Layer | Technology |
| --- | --- |
| Programming Language | Python |
| Sentiment Analysis | DistilBERT |
| NLP / Topic Extraction | spaCy |
| Semantic Similarity | Sentence Transformers |
| Backend API | FastAPI |
| ASGI Server | Uvicorn |
| Frontend | React + Vite |
| Dataset | Coursera Course Reviews — Kaggle |
| NLP Model | `distilbert-base-uncased-finetuned-sst-2-english` |
| Embedding Model | `all-MiniLM-L6-v2` |

---

## 📁 Project Structure

```text
EduSense/
│
├── backend/
│   ├── main.py                  # FastAPI routes
│   ├── sentiment.py             # DistilBERT sentiment analysis
│   ├── topic_extractor.py       # spaCy topic extraction
│   ├── skill_gap.py             # Skill gap detection logic
│   ├── recommender.py            # Semantic resource recommendation
│   ├── skills_db.py              # Skills + learning resources database
│   └── requirements.txt
│
├── frontend/
│   └── src/
│       ├── App.jsx
│       └── components/
│           ├── FeedbackInput.jsx
│           ├── ResultCard.jsx
│           ├── SkillGapCard.jsx
│           └── RecommendationList.jsx
│
├── notebook/
│   └── edusense_evaluation.ipynb
│
├── dataset/
│   └── student_feedback.csv
│
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd EduSense
```

---

### 2. Backend Setup

Navigate to the backend directory:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Download the spaCy English language model:

```bash
python -m spacy download en_core_web_sm
```

Start the backend:

```bash
python main.py
```

Backend API:

```text
http://localhost:8000
```

Swagger API documentation:

```text
http://localhost:8000/docs
```

---

### 3. Frontend Setup

Open a new terminal and navigate to the frontend:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

Frontend:

```text
http://localhost:5173
```

---

## 📡 API Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/` | API health check |
| `POST` | `/analyze` | Analyze a single student feedback |
| `POST` | `/analyze/batch` | Analyze multiple feedback entries |
| `GET` | `/skills` | Retrieve all supported skills |

---

## 📤 Sample API Request

### `POST /analyze`

```json
{
  "text": "I really struggled with recursion and dynamic programming"
}
```

---

## 📥 Sample API Response

```json
{
  "sentiment": {
    "label": "NEGATIVE",
    "score": 0.9997,
    "interpretation": "It looks like you're struggling here."
  },
  "skill_gaps": [
    "Recursion",
    "Dynamic Programming"
  ],
  "possible_gaps": [],
  "strengths": [],
  "gap_severity": "medium",
  "recommendations": [
    {
      "skill": "Recursion",
      "gap_type": "confirmed",
      "resources": [
        {
          "title": "Recursion in Programming - Apna College",
          "url": "https://www.youtube.com/watch?v=sE0-oFXCZFE",
          "type": "video",
          "relevance_score": 0.6852
        }
      ]
    }
  ]
}
```

---

## 🧠 NLP & ML Pipeline

EduSense combines multiple NLP components into a single learning-intelligence pipeline.

```text
                    Input Feedback
                          │
                          ▼
              ┌─────────────────────┐
              │      DistilBERT     │
              │ Sentiment Analysis  │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │       spaCy         │
              │ Topic / Keyword     │
              │    Extraction       │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │   Skill Matching    │
              │  & Gap Detection    │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Sentence Transformer│
              │ Semantic Similarity │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Resource Ranking &  │
              │ Recommendation      │
              └─────────────────────┘
```

---

## 🔬 Model Components

### 1. Sentiment Analysis

EduSense uses:

```text
distilbert-base-uncased-finetuned-sst-2-english
```

to classify student feedback into sentiment categories and estimate confidence.

---

### 2. Topic Extraction

spaCy is used to extract relevant linguistic features and keywords from student feedback.

These extracted signals are matched against the EduSense skills database.

---

### 3. Skill Gap Detection

The extracted topics are compared against a curated database of Computer Science skills.

The system identifies:

- **Confirmed skill gaps**
- **Possible skill gaps**
- **Existing strengths**
- **Overall gap severity**

---

### 4. Resource Recommendation

EduSense uses:

```text
all-MiniLM-L6-v2
```

to calculate semantic similarity between the student's identified learning need and available learning resources.

Resources are then ranked according to their relevance.

---

## 🗄️ Skills Database

EduSense currently covers **18 Computer Science topics** across three difficulty levels.

| Difficulty | Skills |
| --- | --- |
| Beginner | Arrays, Linked Lists, Sorting, OOP, SQL, Python, Web Development, Stacks & Queues |
| Intermediate | Trees, Recursion, DSA, DBMS, Operating Systems, Computer Networks, ML Basics, Hashing |
| Advanced | Graphs, Dynamic Programming |

Each skill contains:

- **15–20 NLP keywords**
- **4 curated learning resources**
- Resource type information
- Semantic relevance scoring

---

## 📚 Learning Resources

The recommendation database contains curated resources from platforms and educators such as:

- Apna College
- Abdul Bari
- CodeWithHarry
- GeeksforGeeks

The system ranks resources based on the detected skill gap and semantic relevance.

---

## 📊 Evaluation & Notebook

The project's experimentation and evaluation workflow is available through the Kaggle notebook:

👉 **[Open EduSense Kaggle Notebook](https://www.kaggle.com/code/rixbh19/edusense-nlp-skill-gap-detection)**

The notebook provides a reproducible environment for exploring the NLP-based skill-gap detection approach.

---

## 🎯 Use Cases

EduSense can be used in:

### 👨‍🎓 Student Learning

Identify concepts a student is struggling with and provide targeted resources.

### 🏫 Educational Platforms

Analyze large volumes of student feedback to discover common learning difficulties.

### 👨‍🏫 Faculty & Mentors

Surface recurring student challenges and support data-driven intervention.

### 📈 Personalized Learning

Generate adaptive learning paths based on individual feedback.

### 🤖 AI Education Assistants

Use student feedback as an input signal for intelligent tutoring systems.

---

## 🔮 Future Improvements

Potential extensions include:

- Fine-tuning domain-specific transformer models
- Multilingual student feedback analysis
- Automated learning-path sequencing
- Student progress tracking
- Knowledge graph-based skill relationships
- User-specific recommendation history
- LLM-powered explanations and tutoring
- Integration with LMS platforms
- Real-time learning analytics dashboard

---
