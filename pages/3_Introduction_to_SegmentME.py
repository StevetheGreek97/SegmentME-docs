import streamlit as st

st.set_page_config(page_title="Introduction to SegmentME", page_icon="🧭", layout='wide')
st.title("SegmentME Annotation Interface")

st.markdown("""
This section describes the SegmentME annotation interface and its key components. 
We recommend reviewing this section before starting your annotation tasks.
""")

st.markdown("### Interface Overview")
st.image("assets/interface.png", 
         caption="SegmentME Interface Overview", 
         width=1000,
         use_column_width=False)

st.markdown("### 🔍 Component Descriptions")

with st.expander("🟥 Menu Bar"):
    st.markdown("""
The top **Menu Bar** gives access to essential actions:
- **File**: Import images, save/export annotations, exit.
- **Actions**: Run model inference (YOLO/SAM).
- **View**: Change view settings (fullscreen etc.).
- **Help**: Open the documentation or About dialog.
""")

with st.expander("⬅️ Control Bar"):
    st.markdown("""
The **Control Bar** on the left contains buttons to:
- Navigate between images (← →)
- Select segmentation tools like:
  - `Segment Anything 2` (SAM2)
  - `SAM2-Box` for box-based segmentation
  - `DEXTR` for extreme points
  - `✎` Manual drawing tool
  - `✂` Intelligent scissors
- Select class label
- Add new classes or remove selected masks
""")

with st.expander("🖼️ Image Display"):
    st.markdown("""
The central **Image Display** panel shows the current image with overlaid annotations.
- You can zoom, pan, and click to select masks.
- Drawing and editing are interactive in this area.
- Keyboard shortcuts:  
  - `S` to save mask  
  - `E` to generate mask with model  
""")

with st.expander("🗂️ Annotation Bar"):
    st.markdown("""
The **Annotation Bar** on the right displays:
- A table of all masks in the current image.
- Each entry shows:
  - **Image name**
  - **Mask ID**
  - **Surface Area**
  - **Class**
- Below the table, **Annotation Statistics** show instance counts per class:
  - Across **All Images**
  - For the **Current Image** only
""")
