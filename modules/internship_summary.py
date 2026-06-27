import streamlit as st


def show():

    st.title("🎓 Internship Summary")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Duration",
        "21 Days"
    )

    col2.metric(
        "Tests Studied",
        "7"
    )

    col3.metric(
        "Simulations",
        "3"
    )

    st.markdown("---")

    st.success("""
    Skills Developed:

    ✔ Transformer Design Concepts

    ✔ Transformer Manufacturing

    ✔ Isolation Transformer Construction

    ✔ Soft Start Systems

    ✔ Transformer Testing

    ✔ Industrial Safety

    ✔ Python Programming

    ✔ Engineering Simulation

    ✔ Technical Documentation
    """)

    st.info("""
    Internship Organization:
    Modern Electric Systems

    Domain:
    Transformer Design and Manufacturing

    Project:
    Isolation Transformer Analysis System

    Student:
    Priyanka G,
    Radhi S &
    Tamilselvi K

    Department:
    Electronics and Communication Engineering
    """)