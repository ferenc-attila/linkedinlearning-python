import os

currentDir = os.getcwd()
newDir = "/result"
# TODO: Erre jo lenne valami szebb, platformfuggetlen megoldas (Windows-on most nem is helyesen mukodik)
resultFileName = currentDir + newDir + "/result.txt"


def create_folder():
    if os.listdir(currentDir).__contains__(newDir.replace("/", "")):
        print("Directory exists!")
    try:
        os.mkdir(currentDir + newDir)
# TODO: Itt hianyos jogosultsag miatti problema eseten mi a helyzet?
    except FileNotFoundError as fnfe:
        print(fnfe)
        print("Parent directory doesn't exists!")


def create_list_of_files(current_folder):
    list_of_files = os.listdir(current_folder)
    for name_of_file_or_folder in list_of_files:
        if os.path.isdir(currentDir + "/" + name_of_file_or_folder):
            list_of_files.remove(name_of_file_or_folder)
    return list_of_files


def count_bytes(list_of_files):
    total_byte_count = 0
    for file_name in list_of_files:
        total_byte_count += os.stat(file_name).st_size
    return total_byte_count


def create_file_content(list_of_files):
    file_list_string = ""
    total_byte_count = count_bytes(list_of_files)
    for file_name in list_of_files:
        file_name += "\n"
        file_list_string += file_name
    return "Total bytecount:" + str(total_byte_count) + "\nFiles list:\n--------------\n" + file_list_string


def write_file(result_file_name, list_of_files):
    result_file = open(result_file_name, "w+")
    if result_file.mode == "w+":
        result_file.write(create_file_content(list_of_files))
        result_file.close()


create_folder()
listOfFiles = create_list_of_files(currentDir)
write_file(resultFileName, listOfFiles)
