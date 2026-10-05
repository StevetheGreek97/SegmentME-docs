import streamlit as st

st.set_page_config(page_title="Models and Training", page_icon="🧠", layout="wide")

st.title("🧠 Models and Training")

st.markdown("""
SegmentME's AI tools run on model checkpoints. One small model ships with every build. The rest download from
**Settings → Models...** or are imported by hand. This page covers the model manager, running a model over a whole
project, and training your own YOLO model.
""")

st.subheader("Model manager")
st.markdown("""
Each model is listed as **Installed**, **Not installed** (click **Download**), or **Not installed (manual
download)** for SAM3. **Cancel** stops a running download or import.

**SAM tool uses** picks the SAM variant behind the sidebar's **SAM** button. If the chosen model isn't installed, it
downloads when you enable SAM. Changing the model while SAM is active reloads it straight away.
""")

st.image("assets/models_panel.png", caption="The model manager", use_container_width=True)

st.markdown("""
| Model | Size | Notes |
|---|---|---|
| SAM2 Tiny | 155.9 MB | Fastest, lowest accuracy. **Included with every build.** |
| SAM2 Small | 184.3 MB | Fast, a bit more accurate than Tiny. |
| SAM2 Base+ | 323.5 MB | Balanced speed and accuracy. |
| SAM2 Large | 898.0 MB | Most accurate SAM2, slower. |
| SAM2.1 Tiny | 156.0 MB | Improved SAM2 release, fastest. |
| SAM2.1 Small | 184.4 MB | Improved SAM2 release, fast. |
| SAM2.1 Base+ | 323.6 MB | Improved SAM2 release, balanced. |
| SAM2.1 Large | 898.1 MB | Improved SAM2 release, most accurate. |
| SAM3 | 3.5 GB | Most accurate. Large and slow on CPU. Gated, see below. |
| DEXTR | 195.7 MB | Segments from 4 extreme points. |
""")

st.markdown("**Installing SAM3:** SAM3 is gated on Hugging Face and can't be downloaded in the app.")
st.markdown("""
1. Request access at **huggingface.co/facebook/sam3**, then download `sam3.pt` once approved.
2. In the model manager, click **Import file...** on the SAM3 row and select `sam3.pt`.
""")

st.markdown("""
**Where models are stored:** the `models` folder next to the app. If that folder isn't writable, SegmentME uses your
per-user folder: `%APPDATA%\\segmentme\\models` on Windows, `~/Library/Application Support/segmentme/models` on
macOS, or `~/.config/segmentme/models` on Linux. **Open folder** shows the one in use. The `SEGMENTME_MODELS_DIR`
environment variable overrides both.
""")

with st.expander("Model download fails"):
    st.markdown("""
Check your internet connection and click **Download** again. The error shown after "Could not install" gives the
cause. If it keeps failing, download the file in a browser and use **Import file...**.
""")

st.subheader("Batch inference")
st.markdown("""
Batch inference runs a model over every image in the project. Start it from **Actions → Run Inference**.

- **YOLO** runs a trained model. Pick one from this project's training runs, or click **Browse...** for any `.pt`
  file.
- **SAM** segments every object automatically. It works with SAM2 and SAM2.1 only. SAM3 has no automatic mode.
  Cellpose-SAM (`cpsam`) checkpoints also work, after `pip install cellpose`.

Set the **Confidence** threshold (default 0.25) and **Image size** (default 1024 × 1024), then click **Run**. Masks are
saved to each image as the run goes, and any new class from the model is added to the project with its own color.
Review the results in the **Annotations** table.
""")

with st.expander("Cellpose-SAM doesn't load"):
    st.markdown("Install the package with `pip install cellpose`, then browse to the `.pt` file again.")

with st.expander("📽️ Watch batch inference"):
    try:
        with open("assets/tour/custom_inference.mp4", "rb") as video_file:
            st.video(video_file.read(), loop=True, autoplay=True)
    except Exception:
        st.info("No video available for this section yet.")

st.subheader("Training a custom model")
st.markdown("""
**1. Export a YOLO dataset.** Training uses the files a YOLO export writes. Click **File → Export annotations**,
choose **YOLO**, set the **Train / Val / Test split**, and click **Export**. The export creates `labels/`, the `images/`
split into sets, `autosplit_train.txt`, `autosplit_val.txt`, `autosplit_test.txt`, and `data.yaml`. Export again after you
change annotations.

**2. Start training.** Click **Actions → Train Custom Model**. On the **Training Settings** tab:

- **Select Model** — the base model: YOLOv8 (`n`, `s`, `m`, `l`, `x`), YOLOv9 (`c`, `e`), or YOLO11 (`n`, `s`, `m`,
  `l`, `x`). Smaller models train faster.
- **Dataset YAML path** — the `data.yaml` from the export.
- **Epochs**, **Batch size**, **Image size**, **Optimizer**, **Project name**, and **Run name**. The output goes to
  `trainings/<project name>/<run name>` in the project folder.
- **Show Advanced Settings** adds max training time, patience, learning rates, momentum, and weight decay.

The **Augmentation Settings** tab controls the random changes applied to training images. The defaults suit most
datasets.

**3. Train.** Click **🚀 Train**. The monitor shows the log as it runs, and **🛑 Stop Training** ends the run early.

**4. Use the model.** The weights are saved to `trainings/<project name>/<run name>/weights/best.pt`. They appear in
the **YOLO** dropdown the next time you open **Run Inference**.
""")

st.markdown("""
**Device.** SegmentME uses an NVIDIA GPU (CUDA build) when one is available, Apple Silicon's Metal GPU (MPS) on macOS,
and otherwise the CPU, with a warning. CPU training is much slower.
""")

with st.expander("\"Missing Files or Folders\" when starting training"):
    st.markdown("Run **File → Export annotations** in YOLO format first, then open **Train Custom Model** again.")

with st.expander("Out of memory during training"):
    st.markdown("Lower **Batch size**, and if needed **Image size**, on the Training Settings tab.")
