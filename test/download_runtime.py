from lightning_crawler.crawler_core.download import Download
import json


def download_runtime(role_path):
    with open('../lightning_crawler/json/roles.json', 'r') as f:
        roles_dict = json.load(f)
    # a = roles_dict.items()
    # print(type(a))
    role = Download(role_url=roles_dict.get(role_path), role_path=role_path)
    role.start()

# download_runtime('周九九_JojoBaby')


def inspect_update_runtime(role_path):
    with open('../lightning_crawler/json/roles.json', 'r') as f:
        roles_dict = json.load(f)
    # a = roles_dict.items()
    # print(type(a))
    role = Download(role_url=roles_dict.get(role_path), role_path=role_path)
    role.inspect_update()


def inspect_img_num_runtime(role_path):
    f = open('../lightning_crawler/json/roles.json', 'r')
    roles_dict = json.load(f)
    f.close()
    f = open('../lightning_crawler/json/albums_key_value.json', 'r')
    big_dict = json.load(f)
    f.close()
    # a = roles_dict.items()
    # print(type(a))
    role = Download(role_url=roles_dict.get(role_path), role_path=role_path)
    role.inspect_image_num(small_dict=big_dict[role_path])


# inspect_update_runtime('周九九_JojoBaby')
# inspect_img_num_runtime('妲己_Toxic')