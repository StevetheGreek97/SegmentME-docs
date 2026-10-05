import streamlit as st

st.set_page_config(page_title="Interface", page_icon="🧭", layout="wide")

st.markdown("""
<style>
    .hero {
        padding: 1.8rem 2rem;
        border-radius: 18px;
        border: 1px solid rgba(128, 128, 128, 0.2);
        background: linear-gradient(135deg,
            rgba(59, 130, 246, 0.16) 0%,
            rgba(16, 185, 129, 0.12) 55%,
            rgba(245, 158, 11, 0.10) 100%);
        margin-bottom: 1.4rem;
    }
    .hero h1 { margin: 0 0 0.4rem 0; font-size: 2.2rem; }
    .hero p { margin: 0; font-size: 1.05rem; opacity: 0.9; max-width: 54rem; }

    .area-card {
        height: 100%;
        padding: 1.2rem 1.3rem;
        border-radius: 16px;
        border: 1px solid rgba(128, 128, 128, 0.22);
        border-left: 5px solid var(--accent);
        background-color: rgba(255, 255, 255, 0.03);
        box-shadow: 0 4px 14px rgba(0, 0, 0, 0.12);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .area-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 26px rgba(0, 0, 0, 0.22);
    }
    .area-head { display: flex; align-items: center; gap: 0.7rem; margin-bottom: 0.5rem; }
    .area-badge {
        width: 2.1rem; height: 2.1rem; border-radius: 50%;
        background: var(--accent); color: #fff;
        display: inline-flex; align-items: center; justify-content: center;
        font-weight: 700; font-size: 0.95rem; flex-shrink: 0;
    }
    .area-head h4 { margin: 0; font-size: 1.15rem; }
    .area-card p { margin: 0; font-size: 0.95rem; opacity: 0.9; }

    .st-key-shot img {
        border-radius: 16px;
        box-shadow: 0 12px 34px rgba(0, 0, 0, 0.25);
        border: 1px solid rgba(128, 128, 128, 0.2);
    }

    .key-card {
        display: flex; align-items: center; gap: 0.9rem;
        padding: 0.8rem 1rem;
        border-radius: 12px;
        border: 1px solid rgba(128, 128, 128, 0.2);
        background-color: rgba(255, 255, 255, 0.03);
        margin-bottom: 0.6rem;
    }
    .key-chip {
        min-width: 6.2rem; text-align: center;
        padding: 0.3rem 0.6rem;
        border-radius: 7px;
        border: 1px solid rgba(128, 128, 128, 0.5);
        border-bottom-width: 3px;
        background-color: rgba(128, 128, 128, 0.12);
        font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
        font-size: 0.92rem;
        white-space: nowrap;
    }
    .key-desc { font-size: 0.95rem; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>🧭 Interface</h1>
    <p>The SegmentME window has four areas. The image in the middle is where most of the work happens, and the
    other three support it.</p>
</div>
""", unsafe_allow_html=True)

areas = [
    ("1", "📋", "Menu bar", "#ef4444", "Files, batch jobs, view options, and model settings."),
    ("2", "🧰", "Sidebar", "#ef4444", "Navigation, the annotation tools, and your classes."),
    ("3", "🖼️", "Image display", "#ef4444", "The current image and its masks. Drawing and editing happen here."),
    ("4", "🗂️", "Annotations panel", "#ef4444", "A table of every mask, plus per-class statistics."),
]
cols = st.columns(4)
for col, (num, icon, title, accent, summary) in zip(cols, areas):
    with col:
        st.markdown(
            f"""
            <div class="area-card" style="--accent: {accent};">
                <div class="area-head">
                    <span class="area-badge">{num}</span>
                    <h4>{icon} {title}</h4>
                </div>
                <p>{summary}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.write("")
with st.container(key="shot"):
    st.image("assets/tour/interface.png", caption="The SegmentME window", use_container_width=True)

st.subheader("Keys and mouse on the image")
keys = [
    ("← / →", "Previous and next image"),
    ("H (hold)", "Hide the mask overlays and see the raw image"),
    ("Delete", "Delete the selected masks, with no confirmation"),
    ("Scroll", "Zoom in and out"),
    ("Middle-drag", "Pan the image"),
    ("Left-click", "Select a mask (when no tool is active)"),
    ("Right-click", "Open the Actions menu for a mask or selection"),
]
left, right = st.columns(2)
for i, (chord, desc) in enumerate(keys):
    chips = "".join(f'<span class="key-chip">{part.strip()}</span>' for part in chord.split("/"))
    target = left if i % 2 == 0 else right
    with target:
        st.markdown(
            f'<div class="key-card">{chips}<span class="key-desc">{desc}</span></div>',
            unsafe_allow_html=True,
        )

st.subheader("Each area in detail")
tab_menu, tab_sidebar, tab_image, tab_panel = st.tabs(
    ["📋 1 · Menu bar", "🧰 2 · Sidebar", "🖼️ 3 · Image display", "🗂️ 4 · Annotations panel"]
)

with tab_menu:
    st.markdown("""
- **File** — **Import Images**; **Annotations** (opens the table and statistics); **Save Results** (a CSV of every
  mask); **Export annotations** (YOLO or COCO); **Exit**.
- **Actions** — **Run Inference** and **Train Custom Model**.
- **View** — **Show Masks** toggles the mask overlay; **Fullscreen Mode**.
- **Settings** — **Models...**, the model manager.
- **Help** — **Documentation** opens this guide; **About** is a placeholder.
""")
    st.page_link("pages/5_Projects_and_Export.py", label="Projects and Export", icon="📂")
    st.page_link("pages/7_Models_and_Training.py", label="Models and Training", icon="🧠")

with tab_sidebar:
    st.markdown("""
- **Navigation** — **Prev** and **Next** move between images (also the ← and → keys).
- **Tools** — **Manual**, **DEXTR**, **SAM**, and **Scissors**. Only one is active at a time, and turning one off
  unloads the model it loaded. The SAM model is chosen in **Settings → Models...**.
- **Classes** — the class dropdown, **Add Class**, and **Remove Selected**.
""")
    st.page_link("pages/6_Tools.py", label="Annotation tools", icon="🛠️")

with tab_image:
    st.markdown("""
The image shows every saved mask. Drawing and editing happen here.

- **Scroll** to zoom. **Middle-drag** to pan.
- **Left-click** a mask to select it when no tool is active.
- **Right-click** a mask, or a selection made in the Annotations table, to open its **Actions** menu: **Set class**,
  **Split mask**, **Brush edit**, **Delete selected**, **Select all masks on image**, and **Clear selection**.
  Right-clicking empty space with no tool active opens the same menu for the current selection.
- **Hold `H`** to hide the mask overlays and see the raw image. Release to bring them back.
- **Delete** removes the selected masks immediately, with no confirmation.

**Split mask** and **Brush edit** only apply to an existing mask, so they live in the Actions menu rather than the
sidebar.
""")

with tab_panel:
    st.markdown("""
Open it from **File → Annotations**. It docks on the right and has two parts:

- **Annotations table** — every mask on the current image, with **Image Name**, **Mask ID**, **Surface Area**, and
  **Class**. Click a row to highlight its mask. Double-click the **Class** cell to rename it. A search box and a class
  filter narrow down large projects.
- **Annotation Statistics** — instance counts per class, across all images and for the current image.
""")
