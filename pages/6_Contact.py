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
st.set_page_config(page_title="Contact", page_icon="📩")
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

st.markdown(
    "👨‍🔬 *SegmentME is developed as part of my work at the "
    "[Population Genomics Group, University of Hamburg](https://www.biologie.uni-hamburg.de/forschung/populationsgenomik.html).*\n\n"
    "🔒 *Your contact information will only be used to respond to your message. "
    "It will not be shared or used for any marketing purposes.*"
)
