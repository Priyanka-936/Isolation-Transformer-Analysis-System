import streamlit as st
from PIL import Image
import os


def show():

    st.title("🏭 Isolation Transformer Construction Viewer")

    image_path = "images/mes_transformer.jpg"

    if os.path.exists(image_path):

        img = Image.open(image_path)

        st.image(
            img,
            caption="Modern Electric Systems Isolation Transformer",
            use_container_width=True
        )

    else:
        st.warning(
            "Transformer image not found."
        )

    st.markdown("---")

    components = {

        "Primary Winding":
        {
            "Function":
            "Receives the input AC voltage and generates magnetic flux.",

            "Material":
            "Copper conductor",

            "Observation":
            "Observed during winding and assembly processes."
        },

        "Secondary Winding":
        {
            "Function":
            "Provides isolated output voltage.",

            "Material":
            "Copper conductor",

            "Observation":
            "Studied winding arrangement and insulation."
        },

        "Laminated Silicon Steel Core":
        {
            "Function":
            "Provides magnetic path and reduces eddy current losses.",

            "Material":
            "CRGO Silicon Steel",

            "Observation":
            "Observed during core assembly."
        },

        "Insulation System":
        {
            "Function":
            "Ensures electrical isolation and safety.",

            "Material":
            "Pressboard and insulation sheets",

            "Observation":
            "Handled insulation materials under supervision."
        },

        "Terminal Assembly":
        {
            "Function":
            "Provides secure electrical connections.",

            "Material":
            "Copper and brass terminals",

            "Observation":
            "Studied terminal arrangement and wiring."
        },

        "Mechanical Frame":
        {
            "Function":
            "Supports transformer structure.",

            "Material":
            "Mild steel frame",

            "Observation":
            "Observed enclosure mounting."
        },

        "Soft Start Circuit":
        {
            "Function":
            "Limits startup inrush current.",

            "Material":
            "Relay, resistor and contactor",

            "Observation":
            "Studied Auto and Manual Soft Start Systems."
        }
    }

    selected = st.selectbox(
        "Select Transformer Component",
        list(components.keys())
    )

    component = components[selected]

    st.subheader(selected)

    st.info(
        f"Function: {component['Function']}"
    )

    st.write(
        f"Material: {component['Material']}"
    )

    st.write(
        f"Internship Observation: {component['Observation']}"
    )

    st.markdown("---")

    st.success("""
    Key Construction Features Observed:

    ✔ Copper Windings

    ✔ Laminated Silicon Steel Core

    ✔ Pressboard Insulation

    ✔ Air Cooling System

    ✔ Heavy Duty Terminal Blocks

    ✔ Soft Start Protection System
    """)