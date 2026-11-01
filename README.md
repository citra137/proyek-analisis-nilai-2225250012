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

Proyek individu ini merancang program Python berbasis terminal
untuk membantu guru atau calon guru matematika merekap nilai
satu kelas.

Pertemuan 14 berfokus pada rancangan proyek.
Implementasi, pengujian, dan dokumentasi hasil dilakukan pada
Pertemuan 15.

Sesuai arahan kelas yang diterima, tugas ini dikerjakan secara
individu dan terpisah dari proyek UAS.

## Status Proyek

Tahap saat ini: perancangan Pertemuan 14.

- Proposal telah disusun.
- Algoritma dan struktur data telah dirancang.
- Pembagian fungsi dan modul telah direncanakan.
- Dua belas test case telah dirancang.
- Implementasi program belum dilakukan.
- Pengujian aktual belum dilakukan.

## Fitur yang Direncanakan

1. Membaca data siswa dari file teks.
2. Memvalidasi format, identitas, dan rentang nilai 0–100.
3. Menghitung jumlah data, rata-rata, minimum, dan maksimum.
4. Menentukan ketuntasan berdasarkan batas 75.
5. Menampilkan dan menyimpan laporan.

Batas 75 adalah asumsi proyek yang ditetapkan dalam proposal.

## Format Data yang Direncanakan

Setiap baris menggunakan format ID,nama,nilai tanpa header.
Nilai desimal menggunakan tanda titik.

Contoh:

```text
A001,Ayu,80
A002,Bima,70
A003,Citra,90
A004,Deni,75
A005,Eka,85

```

Data bersifat fiktif. Baris kosong dilewati.
Baris tidak valid dilaporkan dan tidak ikut dihitung.

## Dokumen Perancangan

- [Proposal proyek](proposal.md): kebutuhan, IPO, pseudocode,
  struktur program, struktur data, tanggung jawab, dan jadwal.
- [Rencana pengujian](tests/test_case.md): dua belas test case
  beserta hasil yang diharapkan.

## Struktur Program yang Direncanakan

| Lokasi | Tanggung Jawab |
|---|---|
| main.py | Mengatur alur utama program. |
| src/input_data.py | Membaca dan memvalidasi data. |
| src/proses.py | Menghitung statistik dan ketuntasan. |
| src/output.py | Menyusun dan menyimpan laporan. |
| data/nilai_contoh.txt | Data siswa fiktif. |
| tests/test_case.md | Rencana dan hasil pengujian. |
| docs/bug_log.md | Catatan bug, perbaikan, dan retest. |
| output/hasil_analisis.txt | Laporan hasil analisis. |

File implementasi dilengkapi pada Pertemuan 15.
Folder kosong belum ditampilkan oleh GitHub.

## Persyaratan dan Rencana Penggunaan

Program direncanakan menggunakan Python 3 dan pustaka standar.
Pengerjaan menggunakan VS Code, Git, dan GitHub.

Setelah implementasi selesai, program dijalankan dari folder
utama proyek melalui terminal PowerShell:

```powershell
py main.py
```

Pada Pertemuan 14, program belum diimplementasikan sehingga
perintah tersebut belum menjadi instruksi untuk program yang siap digunakan.

## Rencana Pengujian

Pengujian mencakup data normal, batas nilai 0 dan 100,
batas ketuntasan 75, input tidak valid, file kosong,
file tidak ditemukan, data campuran, dan penyimpanan laporan.

Hasil aktual serta status PASS/FAIL baru diisi setelah pengujian
dilakukan pada Pertemuan 15.

## Tanggung Jawab Individu

Aulia Citra bertanggung jawab atas perancangan, implementasi,
pengujian, debugging, dokumentasi, dan pengelolaan repositori.

## Referensi dan Bantuan

- Bahan Ajar Pertemuan 14: Perancangan Proyek Program Sederhana,
  Algoritma dan Pemrograman, FKIP Untirta, 2026/2027 Ganjil.
- Bahan Ajar Pertemuan 15: Implementasi, Pengujian, dan Dokumentasi
  Proyek, Algoritma dan Pemrograman, FKIP Untirta, 2026/2027 Ganjil.
- ChatGPT membantu penyusunan rancangan dan panduan praktik.
  Penulis bertanggung jawab mempelajari dan memeriksa hasilnya.