# F07 - Mengubah Jumlah Gadget atau Consumable pada Inventory

bold = '\033[1m'
end = '\033[0m'

from load import gadgetDatas, consumableDatas

#ALGORITMA UTAMA
def ubah_jumlah():
    global gadgetDatas, consumableDatas

    id_item_valid = ['C','G']
    id_item = input("Masukan ID item: ")
    #Cek jenis id item
    if (id_item[0] not in id_item_valid):
        print("Gagal menambahkan ID karena ID tidak valid.")
        return

    #Memilih file mana yang akan dibuka
    filedata = []
    if id_item[0] == 'G':
        filedata = gadgetDatas
    elif id_item[0] == 'C':
        filedata = consumableDatas

    datas = filedata["datas"]
    header = filedata["header"]

    found = False
    i = 0
    while (i < len(datas)):
        if datas[i][0] == id_item:
            index_item = i
            item_dipilih = datas[i]
            nama_item = item_dipilih[1]
            jumlah_item = item_dipilih[3]
            found = True
            i +=1
        else :
            i+=1
        
    if found == False :
        print("Tidak ada item dengan ID tersebut")
        return
        
    input_jumlah = int(input("Masukkan Jumlah : "))
    if type(input_jumlah) != int:
        print("masukkan harus berupa integer")
    else :
        if (input_jumlah + jumlah_item < 0):
            print( bold + str(abs(input_jumlah)) + " " + nama_item + end + " gagal dibuang karena stok kurang. Stok sekarang: " + str(jumlah_item) + "(< " + str(abs(input_jumlah)) + " )")
        elif (input_jumlah > 0 ):
            jumlah_item += input_jumlah
            datas[index_item][3] += input_jumlah
            print( bold + str(abs(input_jumlah)) + " "+ nama_item + end + " berhasil ditambahkan. Stok sekarang: " + str(jumlah_item))
        elif (input_jumlah < 0 ):
            jumlah_item += input_jumlah
            datas[index_item][3] += input_jumlah
            print( bold + str(abs(input_jumlah)) + " " + nama_item + end + " berhasil buang. Stok sekarang: " + str(jumlah_item))

    if id_item[0] == 'G':
        gadgetDatas = {"header": header, "datas": datas}
    elif id_item[0] == 'C':
        consumableDatas = {"header": header, "datas": datas}


