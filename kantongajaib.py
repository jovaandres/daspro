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
import sys

command = ''
while command != "exit":
    command = input(">>>")
    print()
    if command == "login":
        login()
    elif command == "register":
        register()
    elif command == "carirarity":
        cari_rarity()
    elif command == "caritahun":
        cari_tahun()
    elif command == "tambahitem":
        tambah_item()
    elif command == "hapusitem":
        hapus_item()
    elif command == "ubahjumlah":
        ubah_jumlah()
    elif command == "pinjam":
        pinjam_gadget(1)
    elif command == "kembalikan":
        kembalikan()
    elif command == "minta":
        minta_consumable()
    elif command == "riwayatpinjam":
        riwayat_pinjam()
    elif command == "riwayatkembali":
        riwayat_kembali()
    elif command == "riwayatambil":
        riwayat_ambil()
    elif command == "exit":
        sys.exit()
    elif command == "minta":
        minta_consumable()
    else:
        print("Masukkan salah!")
    print()


