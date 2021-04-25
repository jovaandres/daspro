# F07 - Mengubah Jumlah Gadget atau Consumable pada Inventory

bold = '\033[1m'
end = '\033[0m'

def open_csv(file):
    f = open(file,'r',encoding='utf-8-sig')
    raw_lines = f.readlines()
    f.close()
    lines = [raw_line.replace("\n","") for raw_line in raw_lines]
    raw_header = lines.pop(0)
    header = convert_line_to_data(raw_header)
    
    #assign  to arry
    data = []
    for line in lines :
        array_of_data = convert_line_to_data(line)
        real_values = convert_array_data_to_real_values(array_of_data,file)
        data.append(real_values)
    
    data_header = [data,header]
    return data_header

def save_csv(file, data, header):
    datas_as_string = convert_datas_to_string(data,header)
    g = open(file,"w")
    g.write(datas_as_string)
    g.close()

def convert_array_data_to_real_values(array_data, csv):
    arr_cpy = array_data[:]
    if csv == "gadget.csv":
        for i in range(6):
            if(i == 3 or i == 5):
                arr_cpy[i] = int(arr_cpy[i])
    elif csv == "consumable.csv":
        for i in range (5):
            if(i == 3):
                arr_cpy[i] = int(arr_cpy[i])
    elif csv == "consumable_history.csv":
        for i in range (4):
            if(i == 4):
                arr_cpy[i] = int(arr_cpy[i]) 
    return arr_cpy

def convert_line_to_data(line):
    raw_data = []
    tmp = ''
    for i in line :
        if i == ';':
            raw_data.append(tmp)
            tmp = ''
        else :
            tmp +=i
    if tmp : 
        raw_data.append(tmp)

    array_of_data = [data.strip() for data in raw_data]
    return array_of_data

def convert_datas_to_string(data,header):
  string_data = ";".join(header) + "\n"
  for arr_data in data:
    arr_data_all_string = [str(var) for var in arr_data]
    string_data += ";".join(arr_data_all_string)
    string_data += "\n"
  return string_data



#ALGORITMA UTAMA
id_item_valid = ['C','G']
id_item = input("Masukan ID item: ")
print(id_item)
#Cek jenis id item
if (id_item[0] not in id_item_valid):
    print("Gagal menambahkan ID karena ID tidak valid.")
    exit()

#Memilih file mana yang akan dibuka
if id_item[0] == 'G':
    datas = open_csv("gadget.csv")[0]
    header = open_csv("gadget.csv")[1]
elif id_item[0] == 'C':
    datas = open_csv("consumable.csv")[0]
    header = open_csv("consumable.csv")[1]

found = False
i = 0
while (i < len(datas)):
    if datas[i][0] == id_item:
        index_item = i
        item_dipilih = datas[i]
        nama_item = datas[i][1]
        jumlah_item = datas[i][3]
        found = True
        i +=1
    else :
        i+=1
    
if found == False :
    print("Tidak ada item dengan ID tersebut")
    exit()

# for i in range (len(datas)):
#     found = false
#     if datas[i][0] == id_item:
#         index_item = i
#         item_dipilih = datas[i]
#         nama_item = datas[i][1]
#         jumlah_item = datas[i][3]
#         found = True
#         break
        
#     elif id_item not in datas:
#         print("Tidak ada item dengan ID tersebut")
#         exit()

input_jumlah = (input("Masukkan Jumlah : "))
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


print(jumlah_item)
print(datas[0][3])


if id_item[0] == 'G':
    save_csv("gadget.csv",datas,header)
elif id_item[0] == 'C':
    save_csv("consumable.csv",datas,header)


