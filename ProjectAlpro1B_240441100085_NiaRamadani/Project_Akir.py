def ecommerce():
    produk = {} 
    Keranjang = {}  
    favorit = []  
    order = []  

    while True:
        print("\n===== TOKO FASHION CIWI-CIWI =====")
        print("1. Login sebagai Penjual")
        print("2. Login sebagai Pembeli")
        print("3. Keluar")
        print("====================================")

        pilihan_login = input("Pilih menu (1-3): ")
        if pilihan_login == "1":
            if login_penjual():
                mode_penjual(produk, order)
        elif pilihan_login == "2":
            if login_pembeli():
                mode_pembeli(produk, Keranjang, favorit, order)
        elif pilihan_login == "3":
            print("Terima kasih telah menggunakan Toko Fashion Ciwi-Ciwi!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
print
def login_penjual():
    print("\n************ LOGIN ADMIN ************")
    username = input("Masukkan username penjual: ")
    password = input("Masukkan password penjual: ")
    if username == "admin" and password == "1234":
        print("Login sebagai penjual berhasil!")
        return True
    else:
        print("Login gagal! Username atau password salah.")
        return False

def login_pembeli():
    print("\n************ LOGIN USER ************")
    username = input("Masukkan username pembeli: ")
    password = input("Masukkan password pembeli: ")
    print(f"Login berhasil! Selamat datang di TOKO FASHION CIWI-CIWI, {username}!")
    return True

def mode_penjual(produk, order):
    while True:
        print("\n**** SELAMAT DATANG DI DASHBOARD ADMIN ****")
        print("1. Tambah Produk (Create)")
        print("2. Lihat Daftar Produk (Read)")
        print("3. Perbarui Produk (Update)")
        print("4. Hapus Produk (Delete)")
        print("5. Lihat Status Pesanan")
        print("6. Update Status Pesanan")
        print("7. Logout")
        print("*********************************************")

        pilihan = input("Pilih menu (1-7): ")
        if pilihan == "1":
            create_produk(produk)
        elif pilihan == "2":
            read_produk(produk)
        elif pilihan == "3":
            update_produk(produk)
        elif pilihan == "4":
            delete_produk(produk)
        elif pilihan == "5":
            lihat_orderan(order)
        elif pilihan == "6":
           update_status_pengiriman(order)
        elif pilihan == "7":
            print("Logout berhasil. Kembali ke menu utama.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def create_produk(produk):
    print("*********************************************")
    nama = input("Masukkan nama produk: ")
    if nama in produk:
        print(f"Produk '{nama}' sudah ada.")
    else:
        Harga = input("Masukkan harga produk: ")
        deskripsi = input("Masukkan deskripsi produk: ")  
        stok = input("Masukkan jumlah stok produk: ")
        
        if Harga.isdigit() and float(Harga) > 0 and stok.isdigit() and int(stok) >= 0:
            produk[nama] = {"Harga": float(Harga), "Deskripsi": deskripsi, "Stok": int(stok)}
            print(f"Produk '{nama}' berhasil ditambahkan.")
        else:
            print("Harga atau stok tidak valid. Masukkan angka positif.")
        print("*********************************************")

def read_produk(produk):
    if not produk:
        print("Belum ada produk yang tersedia.")
    else:
        print("*********************************************")
        print("Daftar Produk:")
        for nama, info in produk.items():
            stok_info = "Stok habis" if info["Stok"] == 0 else f"Stok: {info['Stok']}"
            print(f" {nama}: Rp {info['Harga']:,.2f} ({stok_info})")
            print(f"   Deskripsi: {info['Deskripsi']}")
        print("*********************************************")


def mode_pembeli(produk, Keranjang, favorit, order):
    while True:
        print("\n**** SELAMAT DATANG DI TOKO FASHION CIWI-CIWI ****")
        print("1. Cari produk ")
        print("2. Tambah ke Keranjang")
        print("3. Lihat Keranjang")
        print("4. Checkout")
        print("5. Lihat Pesanan")
        print("6. Tambah Produk ke Favorit")
        print("7. Lihat Produk Favorit")
        print("8. Beri Penilaian Produk")
        print("9. Logout")
        print("****************************************************")

        pilihan = input("Pilih menu (1-9): ")
        print()
        if pilihan == "1":
            cari_produk(produk)
        elif pilihan == "2":
            Tambah_Keranjang(produk, Keranjang)
        elif pilihan == "3":
            lihat_keranjang(Keranjang)
        elif pilihan == "4":
            checkout(Keranjang,produk, order)
        elif pilihan == "5":
            lihat_orderan(order)
        elif pilihan == "6":
            tambah_ke_favorit(produk, favorit)
        elif pilihan == "7":
            lihat_favorit(produk,favorit)
        elif pilihan == "8":
            merating(produk,order)
        elif pilihan == "9":
            print("Logout berhasil. Kembali ke menu utama.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def cari_produk(produk):
    print("~*~*~*~*~*~*~*~* KATEGORI PRODUK *~*~*~*~*~*~*~*~")
    kategori_produk = {
        "Make Up": [],
        "Baju": [],
        "Celana": [],
        "Aksesoris": [],
        "Hijab": [],
        "Tas": [],
        "Skincare": [],
        "Sepatu": [],
    }

    for nama, info in produk.items():
        kategori_ditemukan = False
        for kategori in kategori_produk.keys():
            if kategori.lower() in nama.lower():
                kategori_produk[kategori].append((nama, info))
                kategori_ditemukan = True
                break
        if not kategori_ditemukan:
            kategori_produk["Lainnya"].append((nama, info))

    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
    print("\nKategori yang Tersedia:")
    for idx, kategori in enumerate(kategori_produk.keys(), 1):
        print(f"{idx}. {kategori}")

    pilihan = input("\nPilih kategori (masukkan nomor): ")
    if pilihan.isdigit() and 1 <= int(pilihan) <= len(kategori_produk):
        kategori_terpilih = list(kategori_produk.keys())[int(pilihan) - 1]
        items = kategori_produk[kategori_terpilih]
        print(f"\nProduk dalam kategori '{kategori_terpilih}':")
        if items:
            for index, (nama, info) in enumerate(items, 1):
                print(f" {index}. {nama}: Rp {info['Harga']:,.2f}")
                print(f"   Deskripsi: {info['Deskripsi']}")
                print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
        else:
            print("  Tidak ada produk dalam kategori ini.")
    else:
        print("Pilihan tidak valid.")
        
def update_produk(produk):
    print("*********************************************")
    if not produk:
        print("Belum ada produk yang tersedia untuk diperbarui.")
    else:
        print("Daftar Produk:")
        for index, nama in enumerate(produk.keys(), 1):
            print(f"{index}. {nama}")

        nama = input("\nMasukkan nama produk yang ingin diperbarui: ")
        if nama not in produk:
            print(f"Produk '{nama}' tidak ditemukan.")
        else:
            harga_baru = input(f"Masukkan harga baru untuk '{nama}': ")
            if harga_baru.isdigit() and float(harga_baru) > 0:
                produk[nama]["Harga"] = float(harga_baru)
                print(f"Harga produk '{nama}' berhasil diperbarui.")
            else:
                print("Harga tidak valid. Masukkan angka positif.")
            print("*********************************************")
def delete_produk(produk):
    if not produk:
        print("Belum ada produk yang tersedia untuk dihapus.")
    else:
        print("\nDaftar Produk:")
        for index, nama in enumerate(produk.keys(), 1):
            print(f"{index}. {nama}")

        nama = input("\nMasukkan nama produk yang ingin dihapus: ")
        if nama in produk:
            del produk[nama]
            print(f"Produk '{nama}' berhasil dihapus.")
        else:
            print(f"Produk '{nama}' tidak ditemukan.")

def Tambah_Keranjang(produk, Keranjang):
    print("~*~*~*~*~*~*~*~* KERANJANG PRODUK *~*~*~*~*~*~*~*~")
    nama = input("Masukkan nama produk yang ingin ditambahkan ke keranjang: ")
    if nama not in produk:
        print(f"Produk '{nama}' tidak ditemukan.")
    else:
        quantity = input("Masukkan jumlah: ")
        if quantity.isdigit() and int(quantity) > 0:
            quantity = int(quantity)
            if produk[nama]["Stok"] < quantity:
                print(f"Stok tidak cukup. Hanya tersedia {produk[nama]['Stok']} unit.")
            else:
                if nama in Keranjang:
                    Keranjang[nama]["quantity"] += quantity
                else:
                    Keranjang[nama] = {"quantity": quantity, "Harga": produk[nama]["Harga"]}
                produk[nama]["Stok"] -= quantity  # Mengurangi stok setelah produk ditambahkan ke keranjang
                print(f"Produk '{nama}' berhasil ditambahkan ke keranjang.")
        else:
            print("Jumlah tidak valid. Masukkan angka positif.")
            print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
def lihat_keranjang(Keranjang):
    if not Keranjang:
        print("Keranjang kosong.")
        return

    while True:
        print("\n~*~*~*~*~*~*~*~* KERANJANG SAYA *~*~*~*~*~*~*~*~")
        total_harga = 0
        for i, (nama, info) in enumerate(Keranjang.items(), 1):
            subtotal = info['quantity'] * info['Harga']
            total_harga += subtotal
            print(f"{i}. {nama}: {info['quantity']} x Rp {info['Harga']:,.2f} = Rp {subtotal:,.2f}")
        print(f"\nTotal: Rp {total_harga:,.2f}")
        print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
        print("\nOpsi:")
        print("1. Tambah jumlah barang")
        print("2. Hapus barang")
        print("3. Kembali ke menu sebelumnya")

        pilihan = input("Pilih opsi (1-3): ").strip()
        if pilihan == "1":
            nama = input("Masukkan nama produk yang ingin ditambah jumlahnya: ").strip()
            if nama in Keranjang:
                jumlah_tambah = input("Masukkan jumlah tambahan: ").strip()
                if jumlah_tambah.isdigit() and int(jumlah_tambah) > 0:
                    Keranjang[nama]['quantity'] += int(jumlah_tambah)
                    print(f"Jumlah produk '{nama}' berhasil ditambahkan.")
                else:
                    print("Jumlah tambahan tidak valid. Masukkan angka positif.")
            else:
                print(f"Produk '{nama}' tidak ditemukan di keranjang.")
        elif pilihan == "2":
            nama = input("Masukkan nama produk yang ingin dihapus dari keranjang: ").strip()
            if nama in Keranjang:
                del Keranjang[nama]
                print(f"Produk '{nama}' berhasil dihapus dari keranjang.")
            else:
                print(f"Produk '{nama}' tidak ditemukan di keranjang.")
        elif pilihan == "3":
            print("Kembali ke menu sebelumnya.")
            print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            
import re

def checkout(Keranjang, produk, order):
    print("~*~*~*~*~*~*~*~* CHECKOUT *~*~*~*~*~*~*~*~")
    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
    if not Keranjang:
        print("Keranjang belanja kosong.")
        return

    print("\nMasukkan informasi pembeli:")
    nama_pembeli = input("Nama pembeli: ").strip()
    alamat_pembeli = input("Alamat tujuan pengiriman: ").strip()

    total_ongkir = 0
    total_harga_produk = 0

    print("\nBerikut daftar produk dalam keranjang:")
    for nama, info in Keranjang.items():
        if nama not in produk or "Harga" not in produk[nama]:
            print(f"Produk '{nama}' tidak memiliki informasi harga. Silakan perbarui daftar produk.")
            continue

        harga_satuan = produk[nama]["Harga"]
        jumlah = info["quantity"]
        harga_total_produk = harga_satuan * jumlah
        total_harga_produk += harga_total_produk

        berat_gram = 0
        if "Deskripsi" in produk[nama]:
            deskripsi = produk[nama]["Deskripsi"]
            berat_match = re.search(r'(\d+(\.\d+)?)\s*(gram|g)', deskripsi, re.IGNORECASE)
            if berat_match:
                berat_gram = float(berat_match.group(1))

        if berat_gram <= 0:
            while True:
                try:
                    berat_gram = float(input(f"Masukkan berat (gram) untuk {jumlah} unit {nama}: "))
                    if berat_gram > 0:
                        break
                    else:
                        print("Berat harus lebih dari 0.")
                except ValueError:
                    print("Masukkan berat dalam angka valid.")

        total_berat_gram = berat_gram * jumlah
        ongkos_produk = 8000 * ((total_berat_gram // 1000) + (1 if total_berat_gram % 1000 != 0 else 0))
        total_ongkir += ongkos_produk

        print(f"{nama}: {jumlah} unit x Rp {harga_satuan:,.2f} = Rp {harga_total_produk:,.2f}")
        print(f"Berat total: {total_berat_gram:.0f} gram, Ongkir: Rp {ongkos_produk:,.2f}")

    total_bayar = total_harga_produk + total_ongkir
    print(f"\nTotal harga produk: Rp {total_harga_produk:,.2f}")
    print(f"Total ongkos kirim: Rp {total_ongkir:,.2f}")
    print(f"Total yang harus dibayar: Rp {total_bayar:,.2f}")

    konfirmasi = input("Apakah Anda ingin melanjutkan checkout? (y/n): ").strip().lower()
    if konfirmasi == "y":
        order.append({
            "Nama Pembeli": nama_pembeli,
            "Alamat Tujuan": alamat_pembeli,
            "Keranjang": Keranjang.copy(),
            "Status": "Sedang Proses Pengemasan",
            "Ongkos Kirim": total_ongkir,
            "Total Harga Produk": total_harga_produk,
            "Total Pembayaran": total_bayar
        })
        Keranjang.clear()
        print(f"Checkout berhasil! Pesanan atas nama {nama_pembeli} sedang diproses.")
        print("\n~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
    else:
        print("Checkout dibatalkan.")
        
def lihat_orderan(order):
    if not order:
        print("\nTidak ada pesanan yang sedang diproses.")
    else:
        print("~*~*~*~*~*~*~*~* STATUS PESANAN *~*~*~*~*~*~*~*~")
        for idx, pesanan in enumerate(order, start=1):
            print(f"\nPesanan {idx}:")
            print(f"Nama Pembeli   : {pesanan['Nama Pembeli']}")
            print(f"Alamat Tujuan  : {pesanan['Alamat Tujuan']}")
            print(f"Status Pesanan : {pesanan['Status']}")
            print(f"Ongkos Kirim   : Rp {pesanan['Ongkos Kirim']:,.2f}")
            print(f"Total Harga    : Rp {pesanan['Total Harga Produk']:,.2f}")
            print(f"Total Bayar    : Rp {pesanan['Total Pembayaran']:,.2f}")
            print("\nProduk dalam pesanan:")
            for nama_produk, info in pesanan["Keranjang"].items():
                print(f"- {nama_produk}: {info['quantity']} x Rp {info['Harga']:,.2f}")
        print("\n~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")

def update_status_pengiriman(order):
    if not order:
        print("Tidak ada pesanan untuk diperbarui statusnya.")
        return

    print("\n=================== DAFTAR PESANAN ===================")
    for idx, pesanan in enumerate(order, start=1):
        print(f"\nPesanan {idx}:")
        print(f"Nama Pembeli   : {pesanan['Nama Pembeli']}")
        print(f"Alamat Tujuan  : {pesanan['Alamat Tujuan']}")
        print(f"Status Pesanan : {pesanan['Status']}")
        print(f"Ongkos Kirim   : Rp {pesanan['Ongkos Kirim']:,.2f}")
        print(f"Total Bayar    : Rp {pesanan['Total Pembayaran']:,.2f}")
        print("\nProduk dalam pesanan:")
        for nama_produk, info in pesanan["Keranjang"].items():
            print(f"- {nama_produk}: {info['quantity']} x Rp {info['Harga']:,.2f}")

    try:
        pilihan = int(input("\nMasukkan nomor pesanan yang ingin diperbarui (0 untuk batal): "))
        if pilihan == 0:
            print("Kembali ke menu sebelumnya.")
            return
        if pilihan < 1 or pilihan > len(order):
            print("Pilihan tidak valid.")
            return

        pesanan = order[pilihan - 1]
        print(f"\nPesanan yang dipilih:\nNama Pembeli: {pesanan['Nama Pembeli']}\nStatus saat ini: {pesanan['Status']}")
        print("\nPilih status pengiriman baru:")
        print("1. Sedang Dikirim")
        print("2. Sampai di Lokasi Tujuan")
        print("3. Kembali")

        status_pilihan = input("Masukkan pilihan status (1-3): ")
        print("\n=====================================================")

        if status_pilihan == "1":
            pesanan["Status"] = "Sedang Dikirim"
            print("Status berhasil diperbarui: Sedang Dikirim")
        elif status_pilihan == "2":
            pesanan["Status"] = "Sampai di Lokasi Tujuan"
            print("Status berhasil diperbarui: Sampai di Lokasi Tujuan")
        elif status_pilihan == "3":
            print("Kembali ke menu sebelumnya.")
        else:
            print("Pilihan tidak valid.")
    except ValueError:
        print("Masukkan nomor valid.")



def tambah_ke_favorit(produk, favorit):
    nama = input("Masukkan nama produk yang ingin ditambahkan ke favorit: ")
    if nama not in produk:
        print(f"Produk '{nama}' tidak ditemukan.")
    elif nama in favorit:
        print(f"Produk '{nama}' sudah ada di daftar favorit.")
    else:
        favorit.append(nama)
        print(f"Produk '{nama}' berhasil ditambahkan ke daftar favorit.")

def lihat_favorit(produk, favorit):
    while True:
        print("\n~**~**~**~** DAFTAR FAVORIT ANDA **~**~**~**")
        if not favorit:
            print("Daftar favorit kosong.")
        else:
            for idx, nama in enumerate(favorit, start=1):
                print(f"{idx}. {nama}")
       
        print("\nPilihan:")
        print("1. Tambah Produk ke Favorit")
        print("2. Hapus Produk dari Favorit")
        print("3. Kembali ke Menu Pembeli")
        print("\n~**~**~**~**~**~**~**~**~**~**~**~**~**~**~**")
        pilihan = input("Pilih menu (1-3): ")
        if pilihan == "1":
            tambah_ke_favorit(produk, favorit)
        elif pilihan == "2":
            hapus_favorit(favorit)
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def tambah_ke_favorit(produk, favorit):
    nama = input("Masukkan nama produk yang ingin ditambahkan ke favorit: ")
    if nama not in produk:
        print(f"Produk '{nama}' tidak ditemukan.")
    elif nama in favorit:
        print(f"Produk '{nama}' sudah ada di daftar favorit.")
    else:
        favorit.append(nama)
        print(f"Produk '{nama}' berhasil ditambahkan ke daftar favorit.")

def hapus_favorit(favorit):
    if not favorit:
        print("Daftar favorit kosong.")
        return

    print("\nDaftar Produk Favorit:")
    for idx, nama in enumerate(favorit, start=1):
        print(f"{idx}. {nama}")

    pilihan = input("Masukkan nomor produk yang ingin dihapus (0 untuk batal): ")
    if pilihan.isdigit():
        pilihan = int(pilihan)
        if 1 <= pilihan <= len(favorit):
            produk_dihapus = favorit.pop(pilihan - 1)
            print(f"Produk '{produk_dihapus}' berhasil dihapus dari daftar favorit.")
        elif pilihan == 0:
            print("Penghapusan dibatalkan.")
        else:
            print("Pilihan tidak valid.")
    else:
        print("Masukkan nomor yang valid.")


def merating(produk, order):
    print("\n********** BERIKAN PENILAIAN PRODUK **********")
    nama = input("Masukkan nama produk yang ingin diberi penilaian: ")

    telah_dibeli = False
    for pesanan in order:
        if nama in pesanan["Keranjang"]:
            telah_dibeli = True
            break

    if not telah_dibeli:
        print(f"Produk '{nama}' belum pernah di-checkout. Anda hanya dapat memberi penilaian pada produk yang telah dibeli.")
        return

    rating = input("Masukkan penilaian (1-5): ")
    if rating.isdigit() and 1 <= int(rating) <= 5:
        if "Rating" not in produk[nama]:
            produk[nama]["Rating"] = []
        produk[nama]["Rating"].append(int(rating))
        print(f"Anda telah memberikan penilaian {rating} untuk produk '{nama}'. Terima kasih!")
        print("*********************************************")
    else:
        print("Penilaian tidak valid. Masukkan angka antara 1 dan 5.")
        print("*********************************************")

ecommerce()