import streamlit as st

def show():

    st.title("🔥 Transformer Inrush Current Calculator")

    kva = st.number_input(
        "Select Transformer Rating (kVA)",
        min_value=1,
        max_value=1000,
        value=10
    )

    voltage = st.number_input(
        "Operating Voltage (V)",
        value=230
    )

    st.subheader("Inrush Current Multiplier")

    multiplier = st.slider(
        "",
        6,
        10,
        8
    )

    rated_current = (kva * 1000) / voltage
    inrush_current = rated_current * multiplier

    st.markdown("## Calculated Results")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Rated Current",
            f"{rated_current:.2f} A"
        )

    with col2:
        st.metric(
            "Estimated Inrush Current",
            f"{inrush_current:.2f} A"
        )

    if inrush_current > rated_current * 5:
        st.warning(
            "High inrush current can trip protective devices."
        )

        st.success(
            "Soft Start System is recommended."
        )

    st.markdown("---")

    st.info(f"""
    ### Engineering Observation

    • Transformer Rating : {kva} kVA

    • Operating Voltage : {voltage} V

    • Rated Current : {rated_current:.2f} A

    • Estimated Inrush Current :
      {multiplier} × Rated Current

    • Calculated Inrush :
      {inrush_current:.2f} A

    During the internship at Modern Electric Systems,
    it was observed that isolation transformers may
    draw 6–10 times the rated current during startup.
    Therefore, soft-start circuits are implemented
    to limit the inrush current and protect equipment.
    """)