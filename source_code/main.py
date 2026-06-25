"""
MAIN RUNNER
Menjalankan seluruh pipeline pengolahan citra digital secara berurutan:
  1. Generate dataset
  2. Konversi citra (RGB->Grayscale, RGB->Biner)
  3. Perbaikan kualitas citra
  4. Filtering
  5. Deteksi tepi
  6. Segmentasi citra

Jalankan: python main.py
"""
import subprocess
import sys

SCRIPTS = [
    "02_konversi_citra.py",
    "03_perbaikan_kualitas.py",
    "04_filtering.py",
    "05_deteksi_tepi.py",
    "06_segmentasi.py",
]

for script in SCRIPTS:
    print(f"\n{'='*60}\nMenjalankan: {script}\n{'='*60}")
    result = subprocess.run([sys.executable, script])
    if result.returncode != 0:
        print(f"Gagal menjalankan {script}, proses dihentikan.")
        sys.exit(1)

print("\nSemua proses pengolahan citra digital selesai dijalankan.")
print("Hasil tersimpan di folder 'output/'.")
