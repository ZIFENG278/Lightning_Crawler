from lightning_crawler.inspect.build_db import RoleDict
from lightning_crawler.inspect.build_db import get_role_database_dict
from lightning_crawler.inspect.build_db import get_roles_dict
from lightning_crawler.inspect.build_db import write_in_json
from lightning_crawler.crawler_core.download import *



class UpdateRoleDatabase(RoleDict):
    """
    Update Role Database
    """

    def __init__(self, role_path=None, role_url=None, path_to_json=None, roles_dict=None, path_to_dist=None):
        super().__init__(role_path=role_path, role_url=role_url, path_to_json=path_to_json, roles_dict=roles_dict)
        self.path_to_dict = path_to_dist

    # def get_db_need_update_num(self, role_path, role_db, all_href_num):
    #     local_exit_folder_num = get_folder_num(self.path_to_dict + "")

    def update(self):
        all_href, access = self.get_all_album_link_wrapper()
        # print(len(all_href))
        role_database_dict = get_role_database_dict(path_to_json=self.path_to_json, role_path=self.role_path)
        if access:
            need_update_num = len(all_href) - role_database_dict['online_total']
            if need_update_num > 0:
                role_database_dict['online_total'] = len(all_href)
                need_update_href = all_href[:need_update_num]
                self.get_albums_info(need_update_href, len(all_href), state='update')
                self.album_index_dict = dict(sorted(self.album_index_dict.items(), key=lambda item: item[0]))
                # index_str = str(len_all_href - 1 - (split_num * i) - index).rjust(3, '0')
                role_database_dict['album'].update(self.album_index_dict)
                write_in_json(file_path=(self.path_to_json + 'json/database/' + self.role_path + '.json'),
                              content=role_database_dict)
                print("success update " + str(need_update_num))
            else:
                print(self.role_path + " no need to update")


class UpdateRoleDatabaseSearch(UpdateRoleDatabase):
    """
    Update search Role database
    """
    def __init__(self, role_path=None, role_url=None, path_to_json=None, roles_dict=None, path_to_dist=None):
        super().__init__(role_path=role_path, role_url=role_url, path_to_json=path_to_json, roles_dict=roles_dict, path_to_dist=path_to_dist)

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

#
# a = UpdateRoleDatabaseSearch()
# a.get_all_album_link()


class UpdateRoleDatabaseWrapper():
    """
    Wrapper to update full db
    """

    def __init__(self, path_to_json, path_to_dist):
        self.path_to_dist = path_to_dist
        self.path_to_json = path_to_json

    def update_all(self):
        roles_dict = get_roles_dict(path_to_json=self.path_to_json)
        with ThreadPoolExecutor(8) as t:  # 更改线程池数量
            for k, v in roles_dict['homepage'].items():
                update_role_db = UpdateRoleDatabase(role_path=k, role_url=v,
                                                    path_to_json=self.path_to_json,
                                                    path_to_dist=self.path_to_dist)
                t.submit(update_role_db.update)

            for k, v in roles_dict['search'].items():
                print('now search')
                update_search_role_db = UpdateRoleDatabaseSearch(role_path=k, role_url=v,
                                                          path_to_json=self.path_to_json,
                                                          path_to_dist=self.path_to_dist)
                t.submit(update_search_role_db.update)




