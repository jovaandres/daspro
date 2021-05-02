from load import gadgetBorrowHistoryDatas, gadgetReturnHistoryDatas, gadgetDatas
from datetime import datetime

header = gadgetBorrowHistoryDatas["header"]
datas = gadgetBorrowHistoryDatas["datas"]

header_pengembalian = gadgetReturnHistoryDatas["header"]
datas_pengembalian = gadgetReturnHistoryDatas["datas"]

header_gadget = gadgetDatas["header"]
data_gadget = gadgetDatas["datas"]

def filter_by_user(_id, array_data):
    user_datas = []
    for data in datas:
        if (data[1] == _id) and not data[5]:
            user_datas.append(data)
    return user_datas

# PINJAM GADGET
def kembalikan(id_peminjam):
    global gadgetReturnHistoryDatas, gadgetBorrowHistoryDatas, gadgetDatas
    user_datas = filter_by_user(id_peminjam, datas)
    num = 1
    for i in user_datas:
        print("{}. {}".format(num, cek_nama(i[2])[0]))
        num += 1
    _id = int(input("Masukkan nomor peminjaman: "))
    if _id not in range(1, len(user_datas) + 1):
        print("Input salah")
        return
    tanggal_peminjaman = input("Tanggal pengembalian: ")
    try:
        datetime.strptime(tanggal_peminjaman, '%d/%m/%Y')
    except ValueError:
        print("Tanggal salah, harus mengikuti format DD/MM/YYYY")
        return
    id_gadget = user_datas[_id-1][2]
    data_nama = cek_nama(id_gadget)
    
    if data_nama[0] != "Not Found":
        datas_pengembalian.append([str(len(datas) + 1), _id, tanggal_peminjaman])
        gadgetReturnHistoryDatas = {"header": header_pengembalian, "datas": datas_pengembalian}
        mark_as_returned(user_datas[_id-1][0])
        ubah_stok(id_gadget, user_datas[_id-1][4])
        gadgetBorrowHistoryDatas = {"header": header, "datas": datas}
        gadgetDatas = {"header": header_gadget, "datas": data_gadget}
        print("Item {} (x{}) berhasil dikembalikan!".format(data_nama[0], datas[_id-1][4]))
                             
def cek_nama(_id):
    i = 0
    while i < len(data_gadget):
        if data_gadget[i][0] == _id:
            return (data_gadget[i][1], i)
        i += 1
    return ("Not Found")

def mark_as_returned(_id):
    i = 0
    while i < len(datas):
        if datas[i][0] == _id:
            datas[i][5] = 1
            return
        i += 1
    return

def ubah_stok(id_gadget, jumlah):
    i = 0
    while i <= len(data_gadget):
        if data_gadget[i][0] == id_gadget:
            data_gadget[i][3] = data_gadget[i][3] + jumlah
            return
        i += 1
    return False
    