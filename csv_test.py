f = open("drama.csv", "r")
raw_lines = f.readlines()
f.close()
lines = [raw_line.replace("\n", "") for raw_line in raw_lines]

def convert_line_to_data(line):
    raw_array_of_data = line.split(",")
    array_of_data = [data.strip() for data in raw_array_of_data]
    return array_of_data

def convert_array_data_to_real_values(array_data):
    arr_copy = array_data[:]
    for i in range(3):
        if (i == 0):
            arr_copy[i] = int(arr_copy[i])
        elif (i == 2):
            arr_copy[i] = float(arr_copy[i])
    return arr_copy

raw_header = lines.pop(0)
header = convert_line_to_data(raw_header)

datas = []
for line in lines:
    array_of_data = convert_line_to_data(line)
    real_values = convert_array_data_to_real_values(array_of_data)
    datas.append(real_values)

def convert_datas_to_string():
    string_data = ",".join(header) + "\n"
    for arr_data in datas:
        arr_data_all_string = [str(var) for var in arr_data]
        string_data += ",".join(arr_data_all_string)
        string_data += "\n"
    return string_data

def modify_datas(idx, col, value):
    if col == 0:
        return
    if col == 2:
        if not (type(value) is int or type(value) is float):
            print("Rating column value type must be integer or float")
            return
    datas[idx][col] = value

modify_datas(0, 2, 8.5)

data_as_string = convert_datas_to_string()
f = open("drama.csv", "w")
f.write(data_as_string)
f.close