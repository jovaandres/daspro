from load import loadGadget
from tambah_history_pinjam import tambah_history_peminjaman, save

filedata = loadGadget()
header = filedata["header"]
datas = filedata["datas"]

# PINJAM GADGET
def pinjam_gadget(id_peminjam):
    _id = input("Masukkan ID item: ")
    tanggal_peminjaman = input("Tanggal peminjaman: ")
    jumlah_peminjaman = int(input("Jumlah peminjaman: "))
    data_nama = cek_nama(_id)
    nama = data_nama[0]
    if nama != "Not Found":
        if cek_stok(_id, jumlah_peminjaman):
            ubah_stok(data_nama[1], jumlah_peminjaman)
            tambah_history_peminjaman(id_peminjam, _id, tanggal_peminjaman, jumlah_peminjaman)
            save()
            print("Item {} (x{}) berhasil dipinjam!".format(nama, jumlah_peminjaman))
        else:
            print("Jumlah item yang tersedia tidak mencukupi permintaan")
    else:
        print("Item dengan ID {} tidak ditemukan!".format(_id))

def ubah_stok(index, jumlah):
    datas[index][3] = datas[index][3] - jumlah
    

def cek_stok(_id, jumlah):
    found = False
    i = 0
    while not found and i <= len(datas):
        if datas[i][0] == _id:
            found = True
            if datas[i][3] >= jumlah:
                return True
        i += 1
    return False

def cek_nama(_id):
    i = 0
    while i < len(datas):
        if datas[i][0] == _id:
            return (datas[i][1], i)
        i += 1
    return ("Not Found")