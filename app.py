import streamlit as st
import cv2
import numpy as np
from PIL import Image

# =========================
# PREPROCESS
# =========================
def preprocess_images(images, size=(256, 256)):
    processed = []
    for img in images:
        img = cv2.resize(img, size)
        img = img / 255.0
        processed.append(img)
    return processed


# =========================
# PYRAMIDS
# =========================
def build_gaussian_pyramid(img, levels=5):
    gp = [img]
    for _ in range(levels):
        img = cv2.pyrDown(img)
        gp.append(img)
    return gp


def build_laplacian_pyramid(gp):
    lp = []
    for i in range(len(gp)-1):
        size = (gp[i].shape[1], gp[i].shape[0])
        expanded = cv2.pyrUp(gp[i+1], dstsize=size)
        lp.append(gp[i] - expanded)
    lp.append(gp[-1])
    return lp


def fuse_pyramids(lp1, lp2):
    fused = []
    for a, b in zip(lp1, lp2):
        fused.append(np.where(np.abs(a) > np.abs(b), a, b))
    return fused


def reconstruct(lp):
    img = lp[-1]
    for i in range(len(lp)-2, -1, -1):
        size = (lp[i].shape[1], lp[i].shape[0])
        img = cv2.pyrUp(img, dstsize=size)
        img = img + lp[i]
    return img


# =========================
# COLOR FUSION
# =========================
def fuse_color(img1, img2):
    channels = []
    
    for i in range(3):
        c1 = img1[:, :, i]
        c2 = img2[:, :, i]

        gp1 = build_gaussian_pyramid(c1)
        gp2 = build_gaussian_pyramid(c2)

        lp1 = build_laplacian_pyramid(gp1)
        lp2 = build_laplacian_pyramid(gp2)

        fused_lp = fuse_pyramids(lp1, lp2)
        fused = reconstruct(fused_lp)

        channels.append(fused)

    return np.stack(channels, axis=2)


# =========================
# STREAMLIT UI
# =========================
st.title("🔥 Multi-Focus Image Fusion System")
st.write("Upload 2 images with different focus levels")

uploaded_files = st.file_uploader(
    "Upload Images",
    type=["jpg", "png", "jpeg"],
    accept_multiple_files=True
)

if uploaded_files and len(uploaded_files) >= 2:

    images = []

    for file in uploaded_files:
        img = Image.open(file).convert("RGB")  # IMPORTANT FIX
        img = np.array(img)
        images.append(img)

    st.subheader("Uploaded Images")

    for img in images:
        st.image(img)   # FIXED (removed broken parameter)

    if st.button("Run Fusion"):

        images = preprocess_images(images)

        img1 = images[0]
        img2 = images[1]

        fused = fuse_color(img1, img2)
        fused = np.clip(fused, 0, 1)

        st.subheader("Fused Output")

        st.image(fused)   # IMPORTANT FIX   