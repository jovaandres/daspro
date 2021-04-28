import argparse
import os
import sys
from load import loadData
from pinjam import pinjam_gadget
from kembalikan import kembalikan
from login import login
from register import register
from tambahitem import tambah_item
from hapusitem import hapus_item
from minta_consumable import minta_consumable
from cari_rarity import cari_rarity
from cari_tahun import cari_tahun
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
    elif command == "pinjam":
        pinjam_gadget(1)
    elif command == "kembalikan":
        kembalikan()
    elif command == "exit":
        sys.exit()
    elif command == "minta":
        minta_consumable()
    else:
        print("Masukkan salah!")
    print()


