

def open_file(file_name):
    file_handle = open(file_name,"w", encoding="utf-8")
    line = file_handle.readline()
    while line:
        print(line)
        line = file_handle.readline()
    file_handle.close()


def copy_file(file_name, target_file_name):
    src_handle = open(file_name,"r", encoding="utf-8")
    dest_handle = open(target_file_name,"w", encoding="utf-8")

    line = src_handle.readline()

    while(line):
        dest_handle.write(line)
        line = src_handle.readline()
    src_handle.close()
    dest_handle.close()

    