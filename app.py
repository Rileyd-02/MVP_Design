import streamlit as st
from generate_brief import generate_ai_brief
from pdf_export import create_pdf
from utils import save_brief_locally, clean_input
from dotenv import load_dotenv
import os

# Load .env locally (optional)
load_dotenv()

st.set_page_config(page_title="Product Brief Generator", page_icon="🧵", layout="centered")
st.title("🩱🩱 Product Brief Generator (OpenRouter AI)")

st.write("Generate structured product briefs for merchandising/design teams instantly.")

# --- Input Fields ---
col1, col2 = st.columns(2)

with col1:
    product_line = st.selectbox("Product Line", ["Active", "Lounge", "Casual", "Athleisure"])
    season = st.selectbox("Season", ["SS25", "AW25", "SS26"])
    customer = st.selectbox("Target Customer", ["Men", "Women", "Kids", "Unisex"])

with col2:
    category = st.text_input("Product Category (Tee, Hoodie, Legging...)")
    style_name = st.text_input("Style Name / Working Name")
    use_case = st.selectbox("Use Case", ["Performance", "Casual", "Lounge", "Training", "Workwear"])

main_fabric = st.text_input("Main Fabric")
secondary_fabric = st.text_input("Secondary Fabric (optional)")
attributes = st.text_area(
    "Key Attributes (comma separated)",
    placeholder="moisture wicking, 4-way stretch, soft-hand feel"
)

st.divider()

# --- Generate Button ---
if st.button("Generate Brief 🚀", type="primary"):
    with st.spinner("Generating product brief…"):
        try:
            # Clean inputs
            inputs = {
                "product_line": clean_input(product_line),
                "category": clean_input(category),
                "style_name": clean_input(style_name),
                "season": clean_input(season),
                "customer": clean_input(customer),
                "use_case": clean_input(use_case),
                "main_fabric": clean_input(main_fabric),
                "secondary_fabric": clean_input(secondary_fabric),
                "attributes": clean_input(attributes)
            }

            result = generate_ai_brief(inputs)

            # Auto-save the brief locally
            saved_file = save_brief_locally(result)
        except Exception as e:
            st.error(f"Error generating brief: {e}")
            st.stop()

        st.success("Brief Generated Successfully!")

        st.subheader("📄 Product Brief")
        st.write(result)

        st.info(f"Brief auto-saved locally: `{saved_file}`")

        # --- Download PDF ---
        pdf_file = create_pdf(result)
        with open(pdf_file, "rb") as f:
            st.download_button(
                label="Download PDF",
                data=f,
                file_name="product_brief.pdf",
                mime="application/pdf"
            )
