# 🧠 Klasifikasi Tumor Otak Berbasis Web
![image](https://github.com/user-attachments/assets/5c52952c-0a03-476f-acd3-0ef0d22474aa)



Aplikasi web sederhana berbasis Flask untuk memprediksi apakah citra MRI otak menunjukkan adanya **tumor atau tidak** menggunakan **ekstraksi fitur GLCM (Gray-Level Co-occurrence Matrix)** dan model Machine Learning (Random Forest).

---

## 📦 Fitur Utama

- ✅ Upload gambar MRI melalui klik atau drag & drop
- ✅ Ekstraksi fitur tekstur citra dengan GLCM
- ✅ Klasifikasi menggunakan model `.pkl` yang sudah dilatih (Random Forest)
- ✅ Antarmuka web sederhana, responsif, dan ringan

---



## 🚀 Cara Menjalankan

### 1. Pastikan Python & pip sudah terinstall

### 2. Install dependensi:

```bash
pip install flask numpy pillow scikit-image scikit-learn opencv-python
```

### 3. Lalu setelahnya clone dan jalankan dengan command ini:
```bash
py app.py
