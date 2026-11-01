from src.proses import tentukan_status


def buat_laporan(data, hasil, batas):
    """Menyusun rincian siswa dan ringkasan dalam bentuk teks."""
    baris = [
        "REKAP DAN ANALISIS NILAI MATEMATIKA",
        "=" * 50,
        "",
        "DAFTAR NILAI SISWA"
    ]

    for siswa in data:
        status = tentukan_status(siswa["nilai"], batas)
        baris.append(
            f'{siswa["id"]} | {siswa["nama"]} | '
            f'{siswa["nilai"]:.2f} | {status}'
        )

    baris.extend([
        "",
        "RINGKASAN",
        f'Jumlah data valid: {hasil["jumlah"]}',
        f'Rata-rata: {hasil["rata_rata"]:.2f}',
        f'Nilai minimum: {hasil["minimum"]:.2f}',
        f'Nilai maksimum: {hasil["maksimum"]:.2f}',
        f"Batas ketuntasan: {batas:.2f}",
        f'Jumlah tuntas: {hasil["tuntas"]}',
        f'Jumlah belum tuntas: {hasil["belum_tuntas"]}'
    ])

    return "\n".join(baris) + "\n"


def simpan_laporan(teks, path):
    """Menyimpan laporan terbaru tanpa mengubah file input."""
    with open(path, "w", encoding="utf-8") as file:
        file.write(teks)