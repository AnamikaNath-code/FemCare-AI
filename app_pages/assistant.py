
import streamlit as st
import streamlit.components.v1 as components
from ui_components import hero, divider, feature_card

AGENT_ID = "agent_6001kxk10p4cehp9z3e4kyc1mrnw"


PAGE_CSS = """
<style>
.assistant-heading {
    text-align: center;
    margin: 0.5rem 0 0.25rem 0;
    color: #5A2A4A;
    font-size: 1.75rem;
    font-weight: 700;
}

.assistant-subheading {
    text-align: center;
    color: #A0607F;
    font-size: 1rem;
    margin-bottom: 1.5rem;
}
</style>
"""


PREVIEW_HTML = """
<style>
html, body {
    margin: 0;
    padding: 0;
    background: transparent;
    font-family: "Segoe UI", sans-serif;
}

.card {
    box-sizing: border-box;
    height: 180px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 10px;
    text-align: center;
    background: linear-gradient(160deg, #FFFFFF, #FFF0F6);
    border: 1px solid #F8C8DC;
    border-radius: 20px;
    box-shadow: 0 8px 24px rgba(214, 51, 132, 0.12);
    padding: 16px;
}

.avatar {
    font-size: 38px;
}

.title {
    color: #5A2A4A;
    font-size: 19px;
    font-weight: 700;
}

.description {
    color: #A0607F;
    font-size: 14px;
    max-width: 450px;
}
</style>

<div class="card">
    <div class="avatar">🌸</div>
    <div class="title">Sakura is ready to help</div>
    <div class="description">
        Your AI companion for PCOS awareness,
        understanding your results and navigating FemCare AI.
    </div>
</div>
"""


def centered_heading(title: str, subtitle: str = ""):

    st.markdown(
        f'<div class="assistant-heading">{title}</div>',
        unsafe_allow_html=True
    )

    if subtitle:
        st.markdown(
            f'<div class="assistant-subheading">{subtitle}</div>',
            unsafe_allow_html=True
        )


def assistant():

    if "chat_open" not in st.session_state:
        st.session_state.chat_open = False

    st.markdown(PAGE_CSS, unsafe_allow_html=True)

    # Hero section
    hero(
        title="Sakura, Your Voice Assistant",
        subtitle=(
            "Ask questions about PCOS or get help using FemCare AI, "
            "by voice or by text."
        ),
        badge="Beta · Voice Agent",
    )

    # About section
    centered_heading(
        "About Sakura",
        "A guide for understanding PCOS and navigating this app. "
        "It is not a replacement for medical care."
    )

    # Feature cards
    col1, col2, col3 = st.columns(3)

    with col1:
        feature_card(
            "💬",
            "Ask in your words",
            "Type or speak questions about symptoms, causes, "
            "and everyday management."
        )

    with col2:
        feature_card(
            "🩺",
            "Understand your results",
            "Get plain-language explanations of what the "
            "prediction and model pages mean."
        )

    with col3:
        feature_card(
            "🌸",
            "Learn at your pace",
            "Clear, supportive answers with no medical jargon "
            "and no judgment."
        )

    divider()

    # Chat section
    centered_heading(
        "Start a conversation",
        "Open Sakura to talk or type your questions."
    )

    if not st.session_state.chat_open:

        components.html(
            PREVIEW_HTML,
            height=195,
            scrolling=False
        )

        left, center, right = st.columns([1, 1, 1])

        with center:
            if st.button(
                "🌸 Open chat with Sakura",
                key="open_chat",
                use_container_width=True
            ):
                st.session_state.chat_open = True
                st.rerun()

    else:

        st.markdown(
            """
            <div style="
                text-align:center;
                color:#5A2A4A;
                font-size:18px;
                font-weight:700;
                margin:10px 0 15px 0;
            ">
                🌸 Chat with Sakura
            </div>
            """,
            unsafe_allow_html=True
        )

        # ElevenLabs agent embed
        components.html(
            f"""
            <!DOCTYPE html>
            <html>
            <head>
                <meta name="viewport"
                      content="width=device-width, initial-scale=1.0">

                <style>
                    html, body {{
                        margin: 0;
                        padding: 0;
                        width: 100%;
                        min-height: 580px;
                        background: transparent;
                        font-family: "Segoe UI", sans-serif;
                    }}

                    .widget-container {{
                        width: 100%;
                        min-height: 560px;
                        display: flex;
                        justify-content: center;
                        align-items: flex-start;
                    }}

                    elevenlabs-convai {{
                        display: block;
                        width: 100%;
                    }}
                </style>
            </head>

            <body>
                <div class="widget-container">
                    <elevenlabs-convai
                        agent-id="{AGENT_ID}">
                    </elevenlabs-convai>
                </div>

                <script
                    src="https://unpkg.com/@elevenlabs/convai-widget-embed"
                    async
                    type="text/javascript">
                </script>
            </body>
            </html>
            """,
            height=600,
            scrolling=False
        )

        left, center, right = st.columns([1, 1, 1])

        with center:
            if st.button(
                "Close chat",
                key="close_chat",
                use_container_width=True
            ):
                st.session_state.chat_open = False
                st.rerun()

    # Medical disclaimer
    st.info(
        "Sakura provides general information only. It cannot diagnose PCOS "
        "or recommend treatment. For medical decisions, consult a "
        "gynecologist or endocrinologist. In an emergency, contact local "
        "emergency services immediately."
    )

    # Conversation tips
    with st.expander("Tips for a better conversation"):

        st.markdown(
            """
- Allow microphone access when your browser asks.
- Speak in full sentences for more accurate answers.
- Avoid sharing personal identifying information.
- Ask Sakura to explain any medical term you do not understand.
"""
        )
