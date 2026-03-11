import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_error


# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="SVR Dashboard", page_icon="📈", layout="wide")


# -----------------------------
# DATA LOADING
# -----------------------------
@st.cache_data
def load_data():
    X, y = load_diabetes(return_X_y=True)
    X = X[:, 9].reshape(-1, 1)   # Use feature 9
    return train_test_split(X, y, test_size=0.2, random_state=42)


X_train, X_test, y_train, y_test = load_data()


# -----------------------------
# SIDEBAR UI
# -----------------------------
st.sidebar.title("Support Vector Regression")

mode = st.sidebar.radio(
    "Hyperparameter Mode",
    ["Default", "Custom Tuning"]
)

# Default parameters
params = {
    "kernel": "rbf",
    "degree": 3,
    "gamma": "scale",
    "coef0": 0.0,
    "tol": 0.001,
    "C": 1.0,
    "epsilon": 0.1,
    "shrinking": True,
    "cache_size": 200,
    "verbose": False,
    "max_iter": -1
}


# -----------------------------
# TUNING PANEL
# -----------------------------
if mode == "Custom Tuning":

    st.sidebar.info(
        "All parameters start with default values. Adjust them as needed."
    )

    params["kernel"] = st.sidebar.selectbox(
        "Kernel",
        ["rbf", "linear", "poly", "sigmoid"]
    )

    if params["kernel"] == "poly":
        params["degree"] = st.sidebar.slider("Polynomial Degree", 2, 10, 3)

    if params["kernel"] in ["rbf", "poly", "sigmoid"]:
        gamma_option = st.sidebar.selectbox(
            "Gamma",
            ["scale", "auto", "custom"]
        )

        if gamma_option == "custom":
            params["gamma"] = st.sidebar.number_input(
                "Gamma Value", value=0.01
            )
        else:
            params["gamma"] = gamma_option

    if params["kernel"] in ["poly", "sigmoid"]:
        params["coef0"] = st.sidebar.number_input("coef0", value=0.0)

    params["tol"] = st.sidebar.number_input(
        "Tolerance", value=0.001, step=0.001
    )

    params["C"] = st.sidebar.number_input(
        "Regularization (C)", min_value=0.01, value=1.0
    )

    params["epsilon"] = st.sidebar.number_input(
        "Epsilon", min_value=0.0, value=0.1
    )

    params["shrinking"] = st.sidebar.selectbox(
        "Shrinking", [True, False]
    )

    params["cache_size"] = st.sidebar.number_input(
        "Cache Size (MB)", value=200
    )

    params["verbose"] = st.sidebar.selectbox(
        "Verbose Output", [True, False]
    )

    params["max_iter"] = st.sidebar.slider(
        "Max Iterations", -1, 500, -1
    )

    with st.sidebar.expander("Tips 💡"):
        st.info(
            "Shrinking may speed up training for large iteration counts. "
            "If tolerance is large, disabling shrinking may be faster."
        )


# -----------------------------
# MODEL
# -----------------------------
model = SVR(**params)


# -----------------------------
# INITIAL PLOT
# -----------------------------
fig, ax = plt.subplots()

X_plot = np.concatenate([X_train, X_test])
y_plot = np.concatenate([y_train, y_test])

ax.scatter(X_plot, y_plot)
ax.set_xlabel("Feature")
ax.set_ylabel("Target")

plot_placeholder = st.pyplot(fig)


# -----------------------------
# TRAIN BUTTON
# -----------------------------
if st.sidebar.button("Run Algorithm"):

    with st.spinner("Training SVR model..."):

        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)

        x_line = np.linspace(
            X_plot.min(),
            X_plot.max(),
            500
        ).reshape(-1, 1)

        y_line = model.predict(x_line)

        fig, ax = plt.subplots()

        ax.scatter(X_plot, y_plot)
        ax.plot(x_line, y_line)

        ax.set_xlabel("Feature")
        ax.set_ylabel("Target")

        plot_placeholder.pyplot(fig)

        mae = mean_absolute_error(y_test, y_pred)

        st.sidebar.success(
            f"Mean Absolute Error: {mae:.2f}"
        )

    st.success("Training Complete!")
