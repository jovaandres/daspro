#hapusitem.py
#F06 - Menghapus Gadget atau Consumables
#tanggal pembuatan: 15 April 2021
#FUNGSI/PROSEDURAL
def convert_array_data_to_real_values(array_data):
  arr_cpy = array_data[:]
  if len(arr_cpy)==6:
    for i in range(6):
        if(i == 3 or i == 5):
            arr_cpy[i] = int(arr_cpy[i])
  elif len(arr_cpy)==5:
      for i in range (5):
        if(i == 3):
            arr_cpy[i] = int(arr_cpy[i]) 
  return arr_cpy

def convert_line_to_data(line):
    raw_data = []
    tmp = ''
    for i in line:
        if i == ';':
            raw_data.append(tmp)
            tmp = ''
        else: 
            tmp += i
    if tmp :
        raw_data.append(tmp)
    
    array_of_data = [data.strip() for data in raw_data]
    return array_of_data

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

#Memilih file mana yang akan dibuka
if id_item[0] == 'G':
    f = open("gadget.csv","r")
elif id_item[0] == 'C':
    f = open("consumable.csv","r")

#Pengaksesan file csv
raw_lines = f.readlines()
f.close()
lines = [raw_line.replace('\n','') for raw_line in raw_lines]
raw_header = lines.pop(0)
header = convert_line_to_data(raw_header)
datas=[]
for line in lines:
  array_of_data = convert_line_to_data(line)
  real_values = convert_array_data_to_real_values(array_of_data)
  datas.append(real_values)

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
