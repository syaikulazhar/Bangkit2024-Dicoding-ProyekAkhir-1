import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

main_df = pd.read_csv("main_data.csv")

# Analisis pertama
# Mengubah tipe data kolom order_purchase_timestamp ke datetime
main_df['order_purchase_timestamp'] = pd.to_datetime(main_df['order_purchase_timestamp'])

# Menghitung jumlah pembelian harian
daily_purchase_counts = main_df['order_purchase_timestamp'].dt.date.value_counts().sort_index().reset_index()
daily_purchase_counts.columns = ['purchase_date', 'purchase_count']

# Menemukan tanggal dengan pembeli terbanyak
max_purchase_date = daily_purchase_counts.loc[daily_purchase_counts['purchase_count'].idxmax()]['purchase_date']
max_purchase_count = daily_purchase_counts['purchase_count'].max()

# Menampilkan Informasi #1 di Streamlit
st.title('Analisis Pembelian Harian')
st.write(f'Tanggal dengan Pembelian Terbanyak: {max_purchase_date}')
st.write(f'Jumlah Pembelian: {max_purchase_count}')

# Visualisasi menggunakan barchart untuk pembelian harian
fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(daily_purchase_counts['purchase_date'], daily_purchase_counts['purchase_count'], color='blue')
ax.set_title('Jumlah Pembelian per Tanggal')
ax.set_xlabel('Tanggal Pembelian')
ax.set_ylabel('Jumlah Pembelian')
plt.xticks(rotation=45)

# Tampilkan data
st.pyplot(fig)

# Analisis kedua
# Hitung jumlah produk yang ada disetiap kategori
category_counts = main_df['product_category_name'].value_counts()

# Menemukan kategori terbanyak
max_category = category_counts.idxmax()
max_category_count = category_counts.max()

# Menampilkan informasi #2 di Streamlit
st.title('Analisis Kategori Produk')
st.write(f'Kategori dengan Produk Terbanyak: {max_category}')
st.write(f'Jumlah Produk: {max_category_count}')

# Melakukan visualisasi menggunakan barchart
plt.figure(figsize=(12, 6))
bars = plt.bar(category_counts.index, category_counts, color='green')
plt.title('Jumlah Produk per Kategori')
plt.xlabel('Kategori Produk')
plt.ylabel('Jumlah Produk')
plt.xticks(rotation=45, ha='right')

# Tampilkan data
st.pyplot(plt)
