from load import gadgetDatas

datas = gadgetDatas["datas"]
header = gadgetDatas["header"]

def cari_rarity() :
# Mencari gadget berdasarkan rarity (C, B, A, S)
# KAMUS LOKAL
# i : integer
# ALGORITMA
    rarity = input("Masukkan rarity : ")
    print()
    print("Hasil pencarian: \n")
    for i in range (len(datas)) :
        if (datas[i][4] == rarity) :                               # mencari index dengan rarity yang sama                 
            print("Nama            :", datas[i][1])                # kolom 1 : nama
            print("Deskripsi       :", datas[i][2])                # kolom 2 : deskripsi
            print("Jumlah          :", datas[i][3], "buah")        # kolom 3 : jumlah
            print("Rarity          :", datas[i][4])                # kolom 4 : rarity
            print("Tahun Ditemukan :", datas[i][5])                # kolom 5 : tahun_ditemukan
            print()
        i += 1
    return 