import streamlit as st
from groq_client import chat_with_groq
from io import BytesIO

st.set_page_config(page_title="Brochure AI", layout="centered")
st.title("📄 Brochure Generator")

st.write("Generate marketing brochures using AI.")

# --- Input form ---
with st.form("brochure_form"):
    company_name = st.text_input("Company name")
    product = st.text_input("Product / Service")
    audience = st.text_input("Target audience")
    tone = st.selectbox("Tone", ["Professional", "Friendly", "Bold", "Luxury", "Playful"])
    submit = st.form_submit_button("Generate Brochure")

# --- Handle generation ---
if submit:
    if not company_name or not product or not audience:
        st.warning("Please fill all fields.")
    else:
        prompt = f"""
You are a marketing copywriter.

Write a brochure for:
Company: {company_name}
Product: {product}
Target audience: {audience}
Tone: {tone}

Structure:
- Headline
- Subheadline
- 3 benefit bullets
- Short call-to-action
"""

        messages = [
            {"role": "system", "content": "You are a helpful marketing assistant."},
            {"role": "user", "content": prompt}
        ]

        with st.spinner("Generating brochure..."):
            result = chat_with_groq(messages)
         
        st.markdown("### 📄 Generated Brochure")
        st.markdown(result)

        st.download_button(
        label="⬇️ Download Brochure",
        data=brochure,
        file_name=f"{company_name}_brochure.txt",
        mime="text/plain"
)
