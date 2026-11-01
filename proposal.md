# Proposal Proyek Individu
# Program Rekap dan Analisis Nilai Matematika

Nama: Aulia Citra
NIM: 2225250012
Kelas: 3F
Program Studi: S1 Pendidikan Matematika FKIP Untirta
Mata Kuliah: Algoritma dan Pemrograman
Semester: 3
Dosen Pengampu: Dr. Aan Hendrayana, S.Si., M.Pd.
Tahun Ajaran: 2026/2027 Ganjil

Proposal ini disusun untuk tugas Pertemuan 14. Implementasi,
pengujian, dan dokumentasi program dilanjutkan pada Pertemuan 15.
Pengerjaan dilakukan secara individu mengikuti arahan kelas.

## 1. Judul Proyek

Program Rekap dan Analisis Nilai Matematika Berbasis Python.

## 2. Latar Belakang

Pengolahan nilai merupakan salah satu kegiatan dalam pembelajaran
matematika. Guru perlu mengetahui rata-rata kelas, nilai terendah,
nilai tertinggi, dan jumlah siswa yang mencapai kriteria ketuntasan.

Perhitungan secara manual perlu dilakukan dengan teliti, terutama
ketika jumlah data bertambah. Kesalahan memasukkan nilai atau
menggunakan pembagi dapat menyebabkan hasil rekap tidak sesuai.

Proyek ini merancang program Python sederhana untuk membaca data
nilai dari file, memeriksa keabsahan data, menghitung statistik,
menentukan ketuntasan, serta menyimpan laporan. Program dijalankan
melalui terminal VS Code.

Materi yang digunakan meliputi variabel, percabangan, perulangan,
fungsi, string, list, dictionary, file I/O, dan penanganan exception.

## 3. Pengguna dan Tujuan

### Pengguna Sasaran

Guru matematika atau calon guru matematika yang membutuhkan
rekap nilai satu kelas.

### Tujuan

1. Membaca data nilai siswa dari file teks.
2. Memastikan data yang diproses memiliki format dan nilai yang valid.
3. Menghitung jumlah data, rata-rata, minimum, dan maksimum.
4. Menentukan status ketuntasan setiap siswa.
5. Menampilkan dan menyimpan laporan hasil analisis.

### Kebutuhan Pengguna

Sebagai calon guru matematika, saya ingin membaca data nilai siswa
dan memperoleh ringkasan hasil belajar agar dapat mengetahui
gambaran nilai kelas serta siswa yang belum mencapai ketuntasan.

## 4. Ruang Lingkup

### Fitur Wajib

| ID | Fitur | Hasil yang Direncanakan |
|---|---|---|
| F01 | Membaca file nilai | Data siswa dibaca dari file teks. |
| F02 | Memvalidasi data | Format salah, identitas kosong, dan nilai di luar 0–100 ditolak dengan pesan. |
| F03 | Menghitung statistik | Jumlah data valid, rata-rata, minimum, dan maksimum diperoleh. |
| F04 | Menentukan ketuntasan | Status setiap siswa serta jumlah tuntas dan belum tuntas diperoleh. |
| F05 | Menampilkan dan menyimpan laporan | Laporan tampil di terminal dan tersimpan dalam file teks. |

### Batasan

1. Program berbasis terminal dan digunakan oleh satu pengguna.
2. Data mewakili satu nilai matematika untuk setiap siswa.
3. File input menggunakan format ID,nama,nilai tanpa baris judul.
4. Nilai berupa angka dalam rentang 0 sampai 100, termasuk kedua batas.
5. Nilai desimal menggunakan tanda titik.
6. Batas ketuntasan proyek ditetapkan 75 sebagai asumsi rancangan,
   bukan ketentuan nilai wajib dari bahan ajar.
7. Nilai >= 75 berstatus Tuntas; nilai < 75 berstatus Belum tuntas.
8. Data contoh bersifat fiktif.
9. Program tidak mencakup GUI, website, database, atau banyak kelas.
10. Grafik dan pengelompokan kategori nilai tidak menjadi fitur wajib.

## 5. Analisis Kebutuhan

### Kebutuhan Fungsional

1. Membaca data/nilai_contoh.txt menggunakan encoding UTF-8.
   Pembacaan direncanakan menggunakan utf-8-sig agar file UTF-8
   dengan maupun tanpa BOM dapat dibaca.
2. Mengabaikan baris kosong.
3. Memisahkan setiap baris menjadi ID, nama, dan nilai.
4. Memeriksa bahwa terdapat tepat tiga bagian.
5. Memeriksa bahwa ID dan nama tidak kosong.
6. Mengonversi nilai menjadi float dan memeriksa rentang 0–100.
7. Melaporkan nomor baris yang tidak valid dan melewatinya.
8. Mengolah seluruh data yang valid.
9. Menampilkan pesan jika file tidak ditemukan.
10. Menampilkan pesan jika tidak terdapat data valid, kemudian
    menghentikan proses tanpa menghitung statistik.
11. Menghitung statistik dan ketuntasan dari data valid.
12. Menyimpan laporan ke output/hasil_analisis.txt.

### Kebutuhan Nonfungsional

1. Program dapat dijalankan menggunakan Python 3 melalui terminal.
2. Program menggunakan pustaka standar Python.
3. Nama variabel dan fungsi mencerminkan kegunaannya.
4. Fungsi input, pengolahan, dan output dipisahkan.
5. Pesan kesalahan menggunakan bahasa yang jelas.
6. File sumber data tidak ditimpa ketika laporan disimpan.
7. Pengujian dapat diulang menggunakan input yang sama.
8. README menjelaskan persyaratan, format data, dan cara menjalankan.

## 6. Input, Process, Output

| Komponen | Rancangan |
|---|---|
| Input | File data/nilai_contoh.txt berisi ID,nama,nilai dan konstanta batas ketuntasan 75. |
| Process | Membaca baris, membersihkan spasi, memvalidasi format dan nilai, menyimpan data valid, menghitung statistik, serta menentukan ketuntasan. |
| Output | Pesan validasi, laporan terminal, dan file output/hasil_analisis.txt. |

### Contoh Input

A001,Ayu,80
A002,Bima,70
A003,Citra,90
A004,Deni,75
A005,Eka,85

### Hasil yang Diharapkan

Jumlah data valid: 5
Rata-rata: 80.00
Nilai minimum: 70.00
Nilai maksimum: 90.00
Batas ketuntasan: 75.00
Jumlah tuntas: 4
Jumlah belum tuntas: 1

Laporan juga memuat ID, nama, nilai, dan status setiap siswa.

Perhitungan rata-rata:
(80 + 70 + 90 + 75 + 85) / 5 = 400 / 5 = 80.

Hasil tersebut merupakan target rancangan dan belum menjadi
klaim hasil pengujian aktual pada Pertemuan 14.

## 7. Rancangan Algoritma

### Pseudocode

MULAI
    Tetapkan batas ketuntasan = 75
    Tetapkan lokasi file input dan file laporan

    COBA membaca file input
    JIKA file tidak ditemukan
        Tampilkan pesan file tidak ditemukan
        SELESAI

    Siapkan list data valid dan list pesan kesalahan

    UNTUK setiap baris dalam file
        Bersihkan spasi dan karakter akhir baris

        JIKA baris kosong
            Lanjutkan ke baris berikutnya

        Pisahkan baris menggunakan koma

        JIKA jumlah bagian bukan tiga
            Catat pesan kesalahan beserta nomor baris
            Lanjutkan ke baris berikutnya

        Ambil ID, nama, dan teks nilai
        Bersihkan spasi pada masing-masing bagian

        JIKA ID atau nama kosong
            Catat pesan kesalahan
            Lanjutkan ke baris berikutnya

        COBA konversi teks nilai menjadi float
        JIKA konversi gagal
            Catat pesan nilai harus berupa angka
            Lanjutkan ke baris berikutnya

        JIKA nilai tidak berada dalam rentang 0 sampai 100
            Catat pesan nilai di luar rentang
            Lanjutkan ke baris berikutnya

        Simpan ID, nama, dan nilai ke list data valid

    Tampilkan pesan kesalahan data jika ada

    JIKA list data valid kosong
        Tampilkan pesan tidak ada data valid
        SELESAI

    Ambil seluruh nilai dari data valid
    Hitung jumlah, rata-rata, minimum, dan maksimum

    UNTUK setiap siswa
        JIKA nilai >= batas ketuntasan
            Tentukan status Tuntas
        SELAIN ITU
            Tentukan status Belum tuntas

    Hitung jumlah tuntas dan belum tuntas
    Susun laporan
    Tampilkan laporan

    COBA simpan laporan ke file output
    JIKA penyimpanan gagal
        Tampilkan pesan kegagalan penyimpanan
    SELAIN ITU
        Tampilkan lokasi laporan yang berhasil disimpan
SELESAI

### Penanganan Kondisi Khusus

| Kondisi | Tindakan |
|---|---|
| File tidak ditemukan | Menangani FileNotFoundError dan menampilkan pesan. |
| Teks nilai bukan angka | Menangani ValueError, melaporkan baris, dan melewatinya. |
| Format atau identitas tidak valid | Melaporkan baris dan melewatinya. |
| Nilai di luar rentang | Menolak baris tersebut. |
| File kosong atau seluruh data tidak valid | Menghentikan pengolahan sebelum pembagian dan pencarian minimum/maksimum. |
| Laporan gagal disimpan | Menangani OSError pada proses penyimpanan dan menampilkan pesan. |

## 8. Struktur Program

### Rancangan File dan Folder

| Lokasi | Tanggung Jawab |
|---|---|
| main.py | Mengatur urutan input, proses, dan output. |
| src/__init__.py | Menandai src sebagai package Python. |
| src/input_data.py | Membaca file dan memvalidasi setiap baris. |
| src/proses.py | Menghitung statistik dan menentukan ketuntasan. |
| src/output.py | Menyusun, menampilkan, dan menyimpan laporan. |
| data/nilai_contoh.txt | Menyimpan data siswa fiktif. |
| tests/test_case.md | Mencatat rencana dan hasil pengujian. |
| docs/bug_log.md | Mencatat bug nyata, penyebab, perbaikan, dan retest. |
| output/.gitkeep | Mempertahankan folder output di Git ketika belum berisi laporan. |
| output/hasil_analisis.txt | Menyimpan laporan setelah implementasi dijalankan. |
| proposal.md | Menjelaskan rancangan proyek Pertemuan 14. |
| README.md | Menjelaskan proyek dan petunjuk penggunaan. |
| .gitignore | Mengabaikan file sementara dan pengaturan lokal. |

Struktur ini merupakan adaptasi rancangan modular untuk proyek
individu. File implementasi akan dilengkapi pada Pertemuan 15.

### Rancangan Fungsi

| Fungsi | Parameter | Hasil atau Efek |
|---|---|---|
| validasi_nilai(nilai) | Nilai numerik | Boolean yang menunjukkan apakah nilai berada dalam rentang 0–100. |
| baca_data(path) | Lokasi file input | List dictionary data valid dan list pesan kesalahan. |
| tentukan_status(nilai, batas) | Nilai siswa dan batas ketuntasan | String Tuntas atau Belum tuntas. |
| hitung_statistik(data, batas) | Data valid dan batas ketuntasan | Dictionary ringkasan statistik dan jumlah ketuntasan. |
| buat_laporan(data, hasil, batas) | Data siswa, ringkasan, dan batas | String laporan. |
| simpan_laporan(teks, path) | String laporan dan lokasi output | Menulis laporan ke file. |
| main() | Tidak ada | Menjalankan alur utama dan menangani kesalahan file yang relevan. |

Laporan direncanakan ditulis dengan mode w karena mewakili hasil
analisis terbaru. File output berbeda dari file input.

## 9. Struktur Data

### List Berisi Dictionary

Contoh data valid:

[
    {"id": "A001", "nama": "Ayu", "nilai": 80.0},
    {"id": "A002", "nama": "Bima", "nilai": 70.0}
]

List digunakan untuk menyimpan kumpulan siswa yang akan diproses
secara berurutan. Dictionary digunakan agar atribut setiap siswa
dapat diakses melalui key yang jelas.

### List Nilai Numerik

Contoh:

[80.0, 70.0, 90.0, 75.0, 85.0]

List ini digunakan untuk perhitungan sum(), len(), min(), dan max().

### Dictionary Ringkasan

Contoh rancangan:

{
    "jumlah": 5,
    "rata_rata": 80.0,
    "minimum": 70.0,
    "maksimum": 90.0,
    "tuntas": 4,
    "belum_tuntas": 1
}

Dictionary memudahkan pengambilan hasil berdasarkan nama informasi.

### String dan List Pesan

String digunakan untuk menyusun laporan.
List string digunakan untuk menyimpan pesan kesalahan tiap baris.

## 10. Rencana Pengujian

Pengujian dirancang sebelum implementasi lengkap. Hasil aktual
dan status PASS/FAIL baru diisi setelah program dijalankan.

| ID | Jenis | Input atau Kondisi | Expected Result |
|---|---|---|---|
| TC01 | Normal | Nilai 80, 70, 90, 75, 85 | Jumlah 5; rata-rata 80; minimum 70; maksimum 90; tuntas 4; belum tuntas 1. |
| TC02 | Batas bawah | Satu siswa dengan nilai 0 | Data valid; rata-rata, minimum, dan maksimum 0; belum tuntas 1. |
| TC03 | Batas atas | Satu siswa dengan nilai 100 | Data valid; rata-rata, minimum, dan maksimum 100; tuntas 1. |
| TC04 | Batas ketuntasan | Nilai 74, 75, 76 | Status berurutan Belum tuntas, Tuntas, Tuntas; rata-rata 75. |
| TC05 | Invalid rentang | Nilai -1 dan 105 | Kedua baris ditolak; pesan kesalahan tampil; tidak ada penghitungan statistik. |
| TC06 | Invalid tipe | Nilai abc | Baris ditolak dengan pesan nilai harus berupa angka. |
| TC07 | Invalid format | Baris A001,Ayu | Baris ditolak karena tidak memiliki tiga bagian. |
| TC08 | Kosong | File kosong | Pesan tidak ada data valid; tidak terjadi pembagian dengan nol. |
| TC09 | File | Lokasi file tidak ditemukan | Pesan file tidak ditemukan; tidak ada traceback yang tidak ditangani. |
| TC10 | Campuran | Satu baris nilai 80, satu baris abc, dan satu baris kosong | Hanya nilai 80 diproses; baris abc dilaporkan; baris kosong dilewati. |
| TC11 | Penyimpanan | Data normal dan lokasi output dapat ditulis | Laporan tersimpan dan isinya sesuai laporan terminal. |
| TC12 | Invalid identitas | Baris A001,,80 | Baris ditolak karena nama kosong. |

Pengujian fungsi inti juga direncanakan menggunakan assert.
Setelah perbaikan bug, test yang gagal dan test terkait yang telah
lulus dijalankan kembali untuk memeriksa regresi.

## 11. Pembagian Tugas dan Tanggung Jawab Individu

Seluruh pekerjaan dilaksanakan oleh Aulia Citra, NIM 2225250012,
sesuai arahan bahwa tugas Pertemuan 14–15 bersifat individu.

| Pekerjaan | Penanggung Jawab | Bukti yang Direncanakan |
|---|---|---|
| Analisis masalah dan kebutuhan | Aulia Citra | Proposal |
| Perancangan algoritma dan data | Aulia Citra | Pseudocode dan rancangan struktur data |
| Implementasi input dan validasi | Aulia Citra | src/input_data.py |
| Implementasi pengolahan | Aulia Citra | src/proses.py |
| Implementasi laporan dan integrasi | Aulia Citra | src/output.py dan main.py |
| Pengujian dan debugging | Aulia Citra | Test case dan bug log |
| Dokumentasi dan pengelolaan GitHub | Aulia Citra | README dan commit history |

Bantuan dokumentasi maupun AI yang digunakan dicantumkan pada
README. Penulis tetap bertanggung jawab memahami dan menjelaskan
algoritma, fungsi, pengujian, serta hasil program.

## 12. Jadwal Pengerjaan

| Tahap | Waktu | Target |
|---|---|---|
| Perancangan | Pertemuan 14 | Proposal, algoritma, struktur data, struktur program, dan rencana test case. |
| Persiapan implementasi | Setelah rancangan selesai | Menyiapkan data contoh serta file program. |
| Implementasi | Pertemuan 15 | Seluruh fitur wajib terintegrasi. |
| Pengujian dan perbaikan | Pertemuan 15 | Test dijalankan, hasil aktual dicatat, dan bug ditangani. |
| Dokumentasi dan pengumpulan | Akhir pengerjaan Pertemuan 15 | README lengkap, commit dan push, serta pemeriksaan repositori. |
| Evaluasi akhir | Sebelum Pertemuan 16 | Memastikan hasil tugas dapat dijalankan ulang dan dijelaskan; pengaturan UAS mengikuti arahan kelas tersendiri. |

Tugas individu Pertemuan 14–15 ini dipisahkan dari proyek UAS
mengikuti informasi kelas yang diterima.

## 13. Repositori GitHub

Nama repositori yang direncanakan:

proyek-analisis-nilai-2225250012

Akun GitHub:

citra137

URL yang direncanakan:

https://github.com/citra137/proyek-analisis-nilai-2225250012

Status saat proposal disusun: repositori belum dibuat dan URL
belum diverifikasi. Bagian ini diperbarui setelah repositori aktif.

Riwayat pengerjaan akan dicatat secara bertahap melalui commit
yang menjelaskan perubahan, misalnya docs, feat, test, dan fix.

## Referensi dan Bantuan

1. Bahan Ajar Pertemuan 14: Perancangan Proyek Program Sederhana,
   mata kuliah Algoritma dan Pemrograman, FKIP Untirta, 2026/2027 Ganjil.
2. Bahan Ajar Pertemuan 15: Implementasi, Pengujian, dan Dokumentasi
   Proyek, mata kuliah Algoritma dan Pemrograman, FKIP Untirta,
   2026/2027 Ganjil.
3. Bantuan ChatGPT digunakan untuk membantu penyusunan rancangan
   dan panduan praktik. Rancangan diperiksa dan dipelajari kembali
   oleh penulis sebelum implementasi.