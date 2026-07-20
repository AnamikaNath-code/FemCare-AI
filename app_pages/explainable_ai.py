import streamlit as st
import pandas as pd
import numpy as np
import joblib
import shap
import matplotlib.pyplot as plt

# ==========================================
# PAGE
# ==========================================

def explainable_ai():
   

    st.error("🚨 DEBUG MARKER: explainable_ai.py v2 is running 🚨")

    st.title("🧠 Explainable AI")
    ...

    st.title("🧠 Explainable AI")
    st.caption(
        "Understand how the Random Forest model arrived at its prediction using SHAP "
        "(SHapley Additive exPlanations)."
    )

    # ==========================================
    # CHECK PREDICTION
    # ==========================================

    if "patient_input_scaled" not in st.session_state:

        st.warning("⚠ Please make a prediction first from the Prediction page.")

        st.stop()

    # ==========================================
    # LOAD FILES
    # ==========================================

    model = joblib.load("models/pcos_model.pkl")
    feature_names = joblib.load("models/feature_names.pkl")

    patient_scaled = st.session_state["patient_input_scaled"]
    patient_input = st.session_state["patient_input"]

    prediction = st.session_state.get("prediction", None)
    probability = st.session_state.get("probability", None)

    # ==========================================
    # HEADER CARDS
    # ==========================================

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:

        if prediction == 1:
            st.error("🔴 High Risk")

        else:
            st.success("🟢 Low Risk")

    with col2:

        if probability is not None:

            st.metric(
                "Prediction Probability",
                f"{probability*100:.2f}%"
            )

    with col3:

        if probability is not None:

            confidence = max(probability, 1-probability)

            st.metric(
                "Model Confidence",
                f"{confidence*100:.2f}%"
            )

    st.divider()

    # ==========================================
    # PATIENT SUMMARY
    # ==========================================

    st.subheader("📋 Patient Summary")

    patient_df = pd.DataFrame(
        patient_input,
        columns=feature_names
    )

    display_columns = [
        "Age (yrs)",
        "BMI",
        "AMH(ng/mL)",
        "Cycle(R/I)",
        "Follicle No. (L)",
        "Follicle No. (R)",
        "FSH/LH"
    ]

    available = [
        c for c in display_columns
        if c in patient_df.columns
    ]

    st.dataframe(
        patient_df[available],
        use_container_width=True
    )

    st.divider()

    # ==========================================
    # SHAP EXPLAINER
    # ==========================================

    with st.spinner("Generating Explainable AI insights..."):

        explainer = shap.TreeExplainer(model)

        shap_values = explainer.shap_values(patient_scaled)

    # Binary classifier compatibility

    if isinstance(shap_values, list):

        shap_values = shap_values[1]

    elif len(shap_values.shape) == 3:

        shap_values = shap_values[:, :, 1]

    # ==========================================
    # FEATURE IMPORTANCE
    # ==========================================

    importance = pd.DataFrame({

        "Feature": feature_names,

        "SHAP Value": shap_values[0]

    })

    importance["Absolute"] = importance["SHAP Value"].abs()

    importance = importance.sort_values(
        "Absolute",
        ascending=False
    )

    st.subheader("⭐ Top 10 Most Influential Features")

    st.dataframe(
        importance.head(10)[["Feature", "SHAP Value"]],
        use_container_width=True
    )