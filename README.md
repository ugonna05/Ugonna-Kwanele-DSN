<<<<<<< HEAD
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
=======
# Ugonna-Kwanele-DSN
DSN/Bluechip hackathon competition 3.0
BERT-Based Recommendation & User Modeling System
Complete Documentation
BERT-Based Recommendation & User Modeling System
Version Python PyTorch Transformers License

An advanced AI-powered recommendation system that understands user behavior and generates realistic reviews

Features • Installation • Quick Start • API Documentation • Examples

Table of Contents
Overview
Features
System Architecture
Installation
Quick Start
API Documentation
Task A: Review Simulation
Task B: Recommendations
Examples
Model Training
Configuration
Performance Metrics
Deployment
Troubleshooting
Contributing
License
Overview
The BERT-Based Recommendation & User Modeling System is a state-of-the-art AI system that combines natural language understanding with collaborative filtering to provide personalized recommendations and simulate user reviews. Built on top of BERT (Bidirectional Encoder Representations from Transformers), this system excels at understanding user preferences and generating realistic review content.

Key Capabilities
Capability	Description
Review Simulation	Generate realistic star ratings and review text for unseen products
User Profiling	Build comprehensive behavioral profiles of users
Personalized Recommendations	Rank products based on individual user preferences
Conversational Recommendations	Multi-turn dialogue-based recommendations
Cold-Start Handling	Effective recommendations for new users and products
Contextual Understanding	Leverage temporal and behavioral context
Features

🎯 Task A: User Modeling & Review Simulation
Star Rating Prediction: Accurately predict ratings (1-5 stars) for any user-product pair
Review Text Generation: Generate realistic, contextually appropriate review text
Sentiment Analysis: Classify review sentiment (Positive/Negative/Neutral)
User Behavior Modeling: Capture writing style, rating patterns, and preferences
Batch Simulation: Simulate multiple reviews efficiently
Confidence Scoring: Each prediction includes a confidence metric

🎯 Task B: Personalized Recommendations
Contextual Recommendations: Incorporate conversation context into rankings
Multi-Turn Dialogue: Handle extended conversations with follow-up questions
Similar Product Discovery: Find products similar to any given item
Cold-Start Strategies: Intelligent fallback for new users/products
Reasoning Generation: Explain why products are recommended
Real-time Adaptation: Update recommendations based on user feedback

Technical Features
BERT-based Embeddings: Deep semantic understanding of text
Multi-Head Attention: Captures complex user-product interactions
GPU Acceleration: Optimized for CUDA-enabled devices
Batch Processing: Efficient handling of large datasets
Model Checkpointing: Automatic saving of best models
Extensible Architecture: Easy to add new features or modify existing ones
System Architecture
┌─────────────────────────────────────────────────────────────────┐
│                    Input Layer                                   │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐        │
│  │  Review  │  │   User   │  │ Product  │  │ Temporal │        │
│  │   Text   │  │   ID     │  │   ID     │  │ Context  │        │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘        │
│       │             │             │             │               │
├───────┼─────────────┼─────────────┼─────────────┼───────────────┤
│       ▼             ▼             ▼             ▼               │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                   BERT Encoder                          │    │
│  │         (Pre-trained Transformer Model)                 │    │
│  └─────────────────────────┬───────────────────────────────┘    │
│                            │                                     │
│       ┌────────────────────┼────────────────────┐               │
│       ▼                    ▼                    ▼               │
│  ┌─────────┐         ┌──────────┐         ┌──────────┐         │
│  │  User   │         │ Product  │         │ Temporal │         │
│  │Embedding│         │Embedding │         │Embedding │         │
│  └────┬────┘         └────┬─────┘         └────┬─────┘         │
│       │                   │                     │               │
│       └───────────────────┼─────────────────────┘               │
│                           ▼                                     │
│              ┌────────────────────────┐                        │
│              │   Cross-Attention      │                        │
│              │  (User-Product         │                        │
│              │   Interaction)         │                        │
│              └────────────┬───────────┘                        │
│                           ▼                                     │
│              ┌────────────────────────┐                        │
│              │    Fusion Layer        │                        │
│              │  (Multi-modal          │                        │
│              │   Integration)          │                        │
│              └────────────┬───────────┘                        │
│                           │                                     │
│         ┌─────────────────┼─────────────────┐                  │
│         ▼                 ▼                 ▼                  │
│    ┌────────┐        ┌──────────┐     ┌──────────┐            │
│    │ Rating │        │Sentiment │     │ Profile  │            │
│    │ Head   │        │  Head    │     │  Head    │            │
│    └────┬───┘        └────┬─────┘     └────┬─────┘            │
│         │                 │                 │                  │
├─────────┼─────────────────┼─────────────────┼──────────────────┤
│         ▼                 ▼                 ▼                  │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                    Output Layer                         │   │
│  │  • Predicted Rating (1-5)                               │   │
│  │  • Sentiment Classification                             │   │
│  │  • User Profile Embedding                               │   │
│  │  • Generated Review Text                                │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
Installation
Prerequisites
Python 3.8 or higher
CUDA-capable GPU (optional, for faster training)
8GB+ RAM recommended
10GB+ disk space for models and data
Step 1: Clone the Repository
git clone https://github.com/yourusername/bert-recommendation-system.git
cd bert-recommendation-system
Step 2: Create Virtual Environment
# Using conda
conda create -n bert-rec python=3.9
conda activate bert-rec

# OR using venv
python -m venv bert-rec-env
source bert-rec-env/bin/activate  # On Windows: bert-rec-env\Scripts\activate
Step 3: Install Dependencies
pip install -r requirements.txt
requirements.txt:

torch>=1.9.0
transformers>=4.20.0
pandas>=1.3.0
numpy>=1.21.0
scikit-learn>=1.0.0
tqdm>=4.62.0
matplotlib>=3.4.0
seaborn>=0.11.0
joblib>=1.1.0
scipy>=1.7.0
networkx>=2.6.0
Step 4: Download BERT Model
The system will automatically download the BERT model on first run:

from transformers import AutoTokenizer, AutoModel
tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
model = AutoModel.from_pretrained('bert-base-uncased')
Quick Start
Basic Usage

# Import the system
from bert_recommendation_system import (
    DataPreprocessor,
    UserModelingBERT,
    ReviewSimulationAgent,
    RecommendationAgent,
    ModelTrainer
)

import pandas as pd
import torch

# 1. Load and preprocess data
preprocessor = DataPreprocessor()
df = preprocessor.load_and_preprocess('Task1.csv')

# 2. Initialize the model
model = UserModelingBERT(
    num_users=len(preprocessor.user_encoder.classes_),
    num_products=len(preprocessor.product_encoder.classes_)
)

# 3. Create agents
review_agent = ReviewSimulationAgent(
    model, tokenizer, df,
    preprocessor.user_encoder,
    preprocessor.product_encoder
)

rec_agent = RecommendationAgent(
    model, tokenizer, df,
    preprocessor.user_encoder,
    preprocessor.product_encoder,
    review_agent
)

# 4. Simulate a review
result = review_agent.simulate_review('User_0', 'Product_X')
print(f"Predicted Rating: {result['predicted_rating']}/5")
print(f"Simulated Review: {result['simulated_review']}")

# 5. Get recommendations
recommendations = rec_agent.recommend_for_user('User_0', n_recommendations=5)
for rec in recommendations['recommendations']:
    print(f"{rec['product_id']}: {rec['similarity_score']:.2%} match")
API Documentation
Class: DataPreprocessor
Handles all data preprocessing tasks.

Method	Description	Parameters	Returns
load_and_preprocess()	Load CSV and preprocess	filepath: str	DataFrame
get_user_stats()	Compute user statistics	df: DataFrame	DataFrame
Example:

preprocessor = DataPreprocessor()
df = preprocessor.load_and_preprocess('reviews.csv')
stats = preprocessor.get_user_stats(df)
print(stats.head())
Class: UserModelingBERT
The main BERT-based neural network for user modeling.

Initialization Parameters
Parameter	Type	Default	Description
bert_model_name	str	'bert-base-uncased'	Pre-trained BERT model
num_users	int	1000	Number of unique users
num_products	int	1000	Number of unique products
embedding_dim	int	768	Dimension of embeddings
hidden_dim	int	256	Hidden layer dimension
dropout	float	0.1	Dropout rate
Methods
Method	Description
forward()	Forward pass through the network
generate_simulated_review()	Generate review text for a user-product pair
set_temperature()	Set generation temperature
Example:

model = UserModelingBERT(
    num_users=5000,
    num_products=10000,
    embedding_dim=768,
    hidden_dim=256
)

# Forward pass
outputs = model(
    input_ids=input_ids,
    attention_mask=attention_mask,
    user_ids=user_ids,
    product_ids=product_ids,
    year=year_tensor,
    review_length=length_tensor
)

print(outputs['rating'])  # Predicted ratings
print(outputs['sentiment_probs'])  # Sentiment probabilities
Class: ReviewSimulationAgent
Agent for simulating user reviews (Task A).

Methods
Method	Description	Returns
simulate_review()	Simulate a single review	dict
batch_simulate()	Simulate multiple reviews	list[dict]
get_user_behavior_analysis()	Analyze user behavior	dict
simulate_review() Return Format
{
    'user_id': str,                    # User identifier
    'product_id': str,                 # Product identifier
    'predicted_rating': float,         # Rating from 1-5
    'predicted_sentiment': str,        # 'Positive', 'Neutral', 'Negative'
    'simulated_review': str,           # Generated review text
    'confidence': float,               # Confidence score (0-1)
    'user_avg_rating': float,          # User's historical average
    'product_avg_rating': float        # Product's historical average
}
Example:

# Simulate a single review
result = review_agent.simulate_review(
    user_id='User_123',
    product_id='Product_456',
    year=2023
)

# Simulate multiple reviews
products = ['P001', 'P002', 'P003']
results = review_agent.batch_simulate('User_123', products)

# Analyze user behavior
analysis = review_agent.get_user_behavior_analysis('User_123')
print(f"Rating consistency: {analysis['review_consistency']:.2%}")
Class: RecommendationAgent
Agent for generating personalized recommendations (Task B).

Methods
Method	Description	Returns
recommend_for_user()	Generate personalized recommendations	dict
conversational_recommendation()	Multi-turn dialogue recommendations	dict
get_similar_products()	Find similar products	list[dict]
recommend_for_user() Parameters
Parameter	Type	Default	Description
user_id	str	Required	User identifier
n_recommendations	int	5	Number of recommendations
context	dict	None	Contextual information
exclude_rated	bool	True	Exclude already rated products
Return Format
{
    'user_id': str,
    'recommendations': [
        {
            'product_id': str,
            'product_summary': str,
            'product_preview': str,
            'similarity_score': float,
            'avg_rating': float,
            'review_count': int,
            'reason': str
        },
        ...
    ],
    'total_available': int,
    'context_used': bool
}
Example:

# Basic recommendations
recs = rec_agent.recommend_for_user('User_123', n_recommendations=10)

# With context
context = {'preference': 'high quality', 'category': 'electronics'}
recs = rec_agent.recommend_for_user('User_123', context=context)

# Conversational
conversation = [
    "I need a durable laptop",
    "Budget is around $1000",
    "Battery life is important"
]
conv_recs = rec_agent.conversational_recommendation(conversation, 'User_123')

# Similar products
similar = rec_agent.get_similar_products('Product_456', n_recommendations=5)
Task A: Review Simulation
Overview
Task A focuses on understanding users deeply enough to simulate their reviews. The system learns each user's unique writing style, rating patterns, and sentiment tendencies.

How It Works
User Profiling: The system builds a comprehensive profile for each user including:

Historical rating distribution
Average review length and complexity
Sentiment patterns over time
Temporal rating trends
Product Understanding: Each product is represented by:

Aggregated review text
Average rating and sentiment distribution
Review count and popularity
Review Generation: When simulating a review, the system:

Predicts the most likely rating (1-5 stars)
Determines appropriate sentiment
Generates contextually relevant review text
Provides confidence score
Use Cases
Use Case	Description	Example
A/B Testing	Test how users might react to new products	Simulate reviews for prototype products
Market Research	Predict reception of upcoming releases	Forecast ratings for unreleased items
User Behavior Analysis	Understand user preferences deeply	Analyze rating patterns and tendencies
Content Generation	Auto-generate review content	Create realistic review examples
Advanced Usage
# Simulate with temporal context
result_2022 = review_agent.simulate_review(user_id, product_id, year=2022)
result_2023 = review_agent.simulate_review(user_id, product_id, year=2023)

# Compare how user's preferences might have changed
print(f"2022 Rating: {result_2022['predicted_rating']}")
print(f"2023 Rating: {result_2023['predicted_rating']}")

# Analyze user behavior over time
behavior = review_agent.get_user_behavior_analysis(user_id)
if behavior['rating_trend'] == 'increasing':
    print("User is becoming more satisfied over time")
elif behavior['rating_trend'] == 'decreasing':
    print("User's satisfaction is declining")
Task B: Recommendations
Overview
Task B focuses on delivering personalized recommendations that go beyond traditional collaborative filtering. The system incorporates contextual signals and supports conversational interaction.

Recommendation Strategies
Strategy	Description	When to Use
Personalized	Based on user's historical preferences	Existing users with history
Contextual	Incorporates conversation context	During interactive sessions
Cold-Start	Popularity-based fallback	New users or products
Similar Products	Based on product embeddings	Finding alternatives
Hybrid	Combines multiple strategies	Best overall performance
Conversational Recommendations
The system supports multi-turn conversations for iterative refinement:

# Example conversation flow
conversation = [
    "I need a new phone",
    "Camera quality is very important",
    "Budget around $800"
]

# Get initial recommendations
response = rec_agent.conversational_recommendation(conversation, user_id)

print(f"Reasoning: {response['reasoning']}")
for rec in response['recommendations']:
    print(f"- {rec['product_id']}")

# User selects a product and provides feedback
follow_up = "I like the first option, but are there any with better battery life?"
conversation.append(follow_up)

# Get refined recommendations
refined = rec_agent.conversational_recommendation(conversation, user_id)
Cold-Start Handling
For new users with no history, the system:

Uses popularity-based recommendations initially
Asks clarifying questions to understand preferences
Updates recommendations based on responses
Builds user profile incrementally
# Cold-start user
new_user = 'NEW_USER_XYZ'
cold_recs = rec_agent.recommend_for_user(new_user)

print("First-time recommendations (popularity-based):")
for rec in cold_recs['recommendations']:
    print(f"- {rec['product_id']} (Popular choice)")

# After getting user feedback, refine
feedback = "I prefer electronics over clothing"
refined_recs = rec_agent.recommend_for_user(
    new_user, 
    context={'preference': feedback}
)
Examples
Example 1: Complete Workflow
# Full pipeline example
from bert_recommendation_system import create_complete_system

# Create the complete system
system = create_complete_system('Task1.csv')

# Get user analysis
user = 'User_123'
analysis = system.review_agent.get_user_behavior_analysis(user)

print(f"""
User Profile: {user}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Total Reviews: {analysis.get('total_reviews', 0)}
Average Rating: {analysis.get('avg_rating', 0):.1f}/5
Rating Consistency: {analysis.get('review_consistency', 0):.2%}
Preferred Sentiment: {analysis.get('sentiment_tendency', 'Unknown')}
""")

# Simulate review for a new product
product = 'New_Product_001'
simulated = system.review_agent.simulate_review(user, product)

print(f"""
Simulated Review
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Product: {product}
Predicted Rating: {simulated['predicted_rating']}/5
Confidence: {simulated['confidence']:.2%}
Review: "{simulated['simulated_review']}"
""")

# Get recommendations based on simulation
recommendations = system.rec_agent.recommend_for_user(user, n_recommendations=3)

print("\nRecommended for you:")
for i, rec in enumerate(recommendations['recommendations'], 1):
    print(f"{i}. {rec['product_id']} (Match: {rec['similarity_score']:.2%})")
    print(f"   {rec['reason']}")
Example 2: Batch Processing
# Batch simulate reviews for multiple users and products
users = ['User_001', 'User_002', 'User_003']
products = ['P100', 'P200', 'P300', 'P400', 'P500']

results = []
for user in users:
    batch_results = review_agent.batch_simulate(user, products)
    results.extend(batch_results)

# Convert to DataFrame for analysis
import pandas as pd
results_df = pd.DataFrame(results)

# Analyze by user
user_stats = results_df.groupby('user_id').agg({
    'predicted_rating': 'mean',
    'confidence': 'mean'
}).round(2)

print("Average predicted ratings by user:")
print(user_stats)

# Analyze by product
product_stats = results_df.groupby('product_id').agg({
    'predicted_rating': 'mean',
    'confidence': 'mean'
}).round(2)

print("\nAverage predicted ratings by product:")
print(product_stats)

# Export results
results_df.to_csv('simulated_reviews.csv', index=False)
Example 3: Recommendation API
# Create a simple recommendation API using Flask
from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize the system (once at startup)
system = create_complete_system('Task1.csv')

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    user_id = data.get('user_id')
    n = data.get('n_recommendations', 5)
    context = data.get('context', {})
    
    recommendations = system.rec_agent.recommend_for_user(
        user_id, 
        n_recommendations=n,
        context=context
    )
    
    return jsonify(recommendations)

@app.route('/simulate', methods=['POST'])
def simulate():
    data = request.json
    user_id = data.get('user_id')
    product_id = data.get('product_id')
    year = data.get('year', 2023)
    
    result = system.review_agent.simulate_review(user_id, product_id, year)
    
    return jsonify(result)

@app.route('/converse', methods=['POST'])
def converse():
    data = request.json
    conversation = data.get('conversation', [])
    user_id = data.get('user_id')
    
    response = system.rec_agent.conversational_recommendation(conversation, user_id)
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
Example 4: Interactive Chatbot
# Interactive recommendation chatbot
def recommendation_chatbot(user_id=None):
    print("🤖 Welcome to the Recommendation Assistant!")
    print("I can help you find products you'll love.\n")
    
    conversation = []
    
    while True:
        user_input = input("\nYou: ")
        
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("\n Thank you for chatting! Goodbye!")
            break
        
        conversation.append(user_input)
        
        # Get recommendations based on conversation
        response = rec_agent.conversational_recommendation(conversation, user_id)
        
        print(f"\n {response['reasoning']}")
        
        if response['recommendations']:
            print("\n Top recommendations:")
            for i, rec in enumerate(response['recommendations'][:3], 1):
                print(f"   {i}. {rec['product_id']} - {rec.get('product_summary', 'Product')[:50]}...")
        
        if response['follow_up_questions']:
            print(f"\n {response['follow_up_questions'][0]}")

# Run the chatbot
recommendation_chatbot(user_id='User_123')
Model Training
Training Configuration
# Configure training parameters
training_config = {
    'batch_size': 16,
    'learning_rate': 2e-5,
    'n_epochs': 5,
    'warmup_steps': 100,
    'weight_decay': 0.01,
    'gradient_clip': 1.0,
    'validation_split': 0.1,
    'random_seed': 42
}

# Initialize trainer
trainer = ModelTrainer(
    model=model,
    train_loader=train_loader,
    val_loader=val_loader,
    learning_rate=training_config['learning_rate']
)

# Train with progress tracking
train_losses, val_losses, maes = trainer.train(n_epochs=5)

# Plot training curves
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(train_losses, label='Train Loss')
plt.plot(val_losses, label='Validation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.title('Training Curves')

plt.subplot(1, 2, 2)
plt.plot(maes, label='MAE')
plt.xlabel('Epoch')
plt.ylabel('MAE (stars)')
plt.legend()
plt.title('Mean Absolute Error')

plt.tight_layout()
plt.savefig('training_curves.png')
plt.show()
Hyperparameter Tuning
from sklearn.model_selection import ParameterGrid

# Define hyperparameter grid
param_grid = {
    'learning_rate': [1e-5, 2e-5, 5e-5],
    'batch_size': [8, 16, 32],
    'hidden_dim': [128, 256, 512],
    'dropout': [0.1, 0.2, 0.3]
}

best_mae = float('inf')
best_params = None

for params in ParameterGrid(param_grid):
    print(f"\nTesting: {params}")
    
    # Reinitialize model with new params
    model = UserModelingBERT(
        num_users=num_users,
        num_products=num_products,
        hidden_dim=params['hidden_dim'],
        dropout=params['dropout']
    )
    
    # Create dataloaders with batch size
    train_loader = DataLoader(train_dataset, batch_size=params['batch_size'], shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=params['batch_size'] * 2)
    
    # Train
    trainer = ModelTrainer(model, train_loader, val_loader, learning_rate=params['learning_rate'])
    _, _, maes = trainer.train(n_epochs=3)
    
    final_mae = maes[-1]
    
    if final_mae < best_mae:
        best_mae = final_mae
        best_params = params
        print(f"✓ New best! MAE: {final_mae:.3f}")

print(f"\n Best Parameters: {best_params}")
print(f" Best MAE: {best_mae:.3f}")
Configuration
System Configuration File
Create a config.yaml file:

# BERT Recommendation System Configuration

model:
  bert_model_name: "bert-base-uncased"
  embedding_dim: 768
  hidden_dim: 256
  dropout: 0.1
  num_attention_heads: 8

training:
  batch_size: 16
  learning_rate: 0.00002
  n_epochs: 5
  warmup_ratio: 0.1
  weight_decay: 0.01
  gradient_clip: 1.0
  save_best: true
  checkpoint_dir: "./checkpoints"

data:
  max_text_length: 128
  validation_split: 0.1
  random_seed: 42
  min_review_length: 10

recommendation:
  default_n_recommendations: 5
  similarity_metric: "cosine"
  cold_start_strategy: "popularity"
  context_weight: 0.3

generation:
  temperature: 0.7
  max_length: 50
  num_return_sequences: 1
  do_sample: true

logging:
  log_level: "INFO"
  log_file: "system.log"
  tensorboard: true
  metrics_interval: 100

api:
  host: "0.0.0.0"
  port: 5000
  debug: false
  rate_limit: 100
Loading Configuration
import yaml

def load_config(config_path='config.yaml'):
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    return config

config = load_config()
print(f"Model config: {config['model']}")
print(f"Training config: {config['training']}")
Performance Metrics
Evaluation Metrics
Metric	Description	Target
MAE	Mean Absolute Error for rating prediction	< 0.5 stars
RMSE	Root Mean Square Error	< 0.7 stars
Accuracy@1	Top-1 recommendation accuracy	> 30%
Recall@10	Recall at 10 recommendations	> 60%
NDCG@10	Normalized Discounted Cumulative Gain	> 0.7
Perplexity	Review generation quality	< 50
Computing Metrics
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

def evaluate_review_simulation(review_agent, test_pairs):
    """Evaluate review simulation performance"""
    predictions = []
    actuals = []
    
    for user_id, product_id, true_rating in test_pairs:
        result = review_agent.simulate_review(user_id, product_id)
        predictions.append(result['predicted_rating'])
        actuals.append(true_rating)
    
    mae = mean_absolute_error(actuals, predictions)
    rmse = np.sqrt(mean_squared_error(actuals, predictions))
    
    # Accuracy within 1 star
    within_1 = np.mean([abs(p - a) <= 1 for p, a in zip(predictions, actuals)])
    
    return {
        'MAE': mae,
        'RMSE': rmse,
        'Accuracy@1star': within_1
    }

def evaluate_recommendations(rec_agent, test_users, ground_truth):
    """Evaluate recommendation performance"""
    hits_at_k = {1: 0, 5: 0, 10: 0}
    total = 0
    
    for user_id in test_users:
        recs = rec_agent.recommend_for_user(user_id, n_recommendations=10)
        recommended_products = [r['product_id'] for r in recs['recommendations']]
        relevant = ground_truth.get(user_id, [])
        
        for k in hits_at_k.keys():
            if any(p in recommended_products[:k] for p in relevant):
                hits_at_k[k] += 1
        total += 1
    
    return {f'Recall@{k}': hits_at_k[k] / total for k in hits_at_k.keys()}
Deployment
Docker Deployment
Create a Dockerfile:

FROM pytorch/pytorch:1.9.0-cuda11.1-cudnn8-runtime

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Download BERT model
RUN python -c "from transformers import AutoTokenizer, AutoModel; AutoTokenizer.from_pretrained('bert-base-uncased'); AutoModel.from_pretrained('bert-base-uncased')"

EXPOSE 5000

CMD ["python", "app.py"
Build and run:

# Build the Docker image
docker build -t bert-recommendation-system .

# Run the container
docker run -p 5000:5000 --gpus all bert-recommendation-system
Cloud Deployment (AWS SageMaker)
import boto3
import sagemaker
from sagemaker.pytorch import PyTorchModel

# Upload model artifacts
s3_model_path = 's3://your-bucket/models/bert-recommendation/'

# Create SageMaker model
model = PyTorchModel(
    model_data=s3_model_path,
    role=sagemaker.get_execution_role(),
    entry_point='inference.py',
    framework_version='1.9',
    py_version='py3'
)

# Deploy to endpoint
predictor = model.deploy(
    initial_instance_count=1,
    instance_type='ml.g4dn.xlarge'
)

# Make predictions
result = predictor.predict({
    'task': 'recommend',
    'user_id': 'User_123',
    'n_recommendations': 5
})
Production API Server
# production_api.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

app = FastAPI(title="BERT Recommendation API")

# Request/Response models
class RecommendRequest(BaseModel):
    user_id: str
    n_recommendations: Optional[int] = 5
    context: Optional[dict] = None

class SimulateRequest(BaseModel):
    user_id: str
    product_id: str
    year: Optional[int] = 2023

class ConversationRequest(BaseModel):
    conversation: List[str]
    user_id: Optional[str] = None

# Initialize system (once at startup)
system = None

@app.on_event("startup")
async def startup_event():
    global system
    system = create_complete_system('Task1.csv')
    print("System initialized successfully")

@app.get("/health")
async def health_check():
    return {"status": "healthy", "model_loaded": system is not None}

@app.post("/recommend")
async def get_recommendations(request: RecommendRequest):
    try:
        result = system.rec_agent.recommend_for_user(
            request.user_id,
            n_recommendations=request.n_recommendations,
            context=request.context
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/simulate")
async def simulate_review(request: SimulateRequest):
    try:
        result = system.review_agent.simulate_review(
            request.user_id,
            request.product_id,
            request.year
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/converse")
async def conversational_recommend(request: ConversationRequest):
    try:
        result = system.rec_agent.conversational_recommendation(
            request.conversation,
            request.user_id
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
Troubleshooting
Common Issues and Solutions
Issue	Possible Cause	Solution
Out of Memory	Batch size too large	Reduce batch size in config
Slow Training	CPU training	Enable GPU with CUDA_VISIBLE_DEVICES=0
Poor Predictions	Insufficient data	Collect more training data or use data augmentation
BERT Download Fails	Network issues	Download manually from Hugging Face
Cold-start Poor Performance	No user data	Use transfer learning from similar domains
Debugging Tips
# Enable detailed logging
import logging
logging.basicConfig(level=logging.DEBUG)

# Check GPU availability
print(f"CUDA available: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"GPU: {torch.cuda.get_device_name(0)}")
    print(f"Memory: {torch.cuda.get_device_properties(0).total_memory / 1e9:.1f} GB")

# Profile model size
def get_model_size(model):
    param_size = sum(p.numel() for p in model.parameters())
    buffer_size = sum(b.numel() for b in model.buffers())
    return (param_size + buffer_size) * 4 / (1024 ** 2)  # MB

print(f"Model size: {get_model_size(model):.2f} MB")

# Check for NaN losses
def check_nan(loss):
    if torch.isnan(loss):
        print("WARNING: NaN loss detected!")
        return True
    return False
Contributing
We welcome contributions! Please follow these steps:

Fork the repository
Create a feature branch
git checkout -b feature/amazing-feature
Commit your changes
git commit -m 'Add amazing feature'
Push to the branch
git push origin feature/amazing-feature
Open a Pull Request
Development Setup
# Clone your fork
git clone https://github.com/yourusername/bert-recommendation-system.git
cd bert-recommendation-system

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest tests/

# Run linting
flake8 bert_recommendation_system/

# Format code
black bert_recommendation_system/
License
This project is licensed under the MIT License - see the LICENSE file for details.

MIT License

Copyright (c) 2024 BERT Recommendation System

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
Acknowledgments
Hugging Face for the transformers library and pre-trained BERT models
PyTorch for the deep learning framework
BERT Paper by Devlin et al. for the foundational architecture
Citation
If you use this system in your research, please cite:

@software{bert_recommendation_system,
  author = {Your Name},
  title = {BERT-Based Recommendation \& User Modeling System},
  year = {2024},
  url = {https://github.com/yourusername/bert-recommendation-system}
}
>>>>>>> 1119dba3c19b9ce014dbdbc237827e740902a2d6
