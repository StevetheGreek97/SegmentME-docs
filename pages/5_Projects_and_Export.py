import streamlit as st
from utils.utils import get_text

st.set_page_config(
    page_title="Projects and Export",
    page_icon="📂",
    layout="wide"
)

st.markdown("""
<style>
    .hero {
        padding: 1.8rem 2rem;
        border-radius: 18px;
        border: 1px solid rgba(128, 128, 128, 0.2);
        background: linear-gradient(135deg,
            rgba(59, 130, 246, 0.16) 0%,
            rgba(139, 92, 246, 0.12) 50%,
            rgba(245, 158, 11, 0.10) 100%);
        margin-bottom: 1.4rem;
    }
    .hero h1 { margin: 0 0 0.4rem 0; font-size: 2.2rem; }
    .hero p { margin: 0; font-size: 1.05rem; opacity: 0.9; max-width: 54rem; }

    .flow {
        display: flex; flex-wrap: wrap; gap: 0.6rem;
        margin: 0 0 1.4rem 0;
    }
    .flow-step {
        flex: 1 1 10rem;
        display: flex; align-items: center; gap: 0.6rem;
        padding: 0.7rem 0.9rem;
        border-radius: 12px;
        border: 1px solid rgba(128, 128, 128, 0.22);
        border-top: 4px solid var(--accent);
        background-color: rgba(255, 255, 255, 0.03);
        font-weight: 600;
    }
    .flow-num {
        width: 1.8rem; height: 1.8rem; border-radius: 50%;
        background: var(--accent); color: #fff;
        display: inline-flex; align-items: center; justify-content: center;
        font-size: 0.85rem; flex-shrink: 0;
    }

    .section-title {
        display: flex; align-items: center; gap: 0.6rem;
        margin: 0 0 0.3rem 0; font-size: 1.4rem; font-weight: 700;
    }
    .section-accent {
        width: 0.35rem; height: 1.5rem; border-radius: 3px;
        background: var(--accent);
    }
    .section-blurb { opacity: 0.85; margin: 0 0 0.8rem 0; }

    [class*="st-key-section-"] {
        border-radius: 16px !important;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.12);
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>📂 Projects and Export</h1>
    <p>Create a project, bring in your images, organize classes and masks, and export your annotations.</p>
</div>
""", unsafe_allow_html=True)

flow = [
    ("1", "🆕", "Create", "#3b82f6"),
    ("2", "🖼️", "Import", "#10b981"),
    ("3", "🏷️", "Classes", "#8b5cf6"),
    ("4", "✂️", "Masks", "#f59e0b"),
    ("5", "📤", "Export", "#ef4444"),
]
steps_html = "".join(
    f'<div class="flow-step" style="--accent: {accent};">'
    f'<span class="flow-num">{num}</span>{icon} {label}</div>'
    for num, icon, label, accent in flow
)
st.markdown(f'<div class="flow">{steps_html}</div>', unsafe_allow_html=True)


def section_header(icon, title, blurb, accent):
    st.markdown(
        f"""
        <div class="section-title" style="--accent: {accent};">
            <span class="section-accent"></span>{icon} {title}
        </div>
        <p class="section-blurb">{blurb}</p>
        """,
        unsafe_allow_html=True,
    )


def video_expander(label, path):
    with st.expander(f"📽️ {label}"):
        try:
            with open(path, "rb") as video_file:
                st.video(video_file.read(), loop=True, autoplay=True)
        except Exception:
            st.info("No video available for this section yet.")


with st.container(border=True, key="section-setup"):
    section_header(
        "🚀", "Set up a project",
        "Each project is self-contained: its own images, classes, and annotations.",
        "#3b82f6",
    )
    left, right = st.columns(2)
    with left:
        st.markdown("#### 🆕 Create a Project")
        create = get_text("create_project")
        st.markdown(create["instructions"])
        if create.get("setup"):
            st.markdown("##### 📁 Project folder")
            st.markdown(create["setup"])
    with right:
        st.markdown("#### 🖼️ Import Images")
        st.markdown(get_text("image_import")["instructions"])
    video_expander("Watch how to create and import images", "assets/tour/set_up_project.mp4")

with st.container(border=True, key="section-classes"):
    section_header(
        "🏷️", "Classes",
        "Name each category you want to annotate, and give it a color you can recognize on the image.",
        "#8b5cf6",
    )
    left, right = st.columns(2)
    with left:
        st.markdown("#### ➕ Add a Class")
        st.markdown(get_text("add_class")["instructions"])
    with right:
        st.markdown("#### ➖ Remove a Class")
        st.markdown(get_text("remove_class")["instructions"])
    video_expander("Watch how to manage classes", "assets/tour/classes.mp4")

with st.container(border=True, key="section-masks"):
    section_header(
        "✂️", "Masks",
        "Delete or rename masks in the image or in the Annotations table.",
        "#f59e0b",
    )
    left, right = st.columns(2)
    with left:
        st.markdown("#### 🗑️ Delete Masks")
        st.markdown(get_text("delete_masks")["instructions"])
    with right:
        st.markdown("#### ✏️ Rename Masks")
        st.markdown(get_text("rename_masks")["instructions"])

    st.markdown("#### 🧺 Select Several Masks")
    st.markdown("""
- **In the image:** with no tool active, left-click each mask to add it to the selection. Click empty space to clear
  the selection.
- **In the Annotations table:** click rows to add or remove them. Each click toggles that row.
- **Right-click the selection** to **Set class** or **Delete selected** for every selected mask at once.
- **Select all masks on image** and **Clear selection** are in the right-click menu.
""")
    video_expander("Watch how to manage masks", "assets/tour/masks.mp4")

with st.container(border=True, key="section-export"):
    section_header(
        "📤", "Export",
        "Get your annotations out for training elsewhere, sharing, or archiving.",
        "#ef4444",
    )
    st.markdown(get_text("export_annotations")["instructions"])
    st.warning(
        "Exporting YOLO annotations deletes and replaces the existing `labels/` folder. Copy any label files you "
        "need before exporting again."
    )
    video_expander("Watch how to export annotations", "assets/tour/export.mp4")

st.write("")
st.page_link("pages/6_Tools.py", label="Next: Annotation tools", icon="🛠️")
