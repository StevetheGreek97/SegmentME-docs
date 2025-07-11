import streamlit as st
import pandas as pd

st.set_page_config(page_title="Discover and Learn", page_icon="🧠")
st.title("🧠 Discover and Learn")

# Intro
st.markdown("""
Welcome to the **Discover and Learn** page. Here you'll find clear explanations of core computer vision terms and a complete guide to setting up a CV project using SegmentME.
""")

# ────────────────────────────────
# TERMINOLOGY SECTION
# ────────────────────────────────

st.divider()
st.header("📘 Terminology")
st.markdown("Grouped definitions of essential concepts in computer vision and annotation.")

groups = {
    "🧠 Vision Tasks": [
        ("Image Classification", "Assign a single label to the entire image."),
        ("Object Detection", "Detect and localize multiple objects using bounding boxes."),
        ("Semantic Segmentation", "Assign a class to every pixel, without separating individual objects."),
        ("Instance Segmentation", "Segment each object instance separately at the pixel level."),
        ("Zero-Shot Segmentation", "Segment unseen object categories using models like SAM.")
    ],
    "✍️ Annotation Concepts": [
        ("Class Label", "The category assigned to an object (e.g., 'eye', 'tail')."),
        ("Annotation", "The process of labeling image content using masks, boxes, or polygons."),
        ("Extreme Points", "Top, bottom, left, and right points used to guide segmentation models like DEXTR."),
        ("Mask", "A binary or class-specific pixel region representing an object."),
        ("Mask Area", "The number of pixels covered by a mask, often converted to cm².")
    ],
    "📦 Geometric Structures": [
        ("Bounding Box (BBox)", "A rectangle enclosing an object, defined by two corner points."),
        ("Polygon", "A precise outline of an object using a list of (x, y) coordinates."),
        ("Centroid", "The geometric center of a segmented region, used for measurements or tracking.")
    ]
}

for group_title, terms in groups.items():
    st.subheader(group_title)
    cols = st.columns(3)
    for i, (term, desc) in enumerate(terms):
        with cols[i % 3]:
            with st.expander(term):
                st.write(desc)

st.divider()
st.header("🛠️ How to Set Up a Computer Vision Project")
st.markdown("A complete walkthrough for building a CV pipeline with SegmentME — from planning and annotation to training and deployment.")

# Structured step-by-step guide
steps = [
    {
        "icon": "🎯",
        "title": "Define the Objective",
        "content": """
Decide what your project is trying to achieve.

**Examples:**
- Classify microscopy images (e.g. healthy vs. infected)
- Segment body parts (e.g. eye, tail, gut)
- Count individuals per image (e.g. Daphnia density)

Define whether your output is:
- Bounding boxes (Object Detection)
- Pixel masks (Instance/Semantic Segmentation)
- Category labels (Classification)
- Or zero-shot masks (SAM)"""
    },
    {
        "icon": "🏷️",
        "title": "Define Classes",
        "content": """
List the object types you'll label.

**Tips:**
- Use short, lowercase names (e.g. `eye`, `tail`, `debris`)
- Keep the number of classes manageable
- Make sure each class is visually distinguishable

**Example:**
```python
classes = ['eye', 'tail', 'gut', 'debris']
```"""
    },
    {
        "icon": "📸",
        "title": "Collect & Curate Images",
        "content": """
Use a variety of images that match real-world conditions.

**Include:**
- Good and poor focus
- Different light conditions
- Background-only (blank) images
- Images with partial or overlapping objects

**Goal:** At least 100–200 samples per class"""
    },
    {
        "icon": "✍️",
        "title": "Annotate Using SegmentME",
        "content": """
Use tools based on your task:

| Tool      | Best For                  |
|-----------|---------------------------|
| SAM2      | Zero-shot instance masks  |
| DEXTR     | Precise user-guided masks |
| Polygon   | Custom fine control       |
| BBox Tool | Faster, coarse marking    |

Save in YOLO format or export masks for segmentation training.
"""
    },
    {
        "icon": "🧠",
        "title": "Choose a Model",
        "content": """
Pick a model architecture that fits your compute and task.

**Options:**
- `YOLOv8-seg`: Fast instance segmentation
- `SAM2`: No training needed (zero-shot)
- `Detectron2`: Custom control, great for research

Start with pretrained models. Fine-tune only when needed.
"""
    },
    {
        "icon": "📊",
        "title": "Train & Validate",
        "content": """
Split your data:
- 70% training
- 15% validation
- 15% testing

**Track:**
- mAP (mean average precision)
- IoU (overlap accuracy)
- Per-class metrics

Use frameworks like Ultralytics CLI or Python API.
"""
    },
    {
        "icon": "🔁",
        "title": "Evaluate & Improve",
        "content": """
After training, visually inspect predictions.

✅ Are all objects found?  
❌ Any overfitting?  
❓ Are masks accurate?

**If needed:**
- Add more diverse samples
- Refine poor annotations
- Retrain on tough cases
"""
    },
    {
        "icon": "🚀",
        "title": "Run Inference or Deploy",
        "content": """
Use your model to annotate new images with SegmentME or a script.

**You can:**
- Measure mask area (e.g. in mm² or pixels)
- Count per-class instances
- Export YOLO `.txt` or result `.csv` files

Integrate predictions into analysis or research workflows.
"""
    }
]

# Render steps in visually clear blocks
for step in steps:
    with st.container():
        col1, col2 = st.columns([1, 9])
        with col1:
            st.markdown(f"### {step['icon']}")
        with col2:
            st.markdown(f"#### {step['title']}")
            st.markdown(step["content"])
    st.markdown("---")
