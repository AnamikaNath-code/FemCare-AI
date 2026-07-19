import streamlit as st
from ui_components import hero, feature_card, stat_pill, section_header, divider, footer


def home():

    hero(
        title="FemCare AI 🌸",
        subtitle="An intelligent healthcare companion for early, explainable PCOS risk prediction — "
                  "using Machine Learning and Explainable AI."
    )

    divider()
    section_header("✨ Key Features")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        feature_card("🌲", "Random Forest", "Core ML model powering the risk prediction.")
    with col2:
        feature_card("🔍", "Explainable AI", "SHAP-based breakdown of what drove the result.")
    with col3:
        feature_card("📊", "Interactive Dashboard", "Explore your results visually.")
    with col4:
        feature_card("📈", "Risk Probability", "See your risk as a clear percentage.")

    col5, col6, col7, col8 = st.columns(4)
    with col5:
        feature_card("🥗", "Lifestyle Tips", "Personalized recommendations based on your inputs.")
    with col6:
        feature_card("⚙️", "Performance Metrics", "Transparent model accuracy and stats.")
    with col7:
        feature_card("🎙", "Voice Assistant", "Ask questions and hear the results aloud.")
    with col8:
        feature_card("💡", "User-Friendly", "Built for clarity, not just for developers.")

    divider()
    section_header("📊 Project Overview")

    col1, col2, col3 = st.columns(3)
    with col1:
        stat_pill("Random Forest", "Machine Learning")
    with col2:
        stat_pill("SHAP AI", "Explainability")
    with col3:
        stat_pill("PCOS Risk", "Prediction")

    # Everything below here is now OUTSIDE the columns,
    # so it spans the full page width as intended.
    st.markdown("---")

    st.header("🩺 What is PCOS?")

    st.write("""
Polycystic Ovary Syndrome (PCOS) is a hormonal disorder that affects women
of reproductive age.

Common symptoms include:

• Irregular menstrual cycles

• Excess hair growth

• Weight gain

• Acne

• Ovarian cysts

Early diagnosis can significantly improve long-term health outcomes.
""")

    st.markdown("---")

    st.header("⚙️ Technologies Used")

    tech1, tech2, tech3 = st.columns(3)

    with tech1:
        st.info("""
Python

Pandas

NumPy
""")

    with tech2:
        st.info("""
Scikit-Learn

Random Forest

SHAP
""")

    with tech3:
        st.info("""
Streamlit

Plotly

ElevenLabs
""")

    divider()
    st.info("👈 Use the sidebar to navigate through the application.")
    footer()