def validasi_nilai(nilai):
    """Memeriksa apakah nilai berada dalam rentang 0 sampai 100."""
    return 0 <= nilai <= 100


def baca_data(path):
    """Membaca data siswa dan mengembalikan data valid serta pesan error."""
    data = []
    pesan_error = []

    with open(path, "r", encoding="utf-8-sig") as file:
        for nomor_baris, baris in enumerate(file, start=1):
            baris = baris.strip()

            if not baris:
                continue

            bagian = baris.split(",")

            if len(bagian) != 3:
                pesan_error.append(
                    f"Baris {nomor_baris}: format harus ID,nama,nilai."
                )
                continue

            id_siswa = bagian[0].strip()
            nama = bagian[1].strip()
            teks_nilai = bagian[2].strip()

            if not id_siswa or not nama:
                pesan_error.append(
                    f"Baris {nomor_baris}: ID dan nama tidak boleh kosong."
                )
                continue

            try:
                nilai = float(teks_nilai)
            except ValueError:
                pesan_error.append(
                    f"Baris {nomor_baris}: nilai harus berupa angka."
                )
                continue

            if not validasi_nilai(nilai):
                pesan_error.append(
                    f"Baris {nomor_baris}: nilai harus antara 0 dan 100."
                )
                continue

            data.append({
                "id": id_siswa,
                "nama": nama,
                "nilai": nilai
            })

    return data, pesan_error