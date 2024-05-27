<a name="readme-top"></a>


<!-- PROJECT LOGO -->
<br />
<div align="center">
<h3 align="center">Basestation</h3>

  <p align="center">
    Repositori untuk basestation tim robot Ver 2.0.2 
    <br />
    <a href="https://github.com/Dhaboav/basestation/issues">Lapor Bug atau issue</a>
  </p>
</div>


<details>
  <summary>Daftar Isi</summary>
  <ol>
    <li><a href="#Requirment">Requirment</a></li>
    <li><a href="#Structure">Struktur repositori</a></li>
    <li><a href="#Detail">Detail dari struktur</a></li>
    <li><a href="#How to use">Cara menggunakan aplikasi</a></li>
    <li><a href="#About">Penjelasan aplikasi</a></li>
  </ol>
</details>


### Requirment
1. Install Python.
2. `pip install psutil` pada Python.
3. Klon repo dari github.
  ```git
   git clone -b edit-branch https://github.com/dhaboav/basestation-robot.git
  ```
<p align="right">(<a href="#readme-top">Kembali ke atas</a>)</p>


### Structure
```
. 
├── MVC
|   |
|   ├── __init__.py
|   ├── client.py
|   ├── controller.py
|   ├── model.py
|   ├── server.py
|   └── view.py
|
├── .gitignore
├── app.py
├── data.json
└── README.md
```
<p align="right">(<a href="#readme-top">Kembali ke atas</a>)</p>


### Detail
1. Bagian `model` berfungsi untuk menyimpan segala data yang akan digunakan pada aplikasi.
2. Bagian `view` mengatur tampilan interface aplikasi.
3. Bagian `controller` mengatur segala perubahan yang terjadi.
4. Bagian `data` dapat dirubah alamat `IP_ADDRESS` menyesuaikan kondisi.
5. Bagian `app` digunakan untuk menjalankan aplikasi.

`HANYA UBAH` bagian `data` dan tidak direkomendasikan untuk mengubah source code selain file data.
<p align="right">(<a href="#readme-top">Kembali ke atas</a>)</p>


### How to use
1. Buat file `data.json` jika tidak tersedia
2. Jalankan `app.py` pada terminal
<p align="right">(<a href="#readme-top">Kembali ke atas</a>)</p>


### About
Aplikasi menggunakan arsitektur MVC (MODEL-VIEW-CONTROLLER) dengan tambahan fungsionalitas client-server dan dibuat dengan bahasa pemrogramaan Python untuk versi saat ini hanya berkerja pada platform Windows dengan limitasi harus dijalankan dengan terminal pada file dengan nama `app.py`.
<p align="right">(<a href="#readme-top">Kembali ke atas</a>)</p>
