import streamlit as st
from utils.utils import get_text

st.set_page_config(page_title="Discover and Learn", page_icon="🧠", layout="wide")
st.title("🧠 Discover and Learn")

# Custom CSS for full-page theme-aware styling
st.markdown("""
    <style>
        /* Default fallback (will apply if no theme is set explicitly) */
        :root {
            --background-color: #0e1117;
            --gradient-start: #1c1f26;
            --gradient-end: #2a2d36;
            --card-bg: rgba(255, 255, 255, 0.05);
            --text-color: #e0e0e0;
            --title-color: #ffd700;
            --shadow-color: rgba(255, 255, 255, 0.07);
        }

        body[data-theme="light"] {
            --background-color: #f4f6fa;
            --gradient-start: #edf0f7;
            --gradient-end: #dfe5f0;
            --card-bg: rgba(255, 255, 255, 0.95);
            --text-color: #2c2c2c;
            --title-color: #e88f00;
            --shadow-color: rgba(0, 0, 0, 0.08);
        }

        body[data-theme="dark"] {
            --background-color: #0e1117;
            --gradient-start: #1c1f26;
            --gradient-end: #2a2d36;
            --card-bg: rgba(255, 255, 255, 0.05);
            --text-color: #e0e0e0;
            --title-color: #ffd700;
            --shadow-color: rgba(255, 255, 255, 0.07);
        }

        [data-testid="stAppViewContainer"] {
            background: linear-gradient(135deg, var(--gradient-start), var(--gradient-end));
            padding: 2rem;
        }

        .step-card {
            background: var(--card-bg);
            backdrop-filter: blur(12px);
            border-radius: 16px;
            padding: 25px;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px var(--shadow-color);
            transition: all 0.3s ease;
            border: 1px solid rgba(255, 255, 255, 0.05);
        }

        .step-card:hover {
            transform: scale(1.01);
        }

        .step-title {
            font-size: 1.7rem;
            font-weight: 700;
            color: var(--title-color);
            margin-bottom: 14px;
        }

        .step-content {
            font-size: 1.05rem;
            line-height: 1.8;
            color: var(--text-color);
        }

        .step-content ul {
            list-style-type: "✔️ ";
            padding-left: 1.4em;
        }

        .step-content li {
            margin-bottom: 10px;
        }

        .highlight-box {
            background-color: rgba(255, 215, 0, 0.1);
            border-left: 4px solid var(--title-color);
            padding: 12px 16px;
            margin-top: 15px;
            border-radius: 10px;
        }

        .terminology-box {
            background: var(--card-bg);
            border-radius: 12px;
            padding: 15px;
            margin-bottom: 20px;
            box-shadow: 0 6px 18px var(--shadow-color);
        }

        .terminology-term {
            font-weight: 600;
            margin-bottom: 6px;
            color: var(--title-color);
        }
    </style>
""", unsafe_allow_html=True)

# ────────────────────────────────
# INTRO
# ────────────────────────────────

st.markdown("""
Welcome to the Discover and Learn page. Explore computer vision concepts and follow a complete walkthrough to plan, annotate, and train your model using SegmentME.
""")

# ────────────────────────────────
# TERMINOLOGY SECTION
# ────────────────────────────────

st.divider()
st.header("📘 Terminology")

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
            st.markdown(f"""
                <div class="terminology-box">
                    <div class="terminology-term">{term}</div>
                    <div style='color: var(--text-color); font-size: 0.95rem;'>{desc}</div>
                </div>
            """, unsafe_allow_html=True)

# ────────────────────────────────
# PROJECT SETUP STEPS
# ────────────────────────────────

st.divider()
st.header("🛠️ How to Set Up a Computer Vision Project")


steps = get_text('discover', 'assets/discover.yaml')

for step in steps:
    content = step['content']
    lines = content.strip().split('\n')
    
    bullets = []
    guidelines = []
    inside_guidelines = False

    for line in lines:
        stripped = line.strip()

        # Start of Annotation Guidelines block
        if "annotation guidelines" in stripped.lower():
            inside_guidelines = True
            continue

        # Gather guideline points
        if inside_guidelines and (stripped.startswith('-') or stripped.startswith('*')):
            cleaned = stripped.lstrip('-* ').strip()
            guidelines.append(f"<li>{cleaned}</li>")
        
        # Otherwise, treat as normal bullet
        elif not inside_guidelines and (stripped.startswith('-') or stripped.startswith('*')):
            cleaned = stripped.lstrip('-* ').strip()
            bullets.append(f"<li>{cleaned}</li>")

    # Main list
    content_html = "<ul>" + "\n".join(bullets) + "</ul>"

    # Add guideline block if it exists
    if guidelines:
        content_html += f"""
        <div class='highlight-box'>
            <strong>Annotation Guidelines</strong>
            <ul>{''.join(guidelines)}</ul>
        </div>
        """

    # Display the card
    st.markdown(f"""
        <div class="step-card">
            <div class="step-title">{step['title']}</div>
            <div class="step-content">{content_html}</div>
        </div>
    """, unsafe_allow_html=True)

