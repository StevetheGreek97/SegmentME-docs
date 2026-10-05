import streamlit as st

st.set_page_config(page_title="Quick Start", page_icon="🚀", layout="wide")

st.title("🚀 Quick Start")

st.markdown("""
This takes you from a folder of images to exported annotations in seven steps. Each step links to the page
with the full details.
""")

st.subheader("1. Install and open SegmentME")
st.markdown("Request your build, then start the app.")
st.page_link("pages/2_Install_and_Setup.py", label="Install and Setup", icon="⚙️")

st.subheader("2. Create a project")
st.markdown("On the startup screen, click **New Project**.")

st.subheader("3. Import images")
st.markdown("Use **File → Import Images**.")

st.subheader("4. Add classes")
st.markdown("In the sidebar, under **Classes**, click **Add Class**.")
st.page_link("pages/5_Projects_and_Export.py", label="Projects and Export", icon="📂")

st.subheader("5. Annotate")
st.markdown("""
Turn on **SAM** in the sidebar. Left-click the object, right-click the background, press **`E`** to generate
the mask, and press **`S`** to save it. DEXTR, Manual, and Scissors work the same way with their own keys.
""")
st.page_link("pages/6_Tools.py", label="Annotation tools", icon="🛠️")

st.subheader("6. Review")
st.markdown("""
Open **File → Annotations** to check every mask. Right-click a mask to set its class, split it, edit it with the
brush, or delete it.
""")
st.page_link("pages/4_Interface.py", label="Interface", icon="🧭")

st.subheader("7. Export")
st.markdown("""
Use **File → Export annotations** for a YOLO or COCO dataset, or **File → Save Results** for a CSV of every mask.
""")

st.divider()
st.markdown("**Next, run models across a project or train your own:**")
st.page_link("pages/7_Models_and_Training.py", label="Models and Training", icon="🧠")
