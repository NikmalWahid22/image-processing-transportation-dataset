# Project Mini - Pengolahan Citra Digital
## Implementasi Teknik Pengolahan Citra untuk Peningkatan Kualitas dan Analisis Gambar Digital
### Studi Kasus: Dataset Citra Transportasi Asli (Mobil, Motor, Kapal, Kereta)

## Struktur Folder
```
source_code/
├── main.py                     -> jalankan ini untuk eksekusi semua tahap berurutan
├── 02_konversi_citra.py        -> Proses 1: RGB->Grayscale, RGB->Biner (Otsu)
├── 03_perbaikan_kualitas.py    -> Proses 2: Histogram Eq, Contrast Stretch, Brightness, Sharpening
├── 04_filtering.py             -> Proses 3: Mean, Median, Gaussian Filter
├── 05_deteksi_tepi.py          -> Proses 4: Sobel, Canny, Prewitt
└── 06_segmentasi.py            -> Proses 5: Thresholding, K-Means, Watershed
```

## Dataset

Dataset terdiri dari 20 citra asli (foto nyata) yang diambil dari koleksi dataset
publik di Kaggle (vehicle/transportation image classification), terbagi rata ke
4 kategori: mobil, motor, kapal, dan kereta (masing-masing 5 citra). Karena resolusi
asli sangat beragam, seluruh citra telah distandarisasi (resize maksimal 640px pada
sisi terpanjang, konversi ke RGB+JPG) dan ditaruh di folder `dataset/`.

## Cara Menjalankan

1. Pastikan Python 3 sudah terpasang.
2. Install dependency:
   ```
   pip install opencv-python numpy pillow
   ```
3. Jalankan seluruh pipeline sekaligus:
   ```
   python main.py
   ```
   Atau jalankan satu per satu sesuai urutan nomor file (02 -> 06).

## Output

Setelah dijalankan, akan terbentuk folder `output/` dengan struktur:
- `output/01_grayscale/`, `output/01_biner/`
- `output/02_histogram_equalization/`, `02_contrast_stretching/`, `02_brightness_adjustment/`, `02_sharpening/`
- `output/03_mean_filter/`, `03_median_filter/`, `03_gaussian_filter/`
- `output/04_sobel/`, `04_canny/`, `04_prewitt/`
- `output/05_thresholding/`, `05_kmeans/`, `05_watershed/`

## Catatan

Ingin ganti dataset dengan foto kendaraan kamu sendiri? Tinggal hapus isi folder
`dataset/`, masukkan foto baru (format .jpg, disarankan resize ke sekitar 640px
agar proses lebih cepat), lalu jalankan ulang `python main.py` atau script 02-06
satu per satu. Skrip akan otomatis memproses semua file yang ada di folder tersebut.

