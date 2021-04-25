from load import load

filedata = load("gadget_borrow_history.csv", "r")
header = filedata["header"]
datas = filedata["datas"]
user_datas = []

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
    _id = input("Masukkan nomor peminjaman: ")
    tanggal_peminjaman = input("Tanggal pengembalian: ")
    nama = cek_nama(_id)

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
    found = False
    i = 0
    while not found and i <= len(datas):
        if datas[i][0] == _id:
            found = True
            return datas[i][1]
        i += 1
    return "Not Found"

def save_to_history(_id, tanggal, jumlah):
    return print("Saved")

filter_by_user("1", datas)
kembalikan()

data_as_string = convert_datas_to_string()
f = open("gadget_borrow_history.csv", "w")
f.write(data_as_string)
f.close