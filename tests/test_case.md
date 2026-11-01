# Rencana Pengujian Program Analisis Nilai

Nama: Aulia Citra
NIM: 2225250012
Kelas: 3F

## Tujuan

Memeriksa pembacaan data, validasi, perhitungan statistik,
ketuntasan, dan penyimpanan laporan sesuai proposal.

Batas ketuntasan yang digunakan dalam proyek adalah 75.
Format setiap baris file input: ID,nama,nilai.

## Rencana Test Case

| ID | Jenis | Input atau Kondisi | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| TC01 | Normal | Nilai 80, 70, 90, 75, 85 dengan identitas valid | Jumlah 5; rata-rata 80; minimum 70; maksimum 90; tuntas 4; belum tuntas 1. | Belum dijalankan | Belum diuji |
| TC02 | Boundary | Satu siswa dengan nilai 0 | Nilai diterima; rata-rata, minimum, dan maksimum 0; belum tuntas 1. | Belum dijalankan | Belum diuji |
| TC03 | Boundary | Satu siswa dengan nilai 100 | Nilai diterima; rata-rata, minimum, dan maksimum 100; tuntas 1. | Belum dijalankan | Belum diuji |
| TC04 | Boundary | Nilai 74, 75, 76 | Status berurutan Belum tuntas, Tuntas, Tuntas; rata-rata 75. | Belum dijalankan | Belum diuji |
| TC05 | Invalid | Nilai -1 dan 105 | Kedua baris ditolak dengan pesan; tidak ada data valid untuk dihitung. | Belum dijalankan | Belum diuji |
| TC06 | Invalid | A001,Ayu,abc | Baris ditolak; pesan nilai harus berupa angka ditampilkan. | Belum dijalankan | Belum diuji |
| TC07 | Invalid | A001,Ayu | Baris ditolak karena jumlah bagian bukan tiga. | Belum dijalankan | Belum diuji |
| TC08 | Empty | File input kosong | Pesan tidak ada data valid; tidak terjadi pembagian dengan nol. | Belum dijalankan | Belum diuji |
| TC09 | File | Lokasi file input tidak ditemukan | Pesan file tidak ditemukan; program berhenti tanpa traceback yang tidak ditangani. | Belum dijalankan | Belum diuji |
| TC10 | Campuran | A001,Ayu,80; A002,Bima,abc; dan satu baris kosong | Hanya Ayu diproses; rata-rata 80; tuntas 1; baris abc dilaporkan dan baris kosong dilewati. | Belum dijalankan | Belum diuji |
| TC11 | Output | Data TC01 dan lokasi output dapat ditulis | File output/hasil_analisis.txt berisi laporan yang sesuai dengan laporan terminal. | Belum dijalankan | Belum diuji |
| TC12 | Invalid | A001,,80 | Baris ditolak dengan pesan nama tidak boleh kosong. | Belum dijalankan | Belum diuji |

Untuk TC10, setiap data ditempatkan pada baris tersendiri.
Tanda titik koma pada tabel hanya memisahkan uraian baris.

## Prosedur Pengujian pada Pertemuan 15

1. Siapkan data sesuai test case menggunakan data fiktif.
2. Jalankan program dari folder utama proyek.
3. Bandingkan hasil aktual dengan expected result.
4. Catat hasil aktual sesuai pengamatan.
5. Beri status PASS jika hasil sesuai, atau FAIL jika berbeda.
6. Catat bug yang ditemukan dalam docs/bug_log.md.
7. Perbaiki bug dan jalankan kembali test yang gagal.
8. Jalankan kembali test terkait yang sebelumnya PASS untuk
   memeriksa kemungkinan regresi.
9. Kembalikan data contoh normal setelah pengujian selesai.

## Kriteria Keberhasilan

- Seluruh fitur wajib sesuai proposal.
- Nilai 0 dan 100 diterima.
- Nilai tepat 75 berstatus Tuntas.
- Data tidak valid dilaporkan dan tidak ikut dihitung.
- File kosong dan file tidak ditemukan ditangani.
- Statistik hanya menggunakan data valid.
- Laporan dapat ditampilkan dan disimpan.
- Minimal lima test case benar-benar dijalankan pada Pertemuan 15.

## Status Pertemuan 14

Dokumen ini berisi rencana pengujian.
Program belum diimplementasikan dan hasil aktual belum tersedia.