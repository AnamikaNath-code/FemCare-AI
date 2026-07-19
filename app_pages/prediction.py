#predicition.py
import streamlit as st
import joblib
import numpy as np

# =====================================
# LOAD TRAINED MODEL
# =====================================

model = joblib.load("models/pcos_model.pkl")
scaler = joblib.load("models/scaler.pkl")
feature_names = joblib.load("models/feature_names.pkl")


def prediction():

    st.title("🩺 PCOS Prediction")

    st.markdown(
        """
        Enter the patient's clinical information below.
        All values should be entered carefully for accurate prediction.
        """
    )

    st.divider()

    # =====================================
    # PERSONAL INFORMATION
    # =====================================

    st.subheader("👤 Personal Information")

    col1, col2 = st.columns(2)

    with col1:

        age = st.number_input(
            "Age (Years)",
            min_value=10,
            max_value=60,
            value=22
        )

        weight = st.number_input(
            "Weight (Kg)",
            min_value=20.0,
            max_value=150.0,
            value=60.0
        )

        height = st.number_input(
            "Height (cm)",
            min_value=100.0,
            max_value=220.0,
            value=160.0
        )

    with col2:

        bmi = weight / ((height / 100) ** 2)

        st.metric(
            "Calculated BMI",
            round(bmi, 2)
        )

        blood_group = st.selectbox(
            "Blood Group",
            [11, 12, 13, 14, 15, 16, 17, 18]
        )

    st.divider()

    # =====================================
    # VITAL SIGNS
    # =====================================

    st.subheader("❤️ Vital Signs")

    col1, col2 = st.columns(2)

    with col1:

        pulse = st.number_input(
            "Pulse Rate (bpm)",
            40,
            150,
            72
        )

        respiratory = st.number_input(
            "Respiratory Rate",
            10,
            40,
            18
        )

        hb = st.number_input(
            "Hemoglobin (g/dL)",
            value=12.0
        )

    with col2:

        systolic = st.number_input(
            "Systolic BP",
            value=120
        )

        diastolic = st.number_input(
            "Diastolic BP",
            value=80
        )

    st.divider()

    # =====================================
    # MENSTRUAL HISTORY
    # =====================================

    st.subheader("📅 Menstrual History")

    col1, col2 = st.columns(2)

    with col1:

        cycle = st.selectbox(
            "Cycle",
            ["Regular", "Irregular"]
        )

        cycle_length = st.number_input(
            "Cycle Length (Days)",
            value=28
        )

        marriage = st.number_input(
            "Marriage Duration (Years)",
            value=2
        )

    with col2:

        pregnant = st.selectbox(
            "Pregnant",
            ["No", "Yes"]
        )

        abortions = st.number_input(
            "Number of Abortions",
            value=0
        )

    st.divider()

    # =====================================
    # HORMONAL PROFILE
    # =====================================

    st.subheader("🧬 Hormonal Profile")

    col1, col2 = st.columns(2)

    with col1:

        beta1 = st.number_input(
            "Beta HCG I",
            value=1.0
        )

        beta2 = st.number_input(
            "Beta HCG II",
            value=1.0
        )

        fsh = st.number_input(
            "FSH (mIU/mL)",
            value=5.0
        )

        lh = st.number_input(
            "LH (mIU/mL)",
            value=5.0
        )

        if lh != 0:
            ratio = fsh / lh
        else:
            ratio = 0

        st.metric(
            "FSH/LH Ratio",
            round(ratio, 2)
        )

    with col2:

        tsh = st.number_input(
            "TSH",
            value=2.5
        )

        amh = st.number_input(
            "AMH",
            value=3.0
        )

        prl = st.number_input(
            "Prolactin",
            value=10.0
        )

        vitamin_d = st.number_input(
            "Vitamin D",
            value=30.0
        )

        progesterone = st.number_input(
            "Progesterone",
            value=1.0
        )

        rbs = st.number_input(
            "Random Blood Sugar",
            value=90.0
        )

    st.divider()

    # =====================================
    # LIFESTYLE FACTORS
    # =====================================

    st.subheader("🥗 Lifestyle Factors")

    col1, col2 = st.columns(2)

    with col1:

        weight_gain = st.selectbox(
            "Weight Gain",
            ["No", "Yes"]
        )

        hair_growth = st.selectbox(
            "Excess Hair Growth",
            ["No", "Yes"]
        )

        skin_darkening = st.selectbox(
            "Skin Darkening",
            ["No", "Yes"]
        )

        hair_loss = st.selectbox(
            "Hair Loss",
            ["No", "Yes"]
        )

    with col2:

        pimples = st.selectbox(
            "Pimples",
            ["No", "Yes"]
        )

        fast_food = st.selectbox(
            "Frequent Fast Food",
            ["No", "Yes"]
        )

        exercise = st.selectbox(
            "Regular Exercise",
            ["No", "Yes"]
        )

    st.divider()

    # =====================================
    # BODY MEASUREMENTS
    # =====================================

    st.subheader("📏 Body Measurements")

    col1, col2 = st.columns(2)

    with col1:

        hip = st.number_input(
            "Hip (inch)",
            min_value=20.0,
            max_value=80.0,
            value=36.0
        )

        waist = st.number_input(
            "Waist (inch)",
            min_value=20.0,
            max_value=80.0,
            value=30.0
        )

    with col2:

        if hip != 0:
            waist_hip = waist / hip
        else:
            waist_hip = 0

        st.metric(
            "Waist-Hip Ratio",
            round(waist_hip, 2)
        )

    st.divider()

    # =====================================
    # ULTRASOUND PARAMETERS
    # =====================================

    st.subheader("🩻 Ultrasound Parameters")

    col1, col2 = st.columns(2)

    with col1:

        follicle_left = st.number_input(
            "Follicle No. (Left)",
            min_value=0,
            value=8
        )

        follicle_right = st.number_input(
            "Follicle No. (Right)",
            min_value=0,
            value=8
        )

        avg_left = st.number_input(
            "Average Follicle Size (Left)",
            value=8.0
        )

    with col2:

        avg_right = st.number_input(
            "Average Follicle Size (Right)",
            value=8.0
        )

        endometrium = st.number_input(
            "Endometrium (mm)",
            value=8.0
        )

    st.divider()

    # =====================================
    # PREDICT BUTTON
    # =====================================

    st.markdown("## 🔍 Prediction")

    predict_btn = st.button(
        "🩷 Predict PCOS",
        use_container_width=True
    )
    # =====================================
    # PREDICTION
    # =====================================

    if predict_btn:

        # Convert categorical inputs
        cycle_value = 2 if cycle == "Regular" else 4

        pregnant_value = 1 if pregnant == "Yes" else 0
        weight_gain_value = 1 if weight_gain == "Yes" else 0
        hair_growth_value = 1 if hair_growth == "Yes" else 0
        skin_darkening_value = 1 if skin_darkening == "Yes" else 0
        hair_loss_value = 1 if hair_loss == "Yes" else 0
        pimples_value = 1 if pimples == "Yes" else 0
        fast_food_value = 1 if fast_food == "Yes" else 0
        exercise_value = 1 if exercise == "Yes" else 0

        # Arrange features in EXACT training order
        input_data = [[
            age,
            weight,
            height,
            bmi,
            blood_group,
            pulse,
            respiratory,
            hb,
            cycle_value,
            cycle_length,
            marriage,
            pregnant_value,
            abortions,
            beta1,
            beta2,
            fsh,
            lh,
            ratio,
            hip,
            waist,
            waist_hip,
            tsh,
            amh,
            prl,
            vitamin_d,
            progesterone,
            rbs,
            weight_gain_value,
            hair_growth_value,
            skin_darkening_value,
            hair_loss_value,
            pimples_value,
            fast_food_value,
            exercise_value,
            systolic,
            diastolic,
            follicle_left,
            follicle_right,
            avg_left,
            avg_right,
            endometrium
        ]]

        # Scale features
        input_scaled = scaler.transform(input_data)

        # Save input for Explainable AI page
        st.session_state["patient_input"] = input_data
        st.session_state["patient_input_scaled"] = input_scaled

        # Predict
        prediction = model.predict(input_scaled)[0]

        probability = model.predict_proba(input_scaled)[0][1]

        st.divider()

        st.header("📋 Prediction Result")

        if prediction == 1:

            st.error("⚠️ High Risk of PCOS")

        else:

            st.success("✅ Low Risk of PCOS")

        st.metric(
            "Prediction Probability",
            f"{probability*100:.2f}%"
        )

        st.progress(float(probability))

        st.divider()

        st.subheader("🩺 Clinical Recommendation")

        if prediction == 1:

            st.warning("""
### Please consult a healthcare professional.

Recommendations:

• Schedule a gynecologist consultation.

• Consider hormonal evaluation.

• Maintain a healthy body weight.

• Exercise regularly.

• Reduce processed & sugary foods.

• Monitor menstrual cycles regularly.

• Follow medical advice before starting treatment.
""")

        else:

            st.success("""
### No significant PCOS risk detected.

Recommendations:

• Maintain a healthy lifestyle.

• Continue regular exercise.

• Eat a balanced diet.

• Stay hydrated.

• Schedule routine health check-ups.

• Monitor symptoms if they develop.
""")

        st.divider()

        st.info(
            "⚠️ This prediction is generated using a Machine Learning model and is intended to assist—not replace—a qualified medical diagnosis."
        )
                