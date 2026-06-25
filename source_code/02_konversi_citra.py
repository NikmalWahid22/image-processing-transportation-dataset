"""
TAHAP 2 - PROSES 1: KONVERSI CITRA
Konversi RGB -> Grayscale dan RGB -> Biner (Hitam-Putih)

- Grayscale: menggunakan formula luminositas standar
  Gray = 0.299*R + 0.587*G + 0.114*B  (ITU-R BT.601, dipakai cv2.COLOR_BGR2GRAY)
- Biner: hasil grayscale di-threshold menggunakan metode Otsu (threshold otomatis)
  sehingga setiap piksel menjadi 0 (hitam) atau 255 (putih).
"""

import os
import cv2
import numpy as np

IN_DIR = "/home/claude/dataset"
OUT_GRAY = "/home/claude/output/01_grayscale"
OUT_BINER = "/home/claude/output/01_biner"

os.makedirs(OUT_GRAY, exist_ok=True)
os.makedirs(OUT_BINER, exist_ok=True)

files = sorted(os.listdir(IN_DIR))

otsu_thresholds = []

for f in files:
    path = os.path.join(IN_DIR, f)
    img_bgr = cv2.imread(path)

    # --- RGB ke Grayscale ---
    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(os.path.join(OUT_GRAY, f), gray)

    # --- Grayscale ke Biner (Otsu thresholding) ---
    thresh_val, biner = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cv2.imwrite(os.path.join(OUT_BINER, f), biner)

    otsu_thresholds.append((f, thresh_val))

print("Konversi selesai untuk", len(files), "gambar.")
print("\nContoh nilai threshold Otsu otomatis (5 gambar pertama):")
for f, t in otsu_thresholds[:5]:
    print(f"  {f:20s} -> threshold = {t}")
