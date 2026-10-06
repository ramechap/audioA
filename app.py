import io
import json
import re
import time

import streamlit as st
from PIL import Image, ImageDraw
from google import genai
from google.genai import types


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Gemini Vision & Audio Scanner",
    page_icon="🎙️",
    layout="wide",
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        font-weight: bold;
        background-color: #FF9D00;
        color: white;
        height: 48px;
        border: none;
    }

    .stButton>button:hover {
        background-color: #E08900;
        color: white;
    }

    h1, .subtitle {
        text-align: center;
    }

    .model-box {
        padding: 10px;
        border-radius: 8px;
        background-color: rgba(128,128,128,0.1);
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# HEADER
# ============================================================

st.title("📸 Gemini Vision Scanner")

st.markdown(
    """
    <p class='subtitle'>
    Scene understanding, object detection, text reading and visual Q&A,
    powered by Google Gemini.
    </p>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# API KEY
# ============================================================

api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
    st.warning(
        "⚠️ Add GEMINI_API_KEY in Streamlit Cloud → Settings → Secrets. "
        "Get your API key from Google AI Studio."
    )
    st.stop()


# ============================================================
# GEMINI CLIENT
# ============================================================

client = genai.Client(api_key=api_key)
