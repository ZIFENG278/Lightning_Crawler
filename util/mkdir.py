import os


def mkdir_with_new(path):
    while True:
        folder = os.path.exists(path)
        if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
            os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径 递归创建
            # print("---  new folder...  ---")
            # print("---  OK  ---")
            break
        else:
            # print("---  There already have this folder!  ---")
            path = path + "new"
            continue
    return path


def mkdir(path):
    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径 递归创建
        # print("---  new folder...  ---")
        # print("---  OK  ---")
    return path


def mkdir_dist_and_path(path):  # TODO fix this dist dir problem
    dist = os.path.exists("dist")
    role_path = os.path.exists(path)
    if not dist:
        os.makedirs("dist")
    if not role_path:
        os.makedirs(path)
