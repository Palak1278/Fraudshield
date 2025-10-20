Project Name: FraudShield – SMS Fraud Detection System
Developed by: Palak

Project Description:
FraudShield is a machine learning–based web application that detects whether an SMS message is spam or legitimate.
It uses Natural Language Processing (NLP) techniques for text cleaning and classification.
The interface is created using Flask (Python backend) and HTML, CSS, and JavaScript (frontend).

Folder Structure:
- app.py → Main backend Flask file
- model.joblib → Trained spam detection model
- vectorizer.joblib → Text vectorizer used by the model
- templates/ → Contains index.html and other pages
- static/ → Contains CSS, images, and JavaScript files
- spam.csv → Dataset used for training (if needed)
- fraudshield_model.ipynb → Jupyter file used for model creation

How to Run Locally:
1. Open Command Prompt and go to the project folder using:
   cd Desktop\FraudShield
2. Install all required packages:
   pip install -r requirements.txt
3. (Optional) Download NLTK corpora:
   python -m textblob.download_corpora
4. Run the application:
   python app.py
5. Open your browser and go to:
   http://127.0.0.1:5000/

Description:
Enter an SMS message in the text box and click "Check".
The app will display whether the message is spam or legitimate, along with a spam probability bar and cleaned text.