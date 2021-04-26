#riwayatambil.py
# F13 - Melihat Riwayat Pengambilan Consumable
#tanggal: 18 April 2021

import time as datetime
from load import load

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
                print("ID pengambilan      :",sorted_datas[idx+i][0])
                print("Nama Pengambil      :",sorted_datas[idx+i][1])
                print("Nama Consumable     :",sorted_list_tanggal[i][2])
                print("Tanggal pengambilan :",sorted_datas[idx+i][3])
                print("Jumlah              :",sorted_datas[idx+i][4])
                print()
            print("Ini adalah akhir dari riwayat pengambilan consumable")
            p = False
            exit()
        #Menampilkan riwayat jika sisa jumlah data > 5
        else:  #len(sorted_datas)>5
            for i in range (5):
                print("ID pengambilan      :",sorted_datas[idx+i][0])
                print("Nama Pengambil      :",sorted_datas[idx+i][1])
                print("Nama Consumable     :",sorted_list_tanggal[idx+i][2])
                print("Tanggal pengambilan :",sorted_datas[idx+i][3])
                print("Jumlah              :",sorted_datas[idx+i][4])
                print()
            print("Apakah Anda ingin melihat riwayat pengambilan consumable lainnya? (Y/N)")
            parameter = input(">>> ")
            if parameter == 'Y':
                idx += 5
                tampil_lagi(sorted_datas,idx)
            elif parameter == 'N':
                print("Pengaksesan riwayat pengambilan consumable selesai")
                exit()
            else: 
                print("Terjadi kesalahan saat input")
                exit()
    return idx   

#ALGORITMA UTAMA

#Pengaksesan file riwayat pengambilan consumable  dan konversi
consume_history = load("consumable_history.csv","r")
header = consume_history["header"]
datas = consume_history["datas"]

#Pengaksesan file consumable dan konversi
consumable = load("consumable.csv","r")
header_consumable = consumable["header"]
datas_consumable = consumable["datas"]


#Mengurutkan tanggal dan id berdasarkan tanggal
#pengambilan secara descending
list_tanggal=[]
for i in range (len(datas)):
    tmp = [] #template buat nyimpen nilai id dan tanggal
    tmp.append(str(datas[i][0]))
    tmp.append(datas[i][3])
    for j in range (len(datas_consumable)):
        if datas[i][2] == datas_consumable[j][0]:
            tmp.append(datas_consumable[j][1])
    tmp.append(datas[i][2])
    list_tanggal.append(tmp) #list_tanggal = [[id,tanggal_pengambilan,nama,id_consumable],[..]..]
sorted_list_tanggal = sorted(list_tanggal, key=lambda t: datetime.strptime(t[1], '%d/%m/%Y' ), reverse= True) #t[1] karena posisi tanggal di arraynya
print(sorted_list_tanggal)

#Mengurutkan data berdasarkan tanggal secara descending
sorted_datas = []
for i in range (len(datas)):
    for j in range (len(datas)):
        if int(sorted_list_tanggal[i][0]) == datas[j][0]:
            sorted_datas.append(datas[j])

#for i in range (len(sorted_list_tanggal)):
  #  print(sorted_list_tanggal[i][2])

#Menampilkan riwayat jika jumlah data <= 5
if len(sorted_datas)<=5:
    for i in range (len(sorted_datas)):
        print("ID pengambilan      :",sorted_datas[i][0])
        print("Nama Pengambil      :",sorted_datas[i][1])
        print("Nama Consumable     :",sorted_list_tanggal[i][2])
        print("Tanggal pengambilan :",sorted_datas[i][3])
        print("Jumlah              :",sorted_datas[i][4])
        print()
    print("Ini adalah akhir dari riwayat pengambilan consumable")
#Menampilkan riwayat jika jumlah data > 5
else:  #len(sorted_datas)>5
    for i in range (5):
        print("ID pengambilan      :",sorted_datas[i][0])
        print("Nama Pengambil      :",sorted_datas[i][1])
        print("Nama Consumable     :",sorted_list_tanggal[i][2])
        print("Tanggal pengambilan :",sorted_datas[i][3])
        print("Jumlah              :",sorted_datas[i][4])
        print()
    print("Apakah Anda ingin melihat riwayat pengambilan consumable lainnya? (Y/N)")
    parameter = input(">>> ")
    if parameter == 'Y':
        idx = 5 #indeks inisiai untuk menampilkan data selanjutnya
        tampil_lagi(sorted_datas,idx)
    elif parameter == 'N':
        print("Pengaksesan riwayat pengambilan consumable selesai")
        exit()
    else: 
        print("Terjadi kesalahan saat input")
        exit()