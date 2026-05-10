import streamlit as st
from supabase import create_client

# 1. Konfigurasi Database (Sudah sesuai gambar 1000049422.jpg Anda)
URL = "https://xdttzqyucjcoheskrrvj.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InhkdHR6cXl1Y2pjb2hlc2tycnZqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzgzMzg1MzgsImV4cCI6MjA5MzkxNDUzOH0r33ZK8WWCcVBbbaPjqMmepCgaWvd6UJdSmspfaJfclc
supabase = create_client(URL, KEY)

# 2. Tampilan Aplikasi
st.set_page_config(page_title="DEDIK AI - Stok", layout="centered")
st.title("📱 DEDIK AI Management")

menu = st.sidebar.selectbox("Pilih Menu", ["Cek Stok", "Tambah Barang", "Kasir"])

if menu == "Cek Stok":
    st.subheader("📦 Daftar Barang")
    try:
        res = supabase.table("produk").select("*").execute()
        if res.data:
            st.table(res.data)
        else:
            st.info("Belum ada data barang.")
    except Exception as e:
        st.error(f"Gagal mengambil data: {e}")

elif menu == "Tambah Barang":
    st.subheader("🆕 Tambah Barang Baru")
    with st.form("form_tambah"):
        nama = st.text_input("Nama Barang")
        stok = st.number_input("Jumlah Stok", min_value=0)
        jual = st.number_input("Harga Jual (Rp)", min_value=0)
        submit = st.form_submit_button("Simpan Barang")
        
        if submit:
            data = {"nama": nama, "stok": stok, "harga_jual": jual}
            supabase.table("produk").insert(data).execute()
            st.success(f"✅ Berhasil menyimpan: {nama}")

elif menu == "Kasir":
    st.subheader("💰 Catat Penjualan")
    st.write("Fitur ini akan membantu Anda mengurangi stok secara otomatis.")
    # Fitur kasir akan kita kembangkan setelah ini
