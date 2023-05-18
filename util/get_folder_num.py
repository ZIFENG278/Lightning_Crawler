import os
from .mkdir import mkdir


def get_folder_num(path):
    mkdir(path)
    files = os.listdir(path)
    folder_num = len(files)
    # print(type(folder_num), folder_num)
    return folder_num


def get_need_update_num(path, all_href_num):
    local_exit_folder_num = get_folder_num("dist/" + path)
    need_update_num = all_href_num - local_exit_folder_num
    return need_update_num


