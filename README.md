# 🚀 Support Vector Regression (SVR) Interactive Dashboard

![Visitor Count](https://komarev.com/ghpvc/?username=shuvayan007&repo=SVR-Dashboard-Heroku&color=blue)

An **interactive machine learning dashboard** built with **Streamlit** that allows users to experiment with **Support Vector Regression (SVR) hyperparameters** and visualize how they affect model performance on **2D datasets**.

This project is designed to help **students, ML practitioners, and aspiring data scientists** understand the behavior of **Support Vector Machines in regression tasks** in an intuitive and visual way.

---

## 🌐 Live Demo

🔗 **Try the Dashboard:**  

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://svr-dashboard.streamlit.app/)

---

## 🧠 Project Overview

**Support Vector Regression (SVR)** is a powerful machine learning algorithm derived from **Support Vector Machines (SVM)** that is widely used for regression tasks.

However, understanding how different **kernel functions and hyperparameters influence the regression curve** can be challenging.

This dashboard provides an **interactive learning environment** where users can:

- Adjust SVR hyperparameters
- Train the model instantly
- Visualize regression curves
- Observe performance changes in real-time

All through an **easy-to-use graphical interface**.

---

## ✨ Features

✅ Interactive **Streamlit Dashboard**  
✅ **Real-time model training** after parameter tuning  
✅ **Regression curve visualization** on 2D datasets  
✅ Adjustable **SVR hyperparameters**  
✅ Performance metrics display  
✅ Educational tool for understanding **Support Vector Machines**

---

## ⚙️ Adjustable Hyperparameters

The dashboard allows users to modify key **SVR parameters** from the **sidebar (hamburger panel)**:

| Parameter | Description |
|----------|-------------|
| `kernel` | Kernel type (linear, poly, rbf, sigmoid) |
| `C` | Regularization parameter controlling model complexity |
| `epsilon` | Defines the epsilon-tube within which no penalty is associated |
| `gamma` | Kernel coefficient for non-linear kernels |
| `degree` | Degree of polynomial kernel (if poly kernel is used) |

Users can experiment with these parameters to observe **how the regression model adapts to the dataset**.

---

## 📊 Visualization

The dashboard visualizes:

- Regression curve of the trained model
- Data distribution in 2D
- Prediction results
- Model performance metrics

This makes the algorithm's learning process **easy to understand visually**.

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **Scikit-learn**
- **NumPy**
- **Matplotlib**
- **Pandas**

---

## 📁 Project Structure

```
SVR-Dashboard-Heroku
│
├── app.py                 # Streamlit application
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
│
└── assets
    └── dashboard_preview.png
```

---

## 🚀 Installation & Local Setup

Clone the repository:

```bash
git clone https://github.com/shuvayan007/SVR-Dashboard-Heroku.git
```

Navigate to the project directory:

```bash
cd SVR-Dashboard-Heroku
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit app:

```bash
streamlit run app.py
```

---

## 🎯 Use Cases

- Machine Learning **education**
- Understanding **Support Vector Machines**
- Demonstrating **hyperparameter tuning**
- Interactive **ML teaching tools**
- Portfolio project for **data science learners**

---

## 📸 Dashboard Preview

<img width="1920" height="1043" alt="image" src="https://github.com/user-attachments/assets/bd44d2f2-52ca-489d-9e4f-639ba1ac20cb" />

---

## 💡 Future Improvements

- Add support for **Kernel comparison visualization**
- Add **multiple dataset selection**
- Add **3D regression visualization**
- Add **training time comparison**
- Add **model evaluation dashboard**

---

## 🤝 Contributing

Contributions are welcome!

If you'd like to improve this project:

1. Fork the repository  
2. Create a feature branch  
3. Submit a pull request  

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

**Shuvayan Pal**

Data Scientist | AI Engineer | Machine Learning Enthusiast

💼 LinkedIn  
🧠 Passionate about **AI, Machine Learning, and building intelligent systems**

---

⭐ If you found this project useful, please consider **starring the repository**!
