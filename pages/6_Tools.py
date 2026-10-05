import streamlit as st
from utils.utils import get_text

st.set_page_config(page_title="Tools", page_icon="🛠️", layout="wide")

st.title("🛠️ Annotation Tools")

st.markdown("""
Four sidebar tools draw a new mask on the current image: **SAM**, **DEXTR**, **Manual**, and **Intelligent
Scissors**. Two editing tools, **Split Mask** and **Brush Edit**, change a mask that already exists. Right-click the
mask to reach them.

Across the tools, **`E`** generates a mask with the model (SAM and DEXTR only), and **`S`** saves it. Split Mask
doesn't need either key: it cuts when you release the mouse.
""")
st.markdown("---")

tools = get_text("tools")

for name, data in tools.items():
    st.subheader(name)
    st.markdown(data["desc"])
    citation = data.get("citation")
    if citation:
        st.markdown(f"**Reference:** {citation}")
    video = data.get("video")
    if video:
        with st.expander(f"📽️ Watch: {name}"):
            st.video(video)
    st.markdown("---")
