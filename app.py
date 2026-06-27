import streamlit as st

from modules import database
from modules import rating_calculator
from modules import inrush_calculator
from modules import softstart_simulation
from modules import testing_dashboard
from modules import construction_viewer
from modules import analytics
from modules import internship_summary

st.set_page_config(
    page_title="MES Isolation Transformer",
    layout="wide"
)

st.sidebar.title("⚡ MES Transformer Analysis")

page = st.sidebar.radio(
    "Select Module",
    [
        "🏠 Home",
        "📊 Database",
        "⚡ Rating Calculator",
        "🔥 Inrush Calculator",
        "📈 Soft Start Simulation",
        "🧪 Testing Dashboard",
        "🏭 Construction Viewer",
        "📊 Analytics",
        "🎓 Internship Summary"
    ]
)

if page == "🏠 Home":

    st.title("⚡ ISOLATION TRANSFORMER ANALYSIS SYSTEM")

    st.subheader("Modern Electric Systems")

    st.success(
        "Internship Project on Isolation Transformers with Soft Start Systems"
    )

    st.markdown("---")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Internship",
            "21 Days"
        )

    with col2:
        st.metric(
            "Transformers",
            "16 Models"
        )

    with col3:
        st.metric(
            "Tests",
            "7"
        )

    with col4:
        st.metric(
            "Status",
            "Completed"
        )

    st.markdown("---")

    st.subheader("📋 Modules Available")

    st.success("""
    ✅ MES Transformer Database
    ✅ Transformer Rating Calculator
    ✅ Inrush Current Calculator
    ✅ Soft Start System Simulation
    ✅ Transformer Testing Dashboard
    ✅ Construction Viewer
    ✅ Transformer Analytics
    ✅ Internship Summary Dashboard
    """)

    st.markdown("---")

    st.subheader("🎓 Internship Details")

    st.info("""
    Company:
    Modern Electric Systems

    Domain:
    Transformer Design and Manufacturing

    Product Studied:
    Isolation Transformers with Soft Start Systems

    Internship Duration:
    21 Days

    Student:
    Priyanka G,Radhi S & Tamilselvi K

    Department:
    Electronics and Communication Engineering
    """)

    st.markdown("---")

    st.progress(100)

    st.caption("""
    ✔ Database
    ✔ Calculations
    ✔ Simulations
    ✔ Testing
    ✔ Analytics
    ✔ Documentation
    """)

    st.markdown("---")

    st.caption(
        "Isolation Transformer Analysis System | "
        "Modern Electric Systems Internship | "
        "Priyanka G | III Year ECE"
    )

elif page == "📊 Database":
    database.show()

elif page == "⚡ Rating Calculator":
    rating_calculator.show()

elif page == "🔥 Inrush Calculator":
    inrush_calculator.show()

elif page == "📈 Soft Start Simulation":
    softstart_simulation.show()

elif page == "🧪 Testing Dashboard":
    testing_dashboard.show()

elif page == "🏭 Construction Viewer":
    construction_viewer.show()

elif page == "📊 Analytics":
    analytics.show()

elif page == "🎓 Internship Summary":
    internship_summary.show()