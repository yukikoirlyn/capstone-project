from msilib import type_short
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import datetime as dt
import altair as alt
import plotly.express as px
from PIL import Image

st.set_page_config(layout="wide")


image = Image.open('286433377_585274886228914_8151508706000016022_n-modified.png')
image2 = Image.open('profil.png')
gmail = Image.open('gmail.png')

with st.sidebar:
    st.markdown('<div style="text-align: center;font-size:60px;font-weight:bold;color:grey;">Hackathon</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: center;font-size:25px;color:grey;">Women in Tech: Cybersecurity and Python</div>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: center;font-size:25px;font-weight:boldcolor:grey;">Meet with us</div>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,2,1])
    with col1:
        st.write("")
    with col2:
        st.image(image)
    with col3:
        st.write("")
    st.markdown('<div style="text-align:center;font-size:20px;color:grey;">Martha Shella Rahmawati</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align:center;font-size:15px;color:grey;">ashella660@gmail.com</div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,2,1])
    with col1:
        st.write("")
    with col2:
        st.image(image2)
    with col3:
        st.write("")
    st.markdown('<div style="text-align:center;font-size:20px;color:grey;">Yukiko Irliyani</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align:center;font-size:15px;color:grey;">irliyaniyukiko@gmail.com</div>', unsafe_allow_html=True)
    

st.markdown('<div style="text-align: center;font-size:60px;font-weight:bold;">Tantangan Cyber Attack di Era Digital</div>', unsafe_allow_html=True)
st.markdown('<br>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify;font-size:20px;">Di era Pandemi ini Pergerakan kegiatan manusia yang semula dilakukan secara konvesional berubah menjadi secara digital, Begitu banyak data dan\
    informasi yang disebarkan secara digital setiap harinya, Padat nya arus lalu lintas\
        informasi dan kegiatan di internet seakan-akan internet menjadi dunia tersendiri\
            tanpa batas. Tentu hal ini tidak terlepas dari banyak nya penyalahgunaan untuk tujuan\
                 yang menyimpang dari norma hukum dan merugikan pihak lain, hal ini disebut\
                     dengan tindakan Cyber Attacks yang berarti tindakan merubah, mengganggu,\
                         mentup akses, mengurangi kinerja, merusak file komputer dan jaringannya, \
                            serta menyebarkan informasi yang tidak benar.</div>', unsafe_allow_html=True)
st.markdown('<br>', unsafe_allow_html=True)
st.markdown("---")
st.markdown('<div style="text-align: center;font-size:30px;font-weight:bold;">Kejadian Cyber Attack di Indonesia</div>', unsafe_allow_html=True)
st.markdown('<br>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("2021","888,711,736","179%")
with col2:
    st.metric("2020", "495,300,000", "170%")
with col3:
    st.metric("2019", "290,300,000")
st.markdown('<br>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify;font-size:20px;">Menurut Badan Siber dan Sandi Negara (BSSN), sedikitnya 888.711.736\
     seragan siber melanda Indonesia dari Januari-Agustus 2021, angka ini\
         meningkat dua kali lipat dibandingkan tahun sebelunya, sebagai \
             perbandingan nya seragan siber yang terjadi di Indonesia sebanyak \
                290 Juta pada 2019 dan 495 juta pada 2020.\
    </div>', unsafe_allow_html=True)
st.markdown('<br>', unsafe_allow_html=True)

df = pd.read_csv("patrolisiber.csv")
df.astype({col: int for col in df.columns[1:]})

type_s = df[['Bulan', 'Child_Porn', 'Criminal', 'Hoax', 'Pemalsuan_Dokumen', 'Pemerasan', 'Pengancaman', 'Penghinaan_Pencemaran', 'Penistaan_Agama', 'Penjualan_narkoba_illegal_di_internet', \
        'Perdagangan_Hewan_yang_Dilindungi', 'Perdagangan_Orang', 'Perjudian', 'Provokasi_Penghasutan']].set_index(['Bulan'])       
 
dfl_unpivot = pd.melt(df, id_vars='Bulan', value_vars=['Child_Porn', 'Criminal', 'Hoax', 'Pemalsuan_Dokumen', 'Pemerasan', 'Pengancaman', 'Penghinaan_Pencemaran', 'Penistaan_Agama', 'Penjualan_narkoba_illegal_di_internet', \
        'Perdagangan_Hewan_yang_Dilindungi', 'Perdagangan_Orang', 'Perjudian', 'Provokasi_Penghasutan'])

lap = px.bar(dfl_unpivot, x = "Bulan", y = "value", color = "variable")
lap.update_layout(xaxis_type='category')
tab1, cht1 = st.columns([1, 4])
with tab1:
    st.write(df, height= 500)
with cht1:
    st.plotly_chart(lap, use_container_width=True)
