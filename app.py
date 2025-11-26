import streamlit as st
from generate_brief import generate_ai_brief
from pdf_export import create_pdf

st.set_page_config(page_title="Product Brief Generator", page_icon="🧵", layout="centered")

st.title("🧵 Product Brief Generator (AI Powered)")

st.write("Generate clean, consistent product briefs for merchandising, design, and PLM teams — instantly.")

# ---- INPUT FIELDS ----
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
attributes = st.text_area("Key Attributes (comma separated)", 
                          placeholder="moisture wicking, 4-way stretch, soft-hand feel")

st.divider()

# ---- GENERATE BUTTON ----
if st.button("Generate Brief 🚀", type="primary"):
    with st.spinner("Generating content with OpenAI…"):
        
        inputs = {
            "product_line": product_line,
            "category": category,
            "style_name": style_name,
            "season": season,
            "customer": customer,
            "use_case": use_case,
            "main_fabric": main_fabric,
            "secondary_fabric": secondary_fabric,
            "attributes": attributes
        }

        try:
            result = generate_ai_brief(inputs)
        except Exception as e:
            st.error(f"Error generating brief: {e}")
            st.stop()

        st.success("Brief Generated Successfully!")

        st.subheader("📄 Final Output")
        st.write(result)

        # Download PDF
        pdf_file = create_pdf(result, "product_brief.pdf")
        with open(pdf_file, "rb") as f:
            st.download_button(
                label="Download PDF",
                data=f,
                file_name="product_brief.pdf",
                mime="application/pdf"
            )
