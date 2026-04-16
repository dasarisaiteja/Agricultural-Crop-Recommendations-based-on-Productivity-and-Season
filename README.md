# 🌱 Agricultural Crop Recommendation System

## 📌 Overview

The **Agricultural Crop Recommendation System** is a Machine Learning-based web application that helps farmers and agricultural stakeholders choose the most suitable crop based on environmental and soil conditions.

The system analyzes key inputs such as soil nutrients and climate factors to recommend the best crop for maximum productivity.

---

## 🚀 Features

* 🌾 Crop recommendation based on soil nutrients (N, P, K)
* 🌡️ Climate-based prediction (temperature, humidity, rainfall)
* 🤖 Machine Learning models (Random Forest, Decision Tree)
* 🌐 User-friendly web interface using Flask
* 📊 Accurate predictions for better agricultural planning

---

## 🛠️ Tech Stack

**Frontend:**

* HTML
* CSS
* Bootstrap

**Backend:**

* Python
* Flask

**Machine Learning:**

* Scikit-learn
* Pandas
* NumPy

---

## 📂 Project Structure

```
Agricultural-Crop-Recommendation/
│
├── app.py                  # Main Flask application
├── fix_model.py            # Model-related script
├── models/
│   ├── RandomForest.pkl    # Trained Random Forest model
│   ├── DecisionTree.pkl    # Trained Decision Tree model
│
├── templates/              # HTML templates
│   ├── index.html
│   ├── crop.html
│   ├── fertilizer.html
│
├── static/                 # CSS, images, JS
│
├── run.bat                 # Script to run the app
└── README.md               # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone <your-repo-link>
cd Agricultural-Crop-Recommendation
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

*(If requirements.txt is not available, install manually:)*

```bash
pip install flask numpy pandas scikit-learn
```

### 3️⃣ Run the application

```bash
python app.py
```

### 4️⃣ Open in browser

```
http://127.0.0.1:5000/
```

---

## 📊 Input Parameters

The model uses the following inputs:

* Nitrogen (N)
* Phosphorus (P)
* Potassium (K)
* Temperature (°C)
* Humidity (%)
* pH value
* Rainfall (mm)

---

## 🤖 Machine Learning Model

* **Random Forest Classifier** (Primary model)
* **Decision Tree Classifier** (Alternative model)

The model is trained on agricultural datasets to predict the most suitable crop.

---

## 📸 Output

* Recommended crop based on input conditions
* Helps improve yield and decision-making

---

## 🎯 Use Cases

* Farmers selecting crops for a season
* Agricultural students for learning ML applications
* Smart farming solutions
* Government/agriculture advisory systems

---

## 🔮 Future Enhancements

* 🌦️ Real-time weather API integration
* 📱 Mobile-friendly UI
* 🌍 Region-specific crop recommendations
* 📈 Yield prediction and analytics
* 🧪 Fertilizer and disease prediction modules

---

## 👨‍💻 Author

**Dasari Sai Teja**

* Full Stack Developer (Fresher)
* Skills: Python, HTML, CSS, Java, SQL

---

## 📜 License

This project is for educational purposes. You can modify and use it as needed.

---

## ⭐ Acknowledgements

* Scikit-learn documentation
* Open agricultural datasets
* Flask framework community
