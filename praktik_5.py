
import requests
import json


def main():
    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url, timeout=15)
    response.raise_for_status()

    data = response.json()

    # Mengambil nama dan email menggunakan map dan lambda
    pengguna = list(map(
        lambda user: {
            "nama": user["name"],
            "email": user["email"],
            "kota": user["address"]["city"]
        },
        data
    ))

    # Menyaring pengguna berdasarkan kota yang mengandung huruf a
    hasil_filter = list(filter(
        lambda user: "a" in user["kota"].lower(),
        pengguna
    ))

    # Mengurutkan berdasarkan nama
    hasil_urut = sorted(
        hasil_filter,
        key=lambda user: user["nama"]
    )

    # Menyimpan hasil ke file JSON
    with open("hasil_pengguna.json", "w", encoding="utf-8") as file:
        json.dump(hasil_urut, file, indent=4, ensure_ascii=False)

    print("Jumlah data API:", len(data))
    print("Jumlah data setelah filter:", len(hasil_urut))
    print("Hasil:")
    print(json.dumps(hasil_urut, indent=4, ensure_ascii=False))
    print("\nData berhasil disimpan ke hasil_pengguna.json")


if __name__ == "__main__":
    try:
        main()
    except requests.RequestException as error:
        print("Gagal mengambil data API:", error)
    except (KeyError, ValueError) as error:
        print("Terjadi kesalahan dalam pengolahan data:", error)
