import sqlite3

conn = sqlite3.connect("diabetes.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS histori_prediksi (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    nama_pasien TEXT,

    jenis_kelamin TEXT,

    kehamilan INTEGER,

    glukosa INTEGER,

    tekanan_darah INTEGER,

    ketebalan_kulit INTEGER,

    insulin INTEGER,

    bmi REAL,

    dpf REAL,

    usia INTEGER,

    algoritma TEXT,

    hasil_prediksi TEXT,

    probabilitas REAL,

    tanggal_prediksi TIMESTAMP DEFAULT CURRENT_TIMESTAMP

)
""")

conn.commit()

conn.close()

print("Database berhasil dibuat")