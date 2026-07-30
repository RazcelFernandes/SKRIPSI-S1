import streamlit as st
import pandas as pd
from background import set_background

set_background()

st.title("📂 Dataset")

df = pd.read_csv("dataset_bersih.csv")

st.dataframe(df,use_container_width=True)



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
