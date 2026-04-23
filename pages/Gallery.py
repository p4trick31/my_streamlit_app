import streamlit as st
from PIL import Image

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(page_title="Gallery", page_icon="🖼", layout="wide")

# ----------------------------
# HEADER
# ----------------------------
st.title("🖼 My Photo Gallery")
st.caption("A collection of my portfolio images and personal snapshots.")

st.divider()

# ----------------------------
# LOAD IMAGES
# ----------------------------
img1 = Image.open("assets/pic1.jpeg")
img2 = Image.open("assets/pic2.jpeg")
img3 = Image.open("assets/pic3.jpeg")

# ----------------------------
# DISPLAY OPTIONS (INTERACTION)
# ----------------------------
view = st.radio(
    "Choose view mode:",
    ["Grid View", "Single Preview"]
)

# ----------------------------
# GRID VIEW
# ----------------------------
if view == "Grid View":

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image(img1, caption="Picture 1", use_container_width=True)

    with col2:
        st.image(img2, caption="Picture 2", use_container_width=True)

    with col3:
        st.image(img3, caption="Picture 3", use_container_width=True)

# ----------------------------
# SINGLE PREVIEW MODE
# ----------------------------
else:
    selected = st.selectbox(
        "Select image to view:",
        ["Picture 1", "Picture 2", "Picture 3"]
    )

    if selected == "Picture 1":
        st.image(img1, caption="Picture 1", use_container_width=True)

    elif selected == "Picture 2":
        st.image(img2, caption="Picture 2", use_container_width=True)

    elif selected == "Picture 3":
        st.image(img3, caption="Picture 3", use_container_width=True)

# ----------------------------
# FOOTER
# ----------------------------
st.divider()
st.success("✨ More photos will be added soon!")
