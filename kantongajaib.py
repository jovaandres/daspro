import argparse
import os
from load import loadData

parser = argparse.ArgumentParser()
parser.add_argument("--data", required=True)
args = parser.parse_args()
loadData(args)

from pinjam import pinjam_gadget
from kembalikan import kembalikan
from login import login
from register import register
from tambahitem import tambah_item
from hapusitem import hapus_item
from minta_consumable import minta_consumable
import sys

command = ''
while command != "exit":
    command = input()
    print()
    if command == "pinjam":
        pinjam_gadget(1)
    elif command == "kembalikan":
        kembalikan()
    elif command == "login":
        login()
    elif command == "register":
        register()
    elif command == "tambahitem":
        tambah_item()
    elif command == "hapusitem":
        hapus_item()
    elif command == "exit":
        sys.exit()
    elif command == "minta":
        minta_consumable()
    else:
        print("Masukkan salah!")
    print()


