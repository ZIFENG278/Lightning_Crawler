import asyncio
import json
import os
import time

import aiohttp

from lightning_crawler.crawler_core.download import Download


def get_roles_database_dict(path_to_json=None):
    with open(path_to_json + "json/roles_database.json", "r") as f:
        roles_database_dict = json.load(f)
    return roles_database_dict


def init_json(path_to_json=None):
    init_dict = {}
    with open(path_to_json + "json/roles_database.json", "w") as f:
        json.dump(init_dict, f, ensure_ascii=False)
        print("database init")


def get_roles_dict(path_to_json=None):
    with open(path_to_json + "json/roles.json", "r") as f:
        roles_dict = json.load(f)
    return roles_dict


class RoleDict(Download):
    def __init__(self, role_path=None, role_url=None, roles_dict=None):
        super().__init__(role_url=role_url, role_path=role_path)
        self.album_index_dict = {}  # TODO

        # if roles_dict is None:
        #     self.roles_dict = self.get_roles_dict()
        # else:
        #     self.roles_dict = roles_dict

    async def aio_get_album_info(self, href, index_str):
        async with aiohttp.ClientSession() as session:
            async with session.get(href, headers=self.header_with_referer) as resp:
                page_content = await resp.text()
                # print(page_content)
                data = self.get_pre_data(resp_text=page_content)
                album_info_dict = {'folder_name': data[1],
                                   'image_num': data[2],
                                   'album_url': href,
                                   'index': index_str
                                   }
                self.album_index_dict[index_str] = album_info_dict
            resp.close()
        await session.close()

        # pass

    async def get_album_tasks(self, all_href):
        tasks = []
        for index, href in enumerate(all_href):
            index_str = str(len(all_href) - 1 - index).rjust(3, '0')
            # print(index_str)
            tasks.append(self.aio_get_album_info(href, index_str))

        await asyncio.wait(tasks)


    def get_albums_info(self, all_href):
        asyncio.run(self.get_album_tasks(all_href=all_href))
        # asyncio.run(self.)

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

        all_href = self.get_all_album_link()
        middle_dict = {'url': self.role_url,
                       'role_name': self.role_path,
                       'online_total': len(all_href)
                       }
        self.get_albums_info(all_href)

        # for index, href in enumerate(all_href):
        #     index_str = str(len(all_href) - 1 - index).rjust(3, '0')
        #
        #     data = self.get_pre_data(href)
        #     album_info_dict = {'folder_name': data[1],
        #                        'image_num': data[2],
        #                        'album_url': href,
        #                        'index': index_str
        #                        }
        #     print(album_info_dict)
        #
        #     album_index_dict[index_str] = album_info_dict
        # album_index_dict = sorted(album_index_dict)

        middle_dict['album'] = dict(sorted(self.album_index_dict.items(), key=lambda item: item[0]))
        # dict(sorted(small_dict.items(), key=lambda item: item[1]))
        # print(json.dumps(middle_dict, ensure_ascii=False, indent=4))
        return middle_dict


class BuildDataBase:
    def __init__(self, path_to_json):
        self.path_to_json = path_to_json
        files_list = os.listdir(self.path_to_json + "json")
        if "roles_database.json" not in files_list:
            init_json()
            self.roles_database_dict = get_roles_database_dict(self.path_to_json)
        else:
            self.roles_database_dict = get_roles_database_dict(self.path_to_json)

    def save_roles_database_json(self):
        with open(self.path_to_json + "json/roles_database.json", "w") as f:
            json.dump(self.roles_database_dict, f, ensure_ascii=False)
            print("database success write in")

    def update_database(self):
        roles_dict = get_roles_dict(self.path_to_json)
        for k, v in roles_dict.items():
            role = RoleDict(role_path=k, role_url=v)
            middle_dict = role.build_personal_db_dict()
            self.roles_database_dict[k] = middle_dict
            print(k + " role database dict success build ")
            # print(self.roles_database_dict)
            time.sleep(60)

            break
        print(json.dumps(self.roles_database_dict, ensure_ascii=False, indent=4))

        self.save_roles_database_json()  # TODO check and consider the save problem

# def build_database_json():
#     with open("role_database.json", "r")
#     big_dict = {}

# a = BuildDataBase()
# a.update_database()
