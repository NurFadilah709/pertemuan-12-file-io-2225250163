nilai = []

with open("data/nilai.txt", "r", encoding="utf-8") as file:
    for nomor, baris in enumerate(file, start=1):
        baris = baris.strip()

        if not baris:
            continue

        try:
            nim, teks_nilai = baris.split(",")
            angka = float(teks_nilai)
            nilai.append(angka)

            print(nim, angka)

        except ValueError:
            print(f"Baris {nomor} tidak valid: {baris}")

if nilai:
    print(f"Rata-rata = {sum(nilai)/len(nilai):.2f}")