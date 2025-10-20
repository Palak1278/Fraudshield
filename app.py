from flask import Flask, request, jsonify, render_template, send_from_directory
import joblib
import re
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
STOPWORDS = set(stopwords.words('english'))
app = Flask(__name__)
model = joblib.load('model.joblib')
vectorizer = joblib.load('vectorizer.joblib')
def clean_text(s):
    s = str(s).lower()
    s = re.sub(r"https?://\S+|www\.\S+", " <URL> ", s)
    s = re.sub(r"\d+", " <NUM> ", s)
    s = re.sub(r"[^\w\s<>]", " ", s)
    tokens = s.split()
    tokens = [t for t in tokens if t not in STOPWORDS]
    return " ".join(tokens)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/cybersafetyhub")
def cyber_safety_hub():
    return render_template("cyber_info.html")
@app.route('/templates/<path:filename>')
def custom_static(filename):
    return send_from_directory('templates', filename)
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json() or {}
    text = data.get('text', "")
    cleaned = clean_text(text)
    vec = vectorizer.transform([cleaned])
    try:
        prob = float(model.predict_proba(vec)[0][1])
        pred = int(model.predict(vec)[0])
    except Exception:
        prob = None
        pred = 0
    label = "Spam" if pred == 1 else "Legitimate"
    return jsonify({"label": label, "probability": prob, "clean": cleaned})
if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)