"""
TAHAP 2 - PROSES 5: SEGMENTASI CITRA
Teknik: Thresholding (Otsu), K-Means Segmentation, Watershed Segmentation

1. Thresholding (Otsu)
   Memisahkan objek (kendaraan) dari background berdasarkan satu nilai
   ambang batas intensitas yang dipilih otomatis (sama prinsipnya dengan
   konversi biner di Proses 1, tapi disini diposisikan sebagai bagian dari
   segmentasi -> memisahkan region objek vs non-objek).

2. K-Means Segmentation
   Mengelompokkan piksel (berdasarkan nilai warna BGR) ke dalam K cluster
   menggunakan algoritma K-Means. Setiap piksel diwarnai sesuai centroid
   cluster-nya, sehingga citra tersegmentasi jadi K warna dominan.

3. Watershed Segmentation
   Menganggap citra sebagai topografi (nilai gradien = ketinggian),
   lalu "menggenangi" dari titik-titik marker hingga bertemu di garis
   batas (watershed line) -> baik untuk memisahkan objek yang saling
   bersentuhan.
"""

import os
import cv2
import numpy as np

IN_DIR = "/home/claude/dataset"
BASE_OUT = "/home/claude/output"

OUT_THRESH = os.path.join(BASE_OUT, "05_thresholding")
OUT_KMEANS = os.path.join(BASE_OUT, "05_kmeans")
OUT_WATERSHED = os.path.join(BASE_OUT, "05_watershed")

for d in [OUT_THRESH, OUT_KMEANS, OUT_WATERSHED]:
    os.makedirs(d, exist_ok=True)

files = sorted(os.listdir(IN_DIR))
K = 3  # jumlah cluster k-means

for f in files:
    img_bgr = cv2.imread(os.path.join(IN_DIR, f))
    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

    # 1. Thresholding (Otsu)
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cv2.imwrite(os.path.join(OUT_THRESH, f), thresh)

    # 2. K-Means Segmentation
    Z = img_bgr.reshape((-1, 3)).astype(np.float32)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)
    _, labels, centers = cv2.kmeans(Z, K, None, criteria, 5, cv2.KMEANS_RANDOM_CENTERS)
    centers = centers.astype(np.uint8)
    kmeans_result = centers[labels.flatten()].reshape(img_bgr.shape)
    cv2.imwrite(os.path.join(OUT_KMEANS, f), kmeans_result)

    # 3. Watershed Segmentation
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, otsu = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    kernel = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(otsu, cv2.MORPH_OPEN, kernel, iterations=2)
    sure_bg = cv2.dilate(opening, kernel, iterations=3)
    dist = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
    _, sure_fg = cv2.threshold(dist, 0.4 * dist.max(), 255, 0)
    sure_fg = sure_fg.astype(np.uint8)
    unknown = cv2.subtract(sure_bg, sure_fg)

    _, markers = cv2.connectedComponents(sure_fg)
    markers = markers + 1
    markers[unknown == 255] = 0

    markers = cv2.watershed(img_bgr.copy(), markers)
    watershed_vis = img_bgr.copy()
    watershed_vis[markers == -1] = [0, 0, 255]  # garis batas watershed -> merah
    cv2.imwrite(os.path.join(OUT_WATERSHED, f), watershed_vis)

print(f"Segmentasi selesai untuk {len(files)} gambar (K-Means, K={K}).")
for d in [OUT_THRESH, OUT_KMEANS, OUT_WATERSHED]:
    print(" -", d)
