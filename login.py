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

    # Validasi apakah username dan password yang dimasukkan sudah tepat
    found = False
    while found == False :
        for i in range(len(datas)):
            if (datas[i][2] == username) and (datas[i][4] == password) :
                found = True
                break
        if found == True:  
            print("Selamat datang {}! di kantong ajaib".format(username))
        else:
            print("Password atau Username Anda Salah")
            username = input("Maukkan Username: ")
            password = input("Masukkan Password: ")

                    

