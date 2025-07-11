import streamlit as st
from utils.utils import get_text

st.set_page_config(
    page_title="Create and Manage Projects",
    page_icon="📂",
    layout="centered"
)

st.title("📂 Create and Manage Projects")

st.markdown(
    """
    Use this guide to create new projects, import data, organize classes, and manage annotations in **SegmentME**.
    """
)

# ---------- Section: Project Creation & Import ----------
st.subheader("🚀 Set up Your Project")

col_keys = {
    "🆕 Create a Project": "create_project",
    "🖼️ Import Images": "image_import"
}
cols = st.columns(2)

for i, (title, key) in enumerate(col_keys.items()):
    with cols[i]:
        st.markdown(f"### {title}")
        data = get_text(key)
        print(data)
        st.markdown(data["instructions"])
        setup = data.get("setup", "")
        if setup:
            st.markdown("##### 📁 Project Folder Structure")
            st.markdown(setup)
   

with st.expander("📽️ Watch how to create and import images"):
    try:
        with open("assets/tour/create_import.mp4", "rb") as video_file:
            st.video(video_file.read(), loop=True, autoplay=True)
    except Exception:
        st.warning("No video available for this section yet.")



# ---------- Section: Add / Remove Classes ----------
st.subheader("🏷️ Manage Annotation Classes")
st.markdown("""
Organize your annotation workflow by adding meaningful class names and assigning colors to them.  
You can also remove existing classes when they are no longer needed — this helps keep your project tidy and focused.
""")
col_keys = {
    "➕ Add a Class": "add_class",
    "➖ Remove a Class": "remove_class"
}
cols = st.columns(2)

for i, (title, key) in enumerate(col_keys.items()):
    with cols[i]:
        st.markdown(f"### {title}")
        data = get_text(key)
        st.markdown(data["instructions"])

with st.expander("📽️ Watch how to manage classes"):
    try:
        with open("assets/tour/add_remove.mp4", "rb") as video_file:
            st.video(video_file.read(), loop=True, autoplay=True)
    except Exception:
        st.warning("No video available for this section yet.")


# ---------- Section: Delete / Rename Masks ----------
st.subheader("✂️ Delete or Rename Masks")

col_keys = {
    "🗑️ Delete Masks": "delete_masks",
    "✏️ Rename Masks": "rename_masks"
}
cols = st.columns(2)

for i, (title, key) in enumerate(col_keys.items()):
    with cols[i]:
        st.markdown(f"### {title}")
        data = get_text(key)
        st.markdown(data["instructions"])

with st.expander("📽️ Watch how to manage masks"):
    try:
        with open("assets/tour/del_rename.mp4", "rb") as video_file:
            st.video(video_file.read(), loop=True, autoplay=True)
    except Exception:
        st.warning("No video available for this section yet.")


st.subheader("Export Annotations")
st.markdown("""Not Implemented yet""")

st.markdown("🔚 *You're all set to manage your project! Continue with annotation or explore the tools above.*")


