 import streamlit as st
from urllib.parse import urlparse
import re

def check_url(url):
    if not url or not url.strip():
        return "⚠️ Please enter a website URL.", ""

    url = url.strip()
    risk_score = 0
    reasons = []

    if not url.lower().startswith("https://"):
        risk_score += 20
        reasons.append("❌ No HTTPS")

    if len(url) > 75:
        risk_score += 15
        reasons.append("⚠️ Very long URL")

    if "@" in url:
        risk_score += 20
        reasons.append("⚠️ @ symbol found")

    if re.search(r"https?://(\d{1,3}\.){3}\d{1,3}", url):
        risk_score += 25
        reasons.append("❌ IP address used instead of domain")

    suspicious_words = [
        "login", "verify", "account", "update",
        "password", "confirm", "secure", "bank"
    ]

    found_words = [
        word for word in suspicious_words
        if word in url.lower()
    ]

    if found_words:
        risk_score += 15
        reasons.append(
            "⚠️ Suspicious words: " + ", ".join(found_words)
        )

    try:
        hostname = urlparse(url).hostname
        if hostname and len(hostname.split(".")) > 3:
            risk_score += 15
            reasons.append("⚠️ Too many subdomains")
    except:
        pass

    risk_score = min(risk_score, 100)

    if risk_score >= 60:
        result = "🔴 HIGH RISK - Possible Phishing Website"
    elif risk_score >= 30:
        result = "🟠 MEDIUM RISK - Be Careful"
    else:
        result = "🟢 LOW RISK - No major suspicious indicators found"

    details = "\n".join(reasons) if reasons else "✅ No suspicious indicators detected."

    return result, f"Risk Score: {risk_score}/100\n\n{details}"


st.set_page_config(
    page_title="AI Phishing Website Detector",
    page_icon="🛡️"
)

st.title("🛡️ AI Phishing Website Detector")
st.write("Enter a website URL to check for common phishing indicators.")

url = st.text_input(
    "Enter Website URL",
    placeholder="https://example.com"
)

if st.button("Check URL"):
    result, details = check_url(url)

    st.subheader("Detection Result")
    st.write(result)

    st.subheader("Risk Analysis")
    st.text(details)
