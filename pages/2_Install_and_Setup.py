import streamlit as st

import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
from utils.utils import is_valid_email
windows_icon_url = "https://commons.wikimedia.org/wiki/File:Windows_logo_-_2002%E2%80%932012_(Black).svg#/media/File:Unofficial_Windows_logo_variant_-_2002%E2%80%932012_(Multicolored).svg"
macos_icon_url = "https://upload.wikimedia.org/wikipedia/commons/f/fa/Apple_logo_black.svg"



# Set up Google Sheets access using secrets
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

# UI setup
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
    col1, col2 = st.columns([1, 12])
    with col1:
        st.image("assets/windows.png", width=50)
    with col2:
        st.markdown("### Windows Installation")

    st.markdown("To access the SegmentME Windows installer, please fill in the form below.")

    with st.container():
        st.markdown("#### 📝 Request Download Link")
        st.markdown("*This helps us keep track of usage and improve the tool.*")

        with st.form("windows_download_form", border=True):
            name = st.text_input("👤 Your Name", placeholder="e.g. John Doe")
            email = st.text_input("📧 Email Address", placeholder="e.g. john@example.com")
            submitted = st.form_submit_button("📥 Get Installer")

            if submitted:
                if not name or not email:
                    st.error("❗ Please fill in both your name and email.")
                elif not is_valid_email(email):
                    st.error("❗ Please enter a valid email address.")
                else:
                    log_download(name, email)
                    st.success("✅ Thanks, your download is ready below:")
                    download_url = "https://github.com/StevetheGreek97/SegmentME-docs/releases/download/v0.0.1/SegmentME.exe"
                    st.markdown(f"[⬇ Download SegmentME for Windows]({download_url})", unsafe_allow_html=True)

# --- macOS tab ---
with tabs[2]:
    col1, col2 = st.columns([1, 12])
    with col1:
        st.image(macos_icon_url, width=30)
    with col2:
        st.markdown("### MacOS Installation")
        st.code("NotImplementedYet")
