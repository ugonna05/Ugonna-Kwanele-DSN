# PersonaMind AI

AI-powered recommendation and behavioral review simulation system built for the BCT LLM Agent Challenge.

## Features

- Semantic product recommendations
- Behavioral user profiling
- AI review simulation
- Sentiment-aware recommendations
- Vector similarity search
- Lightweight AI architecture
- FastAPI backend
- Explainable recommendations

---

## Tech Stack

- FastAPI
- SentenceTransformers
- FAISS
- Pandas
- Scikit-learn
- PyTorch

---

## Project Structure

```bash
PersonaMind-AI/
│
├── app/
├── agents/
├── models/
├── data/
├── notebooks/
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## Installation

```bash
git clone https://github.com/ugonna05/Ugonna-Kwanele-DSN.git

cd Ugonna-Kwanele-DSN

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

---

## Run API

```bash
uvicorn app.main:app --reload
```

---

## API Docs

After starting the server:

```bash
http://127.0.0.1:8000/docs
```

---

## Endpoints

### Recommendations

POST `/recommend`

Example:

```json
{
  "user_id": "A1",
  "query": "high quality coffee",
  "top_k": 5
}
```

---

### Review Simulation

POST `/simulate-review`

Example:

```json
{
  "user_id": "A1",
  "product_id": "P123"
}
```

---

## Deployment

Supports:
- Render
- Railway
- Docker
- HuggingFace Spaces

---

## Team

- Ugonna
- Kwanele Mlalazi