import streamlit as st

st.set_page_config(page_title="Create and Manage Projects", page_icon="📂")
st.title("📂 Create and Manage Projects")

st.markdown("""
Use this guide to create new projects, import data, organize classes, and manage annotations in SegmentME.
""")

# Section 1: Create Project
st.header("🆕 Create a Project")
st.markdown("""
To begin, create a new project workspace:

1. Click **File → New Project**
2. Enter a name (e.g., `experiment_2025`)
3. Choose or create a target folder
4. SegmentME creates subfolders:
   - `images/` – image files
   - `labels/` – YOLO `.txt` annotations
   - `project.yaml` – config and metadata

✅ Projects are saved automatically as you work.
""")

st.divider()

# Section 2: Import Images
st.header("🖼️ Import Images")
st.markdown("""
To add images to your project:

- Go to **File → Import Images**
- Supported formats: `.jpg`, `.png`, `.tif`, `.bmp`
- You can import:
  - A folder of images
  - A single image
  - Or drag-and-drop via the interface

SegmentME automatically displays the images in the central panel.
""")

st.divider()

# Section 3: Add / Remove Classes
st.header("🏷️ Add or Remove Classes")
st.markdown("""
To define the object categories in your project:

### ➕ Add a Class
- Use the **Class Selector** panel (left sidebar)
- Click `+ Add Class`
- Enter a class name (e.g., `tail`, `eye`, `debris`)
- New class appears in the dropdown and color map

### ➖ Remove a Class
- Select the class in the dropdown
- Click `🗑️ Remove Class`
- All masks with this class will be deleted (confirmation required)

✅ Classes are stored in `project.yaml` and saved with the project.
""")

st.divider()

# Section 4: Delete Masks
st.header("✂️ Delete Masks")
st.markdown("""
To remove unwanted masks from an image:

- Click on the mask directly in the image viewer
- Or select it from the **Annotation Table** (right sidebar)
- Press `Delete` or click **🗑️ Remove Mask**

🧠 Tip: You can delete multiple masks at once using checkboxes in the table.
""")

st.divider()

# Section 5: Rename Annotations
st.header("✏️ Rename Annotation Files")
st.markdown("""
To rename annotation files (for better organization):

1. Open the **File → Rename Annotations** dialog  
2. Options:
   - Rename by image name
   - Add class prefix or suffix
   - Replace substrings (e.g., `scan001 → sample001`)

All label `.txt` files will be renamed accordingly, and linked image names will be preserved.

🧪 Use this to standardize file names for training or batch evaluation.
""")
