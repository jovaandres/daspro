from savedata import save_all
import sys

def _exit() :
# keluar dari aplikasi
# KAMUS LOKAL
# valid : boolean
# save : character
# ALGORITMA
    valid = False 
    while (not valid) : # mengulang input sampai valid
        save = input ('Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ')
        
        if (save not in 'yYnN') : # input tidak valid
            print ('Input tidak valid')
        else :
            valid = True # input valid
            if (save == 'y') or (save == 'Y') :
               save_all()
            print("Program Selesai")
            sys.exit()
