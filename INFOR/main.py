# File 4: main.py
from database_generator import inisialisasi_database_dan_ekspor
from query_data import ambil_data_sql
from visualisasi_grafik import tampilkan_5_grafik

def main():
    print("Memulai program analisis data hotel berbasis Database SQLite...")
    
    # 1. Inisialisasi database & otomatis ekspor ke CSV
    sukses = inisialisasi_database_dan_ekspor()
    
    if sukses:
        # 2. Ambil data dari database untuk di-query
        df = ambil_data_sql()
        
        print("\n[INFO] Merender 5 grafik analisis...")
        # 3. Visualisasikan dan simpan grafik ke PNG
        tampilkan_5_grafik(df)
        
        print("\n[SUKSES] Seluruh rangkaian program selesai dijalankan!")

if __name__ == "__main__":
    main()