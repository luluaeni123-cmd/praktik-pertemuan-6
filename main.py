
from sistem_informasi.service.mahasiswa_service import (
    tambah_mahasiswa,
    tampilkan_mahasiswa,
    cari_mahasiswa,
    ubah_mahasiswa,
    hapus_mahasiswa
)
from sistem_informasi.utils.format_data import tampilkan_data


if __name__ == "__main__":
    print(tambah_mahasiswa("001", "Lulu", "Sistem Informasi"))
    print(tambah_mahasiswa("002", "Ani", "Informatika"))

    print("\nSemua mahasiswa:")
    tampilkan_data(tampilkan_mahasiswa())

    print("\nCari mahasiswa:")
    print(cari_mahasiswa("001"))

    print("\nUbah data:")
    print(ubah_mahasiswa("001", "Lulu Aeni", "Sistem Informasi"))

    tampilkan_data(tampilkan_mahasiswa())

    print("\nHapus data:")
    print(hapus_mahasiswa("002"))

    print("\nData akhir:")
    tampilkan_data(tampilkan_mahasiswa())
