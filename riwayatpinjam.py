#riwayatpinjam.py
#F11 - Melihat Riwayat Peminjaman Gadget
#tanggal pembuatan: 17 April 2021

import time as datetime
from load import loadGagdetBorrowHistory

#FUNGSI/PROSEDURAL
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
filedata = loadGagdetBorrowHistory()
header = filedata["header"]
datas = filedata["datas"]

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
        if sorted_list_tanggal[i][0] == datas[j][0]:
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