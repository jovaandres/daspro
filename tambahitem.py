#tambahitem.py
#F05 - Menambah Item 
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
id_item = input("Masukan ID: ")
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

datas_as_string = convert_datas_to_string()
#Memilih file mana yang akan dibuka
if id_item[0] == 'G':
    f = open("gadget.csv","w")
elif id_item[0] == 'C':
    f = open("consumable.csv","w")
f.write(datas_as_string)
f.close()

print("\nItem berhasil ditambahkan ke database")