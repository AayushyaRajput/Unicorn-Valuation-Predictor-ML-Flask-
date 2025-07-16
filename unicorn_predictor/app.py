from flask import Flask, request, render_template
import pickle
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained model and feature columns
model = pickle.load(open('unicorn_valuation_model.pkl', 'rb'))
model_columns = joblib.load(open('model_columns.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Convert form data to dictionary
        form_data = request.form.to_dict()
        print("📥 Received form data:", form_data)

        # Create input dataframe with all expected model columns
        input_df = pd.DataFrame([[0]*len(model_columns)], columns=model_columns)

        # Fill in the user inputs where column names match
        for key, value in form_data.items():
            if key in input_df.columns:
                input_df.at[0, key] = float(value)

        # Predict valuation
        prediction = model.predict(input_df)
        return render_template('index.html', prediction_text=f'🦄 Predicted Valuation: ${prediction[0]:.2f}B')

    except Exception as e:
        return render_template('index.html', prediction_text=f"❌ Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)

