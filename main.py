from ctypes import resize
from numpy import full
from sqlalchemy import column
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

st.title("Efiensi Kebijakan: 'Booster jadi Syarat Mobilitas'")
st.write("Berdasarkan data dari berbagai sumber ditemukan bahwa peningkatan kasus Covid-19 di beberapa negara terjadi begitu signifikan, seperti di Prancis, Italia, dan Jerman. Kenaikan signifikan juga terjadi di negara tetangga, Singapura. Kabar baiknya, Indonesia menempati posisi terendah pada kasus harian terhadap populasi, jika dibandingkan beberapa negara tetangga lainnya.")
st.write("Vaksinasi booster efektif menjadi syarat perjalanan naik pesawat per 17 Juli 2022. Syarat vaksin booster tersebut diatur dalam Surat Edaran No. 70 Tahun 2022 tentang petunjuk Pelaksanaan Perjalanan orang Dalam Negeri (PPDN) dengan transportasi udara, darat, dan laut pada masa pandemi Covid-2019.")
st.write("Penerapan kebijakan baru tersebut dilatarbelakangi oleh capaian vaksinasi booster yang masih rendah. Berdasarkan data Peduli Lindungi, dari rata-rata orang masuk mall perhari sebesar 1,9 juta orang, hanya 24,6 persen yang sudah booster. Di tengah peningkatan kasus yang terjadi, hal ini tentu sangat mengkhawatirkan, mengingat antibodi masyarakat akan semakin berkurang.")
st.write("Wakil Direktur INDEF, Eko Listyanto menilai syarat vaksin booster untuk perjalanan dinilai tidak akan menggangu momentum pemulihan ekonomi yang sedang berjalan. Alasannya, saat ini kesadaran masyarakat untuk mendapatkan vaksin sudah terbangun dan cukup baik.")
st.write(" ")
st.write("Latar belakang tersebut yang membuat saya ingin tahu apakah benar bahwa kebijakan booster tidak mempengaruhi mobilitas masyarakat maupun pemulihan ekonomi")
st.write("Saya ingin mengetahui apakah kebijakan vaksin  booster tidak mempengaruhi mobilitas masyarakat? Sedangkan jika dilogika setiap pertumbuhan mobilitas berarti dapat mempengaruhi pertumbuhan ekonomi? Atau mungkinkah kesyadaran masyarakat saat ini sudah sangat tinggi untuk melakukan vaksin?")
st.write(" ")
st.markdown("---")

st.title("Kebijakan Pemerintah vs Mobilitas Masyarakat")
st.markdown("**Mobilitas Masyarakat Indonesia saat Pandemi**")
# dataset declaration
df = pd.read_csv('mobility_change_202208012334.csv')

df['date'] = pd.to_datetime(df['date'])

# st.dataframe(df)

# line chart
mobility = df[['date', 'retail_and_recreation', 
'grocery_and_pharmacy', 'park', 'transit', 
'workplace', 'resident']].set_index('date').resample('M').sum()

st.line_chart(mobility)

st.write("Hal yang cukup menarik bahwa kenaikan dan penurunan yang terasa berada pada dua kondisi: 1. Pada saat kasus covid meningkat dan 2. Pada saat libur nasional.")
st.write("Diketahui terdapat tiga gelombang kasus covid yaitu yang pertama terjadi hingga akhir Januari 2021, kedua pada saat adanya varian delta di sekitar pertengahan 2021, serta yang ketiga pada akhir 2021 hingga awal 2022")
st.write("Dalam chart tersebut tidak tampak pengaruh dari kebijakan pemerintah dalam memberikan syarat bagi pelaku perjalanan. Jika kita kembali ke belakang, surat edaran syarat vaksin sudah berlaku sejak bulan November 2021 (Surat Edaran Kasatgas Nomor 22 Tahun 2021)")

st.markdown("---")
# heat map
st.markdown("**Heat Maps perubahan Mobilitas Masyarakat berdasarkan Lokasinya**")
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

st.write("Berikan pilihan pada lokasi 'park' di tahun 2022, pada chart tersebut memiliki sesuatu yang unik terlihat pada musim lebaran 2022 nilai yang cukup tinggi. Pada musim liburan saat itu, umumnya masyarakat lebih memilih ke tempat yang outdoor ketimbang harus ke dalam mall. Sehingga, kebijakan pemerintah disini tidak dapat berlaku.")
st.markdown("---")

st.title("Correlation Analysis")
st.markdown("**Bagaimana Korelasi antara Mobilitas Masyarakat dengan Produk Domestik Bruto**")
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

st.write("Melalui regresi linear di atas, dapat menunjukkan bahwa sangat erat kaitannya antara mobilitas masyarakat dengan pertumbuhan ekonomi. Namun juga, terdapat hal yang berbeda pada data di triwulan 3 2021 dan triwulan 1 2022. Keadaan yang menyimpang dapat disebabkan adanya masalah kesehatan/kenaikan kasus covid pada masa itu namun tidak membuat masyarakat hilang kreativitas untuk meningkatkan perekonomian. Sehingga mobilitas rendah, namun juga dapat meningkatkan perekonomian melalui seperti contohnya bekerja dari rumah atau WFH.")

st.markdown("---")
st.markdown("**Produk Domestik Bruto berdasarkan Lapangan Usaha**")
# cek sektor lapangan usaha
dfl = pd.read_csv('pdb_lap_usaha.csv')

#unpivot DataFrame from wide format to long format
dfl_unpivot = pd.melt(dfl, id_vars='lapangan_usaha', value_vars=['triwulan_2_2021', 'triwulan_3_2021', 'triwulan_4_2021', 'triwulan_1_2022'])

lap = px.bar(dfl_unpivot, x = "variable", y = "value", color = "lapangan_usaha", barmode='group')
st.plotly_chart(lap, use_container_width=True)
st.write("Kontribusi terbesar dalam perekonomian Indonesia terdapat pada sektor industri pengolahan. Berdasarkan data tersebut, penyimpangan yang terjadi pada triwulan 4 2021 dan triwulan 1 2022 secara signifikan disebabkan oleh perubahan hasil usaha sektor pertanian, perhutanan, dan perikanan")
st.markdown("---")
st.markdown("Korelasi antara Kenaikan Vaksinasi dan Mobilitas Masyarakat")
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
st.write("Terdapat korelasi yang kuat antara total vaksinasi dengan nilai mobilitas pada tahun 2020 - 2022 (r = 0,773). Hal ini menunjukkan bahwa kesadaran masyarakat terhadap vaksinasi juga dipengaruhi oleh keinginan mereka untuk meningkatkan mobilitas")

st.markdown("---")
st.title("Insight")
st.write("Varian Covid yang semakin bermutasi memaksa pemerintah membentuk kebijakan baru untuk mendorong masyarakat mendapatkan vaksin. Hal ini dijadikan syarat bagi siapa saja yang menggunakan transportasi umum. Banyak pro dan kontra yang terjadi di masyarakat, tak jarang mereka merasa dirugikan dengan kebijakan ini. Lain halnya dengan bidang ekonomi, orang yang semakin hari semakin kreatif membuat kebijakan ini tidak berpengaruh. Berdasarkan data yang telah disajikan, wawasan yang dapat diberikan bahwa pemerintah harus lebih kreatif dalam memberikan kampanye karena kesadaran masyarakat saat ini cukup baik untuk diberikan vaksin, meski mobilitas sangat berkorelasi dengan pertumbuhan ekonomi, namun di era modern seperti sekarang ini, bekerja melalui WFH juga dapat menumbuhkan perekonomian, kesadaran masyarakat untuk melakukan vaksin juga didukung oleh keinginan mereka untuk meningkatkan mobilitas, sehingga peran kebijakan pemerintah juga berpengaruh besar disini")

st.markdown("---")
st.write("Capstone Project, Tetris Program")
st.write("by Yukiko Irliyani (email: irliyaniyukiko@gmail.com)")
