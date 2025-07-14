import streamlit as st
from utils.utils import get_text

st.set_page_config(page_title="SegmentME Manual", 
                   page_icon="/home/steve/Documents/Projects/docsSE/assets/logo.png", 
                   layout="wide")

# Use columns to align image and title
col1, col2 = st.columns([1, 17])  # Adjust ratio as needed

with col1:
    st.image("assets/logo.png", width=70)

with col2:
    st.markdown("## SegmentME Manual")  

st.markdown("""
Welcome to the SegmentME manual! This guide will help you understand how to use SegmentME effectively for your image annotation and segmentation tasks.
""")
st.divider()
st.markdown(get_text("intro"))

try:

    video_file = open("assets/tour/tester.mp4", "rb")
    video_bytes = video_file.read()

    st.video(video_bytes,loop= True,autoplay= True)
    #st.video("assets/tour/tester.mp4", loop= True,autoplay= True,)
except Exception:
    st.markdown("No video available for this section yet.")



st.markdown("---")
st.caption("Made with ❤️ by Stylianos (Steve) Mavrianos – [Lab Website](https://www.biologie.uni-hamburg.de/forschung/populationsgenomik.html) | [GitHub](https://github.com/StevetheGreek97). For any issues or suggestions, please contact me via the [Contact page](https://segmentme.streamlit.app/pages/6_Contact).")
st.caption("This manual is a work in progress. If you have any feedback or suggestions, please let me know!")    

