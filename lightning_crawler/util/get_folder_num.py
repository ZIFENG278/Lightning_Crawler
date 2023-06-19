import os
from .mkdir import mkdir
# from lightning_crawler.inspect.build_db import get_dict


def get_folder_num(path):
    mkdir(path)
    files = os.listdir(path)
    folder_num = len(files)
    # print(type(folder_num), folder_num)
    return folder_num


def get_need_update_num(path, all_href_num):
    local_exit_folder_num = get_folder_num("../dist/" + path)
    need_update_num = all_href_num - local_exit_folder_num
    return need_update_num


def get_need_update_num_from_db(path, role_db):
    local_exit_folder_num = get_folder_num("../dist/" + path)
    need_update_num = role_db['online_total'] - local_exit_folder_num
    return need_update_num
# def get_need_update_num_from_db(path):
#     local_exit_folder_num = get_folder_num("../dist/" + path)
#     db_online = get_dict(path_to_json='../lightning/')

def get_need_update_from_dbV2(path, role_db):
    # need_update_href = []
    need_update_index_str_list = []
    local_exit_folder_index = []
    local_exit_folder_num = get_folder_num("../dist/" + path)
    need_update_num = role_db['online_total'] - local_exit_folder_num

    local_exit_folders = os.listdir('../dist/' + path)
    for i in local_exit_folders:
        folder_index = i[:3]
        # if folder_index in role_db['album']
        local_exit_folder_index.append(folder_index)

    for i in range(len(role_db['album'])-1, -1, -1):
        index_str = str(i).rjust(3, '0')
        if index_str not in local_exit_folder_index:
            # index = len(all_href) - 1 - i
            # need_update_href.append(all_href[index])
            need_update_index_str_list.append(index_str)
            if len(need_update_index_str_list) == need_update_num:
                break
    return need_update_index_str_list



