from load import gadgetDatas, gadgetBorrowHistoryDatas, gadgetReturnHistoryDatas, consumableDatas, consumableHistoryDatas, userDatas
import os

def convert_datas_to_string(header, datas):
  string_data = ";".join(header) + "\n"
  for arr_data in datas:
    arr_data_all_string = [str(var) for var in arr_data]
    string_data += ";".join(arr_data_all_string)
    string_data += "\n"
  return string_data

def save_all():
    folder_name = input("Masukkan nama folder penyimpanan: ")
    global gadgetDatas, gadgetBorrowHistoryDatas, gadgetReturnHistoryDatas, consumableDatas, consumableHistoryDatas, userDatas
    listData = [gadgetDatas, gadgetBorrowHistoryDatas, gadgetReturnHistoryDatas, consumableDatas, consumableHistoryDatas, userDatas]
    listFile = ["gadget.csv", "gadget_borrow_history.csv", "gadget_return_history.csv", "consumable.csv", "consumable_history.csv", "user.csv"]
    for i in range(6):
      x = os.getcwd()
      if folder_name not in os.listdir(x):
        os.mkdir(folder_name)
      f = open(f"{folder_name}\\" + listFile[i], "w")
      f.write(convert_datas_to_string(listData[i]["header"], listData[i]["datas"]))
      f.close()