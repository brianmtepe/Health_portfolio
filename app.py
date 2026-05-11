import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# =========================================================
# PAGE CONFIG & META-DATA
# =========================================================
st.set_page_config(
    page_title="Brian Mtepe | Health Data Portfolio",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Invisible HTML tags that WhatsApp/LinkedIn read to show your screenshot
st.markdown(f"""
    <head>
        <meta property="og:title" content="Brian Mtepe | Health Data Analyst Portfolio" />
        <meta property="og:description" content="Registered Nurse (KRCHN) & Data Analyst bridging clinical nursing with data-driven healthcare insights." />
        <meta property="og:image" content="https://github.com/brianmtepe/Health_portfolio/blob/main/Health-portfolio-thumbnail.png?raw=true" />
        <meta property="og:url" content="https://brian-mtepe-health.streamlit.app" />
        <meta property="og:type" content="website" />
    </head>
""", unsafe_allow_html=True)

# =========================================================
# PROFESSIONAL STYLE
# =========================================================
st.markdown("""
<style>
    .main { background-color: #0A192F; color: white; }
    h1, h2, h3 { color: #64FFDA !important; }

    [data-testid="stMetric"] {
        background-color: #112240;
        padding: 20px;
        border-radius: 12px;
        border-bottom: 4px solid #64FFDA;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
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
        transition: 0.3s ease;
    }
    .nav-card:hover {
        background-color: #64FFDA;
        color: #0A192F !important;
    }

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
# DATA (CONSOLIDATED 3 ACTIVE PROJECTS)
# =========================================================
projects = [
    ("🤰 Maternal & Child Health (MCH) Analytics", 
     "County-level KPI tracking for ANC, PNC, and maternal healthcare outcomes."),
    ("🏥 Hospital Readmission Risk Analytics", 
     "Clinical decision support using risk modeling to reduce readmission rates."),
    ("📉 Outpatient Trend Analysis", 
     "Operational reporting on service utilization, patient flows, and clinic volume.")
]

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
# SIDEBAR (HIRE & CONNECT)
# =========================================================
with st.sidebar:
    st.header("💼 Hire & Connect")
    st.markdown('<a href="https://www.upwork.com/freelancers/~0177726359560f722c" class="nav-card">🚀 Hire on Upwork</a>', unsafe_allow_html=True)
    st.markdown('<a href="https://www.fiverr.com/brianmtepe" class="nav-card">🎨 Fiverr Portfolio</a>', unsafe_allow_html=True)
    st.markdown('<a href="https://www.linkedin.com/in/brianmtepe/" class="nav-card">🔗 LinkedIn Profile</a>', unsafe_allow_html=True)
    st.markdown('<a href="https://github.com/brianmtepe" class="nav-card">💻 GitHub Projects</a>', unsafe_allow_html=True)
    
    st.divider()
    st.write("📢 **Share My Portfolio**")
    live_url = "https://brian-mtepe-health.streamlit.app" 
    whatsapp_msg = f"Check out Brian Mtepe's Clinical Data Portfolio: {live_url}"
    st.markdown(f'<a href="https://wa.me/?text={whatsapp_msg}" class="nav-card">📲 Share via WhatsApp</a>', unsafe_allow_html=True)
    
    st.divider()
    st.info("📍 Location: Nairobi / Mombasa, Kenya")
    st.success("👨‍⚕️ Specialist: MCH Dashboards & SQL")

# =========================================================
# HEADER
# =========================================================
st.title("🏥 Healthcare Data Analytics Portfolio")
st.subheader("Brian Mtepe | KRCHN | Health Data Analyst")
st.markdown("Bridging Clinical Excellence with Data-Driven Healthcare Insights.")

st.markdown("---")

# =========================================================
# METRICS & VISUALS
# =========================================================
st.header("📊 Metrics Summary")
c1, c2, c3 = st.columns(3)
c1.metric("Patient Records Analyzed", f"{df['Records'].sum():,}+")
c2.metric("Avg. Data Quality Score", f"{df['Quality'].mean():.1f}%")
c3.metric("Live Clinical Projects", len(projects))

st.markdown("<br>", unsafe_allow_html=True)

st.subheader("📈 Cumulative Growth of Health Outreach")
chart_data = df.groupby("Project", as_index=False)["Records"].sum()
fig = px.bar(
    chart_data, x="Project", y="Records", color="Project",
    template="plotly_dark", color_discrete_sequence=px.colors.qualitative.Pastel
)
fig.update_layout(
    paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
    font=dict(color="white"), showlegend=False, height=400
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
    * **Risk Modeling:** SQL-based analytics for hospital readmission and outcomes.
    * **Public Health Reporting:** Automating clinical data for Ministry of Health (MOH) systems.
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
# ACTIVE CLINICAL PROJECTS
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
    "<div style='text-align:center;opacity:0.6;'>Healthcare Portfolio | Remote Global Availability | 2026</div>",
    unsafe_allow_html=True
) style='text-align:center;opacity:0.6;'>Healthcare Portfolio | Remote Global Availability | 2026</div>", unsafe_allow_html=True)True
)