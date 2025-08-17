# 🏠 Boston House Price Prediction

An **AI-powered web application** that predicts Boston house prices based on property features such as crime rate, number of rooms, property tax, and more.  
Built with **Flask**, **Scikit-learn**, and a simple **HTML/CSS/JS** interface, the app is user-friendly and deployment-ready.

---

## 📸 Demo
[capture_20250817113538813.bmp](https://github.com/user-attachments/files/21822876/capture_20250817113538813.bmp)



---

## 📌 Features
- Modern and interactive web interface  
- Input **13 property features** to get predictions instantly  
- Model trained on the **Boston Housing Dataset**  
- Supports **Linear Regression** and **Random Forest** models  
- Deployment-ready for **Render**, **Heroku**, or **Vercel**  

---

## 📊 Dataset
The dataset used is the classic **Boston Housing Dataset**:  
[🔗 Boston Housing CSV](https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv)

**Columns:**
- `crim` : per capita crime rate  
- `zn` : proportion of residential land zoned  
- `indus` : proportion of non-retail business acres  
- `chas` : Charles River dummy variable (1 = yes, 0 = no)  
- `nox` : nitric oxide concentration  
- `rm` : average number of rooms per dwelling  
- `age` : proportion of owner-occupied units built before 1940  
- `dis` : distances to employment centers  
- `rad` : accessibility index to radial highways  
- `tax` : property tax rate  
- `ptratio` : pupil–teacher ratio  
- `b` : proportion of Black population  
- `lstat` : % lower status of the population  
- `medv` : **target variable** (median value of owner-occupied homes in $1000s)  

---

## 🚀 Tech Stack
- **Backend:** Flask, Scikit-learn, Pickle/Joblib  
- **Frontend:** HTML, CSS, JavaScript  
- **Deployment:** Render (with Gunicorn)  
- **Language:** Python  

---

## ⚙️ Installation & Run (Single Script)

```bash
# 1. Clone the repository
git clone https://github.com/YourUsername/House_Price_Prediction_Project.git
cd House_Price_Prediction_Project

# 2. Create and activate virtual environment
python -m venv venv
# On Windows
venv\Scripts\activate
# On Mac/Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Flask app
python app.py

# 5. Open your browser at:
# http://127.0.0.1:5000
