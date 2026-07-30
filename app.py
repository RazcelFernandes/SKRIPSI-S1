import streamlit as st

# =====================================
# KONFIGURASI HALAMAN
# =====================================
st.set_page_config(
    page_title="Aplikasi Prediksi Diabetes",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================
# CSS
# =====================================
st.markdown("""
<style>

[data-testid="stAppViewContainer"]{
    background: #111827;
}

[data-testid="stHeader"]{
    background:rgba(0,0,0,0);
}

[data-testid="stToolbar"]{
    right:2rem;
}

.block-container{
    padding-top:2rem;
    padding-bottom:3rem;
}

/* ======================== */
/* HEADER */
/* ======================== */

.main-title{
    text-align:center;
    font-size:48px;
    font-weight:700;
    color:#0F3D91;
}

.sub-title{
    text-align:center;
    font-size:19px;
    color:#2F3A4A;
    margin-bottom:35px;
}

/* ======================== */
/* CONTAINER */
/* ======================== */

.wrapper{
    width:100%;
    display:flex;
    justify-content:center;
}

.content{
    width:850px;
}

/* ======================== */
/* CARD */
/* ======================== */

.card{

    background:rgba(255,255,255,.96);

    border-radius:18px;

    padding:28px 35px;

    margin-bottom:25px;

    box-shadow:0px 8px 25px rgba(0,0,0,.18);

    transition:0.3s;
}

.card:hover{

    transform:translateY(-3px);

    box-shadow:0px 12px 30px rgba(0,0,0,.22);

}

.card h2{

    color:#123B8F;

    margin-bottom:15px;

}

.card p{

    text-align:justify;

    line-height:1.9;

    color:#374151;

}

.card li{

    line-height:1.9;

    color:#374151;

}

/* ======================== */

.warning{

    background:#FFF5E7;

    border-left:7px solid #F59E0B;

}

/* ======================== */

.footer{

    text-align:center;

    color:white;

    margin-top:40px;

    font-size:14px;

}

</style>
""", unsafe_allow_html=True)

# =====================================
# HEADER
# =====================================

st.markdown("""

<div class="main-title">

🩺 Aplikasi Prediksi Diabetes


""", unsafe_allow_html=True)

st.markdown('<div class="wrapper"><div class="content">', unsafe_allow_html=True)

# =====================================
# TENTANG
# =====================================

st.markdown("""

<div class="card">

<h2>👋 Tentang Aplikasi</h2>

<p>

Aplikasi Prediksi Diabetes merupakan aplikasi berbasis Machine Learning yang dirancang untuk membantu melakukan prediksi awal terhadap risiko penyakit diabetes berdasarkan data kesehatan pasien.

</p>

<p>

Sistem ini mengimplementasikan dua algoritma klasifikasi yaitu Support Vector Machine (SVM) dan Random Forest. Kedua algoritma digunakan untuk membandingkan performa klasifikasi sehingga dapat diketahui model yang memiliki tingkat akurasi terbaik.

</p>

</div>

""", unsafe_allow_html=True)

# =====================================
# FITUR
# =====================================

st.markdown("""

<div class="card">

<h2>✨ Fitur Utama</h2>

<ul>

<li>Prediksi risiko diabetes menggunakan algoritma Support Vector Machine (SVM).</li>

<li>Prediksi risiko diabetes menggunakan algoritma Random Forest.</li>

<li>Menampilkan probabilitas hasil prediksi.</li>

<li>Menampilkan evaluasi model secara lengkap.</li>

<li>Menampilkan informasi dataset penelitian.</li>

<li>Tampilan sederhana, modern, dan mudah digunakan.</li>

</ul>

</div>

""", unsafe_allow_html=True)

# =====================================
# PARAMETER PREDIKSI
# =====================================

st.markdown("""

<div class="card">

<h2>📋 Parameter Prediksi</h2>

<p>
Sistem melakukan prediksi berdasarkan beberapa parameter kesehatan pasien
yang umum digunakan dalam penelitian klasifikasi diabetes.
</p>

<ul>

<li><b>Jenis Kelamin</b></li>

<li><b>Jumlah Kehamilan</b></li>

<li><b>Kadar Glukosa</b></li>

<li><b>Tekanan Darah</b></li>

<li><b>Ketebalan Kulit</b></li>

<li><b>Insulin</b></li>

<li><b>Body Mass Index (BMI)</b></li>

<li><b>Diabetes Pedigree Function (DPF)</b></li>

<li><b>Usia</b></li>

</ul>

<p>
Parameter tersebut akan diproses oleh algoritma Machine Learning untuk
menghasilkan prediksi apakah pasien memiliki risiko diabetes atau tidak.
</p>

</div>

""", unsafe_allow_html=True)

# =====================================
# CARA PENGGUNAAN
# =====================================

st.markdown("""

<div class="card">

<h2>📝 Cara Penggunaan</h2>

<ol>

<li>Buka menu <b>Prediksi</b> melalui sidebar.</li>

<li>Masukkan seluruh data pasien sesuai parameter yang tersedia.</li>

<li>Pilih algoritma klasifikasi yang akan digunakan
(Support Vector Machine atau Random Forest).</li>

<li>Tekan tombol <b>Prediksi</b>.</li>

<li>Sistem akan menampilkan hasil prediksi beserta probabilitasnya.</li>

<li>Untuk melihat performa model, buka halaman <b>Evaluasi</b>.</li>

<li>Untuk melihat data penelitian, buka halaman <b>Dataset</b>.</li>

</ol>

</div>

""", unsafe_allow_html=True)

# =====================================
# KEUNGGULAN
# =====================================

st.markdown("""

<div class="card">

<h2>🚀 Keunggulan Aplikasi</h2>

<ul>

<li>Antarmuka sederhana dan mudah digunakan.</li>

<li>Menggunakan dua algoritma Machine Learning.</li>

<li>Memberikan hasil prediksi secara cepat.</li>

<li>Menampilkan probabilitas hasil klasifikasi.</li>

<li>Menyediakan halaman evaluasi model.</li>

<li>Dapat digunakan sebagai media pembelajaran implementasi Machine Learning.</li>

</ul>

</div>

""", unsafe_allow_html=True)

# =====================================
# CATATAN
# =====================================

st.markdown("""

<div class="card warning">

<h2>⚠️ Catatan Penting</h2>

<p>

Aplikasi ini dikembangkan sebagai implementasi algoritma Machine Learning
untuk membantu melakukan prediksi awal terhadap risiko penyakit diabetes.

</p>

<p>

Hasil prediksi bukan merupakan diagnosis medis dan tidak dapat menggantikan
pemeriksaan ataupun konsultasi dengan dokter maupun tenaga kesehatan.

</p>

<p>

Keakuratan hasil prediksi sangat dipengaruhi oleh kualitas dan kelengkapan
data yang dimasukkan oleh pengguna.

</p>

</div>

""", unsafe_allow_html=True)