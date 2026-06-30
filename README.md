# Python Implementation for Pharmacy Business Intelligence Project

## Deskripsi

Repository ini berisi implementasi Python yang digunakan pada Proyek Business Intelligence menggunakan **Global Pharmacy Sales Dataset (2020–2025)**.

Implementasi Python dijalankan melalui **Python Visual pada Microsoft Power BI** untuk mendukung proses analisis data dan visualisasi dashboard.

---

## Dataset

Dataset yang digunakan adalah **Global Pharmacy Sales Dataset (2020–2025)** yang berisi data transaksi penjualan obat, stok, wilayah, kategori produk, serta informasi pelanggan.

---

## Metode Data Mining

### 1. Forecasting

Forecasting digunakan untuk memprediksi pendapatan (Revenue) pada periode berikutnya.

Metode:

- Holt-Winters Exponential Smoothing

Library:

- pandas
- matplotlib
- statsmodels

Output:

- Forecast Line Chart

---

### 2. Clustering

Clustering digunakan untuk mengelompokkan kondisi persediaan obat berdasarkan stok dan sisa masa kedaluwarsa.

Metode:

- K-Means Clustering

Library:

- pandas
- matplotlib
- scikit-learn

Output:

- Scatter Plot Inventory Clustering Analysis

---

## Struktur Repository

```
pharmacy-bi-python
│
├── Forecasting
│   └── forecasting.py
│
├── Clustering
│   └── clustering.py
│
├── requirements.txt
│
└── README.md
```

---

## Software

- Microsoft Power BI Desktop
- Python
- pandas
- matplotlib
- statsmodels
- scikit-learn

---

## Catatan

Seluruh script Python pada repository ini dijalankan menggunakan **Python Visual di Microsoft Power BI**.

Data diterima melalui objek `dataset` yang secara otomatis disediakan oleh Power BI sehingga script tidak memerlukan pembacaan file Excel atau CSV secara langsung.

---

## Kelompok 02

Mata Kuliah Business Intelligence

Program Studi Informatika

Universitas Islam Indonesia
