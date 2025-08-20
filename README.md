# 🧠 Healthcare Recommender System Using Neo4j

Welcome to my graph-powered healthcare recommendation engine! This project combines the power of Neo4j's graph database with machine learning and a Flask-based web interface to deliver intelligent health suggestions based on patient symptoms and relationships.

Built as part of my exploration into graph technologies and smart healthcare systems, this repo demonstrates how interconnected data can drive meaningful insights. Whether you're testing locally or deploying to the cloud, this guide will walk you through setup, usage, and customization.

---

## 📁 Project Structure

- `healthcare_recommender.py` – Graph logic: nodes, relationships, queries
- `ml_predictor.py` – ML model for treatment prediction
- `web_app.py` – Flask server and user interface
- `utils.py` – Helper functions
- `tests.py` – Unit tests for graph and ML logic

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/charwick-K/Healthcare_Recommender-Neo4j.git
cd Healthcare_Recommender-Neo4j
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install neo4j flask scikit-learn pandas numpy
```

---

## 🧬 Neo4j Configuration

### Option A: Local Neo4j (Recommended for Development)

- Download Neo4j Desktop: [neo4j.com/download](https://neo4j.com/download)
- Create a new database (default URI: `bolt://localhost:7687`)
- Set your username and password
- Start the database

### Option B: Neo4j Aura (Cloud)

- Sign up at [neo4j.com/aura](https://neo4j.com/aura)
- Use your Aura Bolt URI: `neo4j+s://<your-id>.databases.neo4j.io:7687`

Update connection details in `web_app.py`:

```python
URI = "bolt://localhost:7687"  # or your Aura URI
USER = "neo4j"
PASSWORD = "your_password"
```

---

## 🧾 Load Sample Data

To populate the graph with demo patients, symptoms, and treatments:

```bash
python healthcare_recommender.py
```

This script creates nodes and relationships. You can extend it to load CSVs or real-world datasets using `import_from_csv()`.

---

## 🌐 Launch the Web App

```bash
python web_app.py
```

Visit [http://localhost:5000](http://localhost:5000) in your browser. Enter a patient name (e.g., `Rohit`) to view health recommendations.

---

## ✅ Run Tests

```bash
python tests.py
```

This runs unit tests for graph queries and ML predictions.

---

## 🧯 Troubleshooting

- **Neo4j Connection Errors**: Ensure the database is running and Bolt port (7687) is open.
- **Missing Modules**: Recheck your `pip install` steps.
- **Empty Graph**: Rerun `create_sample_data()` or use `import_from_csv()` if available.
- **ML Warnings**: Replace dummy data in `ml_predictor.py` with real features for production use.

---

## 📦 Deployment Tips

For production:

```bash
pip install gunicorn
gunicorn -w 4 web_app:app
```

You can also containerize with Docker or deploy to platforms like Heroku. Want to add a UI layer? Try Gradio or integrate IBM Watson for smarter predictions.

---

## 🧠 Author

**Kondru Charwick Hamesh**  
Graph enthusiast | Embedded systems tinkerer | Simulation engineer  
Read more: [Why I Fell in Love with Neo4j](https://medium.com/@charwick14/why-i-fell-in-love-with-neo4j-from-sql-fatigue-to-hands-on-graph-magic-0d82c4c9c302)

## 📜 License

MIT License — free to use, modify, and share.

Let me know if you'd like to add badges, screenshots, or a contribution guide. I can also help you prep this for GraphAcademy certification or turn it into a portfolio piece.
