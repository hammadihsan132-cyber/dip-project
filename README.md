# ****Multi-Focus Image Fusion using Laplacian Pyramid Blending****

A Digital Image Processing project that fuses two multi-focus images into a single, fully sharp image using Gaussian and Laplacian pyramid decomposition — with an interactive Streamlit UI for easy use.

---

## Problem Statement

In photography, a single image often cannot keep all objects in focus simultaneously due to depth-of-field limitations. This project addresses that by combining two images — each sharp in different regions — into one composite image that is sharp throughout.

---

## Methodology / Approach

1. **Load & Preprocess** — Images are loaded in color (BGR), resized to 256×256, and normalized to [0, 1].
2. **Gaussian Pyramid** — Each image is progressively downsampled over 5 levels.
3. **Laplacian Pyramid** — Constructed from the Gaussian pyramid to capture detail at each scale.
4. **Pyramid Fusion** — At each level, the pixel with the higher absolute value (more detail/contrast) is selected from either image.
5. **Reconstruction** — The fused Laplacian pyramid is collapsed back into a full-resolution image.
6. **Per-Channel Processing** — Steps 2–5 are applied independently to each RGB channel to preserve color fidelity.
7. **Streamlit UI** — An interactive web app allows users to upload images and view the fused result in real time.

---

##  Technologies Used

| Tool | Purpose |
|------|---------|
| Python | Core language |
| OpenCV (`cv2`) | Image I/O, resizing, pyramid operations |
| NumPy | Array math and channel manipulation |
| Matplotlib | Visualization of input and fused output |
| Streamlit | Interactive web UI for image upload and result display |

---

##  How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/multi-focus-image-fusion.git
   cd multi-focus-image-fusion
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**
   ```bash
   streamlit run app.py
   ```

4. **Or run the notebook directly**
   ```bash
   jupyter notebook dip_project.ipynb
   ```

> **Google Colab users:** Upload your images to `/content/` and run all cells directly.

---

##  Dependencies

All dependencies are listed in [`requirements.txt`](./requirements.txt):

```
opencv-python
numpy
matplotlib
streamlit
```

---

##  Results

The pipeline outputs a side-by-side comparison of:
- **Image 1** — Sharp in one focal region
- **Image 2** — Sharp in another focal region
- **Fused Image** — Combines the sharpest regions from both

> _Sample result image can be added here._  
> <img width="512" height="513" alt="image" src="https://github.com/user-attachments/assets/ffd1b7ef-9ac2-4850-9aeb-066c1a857aa4" />
)

---

## 🔮 Future Improvements

- [ ] Replace max-absolute-value fusion with a **saliency or variance-based** selection for better quality
- [ ] Add **SSIM / entropy metrics** to quantitatively evaluate fusion quality
- [ ] Support **grayscale and HDR** image inputs
- [ ] Extend to **video frame fusion** for computational photography pipelines

---

##  Project Structure

```
multi-focus-image-fusion/
│
├── dip_project.ipynb      # Core pipeline notebook
├── app.py                 # Streamlit web app
├── requirements.txt       # Python dependencies
├── README.md              # This file
└── assets/                # Sample images and results (optional)
```
## Inut Images
<img width="520" height="520" alt="lytro-14-B" src="https://github.com/user-attachments/assets/baf982a7-7889-4a0d-b9b6-dc2807a6a4f8" />
<img width="520" height="520" alt="lytro-14-B" src="https://github.com/user-attachments/assets/ddf658b3-2654-4432-9984-b4f6ba7efb89" />


---
## Output Image
<img width="515" height="514" alt="image" src="https://github.com/user-attachments/assets/7f5bf132-62a4-4d5f-a3c4-26b8154d048b" />
---


##  Author

***HAMMAD IHSAN*  
Feel free to ask about the project
hammad.ihsan132@gmail.com

