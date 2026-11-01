# Program Rekap dan Analisis Nilai Matematika

## Identitas

- Nama: Aulia Citra
- NIM: 2225250012
- Kelas: 3F
- Program Studi: S1 Pendidikan Matematika FKIP Untirta
- Mata Kuliah: Algoritma dan Pemrograman
- Semester: 3
- Tahun Ajaran: 2026/2027 Ganjil

## Deskripsi

Program Python berbasis terminal untuk membantu guru atau calon
guru matematika merekap nilai satu kelas.

Program membaca data siswa dari file teks, memvalidasi data,
menghitung statistik, menentukan ketuntasan, serta menampilkan
dan menyimpan laporan.

Rancangan disusun pada Pertemuan 14. Implementasi, pengujian,
dan dokumentasi dilakukan pada Pertemuan 15.

Sesuai arahan kelas yang diterima, tugas dikerjakan secara
individu dan terpisah dari proyek UAS.

## Status Proyek

- Lima fitur wajib telah diimplementasikan.
- Program utama berhasil dijalankan dengan data contoh.
- Dua belas pengujian fungsi telah dijalankan dan menghasilkan PASS.
- Penanganan file kosong dan file hilang diperiksa melalui main.py.
- Setelah data normal dikembalikan, program dan pengujian
  dijalankan ulang dengan hasil sesuai.

Proposal awal tetap tersedia dalam [proposal.md](proposal.md)
sebagai dokumentasi rancangan Pertemuan 14.

## Fitur

1. Membaca data siswa dari file teks.
2. Memvalidasi format, identitas, dan nilai dalam rentang 0–100.
3. Menghitung jumlah data valid, rata-rata, minimum, dan maksimum.
4. Menentukan status serta jumlah siswa tuntas dan belum tuntas.
5. Menampilkan laporan di terminal dan menyimpannya ke file.

Batas ketuntasan adalah 75 sebagai asumsi proyek.
Nilai >= 75 berstatus Tuntas.
Nilai < 75 berstatus Belum tuntas.

## Persyaratan

- Python 3.
- Git untuk clone dan pengelolaan versi.
- VS Code sebagai editor yang digunakan dalam praktik.
- Tidak memerlukan instalasi pustaka eksternal.

Lingkungan pengujian: Windows, PowerShell, dan Python 3.14.7.

## Instalasi

Clone repositori dan masuk ke folder proyek:

```powershell
git clone https://github.com/citra137/proyek-analisis-nilai-2225250012.git
cd proyek-analisis-nilai-2225250012
```

Buka folder tersebut melalui File > Open Folder pada VS Code.

Periksa Python:

```powershell
py --version
```

## Format Data Input

File input: data/nilai_contoh.txt.

Setiap baris menggunakan format ID,nama,nilai tanpa header.
Nilai desimal menggunakan tanda titik.

```text
A001,Ayu,80
A002,Bima,70
A003,Citra,90
A004,Deni,75
A005,Eka,85
```

Data bersifat fiktif.

- Baris kosong dilewati.
- Setiap baris harus memiliki tepat tiga bagian.
- ID dan nama tidak boleh kosong.
- Nilai harus dapat dikonversi menjadi angka dalam rentang 0–100.
- Baris tidak valid dilaporkan beserta nomor baris dan dilewati.
- Pembacaan menggunakan utf-8-sig untuk mendukung UTF-8
  dengan maupun tanpa BOM.

## Cara Menjalankan

Dari terminal folder utama proyek:

```powershell
py main.py
```

Pada sistem yang menggunakan perintah python3:

```bash
python3 main.py
```

Program menampilkan rincian siswa dan ringkasan di terminal.
Laporan disimpan ke output/hasil_analisis.txt.

Folder output dibuat otomatis jika belum tersedia.
File input tidak diubah oleh proses penyimpanan laporan.

## Contoh Hasil Aktual

Dengan data contoh yang tersedia:

```text
DAFTAR NILAI SISWA
A001 | Ayu | 80.00 | Tuntas
A002 | Bima | 70.00 | Belum tuntas
A003 | Citra | 90.00 | Tuntas
A004 | Deni | 75.00 | Tuntas
A005 | Eka | 85.00 | Tuntas

RINGKASAN
Jumlah data valid: 5
Rata-rata: 80.00
Nilai minimum: 70.00
Nilai maksimum: 90.00
Batas ketuntasan: 75.00
Jumlah tuntas: 4
Jumlah belum tuntas: 1
```

Rata-rata = (80 + 70 + 90 + 75 + 85) / 5 = 80.

## Struktur Folder dan File

| Lokasi | Tanggung Jawab |
|---|---|
| main.py | Mengatur pembacaan, pengolahan, penampilan, dan penyimpanan. |
| src/__init__.py | Menandai src sebagai package Python. |
| src/input_data.py | Membaca file dan memvalidasi setiap baris. |
| src/proses.py | Menghitung statistik dan menentukan ketuntasan. |
| src/output.py | Menyusun string laporan dan menulisnya ke file. |
| data/nilai_contoh.txt | Data contoh siswa fiktif. |
| tests/__init__.py | Menandai tests sebagai package Python. |
| tests/uji_program.py | Menjalankan dua belas pengujian fungsi dengan assert. |
| tests/test_case.md | Dokumentasi input, expected, actual, dan status pengujian. |
| docs/bug_log.md | Catatan pengujian kondisi khusus dan batasan. |
| output/hasil_analisis.txt | Laporan hasil analisis terakhir yang berhasil disimpan. |
| output/.gitkeep | Mempertahankan folder output di Git. |
| proposal.md | Rancangan awal Pertemuan 14. |
| README.md | Dokumentasi penggunaan proyek. |
| .gitignore | Mengabaikan cache Python dan pengaturan lokal. |

## Alur Program

1. Menentukan lokasi file berdasarkan folder main.py.
2. Membaca dan memvalidasi setiap baris.
3. Menampilkan pesan untuk data yang tidak valid.
4. Menghentikan proses jika tidak terdapat data valid.
5. Menghitung statistik dan ketuntasan.
6. Menyusun serta menampilkan laporan.
7. Menyimpan laporan dan menampilkan status penyimpanan.

## Fungsi dan Struktur Data

- validasi_nilai(): memeriksa rentang nilai.
- baca_data(): menghasilkan list data valid dan list pesan error.
- tentukan_status(): menghasilkan status ketuntasan.
- hitung_statistik(): menghasilkan dictionary ringkasan.
- buat_laporan(): menghasilkan string laporan.
- simpan_laporan(): menulis laporan ke file.
- main(): mengatur alur keseluruhan.

Data siswa menggunakan list berisi dictionary dengan key
id, nama, dan nilai. Ringkasan menggunakan dictionary agar
hasil dapat diakses berdasarkan nama informasinya.

## Cara Menjalankan Pengujian

Dari folder utama:

```powershell
py -m tests.uji_program
```

Pengujian menggunakan assert dan TemporaryDirectory.
File uji fungsi dibuat sementara sehingga data contoh tidak diubah.

Jika assert gagal, pengujian berhenti dengan AssertionError.
Jika seluruh pemeriksaan berhasil, program menampilkan dua belas
baris PASS dan ringkasan pengujian.

## Ringkasan Hasil Pengujian

| ID | Kondisi | Expected | Actual | Status |
|---|---|---|---|---|
| TC01 | Data normal | Jumlah 5; rata-rata 80; min 70; max 90; tuntas 4; belum tuntas 1. | Sesuai seluruh expected. | PASS |
| TC02 | Nilai 0 | Diterima dan belum tuntas. | Diterima; statistik 0; belum tuntas 1. | PASS |
| TC03 | Nilai 100 | Diterima dan tuntas. | Diterima; statistik 100; tuntas 1. | PASS |
| TC04 | Nilai 74, 75, 76 | Belum tuntas, Tuntas, Tuntas; rata-rata 75. | Sesuai expected. | PASS |
| TC05 | Nilai -1 dan 105 | Kedua baris ditolak dengan pesan. | Data kosong dan dua pesan rentang. | PASS |
| TC06 | Nilai abc | Ditolak dengan pesan nilai harus berupa angka. | Sesuai expected. | PASS |
| TC07 | Format dua bagian | Ditolak dengan pesan format. | Sesuai expected. | PASS |
| TC08 | File kosong | Tidak terjadi pembagian nol; main menampilkan pesan tidak ada data valid. | Sesuai expected. | PASS |
| TC09 | File hilang | FileNotFoundError ditangani oleh main dengan pesan. | Pesan file tidak ditemukan tanpa traceback. | PASS |
| TC10 | Data campuran | Hanya nilai 80 diproses; satu pesan; baris kosong dilewati. | Sesuai expected. | PASS |
| TC11 | Simpan laporan | Isi laporan sama dan input tetap. | Pemeriksaan kesamaan berhasil. | PASS |
| TC12 | Nama kosong | Ditolak dengan pesan identitas kosong. | Sesuai expected. | PASS |

Rincian tersedia pada [tests/test_case.md](tests/test_case.md).

TC08 dan TC09 juga diperiksa langsung melalui program utama.
Setelah data normal dikembalikan, laporan normal dan seluruh
pengujian fungsi dijalankan kembali dengan hasil sesuai.

Tidak ada perubahan kode di antara dua pengujian ulang tersebut.

## Penanganan Kesalahan dan Catatan Bug

- FileNotFoundError ditangani pada program utama.
- ValueError saat konversi nilai ditangani per baris.
- Data kosong diperiksa sebelum pengolahan pada program utama.
- Fungsi statistik juga menyediakan hasil aman untuk list kosong.
- OSError ditangani pada pembacaan dan penyimpanan file.

Pada kasus yang telah diuji, belum ditemukan perbedaan hasil
aktual dengan expected result. Penanganan kondisi khusus sudah
tersedia dalam implementasi awal; tidak dicatat sebagai bug
yang ditemukan lalu diperbaiki.

Catatan tersedia pada [docs/bug_log.md](docs/bug_log.md).

## Known Issues dan Batas Pengujian

1. Nama tidak boleh mengandung koma karena format memakai
   pemisah koma dengan tepat tiga bagian.
2. ID ganda belum diperiksa; setiap baris valid dihitung sebagai
   satu data.
3. Jika file hilang atau tidak ada data valid, laporan lama
   tetap tersimpan. Laporan lama bukan hasil proses yang gagal.
4. Laporan menggunakan mode w sehingga hasil sukses terbaru
   menggantikan laporan sebelumnya, sesuai rancangan.
5. Kegagalan izin baca/tulis belum disimulasikan, meskipun
   penanganan OSError sudah tersedia.

## Kontribusi Individu

Aulia Citra bertanggung jawab atas perancangan, implementasi,
integrasi, pelaksanaan pengujian, pemeriksaan hasil,
dokumentasi, serta pengelolaan Git dan GitHub.

## Referensi dan Bantuan

- Bahan Ajar Pertemuan 14: Perancangan Proyek Program Sederhana,
  Algoritma dan Pemrograman, FKIP Untirta, 2026/2027 Ganjil.
- Bahan Ajar Pertemuan 15: Implementasi, Pengujian, dan Dokumentasi
  Proyek, Algoritma dan Pemrograman, FKIP Untirta, 2026/2027 Ganjil.
- ChatGPT digunakan untuk membantu penyusunan rancangan, kode,
  skenario pengujian, dokumentasi, dan panduan praktik.
  Penulis menjalankan program serta pengujian di komputer
  sendiri dan bertanggung jawab memahami serta memeriksa hasilnya.