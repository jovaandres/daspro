# PROGRAM F01 - Register
from load import loadUser

user_datas = loadUser()
header = user_datas["header"]
datas = user_datas["datas"]

def convert_datas_to_string():
    string_data = ";".join(header) + "\n"
    for arr_data in datas:
        arr_data_all_string = [str(var) for var in arr_data]
        string_data += ";".join(arr_data_all_string)
        string_data += "\n"
    return string_data

def save_register(username):
    datas_as_string = convert_datas_to_string()
    f = open("user.csv","w")
    f.write(datas_as_string)
    f.close()
    print("user", username, "baru berhasil disimpan")

# Username harus unik yaitu antar username di user data tidak  boleh sama
def register():
    nama = input("Masukkan nama: ")
    username = input("masukkan username: ")
    password = input("masukkan password: ")
    alamat = input("masukkan alamat: ")
    found = 0
    while found >= 0 :
        for i in range(len(datas)):
            if (datas[i][2] == username): 
                found += 1 # terdapat username yang sama di csv
                break
        if (found > 0) :        
            print("username pengguna sudah digunakan")
            nama = input("Masukkan nama: ")
            username = input("masukkan username: ")
            password = input("masukkan password: ")
            alamat = input("masukkan alamat: ")
            found = 0
        else:
            found = -1
            role = "user"
            user_baru = [len(datas) + 1,nama,username,alamat,password,role]
            datas.append(user_baru)
            save_register(username)
            