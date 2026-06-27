import streamlit as st

def show():

    st.title("⚡ Transformer Rating Calculator")

    kva = st.number_input(
        "Transformer Rating (kVA)",
        min_value=1,
        max_value=1000,
        value=10
    )

    voltage = st.number_input(
        "Operating Voltage (V)",
        value=230
    )

    current = (kva * 1000) / voltage

    st.markdown("## Calculated Results")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Transformer Rating",
            f"{kva} kVA"
        )

    with col2:
        st.metric(
            "Rated Current",
            f"{current:.2f} A"
        )

    st.markdown("---")

    st.subheader("Engineering Calculation")

    st.code(
        f"""
Rated Current = (kVA × 1000) / Voltage

Rated Current = ({kva} × 1000) / {voltage}

Rated Current = {current:.2f} A
        """
    )

    st.markdown("---")

    st.info(f"""
### Engineering Observation

• Transformer Rating : {kva} kVA

• Operating Voltage : {voltage} V

• Rated Current : {current:.2f} A

During my internship at Modern Electric Systems,
I learned that the rated current of an isolation
transformer is determined by its power rating and
operating voltage. This calculation is essential for:

✓ Cable sizing

✓ Protection device selection

✓ Soft start system design

✓ Transformer performance analysis
    """)