import sqlite3

conn = sqlite3.connect('database_hewan.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM HEWAN")
rows = cursor.fetchall()

print("Data Hewan:")
print("="*100)
print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format("id_hewan", "nama_hewan", "jenis", "asal", "jml_skrng", "thn_ditemukan"))
print("-"*100)
for rows in rows:
    print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format(rows[0], rows[1], rows[2], rows[3], rows[4], rows[5]))

conn.close()