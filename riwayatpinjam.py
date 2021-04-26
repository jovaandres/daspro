#riwayatpinjam.py
#F11 - Melihat Riwayat Peminjaman Gadget
#tanggal pembuatan: 17 April 2021

import time as datetime

#FUNGSI/PROSEDURAL
def convert_array_data_to_real_values(array_data):
    arr_cpy = array_data[:]
    for i in range(5):
        if(i == 0 or i == 4):
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

def tampil_lagi(sorted_datas,idx):
    p = True #kondisi untuk loop while
    while p:
        #Menampilkan riwayat jika sisa jumlah data <= 5
        if len(sorted_datas)-idx<=5:
            for i in range (len(sorted_datas)-idx):
                print("ID Peminjaman      :",sorted_datas[idx+i][0])
                print("Nama Pengambil     :",sorted_datas[idx+i][1])
                print("Nama Gadget        :",sorted_datas[idx+i][2])
                print("Tanggal peminjaman :",sorted_datas[idx+i][3])
                print("Jumlah             :",sorted_datas[idx+i][4])
                print()
            print("Ini adalah akhir dari riwayat peminjaman gadget")
            p = False
            exit()
        #Menampilkan riwayat jika sisa jumlah data > 5
        else:  #len(sorted_datas)>5
            for i in range (5):
                print("ID Peminjaman      :",sorted_datas[idx+i][0])
                print("Nama Pengambil     :",sorted_datas[idx+i][1])
                print("Nama Gadget        :",sorted_datas[idx+i][2])
                print("Tanggal peminjaman :",sorted_datas[idx+i][3])
                print("Jumlah             :",sorted_datas[idx+i][4])
                print()
            print("Apakah Anda ingin melihat riwayat peminjaman gadget lainnya? (Y/N)")
            parameter = input(">>> ")
            if parameter == 'Y':
                idx += 5
                tampil_lagi(sorted_datas,idx)
            elif parameter == 'N':
                print("Pengaksesan riwayat peminjaman gadget selesai")
                exit()
            else: 
                print("Terjadi kesalahan saat input")
                exit()
    return idx   

#ALGORITMA UTAMA

#Pengaksesan file dan konversi
f = open("gadget_borrow_history.csv","r")
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

#Mengurutkan tanggal dan id berdasarkan tanggal
#Pengembalian secara descending
list_tanggal=[]
for i in range (len(datas)):
    tmp = [] #template buat nyimpen nilai id dan tanggal
    tmp.append(str(datas[i][0]))
    tmp.append(datas[i][3])
    list_tanggal.append(tmp) #list_tanggal = [[id,tanggal_peminjaman],[..]..]
sorted_list_tanggal = sorted(list_tanggal, key=lambda t: datetime.strptime(t[1], '%d/%m/%Y' ), reverse= True) #t[1] karena posisi tanggal di arraynya

#Mengurutkan data berdasarkan tanggal secara descending
sorted_datas = []
for i in range (len(datas)):
    for j in range (len(datas)):
        if int(sorted_list_tanggal[i][0]) == datas[j][0]:
            sorted_datas.append(datas[j])

#Menampilkan riwayat jika jumlah data <= 5
if len(sorted_datas)<=5:
    for i in range (len(sorted_datas)):
        print("ID Peminjaman      :",sorted_datas[i][0])
        print("Nama Pengambil     :",sorted_datas[i][1])
        print("Nama Gadget        :",sorted_datas[i][2])
        print("Tanggal peminjaman :",sorted_datas[i][3])
        print("Jumlah             :",sorted_datas[i][4])
        print()
    print("Ini adalah akhir dari riwayat peminjaman gadget")
#Menampilkan riwayat jika jumlah data > 5
else:  #len(sorted_datas)>5
    for i in range (5):
        print("ID Peminjaman      :",sorted_datas[i][0])
        print("Nama Pengambil     :",sorted_datas[i][1])
        print("Nama Gadget        :",sorted_datas[i][2])
        print("Tanggal peminjaman :",sorted_datas[i][3])
        print("Jumlah             :",sorted_datas[i][4])
        print()
    print("Apakah Anda ingin melihat riwayat peminjaman gadget lainnya? (Y/N)")
    parameter = input(">>> ")
    if parameter == 'Y':
        idx = 5 #indeks inisiai untuk menampilkan data selanjutnya
        tampil_lagi(sorted_datas,idx)
    elif parameter == 'N':
        print("Pengaksesan riwayat peminjaman gadget selesai")
        exit()
    else: 
        print("Terjadi kesalahan saat input")
        exit()