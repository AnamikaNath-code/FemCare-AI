import streamlit as st
from ui_components import load_css
# -------------------------------
# PAGE CONFIG
# -------------------------------

st.set_page_config(
    page_title="FemCare AI",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded"
)
load_css()
# -------------------------------
# CUSTOM CSS
# -------------------------------

st.markdown("""
<style>

/* ---------- Main App ---------- */

.stApp{
    ackground:#0E1117;
    color:white;
}
            
            /* Main page */

.main .block-container{
    background:#0E1117;
    color:white;
}

/* Paragraphs */

p{
    color:white !important;
}

/* Normal text */

div{
    color:white;
}

/* Labels */

label{
    color:white !important;
}

/* Markdown */

[data-testid="stMarkdownContainer"]{
    color:white;
}

/* ---------- Sidebar ---------- */

section[data-testid="stSidebar"]{
    background:#FFEAF2;
    border-right:2px solid #F8C8DC;
}

/* Sidebar Text */

section[data-testid="stSidebar"] *{
    color:#5A2A4A !important;
}

/* Radio Buttons */

div[role="radiogroup"] label{
    display:flex;
    align-items:center;
    gap:10px;

    padding:10px 12px;
    margin-bottom:8px;

    border-radius:10px;

    transition:0.3s;
}

/* Hover */

div[role="radiogroup"] label:hover{
    background:#FFD6E7;
}

/* Selected Page */

div[role="radiogroup"] [aria-checked="true"]{
    background:#F8BBD0;
    border-radius:10px;
}

/* Headings */



/* Buttons */

.stButton>button{

    width:100%;

    background:#D63384;
    color:white;

    border:none;
    border-radius:10px;

    padding:10px;

    font-weight:bold;
}

.stButton>button:hover{

    background:#AD1457;

    color:white;
}

/* Metric Cards */

[data-testid="metric-container"]{

    background:white;

    border-radius:15px;

    padding:15px;

    box-shadow:0px 2px 10px rgba(0,0,0,.08);
}

hr{
    border:1px solid #F8C8DC;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------
# SIDEBAR
# -------------------------------

st.sidebar.image(
    "assets/logo.png",
    use_container_width=True
)

st.sidebar.markdown(
    """
    <h2 style='text-align:center;color:#D63384;'>
    🌸 FemCare AI
    </h2>

    <p style='text-align:center;color:#7A4A68;font-size:14px;'>
    AI Powered PCOS Prediction
    </p>

    <hr>
    """,
    unsafe_allow_html=True
)

# -------------------------------
# IMPORT PAGES
# -------------------------------

from app_pages.home import home
from app_pages.prediction import prediction
from app_pages.performance import performance
from app_pages.explainable_ai import explainable_ai
from app_pages.assistant import assistant
from app_pages.about import about

# -------------------------------
# NAVIGATION
# -------------------------------

page = st.sidebar.radio(

    "Navigation",

    [

        "🏠 Home",

        "🩺 Prediction",

        "📊 Model Performance",

        "🧠 Explainable AI",

        "🤖 AI Assistant",

        "ℹ️ About"

    ]

)

# -------------------------------
# PAGE ROUTING
# -------------------------------

if page == "🏠 Home":

    home()

elif page == "🩺 Prediction":

    prediction()

elif page == "📊 Model Performance":

    performance()

elif page == "🧠 Explainable AI":

    explainable_ai()

elif page == "🤖 AI Assistant":

    assistant()

elif page == "ℹ️ About":

    about()