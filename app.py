from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the saved model
model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get values from form
        features = [float(x) for x in request.form.values()]
        final_features = np.array([features])
        
        # Make prediction
        prediction = model.predict(final_features)[0]
        output = round(prediction, 2)

        return render_template("index.html", prediction_text=f"🏠 Predicted House Price: ${output * 1000}")
    except Exception as e:
        return render_template("index.html", prediction_text=f"⚠️ Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
