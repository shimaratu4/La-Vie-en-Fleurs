import streamlit as st

# --- DATA HARGA ---
harga_bouquet = {
    "A": 50000,  # Fresh Flower
    "B": 35000,  # Artificial
    "C": 20000   # Pipe Cleaner
}
harga_size = {
    "A": 0,
    "B": 10000,
    "C": 20000
}
harga_aksesoris = {
    "A": 5000,
    "B": 2000,
    "C": 15000,
    "D": 10000,
    "E": 5000
}

# --- KONFIGURASI STREAMLIT ---
st.set_page_config(page_title="𝑳𝒂 𝑽𝒊𝒆 𝒆𝒏 𝑭𝒍𝒆𝒖𝒓𝒔", page_icon="🌷")
st.title("🌷 𝑳𝒂 𝑽𝒊𝒆 𝒆𝒏 𝑭𝒍𝒆𝒖𝒓𝒔")
st.caption("𝒀𝒐𝒖𝒓 𝒑𝒆𝒓𝒔𝒐𝒏𝒂𝒍𝒊𝒛𝒆𝒅 𝒃𝒐𝒖𝒒𝒖𝒆𝒕, 𝒃𝒆𝒂𝒖𝒕𝒊𝒇𝒖𝒍𝒍𝒚 𝒂𝒓𝒓𝒂𝒏𝒈𝒆𝒅")

# --- GAMBAR ATAS ---
st.image(
    "bouquetpp.jpg",
    caption="Celebrate Every Moment with La Vie en Fleurs 💐",
    use_container_width=True
)

# --- PILIH JENIS BOUQUET ---
st.header("1. 𝑷𝒊𝒍𝒊𝒉 𝑱𝒆𝒏𝒊𝒔 𝑩𝒐𝒖𝒒𝒖𝒆𝒕")
jenis_opsi = {
    "A. Fresh Flower 💐 - Rp50.000": "A",
    "B. Artificial 🌼 - Rp35.000": "B",
    "C. Pipe Cleaner 🌸 - Rp20.000": "C"
}
jenis_input = st.selectbox("Pilih jenis bouquet:", list(jenis_opsi.keys()))
kode_jenis = jenis_opsi[jenis_input]
harga_jenis = harga_bouquet[kode_jenis]

# --- GAMBAR JENIS BOUQUET ---
st.image(
    "bouquetjenis.jpg.jpeg",
    caption="CHOOSE UR OWN BOUQUET 💐",
    use_container_width=True
)

# --- PILIH UKURAN ---
st.header("2. 𝑷𝒊𝒍𝒊𝒉 𝑼𝒌𝒖𝒓𝒂𝒏")
ukuran_opsi = {
    "A. Small - Rp0": "A",
    "B. Medium - Rp10.000": "B",
    "C. Large - Rp20.000": "C"
}
ukuran_input = st.radio("Ukuran bouquet:", list(ukuran_opsi.keys()))
kode_ukuran = ukuran_opsi[ukuran_input]
harga_ukuran = harga_size[kode_ukuran]

# --- PILIH AKSESORIS ---
st.header("3. 𝑨𝒅𝒅𝒊𝒕𝒊𝒐𝒏𝒂𝒍 𝑨𝒄𝒄𝒆𝒔𝒔𝒐𝒓𝒊𝒆𝒔 ")

# Catatan penting
st.warning("📌 *Note: Mohon maaf kami tidak menerima request khusus. " \
"Semua produk yang ready hanya tertera di katalog kami.*")

aks_opsi = {
    "A. Pita 🎀 - Rp5.000": "A",
    "B. Kartu Ucapan 📝 - Rp2.000": "B",
    "C. Boneka 🧸 - Rp15.000": "C",
    "D. Lampu LED ✨ - Rp10.000": "D",
    "E. Kupu-kupu 🦋 - Rp5.000": "E"
}
aks_input = st.multiselect("Pilih aksesoris:", list(aks_opsi.keys()))
kode_aks = [aks_opsi[a] for a in aks_input]
harga_aks_total = sum([harga_aksesoris[k] for k in kode_aks])

# --- HITUNG TOTAL ---
total_semua = harga_jenis + harga_ukuran + harga_aks_total

# --- RINGKASAN PESANAN ---
st.header("🧾 𝑹𝒊𝒏𝒈𝒌𝒂𝒔𝒂𝒏 𝑷𝒆𝒔𝒂𝒏𝒂𝒏")
with st.expander("📦 Lihat Detail Pesanan"):
    st.write(f"- **Jenis bouquet:** {kode_jenis} ({jenis_input}) → Rp{harga_jenis}")
    st.write(f"- **Ukuran bouquet:** {kode_ukuran} ({ukuran_input}) → Rp{harga_ukuran}")
    if kode_aks:
        st.write(f"- **Aksesoris:** {', '.join(kode_aks)} → Rp{harga_aks_total}")
    else:
        st.write("- **Aksesoris:** Tidak ada")
    st.markdown(f"### 💰 Total Pesanan: Rp{total_semua}")

# --- TOMBOL PESAN ---
if st.button("✅ Konfirmasi Pesanan"):
    st.success("Pesanan berhasil! 💌 Silakan hubungi kami untuk menyelesaikan pembayaran.")

# --- KONTAK PERSON ---
st.markdown("""
### 📞 ** 𝑪𝒐𝒏𝒕𝒂𝒄𝒕 𝑷𝒆𝒓𝒔𝒐𝒏**

📱 **WhatsApp:** 0857-2490-8874 (Shima Ratu Donita)  
📸 **Instagram:** [@shimaratu4](https://instagram.com/shimaratu4)  
💳 **Payment:** Transfer Bank, Shopeepay, Gopay, Dana  
💬 **Pertanyaan/pesanan khusus/konfirmasi pembayaran:** Silahkan hubungi kami.
""", unsafe_allow_html=True)

# --- GAMBAR TAMBAHAN BAWAH ---
st.image(
    "bouquetlast.jpg",
    caption="🌸Choose your dream Bouquet !",
    use_container_width=True
)