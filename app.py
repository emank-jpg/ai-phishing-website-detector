import streamlit as st

st.set_page_config(
    page_title="Phishing Website Detector",
    page_icon="🛡️"
)

st.title("🛡️ Phishing Website Detector")

st.write("Enter a website URL to check its risk level.")

url = st.text_input(
    "Website URL",
    placeholder="https://example.com"
)

if st.button("Analyse Website"):
    if url == "":
        st.warning("Please enter a website URL.")
    else:
        st.success("URL received successfully!")
        st.write("Website:", url)