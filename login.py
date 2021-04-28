# PROGRAM  
# procedure mengubah data csv menjadi array

from load import userDatas

# ALGORITMA 

def login():
    global userDatas
    datas = userDatas["datas"]
    # Input data
    username = input("Maukkan Username: ")
    password = input("Masukkan Password: ")

    id_user = ''
    role_user = ''

    # Validasi apakah username dan password yang dimasukkan sudah tepat
    found = False
    while found == False :
        for i in range(len(datas)):
            if (datas[i][2] == username) and (datas[i][4] == password) :
                id_user = datas[i][0]
                role_user = datas[i][5]
                found = True
                break
        if found == True:  
            print("Halo {}! Selamat datang di kantong ajaib!".format(username))
            return (id_user, role_user)
        else:
            print("Password atau Username Anda Salah")
            username = input("Maukkan Username: ")
            password = input("Masukkan Password: ")

                    

