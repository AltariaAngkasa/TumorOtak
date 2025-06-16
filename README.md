# 🧠 Klasifikasi Tumor Otak Berbasis Web

Aplikasi web sederhana berbasis Flask untuk memprediksi apakah citra MRI otak menunjukkan adanya **tumor atau tidak** menggunakan **ekstraksi fitur GLCM (Gray-Level Co-occurrence Matrix)** dan model Machine Learning (Random Forest).

---

## 📦 Fitur Utama

- ✅ Upload gambar MRI melalui klik atau drag & drop
- ✅ Ekstraksi fitur tekstur citra dengan GLCM
- ✅ Klasifikasi menggunakan model `.pkl` yang sudah dilatih (Random Forest)
- ✅ Antarmuka web sederhana, responsif, dan ringan

---

## 🗂 Struktur Direktori

tumor_prediksi_web/
├── app.py
├── modelNEW.pkl # Model Random Forest hasil training (harus ditambahkan manual)
├── templates/
│ ├── index.html # Halaman upload
│ └── result.html # Halaman hasil prediksi
├── static/
│ ├── style.css # Styling tampilan web
│ ├── script.js # Drag-and-drop logic
│ └── uploads/ # Folder untuk menyimpan gambar yang diunggah


---

## 🚀 Cara Menjalankan

### 1. Pastikan Python & pip sudah terinstall

### 2. Install dependensi:

```bash
pip install flask numpy pillow scikit-image scikit-learn opencv-python
