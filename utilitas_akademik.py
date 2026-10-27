
def hitung_ipk(nilai_list):
    if not nilai_list:
        return 0.0

    return sum(nilai_list) / len(nilai_list)


def konversi_nilai_huruf(nilai):
    if nilai >= 85:
        return "A"
    elif nilai >= 75:
        return "B"
    elif nilai >= 65:
        return "C"
    elif nilai >= 50:
        return "D"
    else:
        return "E"


def generate_transkrip(nama, nim, nilai_list):
    ipk = hitung_ipk(nilai_list)

    transkrip = {
        "nama": nama,
        "nim": nim,
        "nilai": nilai_list,
        "ipk": round(ipk, 2),
        "nilai_huruf": [
            konversi_nilai_huruf(nilai)
            for nilai in nilai_list
        ]
    }

    return transkrip


if __name__ == "__main__":
    print("Testing module utilitas akademik")
    print("IPK:", hitung_ipk([85, 90, 80]))
