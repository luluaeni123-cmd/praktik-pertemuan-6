
import statistics
import math


def hitung_statistik(data):
    if not data:
        return {}

    hasil = {
        "mean": statistics.mean(data),
        "median": statistics.median(data),
        "modus": statistics.mode(data),
        "range": max(data) - min(data),
        "standard_deviation": statistics.pstdev(data)
    }

    return hasil


if __name__ == "__main__":
    angka = [80, 85, 90, 85, 75, 95]

    hasil = hitung_statistik(angka)

    print("Data:", angka)
    print("Mean:", hasil["mean"])
    print("Median:", hasil["median"])
    print("Modus:", hasil["modus"])
    print("Range:", hasil["range"])
    print("Standard Deviation:", hasil["standard_deviation"])
