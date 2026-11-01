BATAS_KETUNTASAN = 75


def tentukan_status(nilai, batas=BATAS_KETUNTASAN):
    """Menentukan ketuntasan berdasarkan batas yang digunakan."""
    if nilai >= batas:
        return "Tuntas"
    return "Belum tuntas"


def hitung_statistik(data, batas=BATAS_KETUNTASAN):
    """Menghitung statistik dan jumlah ketuntasan data siswa."""
    if not data:
        return {
            "jumlah": 0,
            "rata_rata": 0,
            "minimum": None,
            "maksimum": None,
            "tuntas": 0,
            "belum_tuntas": 0
        }

    daftar_nilai = []
    jumlah_tuntas = 0

    for siswa in data:
        daftar_nilai.append(siswa["nilai"])

        if tentukan_status(siswa["nilai"], batas) == "Tuntas":
            jumlah_tuntas += 1

    jumlah = len(daftar_nilai)

    return {
        "jumlah": jumlah,
        "rata_rata": sum(daftar_nilai) / jumlah,
        "minimum": min(daftar_nilai),
        "maksimum": max(daftar_nilai),
        "tuntas": jumlah_tuntas,
        "belum_tuntas": jumlah - jumlah_tuntas
    }