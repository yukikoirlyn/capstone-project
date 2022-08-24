from ctypes import resize
from matplotlib.pyplot import legend
from numpy import full, size
from sqlalchemy import column
import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

st.set_page_config(layout="wide")
image = Image.open('dqlab.png')
image2 = Image.open('1000_F_121128679_pMxkyQRwMRFiZMru0nG0bFwnxj5qt8kY-removebg-preview.png')

st.markdown("""
<style>
body {
    color: #fff;
    background-color: #000;
}
</style>
    """, unsafe_allow_html=True)

with st.sidebar:
    st.markdown('<div style="text-align: center;font-size:40px;font-weight:bold;color:grey;">Capstone Project</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: center;font-size:15px;color:grey;">TETRIS PROGRAM</div>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<div style="text-align:center;font-size:20px;color:grey;">Yukiko Irliyani</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align:center;font-size:15px;color:grey;">irliyaniyukiko@gmail.com</div>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        st.write("")
    with col2:
        st.image(image)
    with col3:
        st.write("")    

st.markdown('<div style="text-align: center;font-size:30px;font-weight:bold;">Efiensi Kebijakan: </div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: center;font-size:40px;font-weight:bold;">Booster jadi Syarat Mobilitas</div>', unsafe_allow_html=True)
st.markdown('<br>', unsafe_allow_html=True)
st.markdown('<div style="text-align:justify;font-size:15px;">Ditemukan bahwa peningkatan kasus Covid-19\
     di beberapa negara terjadi begitu signifikan, seperti di Prancis, Italia, dan Jerman. Kenaikan\
        signifikan juga terjadi di negara tetangga, Singapura. Kabar baiknya, Indonesia menempati\
            posisi terendah pada kasus harian terhadap populasi, jika dibandingkan beberapa negara\
                tetangga lainnya.\
                    Vaksinasi booster efektif menjadi syarat perjalanan per 17 Juli 2022.\
                        Syarat vaksin booster tersebut diatur dalam Surat Edaran No. 70 Tahun 2022 tentang petunjuk\
                            Pelaksanaan Perjalanan orang Dalam Negeri (PPDN) dengan transportasi udara, darat, dan laut\
                                pada masa pandemi Covid-2019.\
                                    </div>', unsafe_allow_html=True)
st.markdown("---")
st.markdown('<div style="text-align: center;font-size:20px;font-weight:bold;">Laporan Peduli Lindungi</div>', unsafe_allow_html=True)
st.markdown('<br>', unsafe_allow_html=True)
col1, col2, col3 = st.columns([1,1,1])
with col1:
    st.markdown('<div style="text-align: center;font-size:15px;font-weight:bold;">Pengunjung Mall</div>', unsafe_allow_html=True)
    st.image(image2,caption="source: freepik.com")
with col2:
    st.markdown('<div style="text-align: center;font-size:70px;font-weight:bold;">1,9 jt</div>', unsafe_allow_html=True)  
    st.markdown('<div style="text-align: center;font-size:40px;font-weight:bold;">orang</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: center;font-size:15px;font-weight:bold;">per hari</div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div style="text-align: center;font-size:70px;font-weight:bold;">24,6 %</div>', unsafe_allow_html=True)  
    st.markdown('<div style="text-align: center;font-size:40px;font-weight:bold;">booster</div>', unsafe_allow_html=True)                                   
st.markdown('<br>', unsafe_allow_html=True)
st.markdown('<div style="text-align:justify;font-size:15px;">Wakil Direktur INDEF, Eko Listyanto menilai syarat \
    vaksin booster untuk perjalanan dinilai tidak akan menggangu momentum pemulihan ekonomi yang \
        sedang berjalan. Alasannya, saat ini kesadaran masyarakat untuk mendapatkan vaksin \
            sudah terbangun dan cukup baik.\
                </div>', unsafe_allow_html=True)
st.markdown('<br>', unsafe_allow_html=True)
st.markdown('<div style="text-align:justify;font-size:40px;">Lalu?\
                </div>', unsafe_allow_html=True)
st.markdown('<br>', unsafe_allow_html=True)
st.markdown('<div style="text-align:justify;font-size:15px;">Apakah kebijakan vaksin  booster tidak mempengaruhi mobilitas masyarakat?\
    Sedangkan jika dilogika setiap pertumbuhan mobilitas berarti dapat \
        mempengaruhi pertumbuhan ekonomi? Atau mungkinkah kesadaran masyarakat \
            saat ini sudah sangat tinggi untuk melakukan vaksin?\
                </div>', unsafe_allow_html=True)
st.write(" ")
st.markdown("---")

st.markdown('<div style="text-align: center;font-size:30px;font-weight:bold;">Kebijakan Pemerintah vs Mobilitas Masyarakat</div>', unsafe_allow_html=True)
st.markdown('<br>', unsafe_allow_html=True)
st.markdown('<div style="text-align: center;font-size:20px;font-weight:bold;">Mobilitas Masyarakat Indonesia saat Pandemi</div>', unsafe_allow_html=True)
# dataset declaration
df = pd.read_csv('mobility_change_202208012334.csv')

df['date'] = pd.to_datetime(df['date'])

# st.dataframe(df)

# line chart
mobility = df[['date', 'retail_and_recreation', 
'grocery_and_pharmacy', 'park', 'transit', 
'workplace', 'resident']].set_index('date').resample('M').sum()

st.line_chart(mobility)

st.markdown('<div style="text-align: justify;font-size:15px;font-weight:bold;">Hal yang cukup menarik \
    terasa pada dua kondisi:</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justifi;font-size:15px;">1. Pada saat kasus \
    covid meningkat \
        </div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify;font-size:15px;">2. Pada saat libur nasional. \
        </div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify;font-size:15px;">Diketahui terdapat tiga gelombang \
    kasus covid yaitu yang pertama terjadi \
        hingga akhir Januari 2021, kedua pada saat adanya varian delta di sekitar pertengahan 2021,\
            serta yang ketiga pada akhir 2021 hingga awal 2022\
                Berdasarkan data tidak tampak pengaruh dari kebijakan pemerintah dalam memberikan \
                    syarat bagi pelaku perjalanan. Jika kita kembali ke belakang, surat edaran syarat \
                        vaksin sudah berlaku sejak bulan November 2021 (Surat Edaran Kasatgas Nomor 22 Tahun 2021\
        </div>', unsafe_allow_html=True)
st.write("  ")
st.write("")

st.markdown("---")
# heat map
st.markdown('<div style="text-align: center;font-size:20px;font-weight:bold;">Heat Maps perubahan Mobilitas Masyarakat berdasarkan Sektornya</div>', unsafe_allow_html=True)
st.markdown('<br>', unsafe_allow_html=True)
select1, select2 = st.columns(2)
with select1:
    year = st.selectbox("Select Year", ('2020', '2021', '2022'))
with select2:
    business = st.selectbox("Select Business Field", ('retail_and_recreation', 'grocery_and_pharmacy',
    'park', 'transit', 'workplace', 'resident'))

if year == '2020':
    year = '2020_mobility.csv'
elif year == '2021':
    year = '2021_mobility.csv'
else:
    year = '2022_mobility.csv'
    
dfp = pd.read_csv(year)

dfp['date'] = pd.to_datetime(dfp['date'])
dfp_p = dfp.pivot(index='province', columns='date')[business]

heat_m = px.imshow(dfp_p, color_continuous_scale='jet')

heat_m.update_layout(height=500)
st.plotly_chart(heat_m, use_container_width=True)

st.markdown('<div style="text-align:justify;font-size:15px;">Data menjelaskan pada lokasi park \
    di tahun 2022 memiliki sesuatu yang unik. Hal ini terlihat pada musim lebaran \
        (Mei - Juni 2022) memiliki nilai mobilisasi yang cukup tinggi. Pada musim liburan saat itu, umumnya masyarakat \
            lebih memilih ke tempat yang outdoor ketimbang harus ke dalam mall. Sehingga, \
                kebijakan pemerintah disini tidak dapat berlaku.</div>', unsafe_allow_html=True)

st.write("")
st.markdown("---")

st.markdown('<div style="text-align: center;font-size:30px;font-weight:bold;">Correlation Analysist</div>', unsafe_allow_html=True)
st.markdown('<br>', unsafe_allow_html=True)

st.markdown('<div style="text-align: center;font-size:20px;font-weight:bold;">Bagaimana Korelasi antara Mobilitas \
    Masyarakat dengan Produk Domestik Bruto</div>', unsafe_allow_html=True)
# correlation mobility and GDP
dfc = pd.read_csv('cor_pdb_mobility_202208031213.csv')

# normalization 
dfc['pdb'] = (dfc['pdb'] - dfc['pdb'].min()) / (dfc['pdb'].max() - dfc['pdb'].min())
dfc['mobilty'] = (dfc['mobilty'] - dfc['mobilty'].min()) / (dfc['mobilty'].max() - dfc['mobilty'].min())

scatt = px.scatter(dfc, x=dfc['pdb'], y=dfc['mobilty'], color="time_frame", symbol="categories",
    trendline="ols", trendline_scope="overall")
scatt.update_traces(marker_size=20, showlegend=True)

# finding linear regression model
results = px.get_trendline_results(scatt)
alpha = results.iloc[0]["px_fit_results"].params[0]
beta = results.iloc[0]["px_fit_results"].params[1]
rsq = results.iloc[0]["px_fit_results"].rsquared

scatt.data[9].name = 'y = ' + str(round(alpha, 2)) +' + ' + str(round(beta, 8)) + 'x' + ' | R-squared = ' + str(round(rsq, 3))
scatt.data[9].showlegend = True

st.plotly_chart(scatt, use_container_width=True)

st.markdown('<div style="text-align: justify;font-size:15px;">Melalui data di atas, \
    dapat menunjukkan bahwa sangat erat kaitannya antara mobilitas\
        masyarakat dengan pertumbuhan ekonomi. Selain itu, terdapat hal yang berbeda pada data di \
            triwulan 3 2021 dan triwulan 1 2022. Keadaan yang menyimpang dapat disebabkan adanya masalah\
                kesehatan/kenaikan kasus covid pada masa itu namun tidak membuat masyarakat hilang kreativitas\
                    untuk meningkatkan perekonomian.</div>', unsafe_allow_html=True)
st.markdown("---")
st.markdown('<div style="text-align: center;font-size:20px;font-weight:bold;">Produk Domestik Bruto \
    berdasarkan Lapangan Usaha</div>', unsafe_allow_html=True)
# cek sektor lapangan usaha
dfl = pd.read_csv('pdb_lap_usaha.csv')

#unpivot DataFrame from wide format to long format
dfl_unpivot = pd.melt(dfl, id_vars='lapangan_usaha', value_vars=['triwulan_2_2021', 'triwulan_3_2021', 'triwulan_4_2021', 'triwulan_1_2022'])

lap = px.bar(dfl_unpivot, x = "variable", y = "value", color = "lapangan_usaha", barmode='group')
lap.update_layout(
        autosize=False,
        width=800,
        height=500
    )
st.plotly_chart(lap, use_container_width=True)

st.markdown('<div style="text-align: justify;font-size:15px;">Kontribusi terbesar dalam perekonomian Indonesia terdapat pada sektor industri\
    pengolahan. Berdasarkan data tersebut, penyimpangan yang terjadi pada triwulan 4 2021 dan \
        triwulan 1 2022 secara signifikan disebabkan oleh perubahan hasil usaha sektor pertanian,\
            perhutanan, dan perikanan</div>', unsafe_allow_html=True)
st.markdown("---")
st.markdown('<div style="text-align: center;font-size:20px;font-weight:bold;">Korelasi antara Kenaikan \
    Vaksinasi dan Mobilitas Masyarakat</div>', unsafe_allow_html=True)
# correlation between mobility and vaccination
dfv = pd.read_csv('corr_vacc_mobility_202208031539.csv')

corr = px.scatter(dfv, x=dfv['total_vaccinations'], y=dfv['mobility'], color="categories", trendline="ols", trendline_scope="overall")

results_1 = px.get_trendline_results(corr)
alpha_1 = results_1.iloc[0]["px_fit_results"].params[0]
beta_1 = results_1.iloc[0]["px_fit_results"].params[1]
rsq_1 = results_1.iloc[0]["px_fit_results"].rsquared

corr.data[4].name = 'y = ' + str(round(alpha_1, 2)) +' + ' + str(round(beta_1, 8)) + 'x' + ' | R-squared = ' + str(round(rsq_1, 3))
corr.data[4].showlegend = True
st.plotly_chart(corr, use_container_width=True)
st.markdown('<div style="text-align: justify;font-size:15px;">Terdapat korelasi yang kuat antara total vaksinasi \
    dengan nilai mobilitas\
        pada tahun 2020 - 2022 (r = 0,773). Hal ini menunjukkan bahwa kesadaran masyarakat terhadap\
            vaksinasi juga dipengaruhi oleh keinginan mereka untuk meningkatkan mobilitas\
    </div>', unsafe_allow_html=True)

st.markdown("---")
st.markdown('<div style="text-align:justify;font-size:40px;">Insight\
                </div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify;font-size:15px;">Varian Covid yang \
    semakin bermutasi memaksa pemerintah membentuk kebijakan baru untuk mendorong\
        masyarakat mendapatkan vaksin. Hal ini dijadikan syarat bagi siapa saja yang\
            menggunakan transportasi umum. Banyak pro dan kontra yang terjadi di masyarakat,\
                tak jarang mereka merasa dirugikan dengan kebijakan ini. Lain halnya dengan bidang ekonomi,\
                    orang yang semakin hari semakin kreatif membuat kampanye ini tidak berpengaruh.\
                        Berdasarkan data yang telah disajikan, wawasan yang dapat diberikan bahwa pemerintah \
                            harus lebih kreatif dalam memberikan kampanye karena kesadaran masyarakat saat ini \
                                cukup baik untuk diberikan vaksin, meski mobilitas sangat berkorelasi dengan \
                                    pertumbuhan ekonomi. Namun perlu diingat, bekerja melalui WFH juga dapat \
                                        menumbuhkan perekonomian.\
                                             Kesadaran masyarakat untuk melakukan vaksin juga didukung oleh \
                                                keinginan mereka untuk meningkatkan mobilitas, sehingga peran \
                                                    kebijakan pemerintah juga berpengaruh besar disini bagi sebagian masyarakat.\
    </div>', unsafe_allow_html=True)
st.write("     ")

st.markdown("---")
st.write("Capstone Project, Tetris Program")
