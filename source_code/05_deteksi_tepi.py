"""
TAHAP 2 - PROSES 4: DETEKSI TEPI
Teknik: Sobel, Canny, Prewitt

1. Sobel
   Menggunakan kernel turunan pertama arah X dan Y, lalu digabung
   (magnitude) untuk menonjolkan perubahan intensitas (tepi).

2. Canny
   Algoritma multi-tahap: Gaussian smoothing -> gradien -> non-maximum
   suppression -> hysteresis thresholding. Menghasilkan tepi yang lebih
   tipis & bersih dibanding Sobel/Prewitt.

3. Prewitt
   Mirip Sobel tapi bobot kernel konstan (bukan mengikuti distribusi
   gaussian). Diimplementasikan manual dengan cv2.filter2D karena OpenCV
   tidak punya fungsi bawaan untuk Prewitt.
"""

import os
import cv2
import numpy as np

IN_DIR = "/home/claude/dataset"
BASE_OUT = "/home/claude/output"

OUT_SOBEL = os.path.join(BASE_OUT, "04_sobel")
OUT_CANNY = os.path.join(BASE_OUT, "04_canny")
OUT_PREWITT = os.path.join(BASE_OUT, "04_prewitt")

for d in [OUT_SOBEL, OUT_CANNY, OUT_PREWITT]:
    os.makedirs(d, exist_ok=True)

# Kernel Prewitt
prewitt_x = np.array([[-1, 0, 1],
                       [-1, 0, 1],
                       [-1, 0, 1]], dtype=np.float32)
prewitt_y = np.array([[-1, -1, -1],
                       [0, 0, 0],
                       [1, 1, 1]], dtype=np.float32)

files = sorted(os.listdir(IN_DIR))

for f in files:
    img_bgr = cv2.imread(os.path.join(IN_DIR, f))
    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    gray_blur = cv2.GaussianBlur(gray, (3, 3), 0)  # sedikit smoothing dulu

    # 1. Sobel
    sx = cv2.Sobel(gray_blur, cv2.CV_64F, 1, 0, ksize=3)
    sy = cv2.Sobel(gray_blur, cv2.CV_64F, 0, 1, ksize=3)
    sobel_mag = cv2.magnitude(sx, sy)
    sobel_mag = cv2.convertScaleAbs(sobel_mag)
    cv2.imwrite(os.path.join(OUT_SOBEL, f), sobel_mag)

    # 2. Canny
    canny = cv2.Canny(gray_blur, threshold1=50, threshold2=150)
    cv2.imwrite(os.path.join(OUT_CANNY, f), canny)

    # 3. Prewitt
    px = cv2.filter2D(gray_blur.astype(np.float32), -1, prewitt_x)
    py = cv2.filter2D(gray_blur.astype(np.float32), -1, prewitt_y)
    prewitt_mag = cv2.magnitude(px, py)
    prewitt_mag = cv2.convertScaleAbs(prewitt_mag)
    cv2.imwrite(os.path.join(OUT_PREWITT, f), prewitt_mag)

print(f"Deteksi tepi selesai untuk {len(files)} gambar.")
for d in [OUT_SOBEL, OUT_CANNY, OUT_PREWITT]:
    print(" -", d)
