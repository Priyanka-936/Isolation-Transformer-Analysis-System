import streamlit as st
import pandas as pd


def show():

    st.title("📊 MES Isolation Transformer Database")

    data = {
        "Rating (kVA)": [
            1,2,3,5,10,15,25,50,
            100,150,200,250,
            350,500,750,1000
        ],

        "Model Number": [
            "MES-IT-1KVA",
            "MES-IT-2KVA",
            "MES-IT-3KVA",
            "MES-IT-5KVA",
            "MES-IT-10KVA",
            "MES-IT-15KVA",
            "MES-IT-25KVA",
            "MES-IT-50KVA",
            "MES-IT-100KVA",
            "MES-IT-150KVA",
            "MES-IT-200KVA",
            "MES-IT-250KVA",
            "MES-IT-350KVA",
            "MES-IT-500KVA",
            "MES-IT-750KVA",
            "MES-IT-1MVA"
        ],

        "Length (mm)": [
            300,300,300,320,360,380,470,600,
            620,740,880,950,950,1150,1350,1500
        ],

        "Width (mm)": [
            200,200,250,350,320,400,420,450,
            450,500,550,550,650,700,850,850
        ],

        "Height (mm)": [
            350,350,350,360,550,600,600,650,
            650,850,850,950,1150,1300,1500,1500
        ],

        "Weight (kg)": [
            25,35,45,65,90,140,160,295,
            490,525,650,850,980,1100,2050,2250
        ]
    }

    df = pd.DataFrame(data)

    st.subheader("MES Isolation Transformer Specifications")

    st.dataframe(
        df,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader("Search Transformer")

    rating = st.selectbox(
        "Select Transformer Rating",
        df["Rating (kVA)"]
    )

    selected = df[
        df["Rating (kVA)"] == rating
    ]

    st.markdown("### Selected Transformer Details")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Model",
            selected.iloc[0]["Model Number"]
        )

        st.metric(
            "Weight",
            f"{selected.iloc[0]['Weight (kg)']} kg"
        )

    with col2:
        st.metric(
            "Length",
            f"{selected.iloc[0]['Length (mm)']} mm"
        )

        st.metric(
            "Width",
            f"{selected.iloc[0]['Width (mm)']} mm"
        )

    with col3:
        st.metric(
            "Height",
            f"{selected.iloc[0]['Height (mm)']} mm"
        )

        st.metric(
            "Rating",
            f"{rating} kVA"
        )

    st.markdown("---")

    st.info(f"""
### Engineering Observation

• Transformer Rating : {rating} kVA

• Model Number :
  {selected.iloc[0]['Model Number']}

• Dimensions :
  {selected.iloc[0]['Length (mm)']} ×
  {selected.iloc[0]['Width (mm)']} ×
  {selected.iloc[0]['Height (mm)']} mm

• Weight :
  {selected.iloc[0]['Weight (kg)']} kg

During my internship at Modern Electric Systems,
I studied various ratings of isolation transformers
ranging from 1 kVA to 1000 kVA. It was observed that
the dimensions, weight, copper winding quantity,
core size, and insulation requirements increase
with transformer rating.
""")