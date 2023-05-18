import json
import os

from download import Download

def get_roles_database_dict():
    with open("roles_database.json", "r") as f:
        roles_database_dict = json.load(f)
    return roles_database_dict


def init_json():
    init_dict = {}
    with open("roles_database.json", "w") as f:
        json.dump(init_dict, f, ensure_ascii=False)
        print("database init")


def get_roles_dict():
    with open("roles.json", "r") as f:
        roles_dict = json.load(f)
    return roles_dict


class RoleDict(Download):
    def __init__(self, role_path=None, role_url=None, roles_dict=None):
        super().__init__(role_url=role_url, role_path=role_path)
        # if roles_dict is None:
        #     self.roles_dict = self.get_roles_dict()
        # else:
        #     self.roles_dict = roles_dict

    def build_personal_db_dict(self):
        """
        role : {
                'url': 'xxx',
                'role_name': 'self.role_path',
                'online_total': int
                'album':{
                        '000' : {
                                'folder_name' : 'xxx',
                                'img_num': int,
                                'index': '000',
                                'url': 'xxx'
                                }
                        'xxx':{...}
                        }
                }

        """
        # middle_dict = {}
        album_index_dict = {}

        all_href = self.get_all_album_link()
        middle_dict = {'url': self.role_url,
                       'role_name': self.role_path,
                       'online_total': len(all_href)}
        for index, href in enumerate(all_href):
            index_str = str(len(all_href) - 1 - index).rjust(3, '0')
            data = self.get_pre_data(href)
            album_info_dict = {'folder_name': data[1],
                               'image_num': data[2],
                               'album_url': href,
                               'index': index_str
                               }
            print(album_info_dict)

            album_index_dict[index_str] = album_info_dict
        # album_index_dict = sorted(album_index_dict)

        middle_dict['album'] = album_index_dict

        print(json.dumps(middle_dict, ensure_ascii=False, indent=4))
        return middle_dict


class BuildDataBase:
    def __init__(self):
        files_list = os.listdir("./")
        if "roles_database.json" not in files_list:
            init_json()
            self.roles_database_dict = get_roles_database_dict()
        else:
            self.roles_database_dict = get_roles_database_dict()

    def save_roles_database_json(self):
        with open("roles_database", "w") as f:
            json.dump(self.roles_database_dict, f, ensure_ascii=False)
            print("database success write in ")

    def update_database(self):
        roles_dict = get_roles_dict()
        for k, v in roles_dict.items():
            role = RoleDict(role_path=k, role_url=v)
            middle_dict = role.build_personal_db_dict()
            self.roles_database_dict[k] = middle_dict
            print(k + "role database dict success build ")
            print(self.roles_database_dict)
            break
        self.save_roles_database_json()


# def build_database_json():
#     with open("role_database.json", "r")
#     big_dict = {}


# test_role = BuildDb(role_path='周九九_JojoBaby', role_url='https://www.xsnvshen.com/girl/28306')
# test_role.build_personal_db_dict()
a = BuildDataBase()
a.update_database()
