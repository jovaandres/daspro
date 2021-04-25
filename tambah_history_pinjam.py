f = open("gadget_borrow_history.csv", "r")

from load import load

filedata = load("gadget_borrow_history.csv", "r")
header = filedata["header"]
datas = filedata["datas"]

# TAMBAH HISTORY PEMINJAMAN
def tambah_history_peminjaman(_id,id_peminjam,id_gadget,tanggal_peminjaman,jumlah):
    datas.append([_id,id_peminjam,id_gadget,tanggal_peminjaman,int(jumlah)])

def convert_datas_to_string():
    string_data = ",".join(header) + "\n"
    for arr_data in datas:
        arr_data_all_string = [str(var) for var in arr_data]
        string_data += ",".join(arr_data_all_string)
        string_data += "\n"
    return string_data

def save():
    data_as_string = convert_datas_to_string()
    f = open("gadget_borrow_history.csv", "w")
    f.write(data_as_string)
    f.close