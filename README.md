# Unicorn-Valuation-Predictor-ML-Flask-
A machine learning-powered Flask web app that predicts the valuation of startup unicorns based on country, industry, and major investors. Built using scikit-learn, styled with modern glassmorphism UI, and perfect for real-world ML deployment practice.

# 🦄 Unicorn Valuation Predictor (ML + Flask)

A machine learning-powered web app to **predict the valuation of startup unicorns** based on country, industry, and investors — deployed using Flask.

![Unicorn App Screenshot](Screenshot.png) <!-- Optional: Add your own screenshot URL -->

---

## 📊 Problem Statement

"Unicorn" refers to startups valued at **$1 Billion+**. This project uses a dataset of unicorn companies to **train a regression model** that predicts valuation based on categorical features like:

- Country (e.g. USA, India)
- Industry (e.g. Fintech, E-commerce)
- Investor (e.g. SoftBank, Tiger Global)

---

## 💡 Features

- 🧠 ML model (Random Forest Regressor)
- 🔍 Feature importance visualization
- 🌐 Flask web app with a modern UI (2025 glassmorphism)
- 🎨 Responsive design using Bootstrap 5
- 🧪 Predict valuation with just a few inputs (0/1)
- ✅ Perfect for showcasing on LinkedIn / GitHub portfolio

---

## 🧠 ML Model Details

- Trained using: `scikit-learn`
- Model: `RandomForestRegressor`
- Features: One-hot encoded from `Country`, `Industry`, `Main_Investor`
- Target: `Valuation ($B)`
- Preprocessing: OneHotEncoding, `model_columns.pkl` saved to ensure compatibility

---

## 🚀 Demo

> Run the Flask app locally:

```bash
git clone https://github.com/your-username/unicorn_predictor.git
cd unicorn_predictor
pip install -r requirements.txt
python app.py
