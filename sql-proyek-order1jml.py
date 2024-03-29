import sqlite3

# Membuat koneksi ke database atau membuat database baru jika belum ada
koneksi = sqlite3.connect('database_hewan.db')
kursor = koneksi.cursor()

# Menjalankan query SELECT dengan ORDER BY
kursor.execute("SELECT * FROM HEWAN ORDER BY jml_skrng DESC") #ASC|DESC
baris_table = kursor.fetchall()

print("Data Hewan:")
print("="*100)
print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format("id_hewan", "nama_hewan", "jenis", "asal", "jml_skrng", "thn_ditemukan"))
print("-"*100)
for baris in baris_table:
    print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format(baris[0], baris[1], baris[2], baris[3], baris[4], baris[5]))

koneksi.close()