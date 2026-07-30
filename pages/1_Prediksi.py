import streamlit as st
import numpy as np
import joblib
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.units import cm
from io import BytesIO
from datetime import datetime
from reportlab.lib.enums import TA_CENTER

from background import set_background

set_background()

# ==============================
# LOAD MODEL
# ==============================

svm = joblib.load("model/svm_model.pkl")
rf = joblib.load("model/rf_model.pkl")
scaler = joblib.load("model/scaler.pkl")


# ==============================
# MEMBUAT PDF
# ==============================
def generate_pdf(model, prediction, probability, nama, data_pasien):

    buffer = BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        rightMargin=30,
        leftMargin=30,
        topMargin=30,
        bottomMargin=30
    )

    styles = getSampleStyleSheet()

    # ==========================
    # STYLE
    # ==========================

    title_style = styles["Title"]
    title_style.alignment = TA_CENTER
    title_style.textColor = colors.HexColor("#0080FF")
    title_style.spaceAfter = 5

    sub_style = styles["Heading2"]
    sub_style.alignment = TA_CENTER
    sub_style.spaceAfter = 20

    heading_style = styles["Heading2"]
    heading_style.textColor = colors.HexColor("#0055FF")

    normal = styles["Normal"]

    story = []

    # ==========================
    # HEADER
    # ==========================

    story.append(
        Paragraph(
            "DIABETES CLASSIFICATION SYSTEM",
            title_style
        )
    )

    story.append(
        Paragraph(
            "Laporan Hasil Prediksi Diabetes",
            sub_style
        )
    )

    # ==========================
    # INFORMASI
    # ==========================

    info = Table([
    ["Nama Pasien", nama],
    ["Tanggal Prediksi", datetime.now().strftime("%d-%m-%Y %H:%M:%S")],
    ["Algoritma", model],
    ["Hasil Prediksi", prediction]
], colWidths=[5*cm,10*cm])
    
    info.setStyle(TableStyle([

        ("BACKGROUND",(0,0),(0,-1),colors.HexColor("#E3F2FD")),
        ("FONTNAME",(0,0),(-1,-1),"Helvetica-Bold"),
        ("GRID",(0,0),(-1,-1),0.5,colors.grey),
        ("BOTTOMPADDING",(0,0),(-1,-1),8)

    ]))

    story.append(info)

    story.append(Spacer(1,20))

    # ==========================
    # DATA PASIEN
    # ==========================

    story.append(
        Paragraph("DATA PASIEN", heading_style)
    )

    data = [["Parameter","Nilai"]]

    for k,v in data_pasien.items():
        data.append([k,str(v)])

    pasien = Table(
        data,
        colWidths=[7*cm,8*cm]
    )

    pasien.setStyle(TableStyle([

        ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#1976D2")),
        ("TEXTCOLOR",(0,0),(-1,0),colors.white),
        ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),

        ("BACKGROUND",(0,1),(-1,-1),colors.whitesmoke),

        ("GRID",(0,0),(-1,-1),0.3,colors.grey),

        ("BOTTOMPADDING",(0,0),(-1,0),10),

        ("ALIGN",(0,0),(-1,-1),"CENTER")

    ]))

    story.append(pasien)

    story.append(Spacer(1,20))

    # ==========================
    # HASIL
    # ==========================

    story.append(
        Paragraph("HASIL PREDIKSI", heading_style)
    )

    if prediction == "Positif Diabetes":

        warna = colors.HexColor("#FDECEC")
        tulisan = colors.red
        interpretasi = """
Model memprediksi bahwa pasien memiliki indikasi diabetes.
Disarankan untuk melakukan pemeriksaan lebih lanjut
kepada tenaga medis.
"""

    else:

        warna = colors.HexColor("#E8F5E9")
        tulisan = colors.green
        interpretasi = """
Model memprediksi bahwa pasien tidak menunjukkan indikasi diabetes.
Tetap disarankan menjaga pola hidup sehat
dan melakukan pemeriksaan kesehatan secara berkala.
"""

    hasil = Table([
        [prediction],
        [f"Probabilitas : {probability*100:.2f}%"]
    ], colWidths=[15*cm])

    hasil.setStyle(TableStyle([

        ("BACKGROUND",(0,0),(-1,-1),warna),

        ("TEXTCOLOR",(0,0),(-1,0),tulisan),

        ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),

        ("FONTSIZE",(0,0),(-1,0),18),

        ("ALIGN",(0,0),(-1,-1),"CENTER"),

        ("BOTTOMPADDING",(0,0),(-1,-1),15),

        ("GRID",(0,0),(-1,-1),0.3,colors.grey)

    ]))

    story.append(hasil)

    story.append(Spacer(1,20))

    # ==========================
    # INTERPRETASI
    # ==========================

    story.append(
        Paragraph("INTERPRETASI", heading_style)
    )

    story.append(
        Paragraph(
            interpretasi,
            normal
        )
    )

    story.append(Spacer(1,15))

    # ==========================
    # CATATAN
    # ==========================

    story.append(
        Paragraph(
            "<b>Catatan :</b> Hasil prediksi ini merupakan hasil implementasi Machine Learning dan digunakan sebagai alat bantu pengambilan keputusan. Hasil ini bukan merupakan diagnosis medis sehingga tetap diperlukan konsultasi dengan tenaga kesehatan.",
            normal
        )
    )

    story.append(Spacer(1,20))

    doc.build(story)

    pdf = buffer.getvalue()

    buffer.close()

    return pdf
# ==============================
# CSS
# ==============================

st.markdown("""
<style>

.title{
    font-size:38px;
    font-weight:bold;
    color:#2563EB;
}

.subtitle{
    color:gray;
    margin-bottom:30px;
}

.result-card{

    padding:25px;

    border-radius:20px;

    background:#F8FAFC;

    box-shadow:0px 4px 15px rgba(0,0,0,.08);

}

</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🤖 Prediksi Diabetes</div>', unsafe_allow_html=True)

st.markdown(
'<div class="subtitle">Masukkan data pasien untuk melakukan prediksi.</div>',
unsafe_allow_html=True)

# ==============================
# PILIH MODEL
# ==============================

model = st.selectbox(
    "Model Machine Learning",
    [
        "Support Vector Machine",
        "Random Forest"
    ]
)

st.divider()

st.markdown(
    '<div class="subtitle">Masukkan data pasien untuk melakukan prediksi.</div>',
    unsafe_allow_html=True
)

# ==============================
# NAMA PASIEN
# ==============================

nama = st.text_input(
    "👤 Nama Pasien",
    placeholder="Masukkan nama pasien"
)
# ==============================
# FORM INPUT
# ==============================

col1,col2 = st.columns(2)

with col1:

    gender = st.selectbox(
        "Jenis Kelamin",
        ["Perempuan","Laki-laki"]
    )

    pregnancies = st.slider(
        "Kehamilan",
        0,20,1
    )

    glucose = st.slider(
        "Glukosa",
        50,250,120
    )

    blood = st.slider(
        "Tekanan Darah",
        30,150,70
    )

    skin = st.slider(
        "Ketebalan Kulit",
        0,100,20
    )

with col2:

    insulin = st.slider(
        "Insulin",
        0,900,80
    )

    bmi = st.slider(
        "BMI",
        10.0,70.0,25.0
    )

    dpf = st.slider(
        "Diabetes Pedigree Function",
        0.0,3.0,0.5
    )

    age = st.slider(
        "Usia",
        1,100,30
    )

gender = 1 if gender=="Laki-laki" else 0

# ==============================
# BUTTON
# ==============================

st.write("")

predict = st.button(
    "🔍 Prediksi Sekarang",
    use_container_width=True
)

# ==============================
# PREDIKSI
# ==============================

if predict:

    if nama.strip() == "":
        st.warning("⚠️ Silakan masukkan nama pasien terlebih dahulu.")
        st.stop()

    data = np.array([[ 
        gender,
        pregnancies,
        glucose,
        blood,
        skin,
        insulin,
        bmi,
        dpf,
        age
    ]])

    # Prediksi
    if model == "Support Vector Machine":
        data_scaled = scaler.transform(data)
        pred = svm.predict(data_scaled)[0]
        prob = svm.predict_proba(data_scaled)[0][1]
    else:
        pred = rf.predict(data)[0]
        prob = rf.predict_proba(data)[0][1]

    # Hasil
    if pred == 1:
        hasil = "Positif Diabetes"
        st.error("## 🔴 Positif Diabetes")
    else:
        hasil = "Tidak Diabetes"
        st.success("## 🟢 Tidak Diabetes")

    st.progress(float(prob))
    st.metric("Probabilitas Diabetes", f"{prob*100:.2f}%")
    st.info(f"Model yang digunakan: **{model}**")

    # ======================
    # SIMPAN KE DATABASE
    # ======================

    from database.db import get_connection

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO histori_prediksi(
        nama_pasien,
        jenis_kelamin,
        kehamilan,
        glukosa,
        tekanan_darah,
        ketebalan_kulit,
        insulin,
        bmi,
        dpf,
        usia,
        algoritma,
        hasil_prediksi,
        probabilitas
    )
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
    """, (
        nama,
        "Laki-laki" if gender == 1 else "Perempuan",
        pregnancies,
        glucose,
        blood,
        skin,
        insulin,
        bmi,
        dpf,
        age,
        model,
        hasil,
        float(prob)
    ))

    conn.commit()
    conn.close()

    # ======================
    # GENERATE PDF
    # ======================

    data_pasien = {
        "Jenis Kelamin": "Laki-laki" if gender == 1 else "Perempuan",
        "Jumlah Kehamilan": pregnancies,
        "Glukosa": glucose,
        "Tekanan Darah": blood,
        "Ketebalan Kulit": skin,
        "Insulin": insulin,
        "BMI": bmi,
        "Diabetes Pedigree Function": dpf,
        "Usia": age
    }

    pdf = generate_pdf(
        model=model,
        prediction=hasil,
        probability=prob,
        nama=nama,
        data_pasien=data_pasien
    )

    st.download_button(
        label="📄 Download Hasil Prediksi (PDF)",
        data=pdf,
        file_name=f"Hasil_Prediksi_{nama.replace(' ', '_')}.pdf",
        mime="application/pdf",
        use_container_width=True
    )
