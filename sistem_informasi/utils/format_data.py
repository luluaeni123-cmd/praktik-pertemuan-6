
def tampilkan_data(data):
    if not data:
        print("Belum ada data mahasiswa")
        return

    for mahasiswa in data:
        print(
            f"NIM: {mahasiswa['nim']} | "
            f"Nama: {mahasiswa['nama']} | "
            f"Jurusan: {mahasiswa['jurusan']}"
        )
