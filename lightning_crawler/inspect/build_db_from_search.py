from lightning_crawler.inspect.build_db import RoleDict
from lightning_crawler.crawler_core.downloadV3 import *

class RoleDictSearch(RoleDict):
    """
    This class to build database from search role
    if the role have homepage, please use V2
    """
    def __init__(self, role_path=None, role_url=None, path_to_json=None):
        super().__init__(role_path=role_path, role_url=role_url, path_to_json=path_to_json)

    def get_all_album_link(self):
        role_main_resp = requests.get(self.role_url, headers=self.header)
        role_main_resp.encoding = 'utf-8'
        # print(ycc_main_resp.text)
        role_main_resp_bs = BeautifulSoup(role_main_resp.text, "html.parser")
        find_main_class = role_main_resp_bs.find("div", class_="index_listc longConWhite")  # 返回string
        # print(find_main_class)
        role_childs = find_main_class.find_all("a")
        # print(ycc_child_name)
        # ycc_folders_list = []
        role_href_list = []
        for index, role_child in enumerate(role_childs):
            # title = ycc_child.get('title')
            # print(title)
            # ycc_folders_list.append(title)
            index += 1
            if index % 2 != 0:
                href = role_child.get('href')
                # print(href)
                if href[:6] == '/album':
                    role_href_list.append(self.main_url + href)

        role_main_resp.close()
        # print(role_href_list)
        # print(len(role_href_list))
        return role_href_list

    def build_personal_db_dict(self):
        """
        role : {
                'url': 'xxx',
                'role_name': 'self.role_path',
                'from_search': True
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

        all_href, access = self.get_all_album_link_wrapper()
        if access:
            middle_dict = {'role_name': self.role_path,
                           'url': self.role_url,
                           'online_total': len(all_href),
                           'from_search': True,
                           }
            self.get_albums_info(all_href, len(all_href))

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
            self.save_role_database_json(middle_dict)
            # return middle_dict




