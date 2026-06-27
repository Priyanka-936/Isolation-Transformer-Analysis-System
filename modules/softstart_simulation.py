import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


def show():

    st.title("📈 Soft Start System Simulation")

    kva = st.number_input(
        "Transformer Rating (kVA)",
        min_value=1,
        max_value=1000,
        value=10
    )

    voltage = st.number_input(
        "Voltage (V)",
        value=230
    )

    rated_current = (kva * 1000) / voltage
    inrush_current = rated_current * 8

    time = np.linspace(0, 10, 100)

    # Without soft start
    without_softstart = (
        rated_current +
        (inrush_current - rated_current)
        * np.exp(-time)
    )

    # With soft start
    with_softstart = (
        rated_current +
        (rated_current * 1.5)
        * np.exp(-time / 2)
    )

    st.subheader("Startup Current Comparison")

    fig, ax = plt.subplots(figsize=(8,5))

    ax.plot(
        time,
        without_softstart,
        label="Without Soft Start"
    )

    ax.plot(
        time,
        with_softstart,
        label="With Soft Start"
    )

    ax.set_xlabel("Time (seconds)")
    ax.set_ylabel("Current (A)")
    ax.legend()

    st.pyplot(fig)

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Rated Current",
            f"{rated_current:.2f} A"
        )

    with col2:
        st.metric(
            "Estimated Inrush",
            f"{inrush_current:.2f} A"
        )

    st.warning(
        "Without soft start, transformer inrush current can become very high."
    )

    st.success(
        "Soft start reduces startup current and protects equipment."
    )

    st.markdown("""
    ### Engineering Observation

    During the internship at Modern Electric Systems,
    it was observed that isolation transformers
    experience a high transient current during startup.

    The soft start system temporarily limits the
    current using a resistor/contact arrangement
    and gradually brings the transformer to
    normal operating conditions.

    This reduces:

    • Inrush current  
    • Voltage dips  
    • Relay tripping  
    • Stress on transformer windings  
    • Damage to connected equipment
    """)