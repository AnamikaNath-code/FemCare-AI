import streamlit as st
import pandas as pd
import numpy as np
import joblib
import shap
import matplotlib.pyplot as plt

# -----------------------------
# PAGE
# -----------------------------
def explainable_ai():

    st.title("🧠 Explainable AI")

    st.markdown("""
    Understand how the Random Forest model makes predictions using SHAP
    (SHapley Additive exPlanations).
    """)

    # -----------------------------
    # Load Files
    # -----------------------------
    model = joblib.load("models/pcos_model.pkl")
    scaler = joblib.load("models/scaler.pkl")
    feature_names = joblib.load("models/feature_names.pkl")

    # -----------------------------
    # Sample Input
    # -----------------------------
    st.subheader("Sample Patient")

    sample = pd.DataFrame(
        [np.zeros(len(feature_names))],
        columns=feature_names
    )

    st.dataframe(sample)

    # Scale sample
    sample_scaled = scaler.transform(sample)

    # -----------------------------
    # SHAP
    # -----------------------------
    explainer = shap.TreeExplainer(model)

    shap_values = explainer.shap_values(sample_scaled)

    # -----------------------------
    # Summary
    # -----------------------------
    st.subheader("Feature Contribution")

    fig, ax = plt.subplots(figsize=(8,6))

    shap.summary_plot(
        shap_values[:, :, 1],
        sample_scaled,
        feature_names=feature_names,
        show=False
    )

    st.pyplot(fig)

    plt.clf()

    # -----------------------------
    # Feature Importance
    # -----------------------------
    st.subheader("⭐ Top Influential Features")

    importance = pd.DataFrame({

        "Feature": feature_names,

        "Importance": np.abs(shap_values[:, :, 1]).mean(axis=0)

    })

    importance = importance.sort_values(
        "Importance",
        ascending=False
    )

    st.dataframe(importance.head(10))

    # -----------------------------
    # Waterfall Plot
    # -----------------------------
    st.subheader("Prediction Explanation")

    explanation = shap.Explanation(

        values=shap_values[0, :, 1],

        base_values=explainer.expected_value[1],

        data=sample_scaled[0],

        feature_names=feature_names

    )

    fig2 = plt.figure(figsize=(10,6))

    shap.plots.waterfall(
        explanation,
        show=False
    )

    st.pyplot(fig2)

    plt.close("all")