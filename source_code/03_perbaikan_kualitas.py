"""
TAHAP 2 - PROSES 2: PERBAIKAN KUALITAS CITRA
Teknik: Histogram Equalization, Contrast Stretching, Brightness Adjustment, Sharpening

1. Histogram Equalization
   Meratakan distribusi histogram grayscale agar kontras citra meningkat
   secara global. cv2.equalizeHist().

2. Contrast Stretching (Min-Max Normalization)
   Menarik rentang intensitas piksel [min, max] yang ada menjadi [0, 255]
   sehingga kontras citra yang awalnya "sempit" menjadi lebih lebar.

3. Brightness Adjustment
   Menambahkan/mengurangi nilai konstan ke semua piksel:
   new_pixel = old_pixel + beta  (di sini beta = +40, citra jadi lebih terang)

4. Sharpening
   Menggunakan kernel konvolusi unsharp mask sederhana:
       [ 0 -1  0]
       [-1  5 -1]
       [ 0 -1  0]
   untuk mempertegas tepi/detail citra.
"""

import os
import cv2
import numpy as np

IN_DIR = "/home/claude/dataset"
BASE_OUT = "/home/claude/output"

OUT_HE = os.path.join(BASE_OUT, "02_histogram_equalization")
OUT_CS = os.path.join(BASE_OUT, "02_contrast_stretching")
OUT_BA = os.path.join(BASE_OUT, "02_brightness_adjustment")
OUT_SH = os.path.join(BASE_OUT, "02_sharpening")

for d in [OUT_HE, OUT_CS, OUT_BA, OUT_SH]:
    os.makedirs(d, exist_ok=True)

sharpen_kernel = np.array([[0, -1, 0],
                            [-1, 5, -1],
                            [0, -1, 0]], dtype=np.float32)

files = sorted(os.listdir(IN_DIR))

for f in files:
    img_bgr = cv2.imread(os.path.join(IN_DIR, f))
    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

    # 1. Histogram Equalization (pada grayscale)
    he = cv2.equalizeHist(gray)
    cv2.imwrite(os.path.join(OUT_HE, f), he)

    # 2. Contrast Stretching (min-max normalization, pada grayscale)
    min_val, max_val = gray.min(), gray.max()
    if max_val > min_val:
        cs = ((gray.astype(np.float32) - min_val) * 255.0 / (max_val - min_val))
        cs = np.clip(cs, 0, 255).astype(np.uint8)
    else:
        cs = gray.copy()
    cv2.imwrite(os.path.join(OUT_CS, f), cs)

    # 3. Brightness Adjustment (pada citra RGB, beta = +40)
    beta = 40
    ba = cv2.convertScaleAbs(img_bgr, alpha=1.0, beta=beta)
    cv2.imwrite(os.path.join(OUT_BA, f), ba)

    # 4. Sharpening (pada citra RGB)
    sh = cv2.filter2D(img_bgr, -1, sharpen_kernel)
    cv2.imwrite(os.path.join(OUT_SH, f), sh)

print(f"Perbaikan kualitas citra selesai untuk {len(files)} gambar.")
print("Output tersimpan di:")
for d in [OUT_HE, OUT_CS, OUT_BA, OUT_SH]:
    print(" -", d)
