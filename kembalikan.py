from load import load
from tambah_history_pengembalian import tambah_history_pengembalian, save

filedata = load("gadget_borrow_history.csv", "r")
header = filedata["header"]
datas = filedata["datas"]
user_datas = []

file_peminjaman = load("gadget.csv", "r")
data_peminjaman = file_peminjaman["datas"]

def filter_by_user(_id, array_data):
    for data in datas:
        if data[1] == _id:
            user_datas.append(data)

def convert_datas_to_string():
    string_data = ",".join(header) + "\n"
    for arr_data in datas:
        arr_data_all_string = [str(var) for var in arr_data]
        string_data += ",".join(arr_data_all_string)
        string_data += "\n"
    return string_data

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
        print("{}. {}".format(num, i[2]))
        num += 1
    _id = int(input("Masukkan nomor peminjaman: "))
    tanggal_peminjaman = input("Tanggal pengembalian: ")
    id_gadget = datas[_id-1][2]
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
    while i < len(data_peminjaman):
        if data_peminjaman[i][0] == _id:
            return (data_peminjaman[i][1], i)
        i += 1
    return ("Not Found")

filter_by_user("1", datas)
kembalikan()

data_as_string = convert_datas_to_string()
f = open("gadget_borrow_history.csv", "w")
f.write(data_as_string)
f.close