import streamlit as st
from utils.utils import get_text
st.set_page_config(page_title="Tools", page_icon="🛠️")

st.title("🛠️ Annotation Tools in SegmentME")

st.markdown("""
SegmentME provides multiple annotation tools to suit various image segmentation needs.  
**AI-powered tools** let you guide the model interactively, while **manual tools** offer full control over the shape.

### 🎯 Shortcuts 
- Press **`E`** → to execute the segmentation model (only for AI tools)
- Press **`S`** → to finalize and save the mask (all tools)

--- 
""")

tools = get_text("tools")

for name, data in tools.items():
    st.subheader(f"🔹 {name}")
    st.markdown(f" {data['desc']}")
    citation = data.get("citation")
    if citation:
        st.markdown(f"**Relevant Paper:** {citation}")

    try:
        st.video(data["video"])
    except KeyError:
        st.markdown("No video available for this tool.")
    st.markdown("---")
