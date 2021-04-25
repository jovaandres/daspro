def load(filename, mode):
    f = open(filename, mode)
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

def convert_line_to_data(line):
    raw_array_of_data = split_by_chr(line, ",")
    array_of_data = [data.strip() for data in raw_array_of_data]
    return array_of_data

def convert_array_data_to_real_values(array_data, filename):
    arr_copy = array_data[:]
    if filename == "gadget_borrow_history.csv":
        for i in range(5):
            if (i == 4):
                arr_copy[i] = int(arr_copy[i])
    elif filename == "gadget.csv":
        for i in range(6):
            if (i == 3 or i == 5):
                arr_copy[i] = int(arr_copy[i])
    elif filename == "user.csv":
        for i in range(6):
            if (i == 0):
                arr_copy[i] = int(arr_copy[i])
    return arr_copy