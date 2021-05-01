import os
import argparse
import sys
database_dir = ''

parser = argparse.ArgumentParser()
parser.add_argument("data")
args = parser.parse_args()

print("Loading...\n")

def split_by_chr(string_data, pattern):
    arr_splitted = []
    new_string = ""
    for i in string_data:
        if (i == pattern):
            arr_splitted.append(new_string)
            new_string = ""
        else:
            new_string += i
    arr_splitted.append(new_string)
    return arr_splitted

def loadData(args):
    global database_dir
    x = os.getcwd()
    x += f'\\{args.data}'
    database_dir = split_by_chr(str(x), "\\")[-1]

if os.path.exists(args.data):
    loadData(args)
    print('Selamat datang di "Kantong Ajaib!"\n')
else:
    print("Tidak ada nama folder yang diberikan !")
    sys.exit()

def convert_line_to_data(line):
    raw_array_of_data = split_by_chr(line, ";")
    array_of_data = [data.strip() for data in raw_array_of_data]
    return array_of_data

def convert_array_data_to_real_values(array_data, filename):
    arr_copy = array_data[:]
    if filename.endswith("gadget_borrow_history.csv"):
        for i in range(6):
            if (i == 4):
                arr_copy[i] = int(arr_copy[i])
            if (i == 5):
                arr_copy[i] = int(arr_copy[i])
    elif filename.endswith("gadget.csv"):
        for i in range(6):
            if (i == 3 or i == 5):
                arr_copy[i] = int(arr_copy[i])
    elif filename.endswith("consumable.csv"):
        for i in range (5):
            if(i == 3):
                arr_copy[i] = int(arr_copy[i])
    elif filename.endswith("consumable_history.csv"):
        for i in range(5):
            if(i == 0 or i == 4):
                arr_copy[i] = int(arr_copy[i])
    return arr_copy

def load(filename):
    f = open(filename, "r")
    raw_lines = f.readlines()
    f.close()
    lines = [raw_line.replace("\n", "") for raw_line in raw_lines]

    raw_header = lines.pop(0)
    header = convert_line_to_data(raw_header)

    datas = []
    for line in lines:
        array_of_data = convert_line_to_data(line)
        real_values = convert_array_data_to_real_values(array_of_data, filename)
        datas.append(real_values)
    
    return {"header": header, "datas": datas}

userhome = os.getcwd()

gadgetDatas = load(f"{userhome}\\{database_dir}\\gadget.csv")

consumableDatas = load(f"{userhome}\\{database_dir}\\consumable.csv")

userDatas = load(f"{database_dir}\\user.csv")

gadgetBorrowHistoryDatas = load(f"{userhome}\\{database_dir}\\gadget_borrow_history.csv")

gadgetReturnHistoryDatas = load(f"{userhome}\\{database_dir}\\gadget_return_history.csv")

consumableHistoryDatas = load(f"{userhome}\\{database_dir}\\consumable_history.csv")