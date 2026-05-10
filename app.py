import streamlit as st
from supabase import create_client

# Mengambil data rahasia dari menu Secrets secara otomatis
url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]

supabase = create_client(url, key)

st.title("DEDIK AI Management")
st.success("Koneksi Berhasil! Ruang kontrol kode sudah ideal.")

# Mencoba menampilkan data dari tabel
try: 
    # Ganti 'produk' dengan nama tabel asli di Supabase Anda
    data = supabase.table("Daftar produk").select("*").execute()
    st.write("Data Database:", data.data)
except Exception as e:
    st.info("Koneksi database aktif, silakan sesuaikan nama tabel Anda.")
    
