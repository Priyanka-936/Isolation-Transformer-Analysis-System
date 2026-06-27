import streamlit as st
import pandas as pd


def show():

    st.title("🧪 Transformer Testing Dashboard")

    test_data = {
        "Test Performed": [
            "Continuity Test",
            "Insulation Resistance Test",
            "Winding Resistance Test",
            "Turns Ratio Test",
            "Load Test",
            "Visual Inspection",
            "Terminal Tightness Check"
        ],

        "Instrument Used": [
            "Digital Multimeter",
            "Megger (500V)",
            "Micro-ohmmeter",
            "TTR Meter",
            "Load Bank",
            "Visual Inspection",
            "Torque Wrench"
        ],

        "Observation": [
            "Continuity present",
            "IR > 100 MΩ",
            "Within limits",
            "Ratio within ±0.5%",
            "Voltage drop normal",
            "Assembly satisfactory",
            "Connections secure"
        ],

        "Result": [
            "PASS",
            "PASS",
            "PASS",
            "PASS",
            "PASS",
            "PASS",
            "PASS"
        ]
    }

    df = pd.DataFrame(test_data)

    st.subheader("Testing Observation Table")

    st.dataframe(
        df,
        use_container_width=True
    )

    st.success(
        f"Tests Passed: {len(df)}/{len(df)}"
    )

    st.markdown("---")

    selected = st.selectbox(
        "Select Test Procedure",
        df["Test Performed"]
    )

    row = df[
        df["Test Performed"] == selected
    ].iloc[0]

    st.subheader("Test Details")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Instrument",
            row["Instrument Used"]
        )

    with col2:
        st.metric(
            "Result",
            row["Result"]
        )

    st.info(
        row["Observation"]
    )

    st.markdown("---")

    st.subheader("Engineering Observation")

    st.write("""
    During the internship at Modern Electric Systems,
    the following transformer quality tests were studied:

    • Continuity Testing

    • Insulation Resistance Testing

    • Winding Resistance Measurement

    • Turns Ratio Verification

    • Load Testing

    • Visual Inspection

    • Terminal Tightness Verification

    These tests ensure the safety,
    reliability and performance of
    isolation transformers before dispatch.
    """)