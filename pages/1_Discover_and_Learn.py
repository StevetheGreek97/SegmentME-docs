# pages/1_Discover_and_Learn.py
import streamlit as st

st.set_page_config(page_title="Discover and Learn", page_icon="🧠", layout="wide")
st.title("🧠 Discover and Learn")

# Fancy but theme-safe CSS
st.markdown("""
<style>
    /* Card Styling */
    .card {
        padding: 1.2rem 1.5rem;
        margin-bottom: 1.5rem;
        border-radius: 16px;
        background-color: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.07);
        backdrop-filter: blur(10px);
        box-shadow:
            0 4px 10px rgba(0, 0, 0, 0.2),
            0 2px 4px rgba(0, 0, 0, 0.15);
        transition: all 0.2s ease;
    }

    /* Light theme override */
    body[data-theme="light"] .card {
        background-color: rgba(255, 255, 255, 0.8);
        border: 1px solid rgba(0, 0, 0, 0.05);
        box-shadow:
            0 6px 16px rgba(0, 0, 0, 0.15),
            0 3px 8px rgba(0, 0, 0, 0.1);
    }

    /* Hover effect for both themes */
    .card:hover {
        transform: scale(1.01);
        box-shadow:
            0 10px 30px rgba(0, 0, 0, 0.3),
            0 5px 15px rgba(0, 0, 0, 0.2);
    }

    .card h4 {
        margin-top: 0;
        margin-bottom: 0.75rem;
        font-size: 1.45rem;
        font-weight: 700;
        color: var(--primary-color);
    }

    .card ul {
        padding-left: 1.5rem;
        margin-bottom: 0;
    }

    .card p {
        color: var(--text-color);
        font-size: 0.96rem;
        margin: 0;
    }

</style>
""", unsafe_allow_html=True)

st.markdown("The terms used across SegmentME and in image segmentation in general.")

# ─────────────────────────────
# TERMINOLOGY
# ─────────────────────────────
st.divider()
st.header("📘 Terminology")

groups = {
    "🧠 Vision Tasks": [
        ("Image Classification", "Assign a single label to the entire image."),
        ("Object Detection", "Detect and localize multiple objects using bounding boxes."),
        ("Semantic Segmentation", "Assign a class to every pixel."),
        ("Instance Segmentation", "Separate each object instance pixel-wise."),
        ("Zero-Shot Segmentation", "Segment unseen categories using models like SAM."),
    ],
    "✍️ Annotation Concepts": [
        ("Class Label", "The category assigned to an object."),
        ("Annotation", "Labeling using masks, boxes, or polygons."),
        ("Extreme Points", "Key points guiding segmentation models like DEXTR."),
        ("Mask", "Region representing an object."),
        ("Mask Area", "Area in pixels or cm²."),
    ],
    "📦 Geometric Structures": [
        ("Bounding Box", "A rectangle enclosing an object."),
        ("Polygon", "Precise outline using coordinates."),
        ("Centroid", "Center point of a segmented region."),
    ]
}

for section, terms in groups.items():
    st.subheader(section)
    cols = st.columns(3)
    for i, (term, desc) in enumerate(terms):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="card">
                <h4>{term}</h4>
                <p style="margin:0.2rem 0 0;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)
