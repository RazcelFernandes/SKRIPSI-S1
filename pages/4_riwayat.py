import streamlit as st
import sqlite3
import pandas as pd
from background import set_background

set_background()

# ==========================
# Judul Halaman
# ==========================

st.title("📄 Riwayat Prediksi")

st.write(
    "Riwayat seluruh hasil prediksi pasien yang telah dilakukan."
)

# ==========================
# Koneksi Database
# ==========================

conn = sqlite3.connect("diabetes.db")

df = pd.read_sql_query(
    "SELECT * FROM histori_prediksi ORDER BY id DESC",
    conn
)

# ==========================
# Statistik
# ==========================

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Prediksi", len(df))

col2.metric(
    "Positif",
    len(df[df["hasil_prediksi"] == "Positif Diabetes"])
)

col3.metric(
    "Tidak Diabetes",
    len(df[df["hasil_prediksi"] == "Tidak Diabetes"])
)

col4.metric(
    "Model Terbanyak",
    df["algoritma"].mode()[0] if len(df) > 0 else "-"
)

st.divider()

# ==========================
# Pencarian
# ==========================

keyword = st.text_input(
    "🔍 Cari Nama Pasien"
)

if keyword:
    df = df[
        df["nama_pasien"].str.contains(
            keyword,
            case=False,
            na=False
        )
    ]

# ==========================
# Download CSV
# ==========================

st.download_button(
    "📄 Download Riwayat CSV",
    df.to_csv(index=False),
    "riwayat_prediksi.csv",
    "text/csv"
)

st.divider()

# ==========================
# Card Riwayat
# ==========================

for index, row in df.iterrows():

    with st.container(border=True):

        st.subheader(f"👤 {row['nama_pasien']}")

        col1, col2 = st.columns(2)

        with col1:

            st.write(f"**Model :** {row['algoritma']}")
            st.write(f"**Usia :** {row['usia']} Tahun")
            st.write(f"**Glukosa :** {row['glukosa']}")
            st.write(f"**BMI :** {row['bmi']}")

        with col2:

            if row["hasil_prediksi"] == "Positif Diabetes":
                st.error(row["hasil_prediksi"])
            else:
                st.success(row["hasil_prediksi"])

            st.metric(
                "Probabilitas",
                f"{row['probabilitas']*100:.2f}%"
            )

            st.write(
                f"📅 {row['tanggal_prediksi']}"
            )

        with st.expander("👁 Lihat Detail"):

            st.write(f"Jenis Kelamin : {row['jenis_kelamin']}")
            st.write(f"Jumlah Kehamilan : {row['kehamilan']}")
            st.write(f"Tekanan Darah : {row['tekanan_darah']}")
            st.write(f"Ketebalan Kulit : {row['ketebalan_kulit']}")
            st.write(f"Insulin : {row['insulin']}")
            st.write(f"BMI : {row['bmi']}")
            st.write(f"DPF : {row['dpf']}")

        if st.button(
            "🗑 Hapus",
            key=row["id"]
        ):

            conn.execute(
                "DELETE FROM histori_prediksi WHERE id=?",
                (row["id"],)
            )

            conn.commit()

            st.rerun()

conn.close()