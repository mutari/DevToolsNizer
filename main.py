from mongodb import Mongodb
from dotenv import load_dotenv
from funktions import Functions
load_dotenv()

connect = Mongodb()
func = Functions(connect)

while(1):
    input_data = input(":")
    input_data_array = input_data.split(' ')
    cmd_head = input_data_array[0]
    cmd_str = input_data_array[1]
    cmd_args = input_data_array[2:]

    print(cmd_head, cmd_str, cmd_args)

    if(cmd_head == "get-all"):
        func.get_all(cmd_str, cmd_args)