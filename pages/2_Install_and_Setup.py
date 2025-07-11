import streamlit as st

windows_icon_url = "https://commons.wikimedia.org/wiki/File:Windows_logo_-_2002%E2%80%932012_(Black).svg#/media/File:Unofficial_Windows_logo_variant_-_2002%E2%80%932012_(Multicolored).svg"
macos_icon_url = "https://upload.wikimedia.org/wikipedia/commons/f/fa/Apple_logo_black.svg"


st.set_page_config(page_title="Install and Setup", page_icon="⚙️")

st.header("⚙️ Install and Setup")
tabs = st.tabs(["Linux", "Windows", "MacOS"])

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

# Windows installation section
with tabs[1]:
    col1, col2 = st.columns([1, 12])
    with col1:
        st.image('assets/windows.png', width=50)
    with col2:
        st.markdown("### Windows Installation")

        st.markdown("Click the button below to download the SegmentME Windows installer:")

        # 🔁 Replace this with your actual installer URL
        download_url = "https://yourdomain.com/downloads/SegmentME_installer.exe"

        st.markdown(f"[⬇ Download SegmentME Installer]({download_url})", unsafe_allow_html=True)


with tabs[2]:
    col1, col2 = st.columns([1, 12])
    with col1:
        st.image(macos_icon_url, width=30)
    with col2:
        st.code("""
                NotImplimentedYet
                """)
