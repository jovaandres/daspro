# F07 - Mengubah Jumlah Gadget atau Consumable pada Inventory
bold = '\033[1m'
end = '\033[0m'
from load import consumableDatas, consumableHistoryDatas
from datetime import datetime

# def check_item_id (input, range):
#     if (input not in range):
#         print("Tidak ada item dengan ID tersebut")
#         return
    
# ALGORITMA UTAMA
def minta_consumable(id_pengambil):
    global consumableDatas, consumableHistoryDatas
    id_item = input("Masukan ID item: ")
    #Cek jenis id item
    # check_item_id(id_item[0],['C'])

    datas = consumableDatas["datas"]
    header = consumableDatas["header"]
    datas_g =  consumableHistoryDatas["datas"]
    header_g =  consumableHistoryDatas["header"]
    
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

    input_jumlah = int(input("Jumlah : "))
    if input_jumlah <= 0:
        print("Jumlah salah, harus lebih besar dari 0")
        return
    tangga_minta = input("Tanggal permintaan :  ")
    try:
        datetime.strptime(tangga_minta, '%d/%m/%Y')
    except ValueError:
        print("Tanggal salah, harus mengikuti format DD/MM/YYYY")
        return

    if ( jumlah_item - input_jumlah < 0):
        print( bold + str(input_jumlah) + " " + nama_item + end + " gagal diambil karena stok kurang. Stok sekarang: " + str(jumlah_item) + "(< " + str(input_jumlah) + " )")
    elif (jumlah_item - input_jumlah >= 0):
        jumlah_item -= input_jumlah
        datas[index_item][3] -= input_jumlah
        print( bold + str(input_jumlah) + " "+ nama_item + end + " telah berhasil diambil")
    
        history = [1,id_pengambil,id_item,tangga_minta,input_jumlah ]
        datas_g.append(history)
        consumableHistoryDatas = {"header": header_g, "datas": datas_g}

    elif (input_jumlah < 0 ):
        jumlah_item += input_jumlah
        datas[index_item][3] += input_jumlah
        consumableDatas = {"header": header, "datas": datas}
        print( bold + str(input_jumlah) + " " + nama_item + end + " berhasil buang. Stok sekarang: " + str(jumlah_item))