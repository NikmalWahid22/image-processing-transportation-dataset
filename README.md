# Project Mini - Pengolahan Citra Digital
## Implementasi Teknik Pengolahan Citra untuk Peningkatan Kualitas dan Analisis Gambar Digital
### Studi Kasus: Dataset Citra Transportasi Asli (Mobil, Motor, Kapal, Kereta)

## Struktur Folder
source_code/
├── main.py                     -> jalankan ini untuk eksekusi semua tahap berurutan
├── 02_konversi_citra.py        -> Proses 1: RGB->Grayscale, RGB->Biner (Otsu)
├── 03_perbaikan_kualitas.py    -> Proses 2: Histogram Eq, Contrast Stretch, Brightness, Sharpening
├── 04_filtering.py             -> Proses 3: Mean, Median, Gaussian Filter
├── 05_deteksi_tepi.py          -> Proses 4: Sobel, Canny, Prewitt
└── 06_segmentasi.py            -> Proses 5: Thresholding, K-Means, Watershed

## Dataset
Dataset terdiri dari 20 citra asli (foto nyata) dari koleksi dataset publik di Kaggle 
(vehicle/transportation image classification), terbagi rata ke 4 kategori: mobil, 
motor, kapal, dan kereta (masing-masing 5 citra). Seluruh citra sudah distandarisasi 
(resize maksimal 640px, konversi ke RGB+JPG) dan ditaruh di folder dataset/.

## Cara Menjalankan
1. pip install opencv-python numpy pillow
2. python main.py   (atau jalankan satu-satu: 02 -> 06)

## Output
output/01_grayscale, 01_biner, 02_histogram_equalization, 02_contrast_stretching,
02_brightness_adjustment, 02_sharpening, 03_mean_filter, 03_median_filter,
03_gaussian_filter, 04_sobel, 04_canny, 04_prewitt, 05_thresholding, 05_kmeans, 05_watershed

## Catatan
Mau ganti dataset pakai foto sendiri? Hapus isi folder dataset/, masukkan foto baru 
(.jpg, disarankan ~640px), jalankan ulang python main.py.
