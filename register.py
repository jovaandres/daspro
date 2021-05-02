# PROGRAM F01 - Register
from load import userDatas

# Username harus unik yaitu antar username di user data tidak  boleh sama
def register():
    global userDatas
    header = userDatas["header"]
    datas = userDatas["datas"]

    nama = input("Masukkan nama: ")
    username = input("masukkan username: ")
    password = input("masukkan password: ")
    alamat = input("masukkan alamat: ")
    found = 0
    for i in range(len(datas)):
        if (datas[i][1] == username): 
            found += 1 # terdapat username yang sama di csv
            break
    if (found > 0) :        
        print("username pengguna sudah digunakan")
        return
    else:
        found = -1
        role = "User"
        print(f"User {nama} telah berhasil register ke dalam Kantong Ajaib!")
        user_baru = [str(len(datas) + 1), nama, username, alamat, password, role]
        datas.append(user_baru)
        userDatas = {"header": header, "datas": datas}
            