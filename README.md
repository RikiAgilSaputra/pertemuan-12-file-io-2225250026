# Pertemuan 12 - File I/O dan Error Handling
Nama: RIKI AGIL SAPUTRA


NIM: 2225250026


Kelas: 3A
## Tujuan
Membaca, memvalidasi, mengolah, dan menulis data file dengan Python.
## Format File Input
NIM,nilai
## Cara Menjalankan
python3 tugas/rekap_nilai_file.py
## Error yang Ditangani
- FileNotFoundError
- ValueError
## Test Case
### Test Case Wajib

| Kasus | Kondisi | Hasil yang Diharapkan | Hasil Aktual | Status |
| :--- | :--- | :--- | :--- | :--- |
| Normal | Semua baris valid | Semua record diproses dan rekap benar. | Semua record diproses dan rekap benar. | Pass |
| File hilang | nilai.txt tidak tersedia | Pesan file tidak ditemukan; program tidak crash. | Pesan file tidak ditemukan; program tidak crash. | Pass |
| Nilai invalid | A004,abc | Baris invalid dilewati/dilaporkan; record lain tetap diproses. | Baris invalid dilewati/dilaporkan; record lain tetap diproses. | Pass |
| Baris kosong | Ada baris kosong | Baris kosong dilewati. | Baris kosong dilewati. | Pass |
| Batas lulus | Nilai 60 | Dihitung sebagai lulus. | Dihitung sebagai lulus. | Pass |
.
## Refleksi
Salah satu error yang ditemukan adalah file tidak ditemukan dan program menanganinya dengan blok try except.