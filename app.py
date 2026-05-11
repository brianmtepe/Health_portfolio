import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from urllib.parse import quote

# 1. PAGE CONFIG & THUMBNAIL
st.set_page_config(page_title="Brian Mtepe | Health Data Portfolio", page_icon="🏥", layout="wide")

st.markdown(f"""
    <head>
        <meta property="og:title" content="Brian Mtepe | Health Data Analyst Portfolio" />
        <meta property="og:image" content="https://raw.githubusercontent.com/brianmtepe/Health_portfolio/main/Health-portfolio-thumbnail.png" />
        <meta property="og:url" content="https://brian-mtepe-health.streamlit.app" />
    </head>
""", unsafe_allow_html=True)

# 2. STYLING
st.markdown("""
<style>
    .main { background-color: #0A192F; color: white; }
    h1, h2, h3 { color: #64FFDA !important; }
    [data-testid="stMetric"] { background-color: #112240; padding: 20px; border-radius: 12px; border-bottom: 4px solid #64FFDA; }
    .nav-card { background-color: #112240; padding: 12px; border-radius: 8px; border: 1px solid #64FFDA; text-align: center; margin-bottom: 10px; display: block; text-decoration: none !important; color: #64FFDA !important; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# 3. SIDEBAR
with st.sidebar:
    st.header("💼 Hire & Connect")
    st.markdown('<a href="https://www.upwork.com/freelancers/~0177726359560f722c" class="nav-card">🚀 Upwork</a>', unsafe_allow_html=True)
    st.markdown('<a href="https://github.com/brianmtepe" class="nav-card">💻 GitHub</a>', unsafe_allow_html=True)
    whatsapp_msg = quote("Check out Brian Mtepe's Portfolio: https://brian-mtepe-health.streamlit.app")
    st.markdown(f'<a href="https://wa.me/?text={whatsapp_msg}" class="nav-card">📲 Share on WhatsApp</a>', unsafe_allow_html=True)

# 4. MAIN CONTENT
st.title("🏥 Healthcare Data Analytics Portfolio")
st.subheader("Brian Mtepe | KRCHN | Health Data Analyst")
st.divider()

c1, c2, c3 = st.columns(3)
c1.metric("Records Analyzed", "450,000+")
c2.metric("Data Quality", "93.5%")
c3.metric("Live Projects", "3")

st.header("📁 Active Clinical Projects")
p_cols = st.columns(3)
p_cols[0].info("**Maternal & Child Health Analytics**")
p_cols[1].info("**Hospital Readmission Risk**")
p_cols[2].info("**Outpatient Trend Analysis**")

st.divider()
st.markdown("<div style='text-align:center;opacity:0.6;'>Healthcare Portfolio | 2026</div>", unsafe_allow_html=True)==========================
st.markdown("---")
st.markdown(
    "<div style='text-align:center;opacity:0.6;'>Healthcare Portfolio | Remote Global Availability | 2026</div>",
    unsafe_allow_html=True
) style='text-align:center;opacity:0.6;'>Healthcare Portfolio | Remote Global Availability | 2026</div>", unsafe_allow_html=True)True
)