def read_file(file_path:str):
    input_file = open(file_path, 'r')
    return input_file

def write_file(file_path:str):
    input_file = open(file_path, 'w')
    return input_file

def close_file(file_input):
    file_input.close()