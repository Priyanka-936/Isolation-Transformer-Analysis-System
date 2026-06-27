import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show():

    st.title("📊 Transformer Analytics Dashboard")

    st.subheader("MES Isolation Transformer Data Analysis")

    # MES sample data
    df = pd.DataFrame({
        "Rating":[1,2,3,5,10,15,25,50,100,150,250,500,750,1000],
        "Weight":[25,35,45,65,90,140,160,295,490,525,760,1100,1700,2250],
        "Efficiency":[92,93,94,95,96,96.5,97,97.5,98,98.2,98.5,98.8,99,99.2]
    })

    st.dataframe(df)

    st.markdown("---")

    # Graph 1
    st.subheader("1. Transformer Rating vs Weight")

    fig, ax = plt.subplots(figsize=(8,5))

    ax.plot(
        df["Rating"],
        df["Weight"],
        marker='o'
    )

    ax.set_xlabel("Rating (kVA)")
    ax.set_ylabel("Weight (kg)")
    ax.set_title("Rating vs Weight")

    st.pyplot(fig)

    st.info("""
Observation:
As transformer rating increases,
the core size, copper winding
and insulation requirement increase,
which increases the total weight.
""")

    st.markdown("---")

    # Graph 2
    st.subheader("2. Transformer Efficiency")

    fig2, ax2 = plt.subplots(figsize=(8,5))

    ax2.plot(
        df["Rating"],
        df["Efficiency"],
        marker='o'
    )

    ax2.set_xlabel("Rating (kVA)")
    ax2.set_ylabel("Efficiency (%)")
    ax2.set_title("Efficiency vs Rating")

    st.pyplot(fig2)

    st.info("""
Observation:
Higher rated transformers
generally provide better efficiency
because fixed losses become smaller
relative to output power.
""")

    st.markdown("---")

    st.success("""
Key Engineering Findings:

✓ Transformer weight increases with rating.

✓ Efficiency improves with larger transformers.

✓ Core losses and copper losses affect performance.

✓ Soft start systems reduce high inrush current.

✓ Isolation transformers provide electrical safety.
""")