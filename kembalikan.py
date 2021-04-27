from load import loadGagdetBorrowHistory, loadGagdetReturnHistory, loadGadget
from tambah_history_pengembalian import tambah_history_pengembalian, save

filedata =  loadGagdetBorrowHistory()
header = filedata["header"]
datas = filedata["datas"]
user_datas = []

file_peminjaman = loadGagdetReturnHistory()
data_peminjaman = file_peminjaman["datas"]

file_gadget = loadGadget()
data_gadget = file_gadget["datas"]

def filter_by_user(_id, array_data):
    for data in datas:
        if data[1] == _id:
            user_datas.append(data)

def modify_datas(idx, col, value):
    if col == 4:
        if not (type(value) is int):
            print("Jumlah column value type must be integer or float")
            return
    datas[idx][col] = value

# PINJAM GADGET
def kembalikan():
    num = 1
    for i in user_datas:
        print("{}. {}".format(num, cek_nama(i[2])[0]))
        num += 1
    _id = int(input("Masukkan nomor peminjaman: "))
    tanggal_peminjaman = input("Tanggal pengembalian: ")
    id_gadget = user_datas[_id-1][2]
    data_nama = cek_nama(id_gadget)
    if data_nama[0] != "Not Found":
        tambah_history_pengembalian(_id, tanggal_peminjaman)
        save()
        print("Item {} (x{}) berhasil dikembalikan!".format(data_nama[0], datas[_id-1][4]))
                             

def cek_stok(_id, jumlah):
    found = False
    i = 0
    while not found and i <= len(user_datas):
        if user_datas[i][0] == _id:
            found = True
            if user_datas[i][3] >= jumlah:
                return True
        i += 1
    return False

def cek_nama(_id):
    i = 0
    while i < len(data_gadget):
        if data_gadget[i][0] == _id:
            return (data_gadget[i][1], i)
        i += 1
    return ("Not Found")

filter_by_user("1", datas)