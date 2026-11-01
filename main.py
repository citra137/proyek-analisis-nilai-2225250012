from pathlib import Path

from src.input_data import baca_data
from src.proses import BATAS_KETUNTASAN, hitung_statistik
from src.output import buat_laporan, simpan_laporan


def main():
    """Menjalankan pembacaan, analisis, dan penyimpanan laporan."""
    folder_proyek = Path(__file__).resolve().parent
    file_input = folder_proyek / "data" / "nilai_contoh.txt"
    file_output = folder_proyek / "output" / "hasil_analisis.txt"

    try:
        data, pesan_error = baca_data(file_input)
    except FileNotFoundError:
        print("File tidak ditemukan:", file_input)
        return
    except OSError as error:
        print("File input tidak dapat dibaca:", error)
        return

    for pesan in pesan_error:
        print(pesan)

    if not data:
        print("Tidak ada data valid untuk diproses.")
        return

    hasil = hitung_statistik(data, BATAS_KETUNTASAN)
    laporan = buat_laporan(data, hasil, BATAS_KETUNTASAN)

    print(laporan, end="")

    try:
        file_output.parent.mkdir(parents=True, exist_ok=True)
        simpan_laporan(laporan, file_output)
    except OSError as error:
        print("Laporan gagal disimpan:", error)
    else:
        print("\nLaporan berhasil disimpan:", file_output)


if __name__ == "__main__":
    main()