from load import load

filedata = load("gadget_return_history.csv", "r")
header = filedata["header"]
datas = filedata["datas"]

# TAMBAH HISTORY PEMINJAMAN
def tambah_history_pengembalian(id_peminjaman,tanggal_peminjaman):
    datas.append([len(datas) + 1,id_peminjaman,tanggal_peminjaman])

def convert_datas_to_string():
    string_data = ",".join(header) + "\n"
    for arr_data in datas:
        arr_data_all_string = [str(var) for var in arr_data]
        string_data += ",".join(arr_data_all_string)
        string_data += "\n"
    return string_data

def save():
    data_as_string = convert_datas_to_string()
    f = open("gadget_return_history.csv", "w")
    f.write(data_as_string)
    f.close