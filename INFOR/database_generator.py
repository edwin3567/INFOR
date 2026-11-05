# File 1: database_generator.py
import sqlite3
import pandas as pd
import os

def inisialisasi_database_dan_ekspor():
    db_file = 'hotel_impact_analysis.db'
    csv_output = 'hasil_export_hotel.csv'
    
    # Jika database belum ada, kita buatkan tabel dan data awal langsung di SQLite
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    # Membuat tabel jika belum ada
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS hotel_reviews (
            id_review INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_hotel TEXT,
            kota TEXT,
            kualitas_kamar INTEGER,
            kualitas_restoran INTEGER,
            kualitas_layanan INTEGER,
            tingkat_kebersihan INTEGER,
            harga_per_malam INTEGER,
            overall_rating REAL,
            tanggal_review TEXT
        )
    ''')
    conn.commit()
    
    # Cek apakah tabel kosong, jika kosong kita beri data dummy/contoh (atau data dari sumber DB)
    cursor.execute("SELECT COUNT(*) FROM hotel_reviews")
    count = cursor.fetchone()[0]
    
    if count == 0:
        print("[INFO] Database kosong, mengisi data awal ke SQLite...")
        # Contoh data langsung ke DB (bisa disesuaikan dengan database aslimu)
        data_dummy = [
            ("Hotel Merdeka", "Jakarta", 8, 7, 9, 8, 750000, 4.5, "2026-01-01"),
            ("Grand Asia", "Bali", 9, 9, 8, 9, 1200000, 4.8, "2026-01-02"),
            ("Sunset Hotel", "Bali", 7, 6, 7, 7, 500000, 3.9, "2026-01-03"),
            ("Melati Inn", "Surabaya", 6, 5, 6, 6, 300000, 3.5, "2026-01-04"),
            ("Royal Palace", "Bandung", 9, 8, 9, 9, 1500000, 4.7, "2026-01-05")
        ]
        cursor.executemany('''
            INSERT INTO hotel_reviews (nama_hotel, kota, kualitas_kamar, kualitas_restoran, kualitas_layanan, tingkat_kebersihan, harga_per_malam, overall_rating, tanggal_review)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', data_dummy)
        conn.commit()

    print(f"[INFO] Sumber data utama menggunakan Database SQLite: '{db_file}'")
    
    # FITUR UTAMA: Mengekspor data dari Database SQLite menjadi file CSV
    df = pd.read_sql("SELECT * FROM hotel_reviews", conn)
    df.to_csv(csv_output, index=False, encoding='utf-8')
    print(f"[INFO] Data dari database berhasil diekspor menjadi file CSV: '{csv_output}'")
    
    conn.close()
    return True

if __name__ == "__main__":
    inisialisasi_database_dan_ekspor()