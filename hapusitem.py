#hapusitem.py
#F06 - Menghapus Gadget atau Consumables
#tanggal pembuatan: 15 April 2021
#FUNGSI/PROSEDURAL
from load import load

def convert_datas_to_string():
  string_data = ";".join(header) + "\n"
  for arr_data in datas:
    arr_data_all_string = [str(var) for var in arr_data]
    string_data += ";".join(arr_data_all_string)
    string_data += "\n"
  return string_data

#ALGORITMA UTAMA
id_item_valid = ['C','G']
id_item = input("Masukan ID item: ")
#Cek jenis id item
if (id_item[0] not in id_item_valid):
    print("Gagal menambahkan ID karena ID tidak valid.")
    exit()

filedata = []
#Memilih file mana yang akan dibuka
if id_item[0] == 'G':
    filedata = load("gadget.csv","r")
elif id_item[0] == 'C':
    filedata = load("consumable.csv","r")

header = filedata["header"]
datas = filedata["datas"]

para_id = []
for i in range (len(datas)):
    para_id.append(datas[i][0])
for i in range (len(datas)):
    if datas[i][0] == id_item:
        nama_item = datas[i][1]
        item_dipilih = datas[i]
        break
    elif id_item not in para_id:
        print("Tidak ada item dengan ID tersebut.")
        exit()

print("Apakah anda yakin ingin menghapus", ('\033[1m'+ nama_item +'\033[0m'),"(Y/N)?")
parameter = input(">>> ")
if parameter == 'N': #Jika No
    print("Penghapusan item dibatalkan")
    exit()
elif parameter == 'Y': #Jika Yes
    datas.remove(item_dipilih) #Menghapus data yang dipilih
    datas_as_string = convert_datas_to_string()
    #Memilih file mana yang akan dibuka
    if id_item[0] == 'G':
        f = open("gadget.csv","w")
    elif id_item[0] == 'C':
        f = open("consumable.csv","w")
    f.write(datas_as_string)
    f.close()   
    print("\nItem telah berhasil dihapus dari database")
elif parameter != 'Y' or parameter != 'N': #Jika diluar Yes or No
    print("Terjadi kesalahan saat input")
