import os


def problema1(target, to_search):
    result = []
    if os.path.isdir(to_search):
        for (root, dirs, files) in os.walk(to_search):
            for file_name in files:
                if file_name == target:
                    result.append(os.path.join(root, file_name))
    elif os.path.isfile(to_search) and os.path.basename(to_search) == target:
        result.append(os.path.abspath(to_search))
    return result


# print(problema1("lab01.py", "C:\\Users\\aMardare\\Desktop\\python\\before_first_exam\\lab01.py"))


def problema2(target):
    result = {
        "full_path": os.path.abspath(target),
        "full_size": os.path.getsize(target),
        "file_extension": target.split(os.path.extsep)[1],
        "can_read/can_write": os.access(target, os.R_OK) and os.access(target, os.W_OK)
    }
    return result


# print(problema2('C:\\Users\\aMardare\\Desktop\\python\\before_first_exam\\lab01.py'))

def problema3(file_name):
    try:
        wd = open(file_name, "w+")
        for key, value in os.environ.items():
            wd.write(f'{key} \t {value}\n')
        wd.close()
    except:
        print('Something went wrong')


# print(problema3("data.txt"))

def problema4(path):
    if os.path.isfile(path):
        print(f'{path} - FILE')
    elif os.path.isdir(path):
        print(f'{path} - DIRECTORY')
        for item in os.listdir(path):
            problema4(os.path.normcase(os.path.join(path, item)))
    else:
        print(f'{path} - UNKNOWN')


# problema4('../..')


def problema5(source, directory, buffer_size):
    rs = open(source, "r")
    ws = open(os.path.join(directory, os.path.basename(source)), "w+")
    text = rs.read(buffer_size)
    print(text)
    while text:
        print(text)
        ws.write(text)
        text = rs.read(buffer_size)

# problema5('lab06.py', '../../', 10)


def problema6(path):
    files = []
    folders = []
    for root, dirs, files1 in os.walk(path):
            files = files + list(map(lambda file: os.path.normcase(os.path.join(root,file)), files1))
            folders = folders + dirs
    return {
        'full_path': os.path.abspath(path),
        'total_size': os.path.getsize(path),
        'files': files,
        'folders': folders
    }


print(problema6('../'))


# def problema7(path):
