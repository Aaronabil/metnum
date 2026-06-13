# KopiLab - Prediksi Omset Warung Kopi

Aplikasi web tugas Metode Numerik untuk materi Regresi Linear Sederhana.

## Fitur

- Input 3 data modal dan keuntungan penjualan.
- Perhitungan regresi linear sederhana dengan Python Flask.
- Rumus: `y = a + bx`.
- Menampilkan nilai `a`, `b`, persamaan regresi, dan prediksi keuntungan.
- Grafik canvas berisi titik data, garis regresi, dan titik prediksi.
- Desain clean Apple-inspired.

## Struktur Folder

- `app.py`: backend Python Flask dan function regresi.
- `templates/index.html`: tampilan web, form input, grafik, dan request ke API Python.
- `requirements.txt`: dependency Python.

## Cara Setup

1. Extract file zip.
2. Masuk ke folder project:

```bash
cd metnum-regresi-kopi
```

3. Buat virtual environment:

```bash
python -m venv .venv
```

4. Aktifkan virtual environment.

Windows:

```bash
.venv\Scripts\activate
```

Linux / macOS:

```bash
source .venv/bin/activate
```

5. Install dependency:

```bash
pip install -r requirements.txt
```

6. Jalankan aplikasi:

```bash
python app.py
```

7. Buka browser:

```text
http://127.0.0.1:5000
```

## Function Python Utama

Function perhitungan ada di `app.py`:

```python
def simple_linear_regression(points, predict_x):
    ...
```

Function ini menghitung:

```text
b = (nΣxy - ΣxΣy) / (nΣx² - (Σx)²)
a = (Σy - bΣx) / n
y = a + bx
```

Frontend memanggil function ini lewat endpoint:

```text
POST /api/predict
```
