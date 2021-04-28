from load import loadGadget

filedata = loadGadget()
arr_gadget = filedata["datas"]
header = filedata["header"]

def cari_tahun() :
# Mencari gadget berdasarkan tahun ditemukan
# KAMUS LOKAL
# i : integer
# tahun : integer
# found : boolean
# kat : string 
# ALGORITMA
    tahun = int(input("Masukkan tahun: "))
    kat = input("Masukkan kategori: ")
    print()
    print("Hasil pencarian: \n")
        
    i = 0
    found = False
    while (i < (len(arr_gadget))) :
        if (kat == "=") :
            if (arr_gadget[i][5] == tahun) :                        # mencari index dengan tahun yang sama
                found = True                                        
                print("Nama:", arr_gadget[i][1])                    # kolom 1 : nama
                print("Deskripsi:", arr_gadget[i][2])               # kolom 2 : deskripsi
                print("Jumlah:", arr_gadget[i][3], "buah")          # kolom 3 : jumlah
                print("Rarity:", arr_gadget[i][4])                  # kolom 4 : rarity
                print("Tahun Ditemukan:", arr_gadget[i][5])         # kolom 5 : tahun_ditemukan
                print()
            i += 1
        elif (kat == ">") :
            if (arr_gadget[i][5] > tahun) :                         
                found = True
                print("Nama:", arr_gadget[i][1])
                print("Deskripsi:", arr_gadget[i][2])
                print("Jumlah:", arr_gadget[i][3], "buah")
                print("Rarity:", arr_gadget[i][4])
                print("Tahun Ditemukan:", arr_gadget[i][5])
                print()
            i += 1
        elif (kat == "<") :
            if (arr_gadget[i][5] < tahun) :                        
                found = True
                print("Nama:", arr_gadget[i][1])
                print("Deskripsi:", arr_gadget[i][2])
                print("Jumlah:", arr_gadget[i][3], "buah")
                print("Rarity:", arr_gadget[i][4])
                print("Tahun Ditemukan:", arr_gadget[i][5])
                print()
            i += 1
        elif (kat == ">=") :
            if (arr_gadget[i][5] >= tahun) :                       
                found = True
                print("Nama:", arr_gadget[i][1])
                print("Deskripsi:", arr_gadget[i][2])
                print("Jumlah:", arr_gadget[i][3], "buah")
                print("Rarity:", arr_gadget[i][4])
                print("Tahun Ditemukan:", arr_gadget[i][5])
                print()
            i += 1
        else :                                                      # (kat == "<=")
            if (arr_gadget[i][5] <= tahun) :
                found = True
                print("Nama:", arr_gadget[i][1])
                print("Deskripsi:", arr_gadget[i][2])
                print("Jumlah:", arr_gadget[i][3], "buah")
                print("Rarity:", arr_gadget[i][4])
                print("Tahun Ditemukan:", arr_gadget[i][5])
                print()
            i += 1
    if (found == False) :
            print("Tidak ada gadget yang ditemukan")
                    
        
