import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
from utils.utils import is_valid_email, notify_admin
# Icons
windows_icon_url = "https://commons.wikimedia.org/wiki/File:Windows_logo_-_2002%E2%80%932012_(Black).svg#/media/File:Unofficial_Windows_logo_variant_-_2002%E2%80%932012_(Multicolored).svg"
macos_icon_url = "https://upload.wikimedia.org/wikipedia/commons/f/fa/Apple_logo_black.svg"

# Google Sheets setup
scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]
creds = Credentials.from_service_account_info(st.secrets["google"], scopes=scope)
client = gspread.authorize(creds)
sheet = client.open("SegmentME Downloads").sheet1

def log_download(name, email):
    timestamp = datetime.now().isoformat()
    sheet.append_row([timestamp, name, email])

# Page setup
st.set_page_config(page_title="Install and Setup", page_icon="⚙️")
st.header("⚙️ Install and Setup")

tabs = st.tabs(["Linux", "Windows", "MacOS"])

# --- Linux tab ---
with tabs[0]:
    st.markdown("### 🐧 Linux Installation Instructions")
    st.markdown("Follow these steps to install and run SegmentME on most Debian/Ubuntu-based systems:")

    st.markdown("#### Step 1: Update your system and install dependencies")
    st.code("""
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip python3-venv
    """)

    st.markdown("#### Step 2: Create and activate a virtual environment (recommended)")
    st.code("""
python3 -m venv segmentme-env
source segmentme-env/bin/activate
    """)

    st.markdown("#### Step 3: Download or clone SegmentME and install requirements")
    st.code("""
git clone https://github.com/yourusername/SegmentME.git
cd SegmentME
pip install -r requirements.txt
    """)

    st.markdown("#### Step 4: Run SegmentME")
    st.code("python main.py")
    st.success("SegmentME is now installed and running on your Linux system.")

# --- Windows tab ---
with tabs[1]:
    st.image("assets/windows.png", width=50)
    st.markdown("### Windows Installer Request")

    st.markdown("Please fill out the form below to request the Windows version of SegmentME.")
    st.markdown("*You will receive the link by email after your request is approved.*")

    with st.form("windows_download_form", border=True):
        name = st.text_input("🧑 First Name")
        last_name = st.text_input("👨‍🦱 Last Name")
        email = st.text_input("📧 Email Address", placeholder="e.g. john@example.com")
        comments = st.text_area("💬 Comments (optional)", height=100)
        submitted = st.form_submit_button("📨 Submit Request")

        if submitted:
            if not name or not last_name or not email:
                st.error("❗ Please fill in your name, last name, and email.")
            elif not is_valid_email(email):
                st.error("❗ Please enter a valid email address.")
            else:
                # Log in Google Sheet
                log_download(name + " " + last_name, email)

                # Send you an email with their info
                try:
                    notify_admin(
                        name,
                        last_name,
                        email,
                        comments,
                        smtp_user=st.secrets["email"]["user"],
                        smtp_pass=st.secrets["email"]["password"],
                        recipient_email=st.secrets["email"]["user"]
                    )
                    st.success("✅ Thanks! Your request has been submitted. You’ll receive the installer via email soon.")
                except Exception as e:
                    st.warning(f"Request was logged but email failed to send. Error: {e}")
# --- macOS tab ---
with tabs[2]:
    col1, col2 = st.columns([1, 12])
    with col1:
        st.image(macos_icon_url, width=30)
    with col2:
        st.markdown("### MacOS Installation")
    st.code("NotImplementedYet")
