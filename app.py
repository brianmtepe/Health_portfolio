import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from urllib.parse import quote

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="Brian Mtepe | Health Data Portfolio",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# PROFESSIONAL STYLE
# =========================================================
st.markdown("""
<style>

    .main {
        background-color: #0A192F;
        color: white;
    }

    h1, h2, h3 {
        color: #64FFDA !important;
    }

    /* Metric Cards */
    [data-testid="stMetric"] {
        background-color: #112240;
        padding: 20px;
        border-radius: 12px;
        border-bottom: 4px solid #64FFDA;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
    }

    /* Project Cards */
    .tech-box {
        background-color: #112240;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #64FFDA;
        margin-bottom: 10px;
        height: 140px;
    }

    /* Navigation Cards */
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
        transition: 0.3s ease;
    }

    .nav-card:hover {
        background-color: #64FFDA;
        color: #0A192F !important;
    }

    /* Tech Stack */
    .tech-pill {
        background-color: #112240;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #30363d;
        font-family: monospace;
        color: #e6edf3;
        text-align: center;
        font-size: 18px;
    }

</style>
""", unsafe_allow_html=True)

# =========================================================
# PROJECT DATA
# =========================================================
projects = [
    (
        "🤰 Maternal & Child Health (MCH) Analytics",
        "County-level KPI tracking for ANC, PNC, and maternal healthcare outcomes."
    ),

    (
        "🏥 Hospital Readmission Risk Analytics",
        "Clinical decision support using risk modeling to improve patient outcome insights."
    ),

    (
        "📉 Outpatient Trend Analysis",
        "Operational reporting on service utilization, patient flows, and clinic volume."
    )
]

# =========================================================
# SYNTHETIC DATA
# =========================================================
@st.cache_data
def get_data():

    np.random.seed(42)

    names = [p[0] for p in projects]

    df = pd.DataFrame({
        "Project": np.random.choice(names, 300),
        "Records": np.random.randint(500, 2500, 300),
        "Quality": np.random.uniform(88, 99, 300)
    })

    return df

df = get_data()

# =========================================================
# SHARE URL
# =========================================================
live_url = "https://brian-mtepe-health.streamlit.app"

message = quote(
    f"Check out Brian Mtepe's Healthcare Analytics Portfolio: {live_url}"
)

# =========================================================
# SIDEBAR
# =========================================================
with st.sidebar:

    st.header("💼 Hire & Connect")

    st.markdown(
        '<a href="https://www.upwork.com/freelancers/~0177726359560f722c" class="nav-card">🚀 Hire on Upwork</a>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<a href="https://www.fiverr.com/brianmtepe" class="nav-card">🎨 Fiverr Portfolio</a>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<a href="https://www.linkedin.com/in/brianmtepe/" class="nav-card">🔗 LinkedIn Profile</a>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<a href="https://github.com/brianmtepe" class="nav-card">💻 GitHub Projects</a>',
        unsafe_allow_html=True
    )

    st.divider()

    st.write("📢 Share My Portfolio")

    st.markdown(
        f'<a href="https://wa.me/?text={message}" class="nav-card">📲 Share via WhatsApp</a>',
        unsafe_allow_html=True
    )

    st.divider()

    st.info("📍 Location: Nairobi / Mombasa, Kenya")

    st.success(
        "👨‍⚕️ Focus Areas: Healthcare Dashboards, DHIS2 & SQL Analytics"
    )

# =========================================================
# HEADER
# =========================================================
st.title("🏥 Healthcare Data Analytics Portfolio")

st.subheader("Brian Mtepe | KRCHN | Health Data Analyst")

st.markdown("""
Bridging Clinical Excellence with Data-Driven Healthcare Insights.
""")

st.markdown("---")

# =========================================================
# METRICS
# =========================================================
st.header("📊 Metrics Summary")

c1, c2, c3 = st.columns(3)

c1.metric(
    "Patient Records Analyzed",
    f"{df['Records'].sum():,}+"
)

c2.metric(
    "Avg. Data Quality Score",
    f"{df['Quality'].mean():.1f}%"
)

c3.metric(
    "Active Analytics Projects",
    len(projects)
)

# =========================================================
# VISUALIZATION
# =========================================================
st.markdown("<br>", unsafe_allow_html=True)

st.subheader("📈 Clinical Analytics Overview")

chart_data = (
    df.groupby("Project", as_index=False)["Records"]
    .sum()
)

fig = px.bar(
    chart_data,
    x="Project",
    y="Records",
    color="Project",
    template="plotly_dark",
    color_discrete_sequence=px.colors.qualitative.Pastel
)

fig.update_layout(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(color="white"),
    showlegend=False,
    height=400
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# =========================================================
# SKILLS & TECH STACK
# =========================================================
col_left, col_right = st.columns(2)

with col_left:

    st.header("💹 Skills & Expertise")

    st.markdown("""
* **MCH Dashboards:** Strategic tracking of maternal and child health indicators.
* **Risk Modeling:** SQL-based analytics for hospital readmission and patient outcomes.
* **Public Health Reporting:** Structured clinical reporting for healthcare systems and operational insights.
""")

with col_right:

    st.header("🛠️ Tech Stack")

    st.markdown("""
    <div class="tech-pill">
        Python | SQL | Power BI | DHIS2
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# =========================================================
# ACTIVE PROJECTS
# =========================================================
st.header("📁 Active Clinical Projects")

p_cols = st.columns(3)

for idx, (p, d) in enumerate(projects):

    with p_cols[idx]:

        st.markdown(f"""
        <div class="tech-box">
            <b>{p}</b><br>
            <small>{d}</small>
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# FOOTER
# =========================================================
st.markdown("---")

st.markdown(
    "<div style='text-align:center;opacity:0.6;'>Healthcare Analytics Portfolio | Remote Global Availability | 2026</div>",
    unsafe_allow_html=True
)==========================
st.markdown("---")
st.markdown(
    "<div style='text-align:center;opacity:0.6;'>Healthcare Portfolio | Remote Global Availability | 2026</div>",
    unsafe_allow_html=True
)==========================
st.markdown("---")
st.markdown(
    "<div style='text-align:center;opacity:0.6;'>Healthcare Portfolio | Remote Global Availability | 2026</div>",
    unsafe_allow_html=True
)==========================
st.markdown("---")
st.markdown(
    "<div style='text-align:center;opacity:0.6;'>Healthcare Portfolio | Remote Global Availability | 2026</div>",
    unsafe_allow_html=True
)============================
st.markdown("---")
st.markdown(
    "<div style='text-align:center;opacity:0.6;'>Healthcare Portfolio | Remote Global Availability | 2026</div>",
    unsafe_allow_html=True
)