# 🚀 Gradient Boosting Interactive Dashboard

![Visitor Count](https://komarev.com/ghpvc/?username=shuvayan007&repo=gb-dashboard-heroku&color=blue)

An **interactive machine learning dashboard** built with **Streamlit** that allows users to experiment with **Gradient Boosting hyperparameters** and visualize how they affect model performance on **2D datasets**.

This project is designed to help **students, ML practitioners, and aspiring data scientists** understand the behavior of Gradient Boosting in an intuitive and visual way.

---

## 🌐 Live Demo

🔗 **Try the Dashboard:**  
https://gb-dashboard-v3.streamlit.app/

---

## 🧠 Project Overview

Gradient Boosting is one of the most powerful ensemble learning algorithms used in machine learning. However, understanding how different hyperparameters affect its performance can be challenging.

This dashboard provides an **interactive learning environment** where users can:

- Adjust Gradient Boosting hyperparameters
- Train the model instantly
- Visualize decision boundaries
- Observe performance changes in real-time

All through an **easy-to-use graphical interface**.

---

## ✨ Features

✅ Interactive **Streamlit Dashboard**  
✅ **Real-time model training** after parameter tuning  
✅ **Visual decision boundary plotting** on 2D datasets  
✅ Adjustable **Gradient Boosting hyperparameters**  
✅ Performance metrics display  
✅ Educational tool for understanding **ensemble learning**

---

## ⚙️ Adjustable Hyperparameters

The dashboard allows users to modify key Gradient Boosting parameters from the **sidebar (hamburger panel)**:

| Parameter | Description |
|----------|-------------|
| `n_estimators` | Number of boosting stages |
| `learning_rate` | Shrinks the contribution of each tree |
| `max_depth` | Maximum depth of individual trees |
| `min_samples_split` | Minimum samples required to split a node |
| `min_samples_leaf` | Minimum samples required at a leaf node |
| `subsample` | Fraction of samples used for training |
| `random_state` | Controls randomness for reproducibility |

Users can experiment with these parameters to observe **how the model adapts to the dataset**.

---

## 📊 Visualization

The dashboard visualizes:

- Decision boundaries of the trained model
- Data distribution in 2D
- Classification regions
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
Gradient-Boosting-Dashboard
│
├── app.py # Streamlit application
├── requirements.txt # Project dependencies
├── README.md # Project documentation
│
└── assets
└── dashboard_preview.png
```

---

## 🚀 Installation & Local Setup

Clone the repository:

```bash
git clone https://github.com/your-username/gradient-boosting-dashboard.git
```
Gradient-Boosting-Dashboard│├── app.py # Streamlit application

Navigate to the project directory:

```bash
cd gradient-boosting-dashboard
```

Install dependencies:

```bash   
pip install -r requirements.txt
```

Run the Streamlit app:

```bash   
streamlit run app.py
```

🎯 Use Cases
------------

*   Machine Learning **education**
    
*   Understanding **ensemble learning**
    
*   Demonstrating **hyperparameter tuning**
    
*   Interactive **ML teaching tools**
    
*   Portfolio project for **data science learners**
    

📸 Dashboard Preview
--------------------

assets/dashboard_preview.png

💡 Future Improvements
----------------------

*   Add support for **XGBoost and LightGBM**
    
*   Add **multiple dataset selection**
    
*   Add **3D dataset visualization**
    
*   Add **training time comparison**
    
*   Add **model performance leaderboard**
    

🤝 Contributing
---------------

Contributions are welcome!

If you'd like to improve this project:

1.  Fork the repository
    
2.  Create a feature branch
    
3.  Submit a pull request
    

📜 License
----------

This project is licensed under the **MIT License**.

👨‍💻 Author
------------

**Shuvayan Pal**

Data Scientist | AI Engineer | Machine Learning Enthusiast

*   💼 LinkedIn
    
*   🧠 Passionate about **AI, Machine Learning, and building intelligent systems**
