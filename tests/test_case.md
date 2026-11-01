# Hasil Pengujian Program Analisis Nilai

Nama: Aulia Citra
NIM: 2225250012
Kelas: 3F

## Lingkungan dan Cara Pengujian

Pengujian dilakukan pada Windows, PowerShell di VS Code,
dan Python 3.14.7. Batas ketuntasan proyek adalah 75.

Jalankan dari folder utama:

```powershell
py main.py
py -m tests.uji_program
```

Pengujian fungsi menggunakan assert dan file sementara.
Hasil berikut dicatat berdasarkan pengujian yang dijalankan.

## Tabel Hasil Pengujian

| ID | Input/Kondisi | Expected | Actual | Status |
|---|---|---|---|---|
| TC01 | Nilai 80,70,90,75,85 | Jumlah 5; rata-rata 80; min 70; max 90; tuntas 4; belum tuntas 1. | Seluruh hasil sesuai expected. | PASS |
| TC02 | Nilai 0 | Diterima; statistik 0; belum tuntas 1. | Sesuai expected. | PASS |
| TC03 | Nilai 100 | Diterima; statistik 100; tuntas 1. | Sesuai expected. | PASS |
| TC04 | Nilai 74,75,76 | Belum tuntas, Tuntas, Tuntas; rata-rata 75. | Sesuai expected. | PASS |
| TC05 | Nilai -1 dan 105 | Dua baris ditolak dengan pesan rentang. | Data kosong dan dua pesan rentang. | PASS |
| TC06 | A001,Ayu,abc | Ditolak dengan pesan nilai harus berupa angka. | Sesuai expected. | PASS |
| TC07 | A001,Ayu | Ditolak dengan pesan format. | Sesuai expected. | PASS |
| TC08 | File kosong | Program utama menampilkan pesan tidak ada data valid tanpa pembagian nol. | Pesan tampil; fungsi statistik juga aman untuk data kosong. | PASS |
| TC09 | File hilang | Program utama menangani FileNotFoundError dengan pesan tanpa traceback. | Pesan file tidak ditemukan tampil tanpa traceback. | PASS |
| TC10 | Nilai 80, abc, dan baris kosong | Hanya nilai 80 diproses; tuntas 1; satu pesan error. | Sesuai expected. | PASS |
| TC11 | Simpan laporan | Isi file sama dengan string laporan dan input tetap. | Kedua pemeriksaan berhasil. | PASS |
| TC12 | A001,,80 | Ditolak dengan pesan identitas kosong. | Sesuai expected. | PASS |

## Pengujian Program Utama

Selain pengujian fungsi, main.py dijalankan langsung untuk:
1. Data normal.
2. File kosong.
3. File tidak ditemukan.
4. Data normal setelah file dikembalikan.

File kosong menghasilkan:
Tidak ada data valid untuk diproses.

File hilang menghasilkan:
File tidak ditemukan: diikuti lokasi file.

Setelah data normal dikembalikan, hasilnya:
- Jumlah data valid: 5.
- Rata-rata: 80.00.
- Minimum: 70.00.
- Maksimum: 90.00.
- Tuntas: 4.
- Belum tuntas: 1.

## Pengujian Ulang dan Clone

Seluruh dua belas pengujian fungsi dijalankan ulang dan tetap PASS.
Tidak ada perubahan kode di antara pengujian ulang tersebut.

Repositori juga di-clone ke folder pemeriksaan terpisah.
Program utama berhasil dijalankan, dua belas pengujian PASS,
dan git status menunjukkan working tree clean.

## Batas Pengujian

Kegagalan izin baca/tulis belum disimulasikan.
Hasil PASS berlaku untuk pemeriksaan yang dicatat di atas.

Catatan penanganan kondisi khusus dan batasan program tersedia
dalam docs/bug_log.md. Belum ditemukan bug pada kasus yang diuji;
tidak ada riwayat perbaikan bug yang direkayasa.