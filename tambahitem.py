#tambahitem.py
#F05 - Menambah Item 
#tanggal pembuatan: 15 April 2021

from load import gadgetDatas, consumableDatas

def tambah_item():
    global gadgetDatas, consumableDatas
    #ALGORITMA UTAMA
    id_item_valid = ['C','G']
    id_item = input("Masukan ID: ")
    #Cek jenis id item
    if (id_item[0] not in id_item_valid):
        print("Gagal menambahkan ID karena ID tidak valid.")
        exit()

    #Memilih file mana yang akan dibuka
    filedata = []
    if id_item[0] == 'G':
        filedata = gadgetDatas
    elif id_item[0] == 'C':
        filedata = consumableDatas
    
    header = filedata["header"]
    datas = filedata["datas"]

    #Cek ID apakah sudah ada atau belum
    for i in range (len(datas)):
        if id_item == datas[i][0]:
            print("Gagal menambahkan item karena ID sudah ada.")
            exit()  

    #Masukan pengguna selain ID
    nama_item = input("Masukan Nama: ")
    deskripsi_item = input("Masukan Deskripsi: ")
    jumlah_item = int(input("Masukan Jumlah: "))
    rarity_item = input("Masukan Rarity: ")
    #Cek input rarity
    rarity_item_valid = ['C','B','A','S']
    if (rarity_item not in rarity_item_valid):
        print("Input rarity tidak valid!")
        exit()
    if id_item[0] == 'G': #Jika tipe Gadget ada tambahan tahun ditemukan
        tahun_ditemukan = int(input("Masukan tahun ditemukan: "))

    #Ngegabungin data
    item_tambahan = [id_item,nama_item,deskripsi_item,jumlah_item,rarity_item]
    if id_item[0] == 'G': #Jika tipe Gadget ada tambahan tahun ditemukan
        item_tambahan.append(tahun_ditemukan)
    datas.append(item_tambahan)

    #Memilih file mana yang akan dibuka
    if id_item[0] == 'G':
        gadgetDatas = {"header": header, "datas": datas}
    elif id_item[0] == 'C':
        consumableDatas = {"header": header, "datas": datas}

    print("\nItem berhasil ditambahkan ke database")