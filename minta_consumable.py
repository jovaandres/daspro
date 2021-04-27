# F07 - Mengubah Jumlah Gadget atau Consumable pada Inventory
bold = '\033[1m'
end = '\033[0m'
from load import loadConsumable, loadConsumableHistory

id_pengambil = 1

def save_csv(file, data, header):
    datas_as_string = convert_datas_to_string(data,header)
    g = open(file, "w")
    g.write(datas_as_string)
    g.close()

def convert_datas_to_string(data,header):
  string_data = ";".join(header) + "\n"
  for arr_data in data:
    arr_data_all_string = [str(var) for var in arr_data]
    string_data += ";".join(arr_data_all_string)
    string_data += "\n"
  return string_data

def check_item_id (input, range):
    if (input not in range):
        print("Tidak ada item dengan ID tersebut")
        exit()
    
# ALGORITMA UTAMA
def minta_consumable():
    id_item = input("Masukan ID item: ")
    #Cek jenis id item
    check_item_id(id_item[0],['C'])

    filedata = loadConsumable()
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
        exit()


    input_jumlah = int(input("Jumlah : "))
    tangga_minta = input("Tanggal permintaan :  ")

    if ( jumlah_item - input_jumlah < 0):
        print( bold + str(abs(input_jumlah)) + " " + nama_item + end + " gagal diambil karena stok kurang. Stok sekarang: " + str(jumlah_item) + "(< " + str(abs(input_jumlah)) + " )")
    elif (jumlah_item - input_jumlah >= 0):
        jumlah_item -= input_jumlah
        datas[index_item][3] -= input_jumlah
        print( bold + str(abs(input_jumlah)) + " "+ nama_item + end + " telah berhasil diambil")
    
        filedata_g = loadConsumableHistory()
        datas_g =  filedata_g["datas"]
        header_g =  filedata_g["header"]
        history = [1,id_pengambil,id_item,tangga_minta,input_jumlah ]
        datas_g.append(history)
        save_csv("consumable_history.csv",datas_g,header_g)

    elif (input_jumlah < 0 ):
        jumlah_item += input_jumlah
        datas[index_item][3] += input_jumlah
        print( bold + str(abs(input_jumlah)) + " " + nama_item + end + " berhasil buang. Stok sekarang: " + str(jumlah_item))