
class Mahasiswa:
    def __init__(self, nim, nama, jurusan):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan

    def to_dict(self):
        return {
            "nim": self.nim,
            "nama": self.nama,
            "jurusan": self.jurusan
        }
