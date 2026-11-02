
# Pertemuan 12 - File I/O dan Error Handling

**Nama:** Nailah Nur Fadilah
**NIM:** 2225250163
**Kelas:** 3E

## 1. Tujuan
Mempelajari cara membaca, menulis, mengolah, dan menyimpan data menggunakan file Python serta menangani kesalahan menggunakan try-except.

## 2. Struktur Folder
- data: menyimpan file input dan output.
- latihan: menyimpan enam program latihan Python.
- tugas: menyimpan program rekap nilai.

## 3. Format File Input
File nilai.txt menggunakan format NIM,nilai.

Contoh:
A001,85
A002,78
A003,92
A004,abc
A005,74
A006,88

## 4. Cara Menjalankan
Buka terminal VS Code pada folder utama proyek.

Jalankan:
python tugas/rekap_nilai_file.py

## 5. Error yang Ditangani
- FileNotFoundError: terjadi ketika file tidak ditemukan.
- ValueError: terjadi ketika data tidak dapat dikonversi menjadi angka atau formatnya tidak sesuai.

## 6. Test Case
1. Data normal: seluruh data valid berhasil diproses.
2. File hilang: program menampilkan pesan file tidak ditemukan.
3. Nilai invalid: data A004,abc dilewati.
4. Baris kosong: baris kosong dilewati.
5. Batas lulus: nilai 60 dihitung lulus.

## 7. Refleksi
Dalam pengerjaan ini, kesalahan yang ditemukan adalah adanya data nilai yang tidak sesuai format, yaitu A004,abc. Kesalahan tersebut menyebabkan ValueError ketika program melakukan konversi ke tipe float.

Untuk mengatasinya, digunakan try-except agar baris yang tidak valid dapat dilewati tanpa menghentikan seluruh proses. Dengan demikian, data lain tetap dapat dibaca dan diolah dengan benar.
