from pathlib import Path
from tempfile import TemporaryDirectory

from src.input_data import baca_data
from src.proses import hitung_statistik, tentukan_status
from src.output import buat_laporan, simpan_laporan


def siapkan_data(folder, teks):
    """Membuat file sementara lalu membacanya."""
    path = folder / "nilai_uji.txt"
    path.write_text(teks, encoding="utf-8-sig")
    return baca_data(path)


def jalankan_pengujian():
    with TemporaryDirectory() as lokasi:
        folder = Path(lokasi)

        # TC01: data normal.
        data, pesan = siapkan_data(
            folder,
            "A001,Ayu,80\n"
            "A002,Bima,70\n"
            "A003,Citra,90\n"
            "A004,Deni,75\n"
            "A005,Eka,85\n"
        )
        hasil = hitung_statistik(data)
        assert not pesan
        assert hasil == {
            "jumlah": 5,
            "rata_rata": 80.0,
            "minimum": 70.0,
            "maksimum": 90.0,
            "tuntas": 4,
            "belum_tuntas": 1
        }
        print("TC01 PASS | Normal: jumlah 5, rata-rata 80, tuntas 4")

        # TC02: batas bawah.
        data, pesan = siapkan_data(folder, "A001,Ayu,0\n")
        hasil = hitung_statistik(data)
        assert not pesan
        assert hasil["jumlah"] == 1
        assert hasil["rata_rata"] == 0
        assert hasil["minimum"] == 0
        assert hasil["maksimum"] == 0
        assert hasil["belum_tuntas"] == 1
        print("TC02 PASS | Nilai 0 diterima, belum tuntas")

        # TC03: batas atas.
        data, pesan = siapkan_data(folder, "A001,Ayu,100\n")
        hasil = hitung_statistik(data)
        assert not pesan
        assert hasil["jumlah"] == 1
        assert hasil["rata_rata"] == 100
        assert hasil["minimum"] == 100
        assert hasil["maksimum"] == 100
        assert hasil["tuntas"] == 1
        print("TC03 PASS | Nilai 100 diterima, tuntas")

        # TC04: batas ketuntasan.
        data, pesan = siapkan_data(
            folder, "A001,Ayu,74\nA002,Bima,75\nA003,Citra,76\n"
        )
        status = []
        for siswa in data:
            status.append(tentukan_status(siswa["nilai"]))
        assert not pesan
        assert status == ["Belum tuntas", "Tuntas", "Tuntas"]
        assert hitung_statistik(data)["rata_rata"] == 75
        print("TC04 PASS | 74 belum tuntas; 75 dan 76 tuntas")

        # TC05: nilai di luar rentang.
        data, pesan = siapkan_data(
            folder, "A001,Ayu,-1\nA002,Bima,105\n"
        )
        assert data == []
        assert len(pesan) == 2
        assert all("antara 0 dan 100" in teks for teks in pesan)
        print("TC05 PASS | Nilai -1 dan 105 ditolak")

        # TC06: nilai bukan angka.
        data, pesan = siapkan_data(folder, "A001,Ayu,abc\n")
        assert data == []
        assert len(pesan) == 1
        assert "harus berupa angka" in pesan[0]
        print("TC06 PASS | Nilai abc ditolak dengan pesan")

        # TC07: format tidak lengkap.
        data, pesan = siapkan_data(folder, "A001,Ayu\n")
        assert data == []
        assert len(pesan) == 1
        assert "format harus" in pesan[0]
        print("TC07 PASS | Format dua bagian ditolak")

        # TC08: file kosong.
        data, pesan = siapkan_data(folder, "")
        assert data == []
        assert pesan == []
        assert hitung_statistik(data)["jumlah"] == 0
        print("TC08 PASS | Data kosong ditangani tanpa pembagian nol")

        # TC09: file tidak ditemukan pada fungsi pembaca.
        try:
            baca_data(folder / "tidak_ada.txt")
        except FileNotFoundError:
            print("TC09 PASS | FileNotFoundError dapat dikenali")
        else:
            raise AssertionError("File hilang seharusnya memicu FileNotFoundError")

        # TC10: data valid, invalid, dan baris kosong.
        data, pesan = siapkan_data(
            folder, "A001,Ayu,80\nA002,Bima,abc\n\n"
        )
        hasil = hitung_statistik(data)
        assert len(pesan) == 1
        assert hasil["jumlah"] == 1
        assert hasil["rata_rata"] == 80
        assert hasil["tuntas"] == 1
        print("TC10 PASS | Hanya data valid diproses")

        # TC11: penyimpanan laporan dan perlindungan file input.
        teks_input = (
            "A001,Ayu,80\nA002,Bima,70\nA003,Citra,90\n"
            "A004,Deni,75\nA005,Eka,85\n"
        )
        data, pesan = siapkan_data(folder, teks_input)
        hasil = hitung_statistik(data)
        laporan = buat_laporan(data, hasil, 75)
        path_laporan = folder / "hasil_uji.txt"
        simpan_laporan(laporan, path_laporan)
        assert path_laporan.read_text(encoding="utf-8") == laporan
        assert "Rata-rata: 80.00" in laporan
        assert (folder / "nilai_uji.txt").read_text(
            encoding="utf-8-sig"
        ) == teks_input
        print("TC11 PASS | Laporan tersimpan, file input tetap")

        # TC12: nama kosong.
        data, pesan = siapkan_data(folder, "A001,,80\n")
        assert data == []
        assert len(pesan) == 1
        assert "tidak boleh kosong" in pesan[0]
        print("TC12 PASS | Nama kosong ditolak")

    print("\nSelesai: 12 pengujian fungsi PASS.")
    print("Penanganan pesan pada main.py akan diperiksa terpisah.")


if __name__ == "__main__":
    jalankan_pengujian()