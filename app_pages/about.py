import streamlit as st


def about():

    # ----------------------------
    # Custom CSS
    # ----------------------------

    st.markdown("""
    <style>

    .hero{
        background: linear-gradient(90deg,#FFE6F0,#FFF8FB);
        padding:30px;
        border-radius:20px;
        border-left:8px solid #E75480;
        margin-bottom:25px;
    }

    .hero h1{
        color:#E75480;
        font-size:40px;
        margin-bottom:8px;
    }

    .hero p{
        font-size:17px;
        color:#444;
        line-height:1.6;
    }

    .stat{
        background:#FFF7FA;
        padding:20px;
        border-radius:15px;
        text-align:center;
        border:1px solid #F6D4E3;
        box-shadow:0px 3px 10px rgba(0,0,0,0.05);
        box-sizing:border-box;
    }

    .stat h2{
        color:#E75480;
        margin-bottom:5px;
        font-size:32px;
    }

    .stat p{
        color:#555 !important;
        font-size:15px;
        margin:0;
    }

    .feature{
        background:white;
        padding:18px 18px 22px 18px;
        border-radius:15px;
        border:1px solid #ECECEC;
        min-height:145px;
        box-shadow:0px 3px 10px rgba(0,0,0,0.05);
        box-sizing:border-box;
        word-wrap:break-word;
        overflow-wrap:break-word;
        display:flex;
        flex-direction:column;
    }

    .feature h4{
        color:#E75480;
        margin-bottom:8px;
    }

    .feature p{
        color:#555;
        font-size:15px;
        line-height:1.5;
        margin:0;
    }

    .info{
        background:#FFF8FB;
        padding:18px 18px 22px 18px;
        border-radius:15px;
        border:1px solid #F6D4E3;
        min-height:140px;
        box-sizing:border-box;
        word-wrap:break-word;
        overflow-wrap:break-word;
        display:flex;
        flex-direction:column;
    }

    .info h4{
        color:#E75480;
        margin-bottom:8px;
    }

    .info p{
        color:#444 !important;
        font-size:15px;
        line-height:1.6;
        margin:0;
    }

    .info ul{
        margin:0;
        padding-left:20px;
        padding-bottom:2px;
        color:#444;
        font-size:15px;
        line-height:2.1;
    }

    .info ul li{
        margin-bottom:4px;
    }

    .footer{
        text-align:center;
        color:gray;
        font-size:13px;
        margin-top:30px;
    }

    ::selection{
        background:#F6AFC9;
        color:#3A0D1F;
    }

    ::-moz-selection{
        background:#F6AFC9;
        color:#3A0D1F;
    }

    </style>
    """, unsafe_allow_html=True)

    # ----------------------------
    # HERO
    # ----------------------------

    st.markdown(
        '<div class="hero">'
        '<h1>🌸 FemCare AI</h1>'
        '<p>An Explainable Artificial Intelligence platform for '
        '<b>early PCOS risk prediction</b>. '
        'FemCare AI combines Machine Learning with SHAP '
        'Explainability to provide transparent and '
        'interpretable healthcare insights.</p>'
        '</div>',
        unsafe_allow_html=True
    )

    # ----------------------------
    # STATS
    # ----------------------------

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(
            '<div class="stat"><h2>1</h2><p>Optimized ML Model</p></div>',
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            '<div class="stat"><h2>43</h2><p>Clinical Features</p></div>',
            unsafe_allow_html=True
        )

    with c3:
        st.markdown(
            '<div class="stat"><h2>SHAP</h2><p>Explainable Predictions</p></div>',
            unsafe_allow_html=True
        )

    st.write("")

    # ----------------------------
    # FEATURES
    # ----------------------------

    st.subheader("✨ What Makes FemCare AI Different?")

    a, b = st.columns(2)

    with a:
        st.markdown(
            '<div class="feature">'
            '<h4>🩺 Smart Prediction</h4>'
            '<p>Random Forest analyzes clinical parameters '
            'to estimate PCOS risk efficiently.</p>'
            '</div>',
            unsafe_allow_html=True
        )

        st.write("")

        st.markdown(
            '<div class="feature">'
            '<h4>📊 Performance Analysis</h4>'
            '<p>Evaluate accuracy, F1-score, ROC curve '
            'and feature importance.</p>'
            '</div>',
            unsafe_allow_html=True
        )

    with b:
        st.markdown(
            '<div class="feature">'
            '<h4>🧠 Explainable AI</h4>'
            '<p>SHAP highlights features influencing '
            'each prediction.</p>'
            '</div>',
            unsafe_allow_html=True
        )

        st.write("")

        st.markdown(
            '<div class="feature">'
            '<h4>🌸 Interactive Design</h4>'
            '<p>Streamlit dashboard with simple '
            'and user-friendly interaction.</p>'
            '</div>',
            unsafe_allow_html=True
        )

    st.divider()

    # ----------------------------
    # TECHNOLOGY
    # ----------------------------

    st.subheader("⚙ Technology Stack")

    left, right = st.columns(2)

    with left:
        st.markdown(
            '<div class="info">'
            '<h4>💻 Development</h4>'
            '<ul>'
            '<li>🐍 Python</li>'
            '<li>🌐 Streamlit</li>'
            '<li>📊 Pandas & NumPy</li>'
            '<li>📈 Matplotlib</li>'
            '</ul>'
            '</div>',
            unsafe_allow_html=True
        )

    with right:
        st.markdown(
            '<div class="info">'
            '<h4>🤖 AI & Machine Learning</h4>'
            '<ul>'
            '<li>🌲 Random Forest</li>'
            '<li>📚 Scikit-learn</li>'
            '<li>🧠 SHAP</li>'
            '<li>💾 Joblib</li>'
            '</ul>'
            '</div>',
            unsafe_allow_html=True
        )

    st.divider()

    # ----------------------------
    # FUTURE
    # ----------------------------

    st.subheader("🚀 Future Enhancements")

    st.markdown("""
🌸 Voice-enabled AI Assistant

📱 Mobile-friendly healthcare platform

☁ Cloud-based deployment

🩺 Personalized health insights

📊 Advanced explainability dashboard
""")

    st.divider()

    # ----------------------------
    # PROJECT VISION
    # ----------------------------

    st.subheader("🎯 Project Vision")

    x, y = st.columns(2)

    with x:
        st.markdown(
            '<div class="info">'
            '<h4>Goal</h4>'
            '<p>Build an Explainable AI system '
            'for early PCOS risk prediction.</p>'
            '</div>',
            unsafe_allow_html=True
        )

    with y:
        st.markdown(
            '<div class="info">'
            '<h4>Vision</h4>'
            '<p>Make AI-based healthcare insights '
            'accessible and understandable.</p>'
            '</div>',
            unsafe_allow_html=True
        )

    st.divider()

    # ----------------------------
    # DISCLAIMER
    # ----------------------------

    st.warning("""
    **Medical Disclaimer**

    FemCare AI is an educational AI project developed
    for research purposes.

    Predictions should not be considered a medical
    diagnosis. Always consult healthcare professionals
    for medical advice.
    """)

    # ----------------------------
    # FOOTER
    # ----------------------------

    st.markdown(
        '<div class="footer">'
        '❤️ FemCare AI • Explainable AI for Early PCOS Risk Prediction • 2026'
        '</div>',
        unsafe_allow_html=True
    )
