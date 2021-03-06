#riwayatpinjam.py
#F11 - Melihat Riwayat Peminjaman Gadget
#tanggal pembuatan: 17 April 2021

import time as datetime
from load import gadgetBorrowHistoryDatas, gadgetDatas, userDatas

#FUNGSI/PROSEDURAL

def tampil_lagi(sorted_datas,idx):
    p = True #kondisi untuk loop while
    while p:
        #Menampilkan riwayat jika sisa jumlah data <= 5
        if len(sorted_datas)-idx<=5:
            for i in range (len(sorted_datas)-idx):
                print("ID Peminjaman      :",sorted_datas[idx+i][0])
                print("Nama Pengambil     :",cek_nama_user(sorted_datas[idx+i][1]))
                print("Nama Gadget        :",cek_nama(sorted_datas[idx+i][2]))
                print("Tanggal peminjaman :",sorted_datas[idx+i][3])
                print("Jumlah             :",sorted_datas[idx+i][4])
                print()
            print("Ini adalah akhir dari riwayat peminjaman gadget")
            p = False
        #Menampilkan riwayat jika sisa jumlah data > 5
        else:  #len(sorted_datas)>5
            for i in range (5):
                print("ID Peminjaman      :",sorted_datas[idx+i][0])
                print("Nama Pengambil     :",cek_nama_user(sorted_datas[idx+i][1]))
                print("Nama Gadget        :",cek_nama(sorted_datas[idx+i][2]))
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
            else: 
                print("Terjadi kesalahan saat input")
    return idx   

#ALGORITMA UTAMA

def riwayat_pinjam():
    global gadgetBorrowHistoryDatas
    #Pengaksesan file dan konversi
    datas = gadgetBorrowHistoryDatas["datas"]

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
            print("Nama Pengambil     :",cek_nama_user(sorted_datas[i][1]))
            print("Nama Gadget        :",cek_nama(sorted_datas[i][2]))
            print("Tanggal peminjaman :",sorted_datas[i][3])
            print("Jumlah             :",sorted_datas[i][4])
            print()
        print("Ini adalah akhir dari riwayat peminjaman gadget")
    #Menampilkan riwayat jika jumlah data > 5
    else:  #len(sorted_datas)>5
        for i in range (5):
            print("ID Peminjaman      :",sorted_datas[i][0])
            print("Nama Pengambil     :",cek_nama_user(sorted_datas[i][1]))
            print("Nama Gadget        :",cek_nama(sorted_datas[i][2]))
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
        else: 
            print("Terjadi kesalahan saat input")

def cek_nama_user(_id):
    global userDatas
    i = 0
    while i < len(userDatas["datas"]):
        if userDatas["datas"][i][0] == _id:
            return userDatas["datas"][i][2]
        i += 1
    return ("Not Found")

def cek_nama(_id):
    global gadgetDatas
    i = 0
    while i < len(gadgetDatas["datas"]):
        if gadgetDatas["datas"][i][0] == _id:
            return gadgetDatas["datas"][i][1]
        i += 1
    return ("Not Found")