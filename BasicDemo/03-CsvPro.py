
import  csv

def csv_read(file_name):
    csv_file = open(file_name, encoding="utf-8")
    read_handle = csv.reader(csv_file, delimiter=" ", quoting="|")

    for line in read_handle:
        print(",".join(line))

    csv_file.close()

def csv_writ( dest_file):
    csv_file = open(dest_file,"a", encoding="utf-8")
    writer_handle = csv.writer(csv_file)
    writer_handle.writerow("aa", "bb", "cc","dd")
    csv_file.close()
    pass
