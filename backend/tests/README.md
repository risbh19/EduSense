# Backend regression tests

From the repository root, using Python 3.12:

```sh
python -m pip install -r backend/tests/requirements.txt
python -m unittest discover -s backend/tests -v
```

These tests call the real FastAPI endpoints and SQLAlchemy models against a new
in-memory SQLite database per test. Model inference is stubbed, so no spaCy,
Transformers, Sentence Transformers or model downloads are required. The tests
do not read or modify `edusense.db` and do not validate NLP model accuracy.
