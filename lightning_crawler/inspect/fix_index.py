from lightning_crawler.crawler_core.download import Download
import json
import os
from lightning_crawler.json.key_value_to_json import update_single_role_json

class FixIndex(Download):
    def __init__(self, role_url, role_path):
        super().__init__(role_url, role_path)

    def get_json_dict(self):
        with open('../json/albums_key_value.json', 'r') as f:
            roles_dict = json.load(f)
        # print(json.dumps(roles_dict ,ensure_ascii=False, indent=4))
        return roles_dict

    def fix_index(self):
        old_big_dict = self.get_json_dict()
        all_href = self.get_all_album_link()
        for index, href in enumerate(all_href):
            index_str = str(len(all_href) - 1 - index).rjust(3, '0')
            date = self.get_pre_data(href)
            if date[1] in old_big_dict[self.role_path] and old_big_dict[self.role_path][date[1]] != index_str:
                old_name = old_big_dict[self.role_path][date[1]] + date[1]
                new_name = index_str + date[1]
                pwd = ''
                os.rename("dist/" + self.role_path + "/" + old_name, "dist/" + self.role_path + "/" + new_name)
                print("change name form " + old_name)
                print("to " + new_name)

        update_single_role_json(role_path=self.role_path, path='../../')
        # return all_href



# test = FixIndex('https://www.xsnvshen.com/girl/22490', '月音瞳_YueYintong')
# a = test.fix_index()
# print(a)

# def test():
#     os.rename("dist/test", "dist/test2")

# test()