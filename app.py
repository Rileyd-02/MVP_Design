import streamlit as st
from generate_brief import generate_ai_brief
from utils import save_brief_locally, clean_input
from pdf_export import create_pdf
from dotenv import load_dotenv

load_dotenv()

st.set_page_config("Product Brief Generator", "🩱")
st.title("🧵 Product Brief Generator (OpenRouter)")

col1, col2 = st.columns(2)

with col1:
    product_line = st.selectbox("Product Line", ["Active", "Casual", "Lounge"])
    season = st.selectbox("Season", ["SS25", "AW25"])
    customer = st.selectbox("Customer", ["Men", "Women", "Kids"])

with col2:
    category = st.text_input("Category")
    style_name = st.text_input("Style Name")
    use_case = st.selectbox("Use Case", ["Performance", "Casual", "Lounge"])

main_fabric = st.text_input("Main Fabric")
secondary_fabric = st.text_input("Secondary Fabric")
attributes = st.text_area("Key Attributes")

if st.button("Generate Brief 🚀", type="primary"):
    with st.spinner("Generating…"):
        inputs = {
            "product_line": clean_input(product_line),
            "category": clean_input(category),
            "style_name": clean_input(style_name),
            "season": season,
            "customer": customer,
            "use_case": use_case,
            "main_fabric": clean_input(main_fabric),
            "secondary_fabric": clean_input(secondary_fabric),
            "attributes": clean_input(attributes)
        }

        brief = generate_ai_brief(inputs)
        saved = save_brief_locally(brief)

    st.success("Brief generated!")
    st.write(brief)
    st.info(f"Saved locally: {saved}")

    pdf = create_pdf(brief)
    with open(pdf, "rb") as f:
        st.download_button("Download PDF", f, file_name="product_brief.pdf")
