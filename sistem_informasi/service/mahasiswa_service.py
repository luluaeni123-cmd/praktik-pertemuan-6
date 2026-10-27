
from sistem_informasi.model.mahasiswa import Mahasiswa

database = {}


def tambah_mahasiswa(nim, nama, jurusan):
    if nim in database:
        return "NIM sudah terdaftar"

    mahasiswa = Mahasiswa(nim, nama, jurusan)
    database[nim] = mahasiswa.to_dict()
    return "Mahasiswa berhasil ditambahkan"


def tampilkan_mahasiswa():
    return list(database.values())


def cari_mahasiswa(nim):
    return database.get(nim)


def ubah_mahasiswa(nim, nama, jurusan):
    if nim not in database:
        return "Mahasiswa tidak ditemukan"

    database[nim]["nama"] = nama
    database[nim]["jurusan"] = jurusan
    return "Data mahasiswa berhasil diubah"


def hapus_mahasiswa(nim):
    if nim not in database:
        return "Mahasiswa tidak ditemukan"

    del database[nim]
    return "Data mahasiswa berhasil dihapus"
