# 🚗 Digital Image Processing — Vehicle & Transportation Dataset

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-5C3EE8?style=flat&logo=opencv&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-latest-013243?style=flat&logo=numpy&logoColor=white)
![Status](https://img.shields.io/badge/status-completed-brightgreen?style=flat)
![License](https://img.shields.io/badge/license-MIT-blue?style=flat)

Implementasi teknik **pengolahan citra digital** untuk peningkatan kualitas dan analisis gambar, diterapkan pada dataset citra transportasi nyata (mobil, motor, kapal, kereta). Project ini mencakup 5 kelompok proses utama: **konversi**, **perbaikan kualitas**, **filtering**, **deteksi tepi**, dan **segmentasi citra** — dibangun menggunakan Python, OpenCV, NumPy, dan Pillow.

---

##  Fitur / Proses yang Diimplementasikan

| No | Proses | Teknik |
|----|--------|--------|
| 1 | **Konversi Citra** | RGB → Grayscale, RGB → Biner (Otsu Thresholding) |
| 2 | **Perbaikan Kualitas** | Histogram Equalization, Contrast Stretching, Brightness Adjustment, Sharpening |
| 3 | **Filtering** | Mean Filter, Median Filter, Gaussian Filter |
| 4 | **Deteksi Tepi** | Sobel, Canny, Prewitt |
| 5 | **Segmentasi Citra** | Thresholding, K-Means Segmentation, Watershed Segmentation |

---

##  Hasil Evaluasi Kuantitatif

**Filtering** — Varians Laplacian (indikator ketajaman/detail citra):

| Jenis Citra | Varians Laplacian |
|---|---|
| Asli (sebelum filter) | 719.29 |
| Mean Filter (5x5) | 35.47 |
| Median Filter (5x5) | 214.50 |
| Gaussian Filter (5x5) | 85.64 |

**Konversi Citra** — Nilai threshold Otsu otomatis bervariasi antar citra (87–160), membuktikan metode ini adaptif terhadap karakteristik pencahayaan masing-masing foto.

---

##  Struktur Folder

```
.
├── source_code/                          # Seluruh script Python
│   ├── main.py                           # Jalankan ini untuk eksekusi semua tahap
│   ├── 02_konversi_citra.py
│   ├── 03_perbaikan_kualitas.py
│   ├── 04_filtering.py
│   ├── 05_deteksi_tepi.py
│   ├── 06_segmentasi.py
│   └── README.md
├── dataset/                              # 20 citra asli (mobil, motor, kapal, kereta)
├── output/                               # Hasil seluruh proses pengolahan citra
│   ├── 01_grayscale/  01_biner/
│   ├── 02_histogram_equalization/  02_contrast_stretching/
│   ├── 02_brightness_adjustment/   02_sharpening/
│   ├── 03_mean_filter/  03_median_filter/  03_gaussian_filter/
│   ├── 04_sobel/  04_canny/  04_prewitt/
│   └── 05_thresholding/  05_kmeans/  05_watershed/
├── Laporan_Pengolahan_Citra_Digital.docx
└── Presentasi_Pengolahan_Citra_Digital.pptx
```

---

##  Cara Menjalankan

### 1. Clone repo
```bash
git clone https://github.com/username/nama-repo.git
cd nama-repo/source_code
```

### 2. Install dependency
```bash
pip install opencv-python numpy pillow
```

### 3. Jalankan
Jalankan seluruh pipeline sekaligus:
```bash
python main.py
```
Atau satu per satu sesuai urutan:
```bash
python 02_konversi_citra.py
python 03_perbaikan_kualitas.py
python 04_filtering.py
python 05_deteksi_tepi.py
python 06_segmentasi.py
```

Hasil akan otomatis tersimpan di folder `output/`.

---

##  Dataset

Dataset berisi **20 citra asli** (foto nyata, bukan ilustrasi) yang diambil dari koleksi dataset publik di [Kaggle](https://www.kaggle.com/datasets) (vehicle/transportation image classification), terbagi rata ke 4 kategori:

| Kategori | Jumlah |
|---|---|
|  Mobil | 5 |
|  Motor | 5 |
|  Kapal | 5 |
|  Kereta | 5 |

Seluruh citra telah distandarisasi (resize maksimal 640px pada sisi terpanjang, konversi ke RGB + JPG) agar konsisten saat diproses.

Ingin pakai foto sendiri? Tinggal ganti isi folder `dataset/` dengan foto baru (`.jpg`), lalu jalankan ulang `python main.py`.

---

##  Tech Stack

- **Python 3**
- **OpenCV** — operasi pengolahan citra utama
- **NumPy** — operasi array & numerik
- **Pillow (PIL)** — I/O & manipulasi citra tambahan

---


##  Kesimpulan Singkat

- Otsu Thresholding adaptif terhadap variasi pencahayaan antar citra (threshold bervariasi 87–160).
- **Median** & **Gaussian Filter** lebih unggul menjaga ketajaman tepi dibanding **Mean Filter**.
- **Canny** memberikan hasil deteksi tepi paling bersih & presisi dibanding Sobel/Prewitt.
- **K-Means Segmentation (K=3)** paling representatif memisahkan objek dari latar kompleks dibanding Thresholding & Watershed.

---

