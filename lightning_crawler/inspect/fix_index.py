from lightning_crawler.crawler_core.download import Download
import json
import os
from lightning_crawler.json.key_value_to_json import update_single_role_json

class FixIndex():
    """
        base database to fix index
    """
    def __init__(self, role_path, path_to_json=None, path_to_dist=None):
        self.role_path = role_path
        self.path_to_json = path_to_json
        self.path_to_dist = path_to_dist
    def get_json_dict(self):
        with open(self.path_to_json + 'json/database/' + self.role_path + ".json", 'r') as f:
            roles_dict = json.load(f)
        # print(json.dumps(roles_dict ,ensure_ascii=False, indent=4))
        return roles_dict

    def fix_index(self):
        album_folders = os.listdir(self.path_to_dist + 'dist/' + self.role_path)
        role_database_dict = self.get_json_dict()
        for album_folder in album_folders:
            album_index = album_folder[:3]
            album_title = album_folder[3:]
            if album_title != role_database_dict['album'][album_index]['folder_name']:
                for i in role_database_dict['album'].values():
                    # print(i)
                    if i['folder_name'] == album_title:
                        new_name = i['index'] + i['folder_name']

                        os.rename(self.path_to_dist + "dist/" + self.role_path + "/" + album_folder,
                                  self.path_to_dist + "dist/" + self.role_path + "/" + new_name)
                        print("change name form " + album_folder)
                        print("to " + new_name)

        # update_single_role_json(role_path=self.role_path, path='../../')
        # return all_href



# test = FixIndex('https://www.xsnvshen.com/girl/22490', '月音瞳_YueYintong')
# a = test.fix_index()
# print(a)

# def test():
#     os.rename("dist/test", "dist/test2")

# test()