def baca_nilai(nama_file):
    hasil = []
    try:
        with open(nama_file, "r", encoding="utf-8")as file:
            for baris in file:
                baris = baris.strip()
                if not baris:
                    continue
                try:
                    nim, teks_nilai = baris.split()
                    hasil.append(nim, float (teks_nilai))
                except ValueError:
                    print("data dilewati karena tidak valid: {baris}")
            
    except FileNotFoundError:
        print (f"file tidak ditemukan: {nama_file}")
    return hasil


