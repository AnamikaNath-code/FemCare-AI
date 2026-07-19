"""
ui_components.py
Reusable UI building blocks for the SAKHI app.
Import these into app.py and every page under pages/.
"""

import streamlit as st
from pathlib import Path


def load_css():
    """Inject the custom stylesheet. Call this once at the top of every page."""
    css_path = Path(__file__).parent / "assets" / "style.css"
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def hero(title: str, subtitle: str, badge: str = "PCOS Prediction · Explainable AI"):
    """Big gradient hero banner for the top of a page."""
    st.markdown(
        f"""
        <div class="hero-container">
            <div class="hero-badge">{badge}</div>
            <div class="hero-title">{title}</div>
            <div class="hero-subtitle">{subtitle}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def section_header(title: str, subtitle: str = ""):
    """Consistent section title used across pages."""
    st.markdown(f'<div class="section-title">{title}</div>', unsafe_allow_html=True)
    if subtitle:
        st.markdown(f'<div class="section-subtitle">{subtitle}</div>', unsafe_allow_html=True)


def feature_card(icon: str, title: str, text: str):
    """A single feature/info card. Use inside st.columns()."""
    st.markdown(
        f"""
        <div class="sakhi-card">
            <div class="sakhi-card-icon">{icon}</div>
            <div class="sakhi-card-title">{title}</div>
            <div class="sakhi-card-text">{text}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def stat_pill(number: str, label: str):
    """A small stat/metric pill."""
    st.markdown(
        f"""
        <div class="stat-pill">
            <div class="stat-number">{number}</div>
            <div class="stat-label">{label}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def divider():
    st.markdown('<hr class="sakhi-divider">', unsafe_allow_html=True)


def footer(text: str = "Made with care, for women's health · SAKHI © 2026"):
    st.markdown(f'<div class="sakhi-footer">{text}</div>', unsafe_allow_html=True)
