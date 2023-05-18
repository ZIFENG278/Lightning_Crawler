import os

def get_file_list(file_path):
    dir_list = os.listdir(file_path)
    if not dir_list:
        return
    else:
        # 注意，这里使用lambda表达式，将文件按照最后修改时间顺序升序排列
        # os.path.getmtime() 函数是获取文件最后修改时间
        # os.path.getctime() 函数是获取文件最后创建时间
        dir_list = sorted(dir_list,  key=lambda x: os.path.getctime(os.path.join(file_path, x)))
        # print(dir_list)
        return dir_list


# dist = os.listdir("/home/zifeng/Greaseheads_share/dist")
# # dist.pop('优优_Yoo', '周九九_JojoBaby', '月音瞳_YueYintong', '江真真_JiangZhenzhen')
# dist.remove('优优_Yoo')
# dist.remove('周九九_JojoBaby')
# dist.remove('月音瞳_YueYintong')
# dist.remove('江真真_JiangZhenzhen')
# dist.remove('anonymous')
#
# dist = ['肉肉_Lavinia']
# pwd = "/home/zifeng/Greaseheads_share/dist/"
# print(dist)
# for i in dist:
#     role_path = pwd + i
#     role_albums = get_file_list(role_path)
#     for index, name in enumerate(role_albums):
#         add_index = str(index).rjust(3, '0')
#         os.rename(role_path + "/" + name, role_path + "/" + name[4:-1])
# a = get_file_list("/home/zifeng/Greaseheads_share/dist/优优_Yoo")
# ra = list(reversed(a))
# print(a)
# print(ra)
# path = "/home/zifeng/Greaseheads_share/dist/优优_Yoo"
# for index, name in enumerate(a):
#     add_index = str(index).rjust(3, '0')
#
#     os.rename(path + "/" + name, path + "/" + add_index + name)
# print(11111)