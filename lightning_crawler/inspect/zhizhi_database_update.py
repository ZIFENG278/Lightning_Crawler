from lightning_crawler.inspect.build_db import get_role_database_dict
from lightning_crawler.inspect.zhizhi_databse_fix import RoleDictZhizhi
from lightning_crawler.inspect.build_db import write_in_json



class UpdateZhiZhiDB(RoleDictZhizhi):
    def __init__(self, path_to_json):
        self.path_to_json = path_to_json
        self.role_path = "芝芝_Booty"
        self.role_url = "https://www.xsnvshen.com/girl/22899"
        super().__init__(role_path=self.role_path, role_url=self.role_url, path_to_json=self.path_to_json)
        self.zhizhi_database_dict = get_role_database_dict(path_to_json=self.path_to_json, role_path=self.role_path)


    def update(self):
        all_href = self.get_all_album_link()
        need_update_num = len(all_href) - self.zhizhi_database_dict['online_total']

        if need_update_num > 0:
            self.zhizhi_database_dict['online_total'] = len(all_href)
            need_update_href = all_href[:need_update_num]
            self.get_albums_info(need_update_href, len(all_href), state='update')
            self.album_index_dict = dict(sorted(self.album_index_dict.items(), key=lambda item: item[0]))
            # index_str = str(len_all_href - 1 - (split_num * i) - index).rjust(3, '0')
            self.zhizhi_database_dict['album'].update(self.album_index_dict)
            write_in_json(file_path=(self.path_to_json + 'json/database/' + self.role_path + '.json'),
                          content=self.zhizhi_database_dict)
            print("success update " + str(need_update_num))
        else:
            print('芝芝_Booty no need to update ')
