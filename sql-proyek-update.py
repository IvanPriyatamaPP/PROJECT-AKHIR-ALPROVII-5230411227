# UPDATE table_name
# SET column1 = value1, column2 = value2, ...
# WHERE condition;
import sqlite3

# Membuat koneksi ke database atau membuat database baru jika belum ada
conn = sqlite3.connect('database_hewan.db')
cursor = conn.cursor()

# Data yang ingin diubah
id_hewan = 3
jml_skrng = 900

# Menjalankan query UPDATE
cursor.execute(f"UPDATE HEWAN SET jml_skrng = {jml_skrng} WHERE id_hewan = {id_hewan}")
conn.commit()

# Menampilkan pesan setelah update berhasil
if cursor.rowcount > 0:
    print(f"Data hewan dengan ID {id_hewan} berhasil diupdate.")
else:
    print(f"Tidak ada data hewan dengan ID {id_hewan}.")

# Menutup koneksi
conn.close()
