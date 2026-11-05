import sqlite3
import pandas as pd

def ambil_data_sql():
    conn = sqlite3.connect('hotel_impact_analysis.db')
    
    print("=" * 65)
    print("ANALISIS DATABASE RATING HOTEL (TOP 10 HOTEL TERBAIK)")
    print("=" * 65)
    
    query_top10 = '''
        SELECT "ID Review", "Nama Hotel", Kota, "Kualitas Kamar (1-10)", "Overall Rating (1-5)", "Harga per Malam (IDR)"
        FROM hotel_reviews 
        ORDER BY "Overall Rating (1-5)" DESC 
        LIMIT 10
    '''
    df_top10 = pd.read_sql(query_top10, conn)
    print("\n--- TOP 10 HOTEL DENGAN RATING TERTINGGI ---")
    print(df_top10.to_string(index=False))
    print("-" * 65)
    
    df_full = pd.read_sql('SELECT * FROM hotel_reviews', conn)
    conn.close()
    
    return df_full

if __name__ == "__main__":
    ambil_data_sql()