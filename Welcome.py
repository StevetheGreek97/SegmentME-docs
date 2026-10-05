import streamlit as st
from utils.utils import get_text

st.set_page_config(page_title="SegmentME Manual", page_icon="assets/logo.png", layout="wide")

col1, col2 = st.columns([1, 17])
with col1:
    st.image("assets/logo.png", width=70)
with col2:
    st.markdown("## SegmentME Manual")

st.markdown(get_text("intro"))

st.markdown("### Start here")
row1 = st.columns(4)
with row1[0]:
    st.page_link("pages/3_Quick_Start.py", label="Quick Start", icon="🚀")
with row1[1]:
    st.page_link("pages/2_Install_and_Setup.py", label="Install and Setup", icon="⚙️")
with row1[2]:
    st.page_link("pages/4_Interface.py", label="Interface", icon="🧭")
with row1[3]:
    st.page_link("pages/6_Tools.py", label="Annotation Tools", icon="🛠️")

st.markdown("### Reference")
row2 = st.columns(4)
with row2[0]:
    st.page_link("pages/5_Projects_and_Export.py", label="Projects and Export", icon="📂")
with row2[1]:
    st.page_link("pages/7_Models_and_Training.py", label="Models and Training", icon="🧠")
with row2[2]:
    st.page_link("pages/1_Discover_and_Learn.py", label="Terminology", icon="📘")
with row2[3]:
    st.page_link("pages/8_Contact.py", label="Contact", icon="📩")

st.divider()

try:
    with open("assets/tour/tester.mp4", "rb") as video_file:
        st.video(video_file.read(), loop=True, autoplay=True)
except Exception:
    pass

st.caption(
    "Made by Stylianos (Steve) Mavrianos, [Population Genomics Lab](https://www.biologie.uni-hamburg.de/forschung/populationsgenomik.html), "
    "[GitHub](https://github.com/StevetheGreek97)."
)
