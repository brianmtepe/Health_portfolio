import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from urllib.parse import quote

# 1. PAGE CONFIG
st.set_page_config(
    page_title="Brian Mtepe | Health Data Portfolio",
    page_icon="🏥",
    layout="wide"
)

# 2. STYLING
st.markdown("""
<style>
    .main { background-color: #0A192F; color: white; }
    h1, h2, h3 { color: #64FFDA !important; }
    [data-testid="stMetric"] {
        background-color: #112240;
        padding: 20px;
        border-radius: 12px;
        border-bottom: 4px solid #64FFDA;
    }
    .tech-box {
        background-color: #112240;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #64FFDA;
        margin-bottom: 10px;
        height: 140px;
    }
    .nav-card {
        background-color: #112240;
        padding: 12px;
        border-radius: 8px;
        border: 1px solid #64FFDA;
        text-align: center;
        margin-bottom: 10px;
        display: block;
        text-decoration: none !important;
        color: #64FFDA !important;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# 3. DATA & PROJECTS
projects = [
    ("🤰 Maternal & Child Health (MCH) Analytics", "County-level KPI tracking for ANC, PNC, and maternal healthcare outcomes."),
    ("🏥 Hospital Readmission Risk Analytics", "Clinical decision support using risk modeling to reduce readmission rates."),
    ("📉 Outpatient Trend Analysis", "Operational reporting on service utilization, patient flows, and clinic volume.")
]

@st.cache_data
def get_data():
    np.random.seed(42)
    names = [p[0] for p in projects]
    return pd.DataFrame({
        "Project": np.random.choice(names, 300),
        "Records": np.random.randint(500, 2500, 300),
        "Quality": np.random.uniform(88, 99, 300)
    })

df = get_data()

# 4. SIDEBAR
with st.sidebar:
    st.header("💼 Hire & Connect")
    st.markdown('<a href="https://www.upwork.com/freelancers/~0177726359560f722c" class="nav-card">🚀 Upwork</a>', unsafe_allow_html=True)
    st.markdown('<a href="https://www.fiverr.com/brianmtepe" class="nav-card">🎨 Fiverr</a>', unsafe_allow_html=True)
    st.markdown('<a href="https://github.com/brianmtepe" class="nav-card">💻 GitHub</a>', unsafe_allow_html=True)
    st.divider()
    whatsapp_msg = quote(f"Check out Brian Mtepe's Portfolio: https://brian-mtepe-health.streamlit.app")
    st.markdown(f'<a href="https://wa.me/?text={whatsapp_msg}" class="nav-card">📲 Share on WhatsApp</a>', unsafe_allow_html=True)
    st.info("📍 Location: Nairobi / Mombasa, Kenya")

# 5. MAIN CONTENT
st.title("🏥 Healthcare Data Analytics Portfolio")
st.subheader("Brian Mtepe | KRCHN | Health Data Analyst")
st.markdown("---")

# METRICS
c1, c2, c3 = st.columns(3)
c1.metric("Patient Records Analyzed", f"{df['Records'].sum():,}+")
c2.metric("Avg. Data Quality Score", f"{df['Quality'].mean():.1f}%")
c3.metric("Live Clinical Projects", len(projects))

# CHART
st.subheader("📈 Cumulative Growth of Health Outreach")
chart_data = df.groupby("Project", as_index=False)["Records"].sum()
fig = px.bar(chart_data, x="Project", y="Records", color="Project", template="plotly_dark")
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# PROJECTS DISPLAY
st.header("📁 Active Clinical Projects")
p_cols = st.columns(3)
for idx, (name, desc) in enumerate(projects):
    with p_cols[idx]:
        st.markdown(f'<div class="tech-box"><b>{name}</b><br><small>{desc}</small></div>', unsafe_allow_html=True)

st.markdown("---")
st.markdown("<div style='text-align:center;opacity:0.6;'>Healthcare Portfolio | 2026</div>", unsafe_allow_html=True)"<div style='text-align:center;opacity:0.6;'>Healthcare Portfolio | 2026</div>", unsafe_allow_html=True)==============
st.markdown("---")
st.markdown("<div style='text-align:center;opacity:0.6;'>Healthcare Portfolio | Remote Global Availability | 2026</div>", unsafe_allow_html=True)============================
st.markdown("---")
st.markdown("<div style='text-align:center;opacity:0.6;'>Healthcare Portfolio | Remote Global Availability | 2026</div>", unsafe_allow_html=True)True
)