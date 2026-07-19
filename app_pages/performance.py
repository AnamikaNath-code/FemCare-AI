import streamlit as st
import pandas as pd
import plotly.express as px

def performance():

    st.title("📊 Model Performance")

    st.markdown("""
This page summarizes the performance of different Machine Learning models
used for PCOS prediction.
""")

    st.divider()
    st.success("""
### 🏆 Selected Model

**Random Forest Classifier**

Random Forest was selected for deployment because it provides:

- High Accuracy
- Stable Performance
- Robust Predictions
- Excellent compatibility with SHAP Explainable AI
""")

    st.subheader("📈 Random Forest Performance")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Accuracy",
            "91%"
        )

    with col2:
        st.metric(
            "Precision",
            "93%"
        )

    with col3:
        st.metric(
            "Recall",
            "78%"
        )

    with col4:
        st.metric(
            "F1 Score",
            "85%"
        )

    st.divider()        
    st.subheader("🏆 Model Comparison")

    models = pd.DataFrame({

        "Model":[

            "Logistic Regression",
            "Decision Tree",
            "Random Forest",
            "KNN",
            "SVM",
            "Naive Bayes",
            "AdaBoost",
            "Gradient Boosting",
            "XGBoost"

        ],

        "Accuracy":[

            91,
            88,
            91,
            89,
            89,
            86,
            91,
            92,
            94

        ]

    })

    st.dataframe(
        models,
        use_container_width=True
    )


    fig = px.bar(

        models,

        x="Model",

        y="Accuracy",

        text="Accuracy",

        color="Accuracy",

        color_continuous_scale="RdPu"

    )

    fig.update_layout(

        height=500,

        xaxis_title="Model",

        yaxis_title="Accuracy (%)"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    st.subheader("🌲 Why Random Forest?")

    st.info("""

Random Forest was chosen because it:

✅ Handles non-linear relationships

✅ Reduces overfitting through ensemble learning

✅ Performs well on healthcare datasets

✅ Works efficiently with structured clinical data

✅ Integrates seamlessly with SHAP Explainable AI

""")

    st.divider()

    st.subheader("🚀 Future Improvements")

    st.write("""

Although Random Forest performs well,
future versions of FemCare AI may include:

- XGBoost
- LightGBM
- CatBoost
- Deep Learning Models

to further improve prediction accuracy.

""")
    
        