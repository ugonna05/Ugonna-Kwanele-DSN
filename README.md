# PersonaMind AI

AI-powered recommendation and behavioral review simulation platform built for the **DSN / Bluechip Hackathon Competition 3.0**.
PersonaMind AI combines semantic search, user behavior modeling, review simulation, and explainable recommendations into a lightweight and deployable AI system.

---

##  Live Demo

**API Base URL:**
[PersonaMind AI Live API](https://ugonna-kwanele-dsn-3.onrender.com?utm_source=chatgpt.com)

**Interactive API Documentation:**
[Swagger Docs](https://ugonna-kwanele-dsn-3.onrender.com/docs?utm_source=chatgpt.com)

---

## 📌 Overview

PersonaMind AI is an intelligent recommendation and user modeling system designed to:

* Understand user preferences semantically
* Simulate realistic product reviews
* Generate personalized recommendations
* Explain recommendation reasoning
* Handle cold-start recommendation scenarios
* Provide lightweight deployment for cloud platforms

The system uses modern NLP and embedding techniques to model users and products while remaining efficient enough for deployment on free-tier infrastructure.

---

##  Features

###  Recommendation Engine

* Semantic product recommendations
* Personalized ranking
* Context-aware recommendations
* Similarity-based retrieval
* Cold-start handling
* Explainable recommendations

###  User Modeling

* Behavioral profiling
* Preference extraction
* Sentiment-aware analysis
* User-product interaction modeling

###  Review Simulation

* AI-generated simulated reviews
* Rating prediction
* Sentiment estimation
* Confidence scoring

### ⚡ Engineering Features

* Lightweight deployment architecture
* FastAPI backend
* REST API support
* Vector similarity search
* Cloud deployment ready
* Docker support

---

##  System Architecture

```text
User Query/Input
        │
        ▼
┌──────────────────────┐
│ Semantic Embeddings  │
│ SentenceTransformer  │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│ Vector Search Layer  │
│      FAISS Index     │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│ Recommendation Agent │
│ User Modeling Agent  │
│ Review Agent         │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│ Explainable Results  │
│ Reviews + Rankings   │
└──────────────────────┘
```

---

## 🛠️ Tech Stack

### Backend

* Python
* FastAPI
* Uvicorn

### AI / Machine Learning

* SentenceTransformers
* FAISS
* Scikit-learn
* NumPy
* Pandas

### Deployment

* Render
* Docker
* Railway
* Hugging Face Spaces

---

## 📂 Project Structure

```text
Ugonna-Kwanele-DSN/
│
├── app/
│   ├── main.py
│   ├── recommendation.py
│   ├── review_simulator.py
│   ├── preprocessing.py
│   └── utils.py
│
├── data/
│   └── dataset.csv
│
├── models/
│
├── agents/
│
├── notebooks/
│
├── requirements.txt
├── Dockerfile
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/ugonna05/Ugonna-Kwanele-DSN.git

cd Ugonna-Kwanele-DSN
```

---

### 2. Create Virtual Environment

#### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

#### Linux / Mac

```bash
python -m venv venv

source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the API

Start the FastAPI server locally:

```bash
uvicorn app.main:app --reload
```

Server runs at:

```text
http://127.0.0.1:8000
```

---

## 📖 API Documentation

Once the server is running:

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

---

# 🔌 API Endpoints

---

## 🧠 Recommendation Endpoint

### POST `/recommend`

Generate personalized product recommendations.

### Example Request

```json
{
  "user_id": "A1",
  "query": "high quality coffee",
  "top_k": 5
}
```

### Example Response

```json
{
  "recommendations": [
    {
      "product_id": "P101",
      "score": 0.91,
      "reason": "Matches preference for premium coffee products"
    }
  ]
}
```

---

## ✍️ Review Simulation Endpoint

### POST `/simulate-review`

Generate a simulated review for a user-product pair.

### Example Request

```json
{
  "user_id": "A1",
  "product_id": "P123"
}
```

### Example Response

```json
{
  "predicted_rating": 4.5,
  "sentiment": "Positive",
  "review": "Excellent quality and worth the price."
}
```

---

## ❤️ Health Check Endpoint

### GET `/health`

Checks whether the API is running successfully.

### Example Response

```json
{
  "status": "healthy"
}
```

---

# 🧪 Example Usage

## Python Example

```python
import requests

url = "http://127.0.0.1:8000/recommend"

payload = {
    "user_id": "A1",
    "query": "gaming laptop",
    "top_k": 3
}

response = requests.post(url, json=payload)

print(response.json())
```

---

# 🐳 Docker Deployment

## Build Docker Image

```bash
docker build -t personamind-ai .
```

## Run Container

```bash
docker run -p 8000:8000 personamind-ai
```

---

# ☁️ Deployment Platforms

PersonaMind AI supports deployment on:

* Render
* Railway
* Docker
* Hugging Face Spaces

---

# 📊 Key Capabilities

| Capability        | Description                            |
| ----------------- | -------------------------------------- |
| Semantic Search   | Understands meaning, not just keywords |
| Review Simulation | Generates realistic AI reviews         |
| User Modeling     | Learns user preferences and patterns   |
| Explainability    | Provides recommendation reasoning      |
| Lightweight AI    | Optimized for free-tier deployment     |
| REST API          | Easy integration into applications     |

---

# 🔍 Explainable Recommendations

PersonaMind AI does not only recommend products — it also explains *why* they were recommended.

Example:

```json
{
  "product": "Premium Coffee Beans",
  "reason": "Recommended because the user prefers high-quality coffee products with strong ratings."
}
```

---

# 📈 Future Improvements

* Conversational recommendation chatbot
* Real-time feedback learning
* Advanced hybrid recommendation models
* User memory system
* Multi-modal recommendations
* Fine-tuned transformer models
* GPU optimization

---

# 👨‍💻 Team

### 👤 Ugonna

### 👤 Kwanele Mlalazi

---

#  Competition

Built for:

**DSN / Bluechip Hackathon Competition 3.0**

---

# 📜 License

This project is licensed under the MIT License.

```text
MIT License

Copyright (c) 2026

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files...
```

---

# 🙏 Acknowledgments

Special thanks to:

* [FastAPI](https://fastapi.tiangolo.com?utm_source=chatgpt.com)
* [Hugging Face](https://huggingface.co?utm_source=chatgpt.com)
* [Sentence Transformers](https://www.sbert.net?utm_source=chatgpt.com)
* [FAISS](https://faiss.ai?utm_source=chatgpt.com)
* [Render](https://render.com?utm_source=chatgpt.com)

---

# ⭐ Repository

[GitHub Repository](https://github.com/ugonna05/Ugonna-Kwanele-DSN?utm_source=chatgpt.com)

If you found this project useful, consider starring the repository ⭐
