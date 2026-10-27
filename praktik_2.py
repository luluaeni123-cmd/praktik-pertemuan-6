
def validasi_data(data, schema, *args, **kwargs):
    errors = []

    for nama_field, aturan in schema.items():
        if nama_field not in data:
            errors.append(f"{nama_field} wajib diisi")
            continue

        nilai = data[nama_field]
        tipe = aturan.get("type")

        if tipe is not None:
            if tipe is int and isinstance(nilai, bool):
                errors.append(f"{nama_field} harus bertipe int")
                continue

            if not isinstance(nilai, tipe):
                errors.append(f"{nama_field} harus bertipe {tipe.__name__}")
                continue

        if "min" in aturan and nilai < aturan["min"]:
            errors.append(f"{nama_field} minimal {aturan['min']}")

        if "max" in aturan and nilai > aturan["max"]:
            errors.append(f"{nama_field} maksimal {aturan['max']}")

    for pesan in args:
        errors.append(str(pesan))

    for nama, nilai in kwargs.items():
        if not nilai:
            errors.append(f"Validasi tambahan gagal: {nama}")

    return len(errors) == 0, errors


if __name__ == "__main__":
    data_mahasiswa = {
        "nama": "Lulu",
        "umur": 21,
        "nilai": 85
    }

    schema = {
        "nama": {"type": str},
        "umur": {"type": int, "min": 17, "max": 60},
        "nilai": {"type": (int, float), "min": 0, "max": 100}
    }

    valid, errors = validasi_data(data_mahasiswa, schema)

    print("Data valid:", valid)
    print("Kesalahan:", errors)
