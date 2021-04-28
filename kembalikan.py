from load import gadgetBorrowHistoryDatas, gadgetReturnHistoryDatas, gadgetDatas

datas = gadgetBorrowHistoryDatas["datas"]
user_datas = []

header_pengembalian = gadgetReturnHistoryDatas["header"]
datas_pengembalian = gadgetReturnHistoryDatas["datas"]

data_gadget = gadgetDatas["datas"]

def filter_by_user(_id, array_data):
    for data in datas:
        if data[1] == _id and not data[5]:
            user_datas.append(data)

def modify_datas(idx, col, value):
    if col == 4:
        if not (type(value) is int):
            print("Jumlah column value type must be integer or float")
            return
    datas[idx][col] = value

# PINJAM GADGET
def kembalikan():
    global gadgetReturnHistoryDatas
    num = 1
    for i in user_datas:
        print("{}. {}".format(num, cek_nama(i[2])[0]))
        num += 1
    _id = int(input("Masukkan nomor peminjaman: "))
    tanggal_peminjaman = input("Tanggal pengembalian: ")
    id_gadget = user_datas[_id-1][2]
    data_nama = cek_nama(id_gadget)
    if data_nama[0] != "Not Found":
        datas_pengembalian.append([len(datas) + 1, _id, tanggal_peminjaman])
        gadgetReturnHistoryDatas = {"header": header_pengembalian, "datas": datas_pengembalian}
        print("Item {} (x{}) berhasil dikembalikan!".format(data_nama[0], datas[_id-1][4]))
                             
def cek_nama(_id):
    i = 0
    while i < len(data_gadget):
        if data_gadget[i][0] == _id:
            return (data_gadget[i][1], i)
        i += 1
    return ("Not Found")

filter_by_user("1", datas)