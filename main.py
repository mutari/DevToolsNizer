from mongodb import Mongodb
from dotenv import load_dotenv
from funktions import Functions
import os
load_dotenv()

connect = Mongodb()
func = Functions(connect)

while 1:
    input_data = input(":")
    input_data_array = input_data.split(' ')
    cmd_head = input_data_array[0]
    if len(input_data_array) > 1:
        cmd_str = input_data_array[1]
    cmd_args = input_data_array[2:]

    if cmd_head == "get-all":
        func.get_all(cmd_str, cmd_args)
    elif cmd_head == "clear-all":
        if func.alert_comfirm():
            func.clear_all(cmd_str, cmd_args)
    elif cmd_head == "sys-clear":
        os.system("clear")