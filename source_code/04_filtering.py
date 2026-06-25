"""
TAHAP 2 - PROSES 3: FILTERING (PEREDAM NOISE)
Teknik: Mean Filter, Median Filter, Gaussian Filter

1. Mean Filter (Average Filter)
   Mengganti setiap piksel dengan rata-rata piksel tetangga dalam kernel
   k x k. Efektif meredam noise tapi cenderung membuat tepi blur.
   cv2.blur(img, (5,5))

2. Median Filter
   Mengganti setiap piksel dengan nilai median dari piksel tetangga.
   Sangat efektif untuk salt-and-pepper noise dan menjaga tepi lebih baik
   dibanding mean filter. cv2.medianBlur(img, 5)

3. Gaussian Filter
   Mirip mean filter tapi bobot tetangga mengikuti distribusi Gaussian
   (piksel tengah berbobot lebih besar). Hasil lebih halus & natural.
   cv2.GaussianBlur(img, (5,5), sigmaX=0)

Catatan: agar pengujian noise lebih representatif, sebagian noise gaussian
dari proses akuisisi citra (Tahap 1) memang sengaja dipertahankan supaya
efek tiap filter terlihat jelas perbedaannya.
"""

import os
import cv2
import numpy as np

IN_DIR = "/home/claude/dataset"
BASE_OUT = "/home/claude/output"

OUT_MEAN = os.path.join(BASE_OUT, "03_mean_filter")
OUT_MEDIAN = os.path.join(BASE_OUT, "03_median_filter")
OUT_GAUSS = os.path.join(BASE_OUT, "03_gaussian_filter")

for d in [OUT_MEAN, OUT_MEDIAN, OUT_GAUSS]:
    os.makedirs(d, exist_ok=True)

files = sorted(os.listdir(IN_DIR))

KSIZE = 5  # ukuran kernel 5x5

for f in files:
    img_bgr = cv2.imread(os.path.join(IN_DIR, f))

    # 1. Mean Filter
    mean_f = cv2.blur(img_bgr, (KSIZE, KSIZE))
    cv2.imwrite(os.path.join(OUT_MEAN, f), mean_f)

    # 2. Median Filter
    median_f = cv2.medianBlur(img_bgr, KSIZE)
    cv2.imwrite(os.path.join(OUT_MEDIAN, f), median_f)

    # 3. Gaussian Filter
    gauss_f = cv2.GaussianBlur(img_bgr, (KSIZE, KSIZE), sigmaX=0)
    cv2.imwrite(os.path.join(OUT_GAUSS, f), gauss_f)

print(f"Filtering selesai untuk {len(files)} gambar (kernel {KSIZE}x{KSIZE}).")
for d in [OUT_MEAN, OUT_MEDIAN, OUT_GAUSS]:
    print(" -", d)

# ---- Evaluasi kuantitatif sederhana: standar deviasi noise pada area langit ----
print("\nEvaluasi std-dev intensitas (area langit, citra lebih halus -> std lebih kecil):")
sample = files[0]
orig = cv2.cvtColor(cv2.imread(os.path.join(IN_DIR, sample)), cv2.COLOR_BGR2GRAY)
mean_s = cv2.cvtColor(cv2.imread(os.path.join(OUT_MEAN, sample)), cv2.COLOR_BGR2GRAY)
median_s = cv2.cvtColor(cv2.imread(os.path.join(OUT_MEDIAN, sample)), cv2.COLOR_BGR2GRAY)
gauss_s = cv2.cvtColor(cv2.imread(os.path.join(OUT_GAUSS, sample)), cv2.COLOR_BGR2GRAY)

roi = (slice(0, 40), slice(0, 320))  # baris atas = area langit
print(f"  Asli           : std = {orig[roi].std():.2f}")
print(f"  Mean Filter    : std = {mean_s[roi].std():.2f}")
print(f"  Median Filter  : std = {median_s[roi].std():.2f}")
print(f"  Gaussian Filter: std = {gauss_s[roi].std():.2f}")
