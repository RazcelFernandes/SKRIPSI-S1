import streamlit as st
import pandas as pd
from background import set_background

set_background()

# =====================================
# KONFIGURASI HALAMAN
# =====================================
st.set_page_config(
    page_title="Evaluasi Model",
    page_icon="📈",
    layout="wide"
)

# =====================================
# CSS
# =====================================
st.markdown("""
<style>

.main-title{
    text-align:center;
    font-size:40px;
    font-weight:bold;
    color:#1E3A8A;
}

.sub-title{
    text-align:center;
    color:#64748B;
    font-size:17px;
    margin-bottom:30px;
}

.container{
    max-width:900px;
    margin:auto;
}

.card{
    background:#FFFFFF;
    padding:25px 30px;
    border-radius:15px;
    box-shadow:0px 4px 15px rgba(0,0,0,.08);
    margin-bottom:25px;
}

.card h2{
    color:#1E3A8A;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# HEADER
# =====================================

st.markdown("""
<div class="main-title">
📈 Evaluasi Model
</div>

<div class="sub-title">
Perbandingan performa algoritma Support Vector Machine (SVM) dan Random Forest.
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="container">', unsafe_allow_html=True)

# =====================================
# PERBANDINGAN MODEL
# =====================================

st.markdown("""
<div class="card">
<h2>📊 Perbandingan Performa Model</h2>
</div>
""", unsafe_allow_html=True)

comparison = pd.DataFrame({
    "Metrik": [
        "Accuracy",
        "Precision",
        "Recall",
        "F1-Score"
    ],
    "Support Vector Machine": [
        "98.07%",
        "98.83%",
        "97.25%",
        "98.03%"
    ],
    "Random Forest": [
        "86.12%",
        "87.29%",
        "84.19%",
        "85.71%"
    ]
})

st.dataframe(
    comparison,
    use_container_width=True,
    hide_index=True
)

st.info("""
**Kesimpulan**

Berdasarkan hasil evaluasi, algoritma **Support Vector Machine (SVM)** memperoleh
nilai Accuracy, Precision, Recall, dan F1-Score yang lebih tinggi dibandingkan
Random Forest. Oleh karena itu, SVM menjadi model dengan performa terbaik pada
penelitian ini.
""")

st.markdown("</div>", unsafe_allow_html=True)




# =====================================
# CSS
# =====================================
st.markdown("""
<style>

.stApp{
     background-color:#030202;
    background-size:cover;
    background-position:center;
    background-repeat:no-repeat;
    background-attachment:fixed;
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
