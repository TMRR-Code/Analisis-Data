import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

days = pd.read_csv("days_clean.csv")
hours = pd.read_csv("hours_clean.csv") 

# Contoh DataFrame untuk ilustrasi (gantilah dengan DataFrame Anda)
data = {
    'datetime': pd.to_datetime(hours['datetime']),
    'date': pd.to_datetime(days['dteday']),
    'casual_day': days["casual"],
    'casual_hour': hours["casual"],
    'hour': hours["hr"],
    'day': hours["weekday"],
    'total': hours["cnt"],
    'registered_day': days["registered"],
    'registered_hour': hours["registered"]
}
df = pd.DataFrame(data)

# Membuat tab untuk grafik
tab1,tab2,tab3,tab4,tab5,tab6 = st.tabs(["Grafik Casual 1", "Grafik Registered 1",
                               "Grafik Casual 2","Grafik Registered 2",
                               "Grafik Total Penggunaan/Hari",
                               "Grafik Total Penggunaan/Waktu"])


# Tab pertama: Menampilkan grafik pengguna casual
with tab1:
    # Membuat figure dan 1 subplot untuk casual
    fig, ax = plt.subplots(figsize=(18, 5))
    ax.plot(df['date'], df['casual_day'], label='Pengguna Casual', color='b', linewidth=1.5)
    ax.set_title('Jumlah Pengguna Casual Berdasarkan Waktu', fontsize=14)
    ax.set_xlabel('Waktu Penyewaan Sepeda', fontsize=12)
    ax.set_ylabel('Jumlah Penyewaan Sepeda', fontsize=12)
    ax.legend()
    plt.xticks(rotation=45)
    ax.grid(True)
    plt.tight_layout()
    
    # Menampilkan grafik di tab 1
    st.pyplot(fig)

# Tab kedua: Menampilkan grafik pengguna registered
with tab2:
    # Membuat figure dan 1 subplot untuk registered
    fig, ax = plt.subplots(figsize=(18, 5))
    ax.plot(df['date'], df['registered_day'], label='Pengguna Registered', color='g', linewidth=1.5)
    ax.set_title('Jumlah Pengguna Registered Berdasarkan Waktu', fontsize=14)
    ax.set_xlabel('Waktu Penyewaan Sepeda', fontsize=12)
    ax.set_ylabel('Jumlah Penyewaan Sepeda', fontsize=12)
    ax.legend()
    plt.xticks(rotation=45)
    ax.grid(True)
    plt.tight_layout()
    
    # Menampilkan grafik di tab 2
    st.pyplot(fig)

with tab3:
    # Membuat figure dan 1 subplot untuk casual
    fig, ax = plt.subplots(figsize=(18, 5))
    ax.plot(df['datetime'], df['casual_hour'], label='Pengguna Casual', color='b', linewidth=1.5)
    ax.set_title('Jumlah Pengguna Casual Berdasarkan Tanggal dan Waktu', fontsize=14)
    ax.set_xlabel('Waktu Penyewaan Sepeda', fontsize=12)
    ax.set_ylabel('Jumlah Penyewaan Sepeda', fontsize=12)
    ax.legend()
    plt.xticks(rotation=45)
    ax.grid(True)
    plt.tight_layout()
    
    # Menampilkan grafik di tab 1
    st.pyplot(fig)

with tab4:
    # Membuat figure dan 1 subplot untuk registered
    fig, ax = plt.subplots(figsize=(18, 5))
    ax.plot(df['datetime'], df['registered_hour'], label='Pengguna Registered', color='g', linewidth=1.5)
    ax.set_title('Jumlah Pengguna Registered Berdasarkan Tanggal dan Waktu', fontsize=14)
    ax.set_xlabel('Waktu Penyewaan Sepeda', fontsize=12)
    ax.set_ylabel('Jumlah Penyewaan Sepeda', fontsize=12)
    ax.legend()
    plt.xticks(rotation=45)
    ax.grid(True)
    plt.tight_layout()
    
    # Menampilkan grafik di tab 2
    st.pyplot(fig)

with tab5:
    # Menghitung total penyewaan sepeda untuk setiap hari
    daily_rentals = df.groupby('day')['total'].sum().reset_index()

    # Menampilkan hari dengan pemakaian sepeda paling banyak
    max_day = daily_rentals.loc[daily_rentals['total'].idxmax()]

    # Membuat histogram di Streamlit
    st.title("Histogram Pemakaian Sepeda Setiap Hari")

    # Membuat grafik histogram
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(daily_rentals['day'], daily_rentals['total'], color='skyblue')

    # Menambahkan label dan judul
    ax.set_xlabel('Hari', fontsize=12)
    ax.set_ylabel('Jumlah Penyewaan Sepeda', fontsize=12)
    ax.set_title('Pemakaian Sepeda Setiap Hari', fontsize=14)

    # Menandai hari dengan pemakaian sepeda paling banyak
    ax.annotate(f'Maksimum: {max_day["total"]}', 
                xy=(max_day['day'], max_day['total']), 
                xytext=(max_day['day'], max_day['total'] + 5),
                arrowprops=dict(facecolor='black', arrowstyle='->'))

    # Menampilkan grid
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    # Menampilkan grafik di Streamlit
    st.pyplot(fig)

with tab6:
    # Mengelompokkan berdasarkan hari (weekday) dan jam (hr), lalu menghitung total penyewaan
    grouped = df.groupby(['day', 'hour'])['total'].sum().reset_index()

    # Mengurutkan hasil berdasarkan hari dan jam
    grouped_sorted = grouped.sort_values(by=['day', 'hour'])

    # Membuat pivot table untuk format plotting
    pivot_table = grouped_sorted.pivot(index='hour', columns='day', values='total').fillna(0)

    # Membuat grafik di Streamlit
    st.title("Pemakaian Sepeda Berdasarkan Hari dan Jam")

    # Membuat grafik bar
    fig, ax = plt.subplots(figsize=(12, 6))
    pivot_table.plot(kind='bar', stacked=False, ax=ax)

    # Menambahkan label dan judul
    ax.set_xlabel('Jam (hour)', fontsize=12)
    ax.set_ylabel('Jumlah Penyewaan Sepeda', fontsize=12)
    ax.set_title('Pemakaian Sepeda Berdasarkan Hari dan Jam', fontsize=14)

    # Menampilkan grid
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    # Menampilkan legenda
    ax.legend(title='Hari', bbox_to_anchor=(1.05, 1), loc='upper left')

    # Menampilkan grafik di Streamlit
    st.pyplot(fig)