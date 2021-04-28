#riwayatkembali.py
# F12 - Melihat Riwayat Pengembalian Gadget
#tanggal: 18 April 2021

import time as datetime
from load import gadgetDatas, gadgetReturnHistoryDatas

def tampil_lagi(sorted_datas,idx):
    p = True #kondisi untuk loop while
    while p:
        #Menampilkan riwayat jika sisa jumlah data <= 5
        if len(sorted_datas)-idx<=5:
            for i in range (len(sorted_datas)-idx):
                print("ID Pengembalian      :",sorted_datas[idx+i][0])
                print("Nama Pengembali     :",sorted_datas[idx+i][1])
                # print("Nama Gadget        :",sorted_list_tanggal[i][2])
                print("Tanggal pengembalian :",sorted_datas[idx+i][2])
                print()
            print("Ini adalah akhir dari riwayat pengembalian gadget")
            p = False
        #Menampilkan riwayat jika sisa jumlah data > 5
        else:  #len(sorted_datas)>5
            for i in range (5):
                print("ID Pengembalian      :",sorted_datas[idx+i][0])
                print("Nama Pengembali       :",sorted_datas[idx+i][1])
                # print("Nama Gadget          :",sorted_list_tanggal[idx+i][2])
                print("Tanggal pengembalian :",sorted_datas[idx+i][2])
                print()
            print("Apakah Anda ingin melihat riwayat pengembalian gadget lainnya? (Y/N)")
            parameter = input(">>> ")
            if parameter == 'Y':
                idx += 5
                tampil_lagi(sorted_datas,idx)
            elif parameter == 'N':
                print("Pengaksesan riwayat pengembalian gadget selesai")
            else: 
                print("Terjadi kesalahan saat input")
    return idx   

#ALGORITMA UTAMA

def riwayat_kembali():
    global gadgetDatas, gadgetReturnHistoryDatas

    #Pengaksesan file riwayat pengembalian gadget  dan konversi
    datas = gadgetReturnHistoryDatas["datas"]

    #Pengaksesan file gadget dan konversi
    datas_gadget = gadgetDatas["datas"]

    #Mengurutkan tanggal dan id berdasarkan tanggal
    #Pengembalian secara descending
    list_tanggal=[]
    for i in range (len(datas)):
        tmp = [] #template buat nyimpen nilai id dan tanggal
        tmp.append(str(datas[i][0]))
        tmp.append(datas[i][2])
        for j in range (len(datas_gadget)):
            if datas[i][2] == datas_gadget[j][0]:
                tmp.append(datas_gadget[j][1])
        tmp.append(datas[i][2])
        list_tanggal.append(tmp) #list_tanggal = [[id,tanggal_pengembalian,nama,id_gadget],[..]..]
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
            print("ID Pengembalian      :",sorted_datas[i][0])
            print("Nama Pengembali       :",sorted_datas[i][1])
            # print("Nama Gadget          :",sorted_list_tanggal[i][2])
            print("Tanggal pengembalian :",sorted_datas[i][2])
            print()
        print("Ini adalah akhir dari riwayat pengembalian gadget")
    #Menampilkan riwayat jika jumlah data > 5
    else:  #len(sorted_datas)>5
        for i in range (5):
            print("ID Pengembalian      :",sorted_datas[i][0])
            print("Nama Pengembali       :",sorted_datas[i][1])
            # print("Nama Gadget          :",sorted_list_tanggal[i][2])
            print("Tanggal pengembalian :",sorted_datas[i][2])
            print()
        print("Apakah Anda ingin melihat riwayat pengembalian gadget lainnya? (Y/N)")
        parameter = input(">>> ")
        if parameter == 'Y':
            idx = 5 #indeks inisiai untuk menampilkan data selanjutnya
            tampil_lagi(sorted_datas,idx)
        elif parameter == 'N':
            print("Pengaksesan riwayat pengembalian gadget selesai")
        else: 
            print("Terjadi kesalahan saat input")