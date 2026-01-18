'''
import streamlit as st
from google import genai
import os

# --- 1. REMOVED DOTENV LOGIC ---
# Instead of loading from .env, we use Streamlit Secrets
if "REPLICATE_API_TOKEN" in st.secrets:
    os.environ["REPLICATE_API_TOKEN"] = st.secrets["REPLICATE_API_TOKEN"]

if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# --- 2. REST OF CONFIG ---
SEGMENTATION_MODEL_NAME = "facebook/sam-vit-huge"
DEPTH_ESTIMATION_MODEL = "Intel/dpt-large"
DEFAULT_IMAGE_SIZE = (512, 512)
ALPHA = 0.5
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
LABELS = ["wall", "floor", "ceiling", "furniture"]

'''

import streamlit as st
from google import genai  # Modern 2026 import

# This replaces the old genai.configure()
def get_ai_client():
    api_key = st.secrets.get("GOOGLE_API_KEY")
    if not api_key:
        st.error("Missing GOOGLE_API_KEY in Streamlit Secrets!")
        st.stop()
    return genai.Client(api_key=api_key)

DEFAULT_IMAGE_SIZE = (1024, 1024)
