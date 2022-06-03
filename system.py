import os

MAIN_FILES = ["main.py", "system.py", "ui.py", "config.txt"]
MAIN_DIR = os.getcwd()


def list_2_path(l):
    listOut = list()
    for file in l:
        directory = os.path.join(MAIN_DIR, file)
        listOut.append(directory)
    return listOut


def check_sys_files():
    print("... Checking system files ...")
    files = list_2_path(MAIN_FILES)
    index = 0
    check = True
    try:
        for file in files:
            if os.path.exists(file):
                print(f"... File: {MAIN_FILES[index]} , Found: {files[index]}")
            else:
                print(f"... Missing file: {files[index]}")
                check = False
                break
            index += 1
    except ValueError:
        print("...Something went wrong...")


def raw_file_2_raw_list(fn):
    try:
        with open(fn, encoding='UTF-8') as f:
            li = list()
            for line in f:
                li.append(line)
        return li
    except ValueError:
        print(f'Not found: {fn}')


def strip_list2list(l):
    outList = list()
    for index in range(len(l)):
        if len(l[index].strip()) == 0:
            pass
        else:
            tempTxT = l[index].strip()
            outList.append(tempTxT)

    return outList


def config_2_dict():
    outPut = dict()
    configPath = list_2_path(MAIN_FILES)[3]
    rawList = strip_list2list(raw_file_2_raw_list(configPath))
    for item in range(len(rawList)):
        if rawList[item].find('=') != -1:
            label, value = rawList[item].split('=')
            if value.find(',') != -1:
                valList: list = value.split(',')
                outPut[label] = valList
            else:
                outPut[label] = value
    return outPut
