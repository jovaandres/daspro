from load import loadData
from login import login
from register import register
from cari_rarity import cari_rarity
from cari_tahun import cari_tahun
from tambahitem import tambah_item
from hapusitem import hapus_item
from ubah_jumlah_gadget import ubah_jumlah
from pinjam import pinjam_gadget
from kembalikan import kembalikan
from minta_consumable import minta_consumable
from minta_consumable import minta_consumable
from riwayatpinjam import riwayat_pinjam
from riwayatkembali import riwayat_kembali
from riwayatambil import riwayat_ambil
from savedata import save_all
from _help import _help
from _exit import _exit

print("Silahkan Login Terlebih Dahulu\n")

userdata = login()
id_user = userdata[0]
role_user = userdata[1]

command = ''
while command != "exit":
    command = input(">>> ")
    print()
    if command == "login":
        userdata = login()
        id_user = userdata[0]
        role_user = userdata[1]
    elif command == "register":
        if role_user == "Admin":
            register()
        else:
            print("Masukan salah!")
    elif command == "carirarity":
        cari_rarity()
    elif command == "caritahun":
        cari_tahun()
    elif command == "tambahitem":
        if role_user == "Admin":
            tambah_item()
        else:
            print("Masukan salah!")
    elif command == "hapusitem":
        if role_user == "Admin":
            hapus_item()
        else:
            print("Masukan salah!")
    elif command == "ubahjumlah":
        if role_user == "Admin":
            ubah_jumlah()
        else:
            print("Masukan salah!")
    elif command == "minta":
        if role_user == "User":
            minta_consumable(id_user)
        else:
            print("Masukan salah!")
    elif command == "pinjam":
        if role_user == "User":
            pinjam_gadget(id_user)
        else:
            print("Masukan salah!")
    elif command == "kembalikan":
        if role_user == "User":
            kembalikan(id_user)
        else:
            print("Masukan salah!")
    elif command == "riwayatpinjam":        
        if role_user == "Admin":
            riwayat_pinjam()
        else:
            print("Masukan salah!")
    elif command == "riwayatkembali":
        if role_user == "Admin":
            riwayat_kembali()
        else:
            print("Masukan salah!")    
    elif command == "riwayatambil":
        if role_user == "Admin":
            riwayat_ambil()
        else:
            print("Masukan salah!")  
    elif command == "save":
        save_all()
    elif command == "help":
        _help()
    elif command == "exit":
        _exit()
    else:
        print("Masukkan salah!")
    print()

