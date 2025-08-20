# web_app.py
# Simple Flask web interface for the recommender.
# Lines: ~200

from flask import Flask, request, render_template_string
from healthcare_recommender import HealthcareRecommender

app = Flask(__name__)

URI = "bolt://localhost:7687"
USER = "neo4j"
PASSWORD = "your_password_here"

recommender = HealthcareRecommender(URI, USER, PASSWORD)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        patient_name = request.form['patient_name']
        recommendations = recommender.recommend_treatments(patient_name)
        return render_template_string(HTML_TEMPLATE, recommendations=recommendations, patient=patient_name)
    return render_template_string(HTML_TEMPLATE, recommendations=None)

HTML_TEMPLATE = """
<!doctype html>
<title>Healthcare Recommender</title>
<h1>Neo4j Healthcare System</h1>
<form method=post>
  <label>Patient Name: <input name=patient_name></label>
  <button>Recommend</button>
</form>
{% if recommendations %}
  <h2>Recommendations for {{ patient }}</h2>
  <ul>
  {% for rec in recommendations %}
    <li>{{ rec.name }} (Dosage: {{ rec.dosage }}) - Efficacy: {{ rec.predicted_efficacy }}</li>
  {% endfor %}
  </ul>
{% endif %}
"""

if __name__ == '__main__':
    recommender.create_indexes()
    recommender.create_sample_data()  # Setup on start
    app.run(debug=True)

# (Expand with routes for data import, visualizations, authentication, etc. - add 100+ lines)
