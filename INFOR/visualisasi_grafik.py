# File 3: visualisasi_grafik.py
import matplotlib.pyplot as plt

def tampilkan_5_grafik(df):
    fig, axes = plt.subplots(3, 2, figsize=(15, 18))

    # Grafik 1: Kualitas Kamar vs Rating
    axes[0, 0].scatter(df['Kualitas Kamar (1-10)'], df['Overall Rating (1-5)'], alpha=0.4, color='royalblue')
    axes[0, 0].set_title('1. Dampak Kualitas Kamar terhadap Rating', fontsize=12, fontweight='bold')
    axes[0, 0].set_xlabel('Skor Kualitas Kamar (1-10)')
    axes[0, 0].set_ylabel('Overall Rating (1-5)')

    # Grafik 2: Rata-rata Rating per Restoran
    df_rest = df.groupby('Kualitas Restoran (1-10)')['Overall Rating (1-5)'].mean().reset_index()
    axes[0, 1].bar(df_rest['Kualitas Restoran (1-10)'], df_rest['Overall Rating (1-5)'], color='darkorange', edgecolor='black')
    axes[0, 1].set_title('2. Rata-rata Rating per Kualitas Restoran', fontsize=12, fontweight='bold')
    axes[0, 1].set_xlabel('Skor Kualitas Restoran')
    axes[0, 1].set_ylabel('Rata-rata Rating')

    # Grafik 3: Dampak Kebersihan
    df_clean = df.groupby('Tingkat Kebersihan (1-10)')['Overall Rating (1-5)'].mean().reset_index()
    axes[1, 0].bar(df_clean['Tingkat Kebersihan (1-10)'], df_clean['Overall Rating (1-5)'], color='forestgreen', edgecolor='black')
    axes[1, 0].set_title('3. Dampak Tingkat Kebersihan terhadap Rating', fontsize=12, fontweight='bold')
    axes[1, 0].set_xlabel('Skor Kebersihan')
    axes[1, 0].set_ylabel('Rata-rata Rating')

    # Grafik 4: Harga vs Rating (Warna = Layanan)
    scatter = axes[1, 1].scatter(
        df['Harga per Malam (IDR)'], 
        df['Overall Rating (1-5)'], 
        c=df['Kualitas Layanan (1-10)'], 
        cmap='viridis', 
        alpha=0.6
    )
    axes[1, 1].set_title('4. Hubungan Harga vs Rating (Warna = Layanan)', fontsize=12, fontweight='bold')
    axes[1, 1].set_xlabel('Harga per Malam (IDR)')
    axes[1, 1].set_ylabel('Overall Rating')
    cbar = fig.colorbar(scatter, ax=axes[1, 1])
    cbar.set_label('Skor Layanan')

    # Grafik 5: Korelasi Faktor
    cols = [
        'Kualitas Kamar (1-10)', 'Kualitas Restoran (1-10)', 
        'Kualitas Layanan (1-10)', 'Tingkat Kebersihan (1-10)', 
        'Harga per Malam (IDR)', 'Overall Rating (1-5)'
    ]
    correlation = df[cols].corr()['Overall Rating (1-5)'].drop('Overall Rating (1-5)')
    axes[2, 0].barh(correlation.index, correlation.values, color='purple', edgecolor='black')
    axes[2, 0].set_title('5. Tingkat Pengaruh (Korelasi) Tiap Faktor', fontsize=12, fontweight='bold')
    axes[2, 0].set_xlabel('Nilai Korelasi (Pearson)')
    axes[2, 0].set_xlim(0, 1)

    # Hapus subplot ke-6 yang kosong
    fig.delaxes(axes[2, 1])

    plt.tight_layout()
    
    # OTOMATIS MENYIMPAN KE FILE PNG
    output_image = 'grafik_analisis_hotel.png'
    plt.savefig(output_image, dpi=300)
    print(f"[INFO] Grafik berhasil dirender dan disimpan otomatis sebagai '{output_image}' di folder proyek!")
    
    plt.show()