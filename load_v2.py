import argparse
import os
import sys

parser = argparse.ArgumentParser()
parser.add_argument("nama_folder")
folder = parser.parse_args()

if os.path.exists(folder.nama_folder):
    print(folder.nama_folder)
    os.chdir(folder.nama_folder)
    print("current working file is " + os.getcwd())
    print('Selamat datang di "Kantong Ajaib!"')
else:
    print("Tidak ada nama folder yang diberikan !")
    sys.exit()

