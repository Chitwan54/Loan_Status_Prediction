from flask import Flask, render_template, request, jsonify
import pickle as pkl
import pandas as pd

app = Flask(__name__)

# Load your pre-trained machine learning model
model = pkl.load(open('model_files/model.pkl', 'rb'))
scaler = pkl.load(open('model_files/scaler.pkl', 'rb'))

# Define a route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define a route for predicting loan approval
@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from the form
    input_data = {
        'cibil_score': int(request.form['Cibil Score']),
        'loan_term': request.form['Loan Term'],
    }

    # Convert input data to a DataFrame
    input_df = pd.DataFrame([input_data])
    input_df['cibil_score'] = input_df['cibil_score'].astype(float)
    input_df['loan_term'] = input_df['loan_term'].astype(float)

    input_df_scaled = scaler.transform(input_df)

    # Make predictions using the model
    prediction = model.predict_proba(input_df_scaled)[:, 1]
    best_threshold = 0.55589014

    # Display the prediction result
    result = 'Approved' if prediction > best_threshold else 'Not Approved'
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
