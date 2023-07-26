from lightning_crawler.crawler_core.downloadV3 import DownloadV3
from lightning_crawler.inspect.build_db import get_roles_dict
import json
from lightning_crawler.inspect.build_db_from_search import RoleDictSearch


def add_search_role(role_path, role_url):
    a = DownloadV3(role_url=role_url, role_path=role_path)
    _, access = a.get_all_album_link_wrapper()
    if access:
        roles_dict = get_roles_dict(path_to_json='../lightning_crawler/')
        if role_path in roles_dict['search'].keys():
            print(role_path + ' have exist in rolesV3.json')
        else:
            roles_dict['search'].update({role_path: role_url})
            with open('../lightning_crawler/json/rolesV3.json', 'w', encoding='utf8') as f:
                json.dump(roles_dict, f, ensure_ascii=False)

            # build = input('build ' + role_path + " database (Y/es) or (N/o)")
            # if build == 'Y' or build == 'Yes':
            print("please wait to build database")
            role_db = RoleDictSearch(role_path=role_path, role_url=role_url, path_to_json='../lightning_crawler/')
            role_db.build_personal_db_dict()
            # else:
            #     role_db = {}
            #     with open('../lightning_crawler/json/database/' + role_path + ".json", "w") as f:
            #         json.dump(role_db, f, ensure_ascii=False)
            #     print(role_path + ' database would build later')
    else:
        print("this url is broken, please check again")

add_search_role(role_path='幼幼_YouYou', role_url='https://www.xsnvshen.com/search?w=%E5%B9%BC%E5%B9%BC')