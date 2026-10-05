import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import re

# --- Auth with Google Sheets ---
scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]
creds = Credentials.from_service_account_info(st.secrets["google"], scopes=scope)
client = gspread.authorize(creds)
sheet = client.open("SegmentME Downloads").worksheet("Contact")  # assumes second worksheet

def log_contact(name, email, message):
    timestamp = datetime.now().isoformat()
    sheet.append_row([timestamp, name, email, message])

# --- Page Setup ---
st.set_page_config(page_title="Contact", page_icon="📩", layout="wide")
st.title("📩 Contact Me")
st.caption("Having trouble with SegmentME or just want to say hi? I'm happy to hear from you!")

# --- Add Illustration ---

st.markdown("### 📬 How can I help?")
st.markdown(
    """
    Fill in the form below to send me a message directly.
    I typically respond within 1–2 days.
    
    You can ask about:
    - ❓ Issues installing or using SegmentME
    - 🐞 Reporting a bug
    - 💡 Feature requests
    - 🙋 General feedback or questions

    If something went wrong, attach your log file, `segmentme.log`:
    - **Windows:** `%APPDATA%\\segmentme\\logs`
    - **macOS:** `~/Library/Logs/segmentme`
    - **Linux:** `~/.config/segmentme/logs`
    """
)

st.markdown("---")

# --- Contact Form ---
with st.form("contact_form", border=True):
    name = st.text_input("👤 Your Name", placeholder="e.g. John Doe")
    email = st.text_input("📧 Email Address", placeholder="e.g. john@example.com")
    message = st.text_area("💬 Your Message", placeholder="Describe the issue or your suggestion...")
    submitted = st.form_submit_button("📨 Send Message")

    if submitted:
        if not name or not email or not message:
            st.error("❗ Please fill in all fields.")
        elif not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            st.error("❗ Please enter a valid email address.")
        else:
            log_contact(name, email, message)
            st.success("✅ Your message has been sent! I’ll get back to you as soon as possible.")
            st.balloons()

# --- Footer: Links & Credits ---
st.markdown("---")
st.markdown(
    "🔗 Useful Links: "
    "[GitHub](https://github.com/StevetheGreek97/SegmentME-docs) • "
    "[Documentation](https://segmentme.streamlit.app/) • "
    "[Research Group](https://www.biologie.uni-hamburg.de/forschung/populationsgenomik.html)"
)

st.markdown("---")
st.caption("☕ **Support This Project**")
st.caption(
    "SegmentME is open source and developed with love as part of my academic work. "
    "If you find it useful and want to support its development, consider buying me a coffee via PayPal 💙"
)

# Replace with your real PayPal.me link or donation button
st.caption(
    "[![Donate via PayPal](https://img.shields.io/badge/Donate-PayPal-blue.svg?logo=paypal&style=for-the-badge)]"
    "(https://www.paypal.me/yourusername)"
)
