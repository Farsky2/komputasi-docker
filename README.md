# Project 1 – Containerisasi Aplikasi API Sederhana Menggunakan Docker

**Mata Kuliah:** Komputasi Paralel dan Terdistribusi
**Nama:** Farid Kasyfil Aziz 
**NIM:** *2455208059*
**Kelas:** 5RPL
**Pilihan:** Pilihan 2 – Containerisasi Menggunakan Docker

---

## 1. Deskripsi Singkat

Project ini membuat sebuah **API sederhana** menggunakan Python (Flask) dan menjalankannya di dalam **Docker container**. API menyediakan tiga endpoint:

| Endpoint | Fungsi | Contoh |
|---|---|---|
| `/` | Pesan sambutan | `http://localhost:5000/` |
| `/tambah?a=..&b=..` | Penjumlahan dua angka | `http://localhost:5000/tambah?a=5&b=3` |
| `/kali?a=..&b=..` | Perkalian dua angka | `http://localhost:5000/kali?a=4&b=6` |

## 2. Struktur Project

```
Project docker/
├── app.py             # Kode aplikasi Flask
├── requirements.txt   # Daftar dependensi Python
├── Dockerfile         # Instruksi membuat Docker image
├── README.md          # Dokumentasi
└── screenshots/       # Bukti hasil percobaan
```

## 3. Teknologi yang Digunakan

- Python 3.12 dan Flask
- Docker Desktop (versi 29.9.3)
- Visual Studio Code dan PowerShell

## 4. Penjelasan Dockerfile

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]
```

| Instruksi | Penjelasan |
|---|---|
| `FROM python:3.12-slim` | Memakai image dasar Python 3.12 versi ringan |
| `WORKDIR /app` | Menetapkan folder kerja di dalam container |
| `COPY requirements.txt .` | Menyalin daftar dependensi ke container |
| `RUN pip install ...` | Memasang Flask di dalam image |
| `COPY app.py .` | Menyalin kode aplikasi ke container |
| `EXPOSE 5000` | Menandai aplikasi memakai port 5000 |
| `CMD ["python", "app.py"]` | Perintah yang dijalankan saat container start |

Dependensi disalin dan dipasang **sebelum** menyalin `app.py` agar Docker dapat memakai cache layer, sehingga build berikutnya lebih cepat jika hanya kode yang berubah.

## 5. Cara Menjalankan

**Prasyarat:** Docker Desktop terpasang dan statusnya *Engine running*.

**1. Build image**
```bash
docker build -t api-sederhana .
```

**2. Jalankan container**
```bash
docker run -d -p 5000:5000 --name api-farid api-sederhana
```
Opsi `-d` menjalankan di background, dan `-p 5000:5000` menghubungkan port 5000 komputer dengan port 5000 container.

**3. Cek container**
```bash
docker ps
```

**4. Akses aplikasi** melalui browser atau:
```bash
curl.exe "http://localhost:5000/tambah?a=5&b=3"
```

**5. Hentikan dan hapus container**
```bash
docker stop api-farid
docker rm api-farid
```

## 6. Hasil Implementasi

### a. Instalasi Docker berhasil
`docker run hello-world` menampilkan pesan "Hello from Docker!".

![hello-world](screenshots/01-hello-world.png)

### b. Build image berhasil
![docker build](screenshots/02-docker-build.png)

### c. Container berjalan
Hasil `docker ps` menunjukkan container `api-farid` berstatus *Up* dan port `5000` terhubung.

![docker ps](screenshots/03-docker-ps.png)

### d. Hasil di browser
Contoh akses `http://localhost:5000/tambah?a=5&b=3` menghasilkan:
```json
{"a":5.0,"b":3.0,"hasil":8.0}
```

![browser](screenshots/04-browser.png)

### e. Tampilan Docker Desktop
![docker desktop](screenshots/05-docker-desktop.png)

## 7. Kendala yang Dihadapi

- **Error `failed to read dockerfile: no such file or directory`.** Penyebabnya terminal berada di folder induk, sedangkan `Dockerfile` ada di subfolder `Project docker`. Solusinya pindah folder dengan `cd "Project docker"` lalu build ulang.
- **Docker dalam Resource Saver mode.** Engine perlu dinyalakan terlebih dahulu lewat tombol Play di Docker Desktop.

## 8. Kesimpulan

Aplikasi API sederhana berhasil dibuat, dikemas menjadi Docker image melalui Dockerfile, lalu dijalankan sebagai container. Dengan Docker, aplikasi berjalan di lingkungan yang terisolasi dan konsisten, sehingga tidak bergantung pada instalasi Python di komputer. Aplikasi yang sama dapat dijalankan di komputer lain hanya dengan Docker dan perintah `docker build` serta `docker run`.

## 9. Referensi

- Dokumentasi Docker: https://docs.docker.com/
- Dokumentasi Flask: https://flask.palletsprojects.com/
- Docker Hub, image Python: https://hub.docker.com/_/python