# Catatan Pengujian dan Bug

Nama: Aulia Citra
NIM: 2225250012

## Status Bug

Pada pengujian yang telah dijalankan, belum ditemukan bug yang
menyebabkan hasil berbeda dari expected result.

Tidak ada bug atau proses perbaikan yang direkayasa untuk
mengisi catatan ini.

## Kondisi yang Diperiksa

| Kondisi | Risiko | Penanganan | Hasil |
|---|---|---|---|
| File kosong | Pembagian nol atau pencarian minimum/maksimum pada data kosong. | Program utama menghentikan proses jika tidak ada data valid. Fungsi statistik juga memeriksa data kosong. | PASS |
| File tidak ditemukan | Program berhenti dengan traceback. | FileNotFoundError ditangani dalam main(). | PASS |
| Nilai bukan angka | Konversi float gagal. | ValueError ditangani per baris dan data dilewati. | PASS |
| Nilai di luar 0–100 | Statistik memakai nilai tidak valid. | Pemeriksaan rentang menolak baris tersebut. | PASS |
| Nilai tepat 75 | Salah menentukan ketuntasan. | Operator >= memasukkan nilai 75 sebagai Tuntas. | PASS |

Penanganan tersebut sudah tersedia pada implementasi awal.
Tabel ini mencatat hasil pengujian penanganan kondisi khusus,
bukan riwayat bug yang ditemukan lalu diperbaiki.

## Known Issues dan Batasan

1. Nama siswa tidak boleh mengandung koma karena format input
   menggunakan pemisah koma dengan tepat tiga bagian.
2. ID siswa ganda belum diperiksa. Setiap baris valid dihitung
   sebagai satu data.
3. Jika file input hilang atau tidak ada data valid, laporan
   sebelumnya tetap tersimpan. Laporan lama bukan hasil proses
   yang gagal tersebut.
4. Kegagalan izin baca dan tulis belum disimulasikan.

## Tindak Lanjut Jika Ditemukan Bug

Catat input pemicu, expected, actual, lokasi kode, penyebab,
perbaikan minimal, hasil retest, dan pemeriksaan regresi.