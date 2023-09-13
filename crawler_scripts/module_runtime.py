"""
0 add role_path and role json
1 build db
2 inspect the db (or update) must
    2.5 optional fix index,
3 DownloadV2(all role album) or Download(anonymous)
4 inspect local image
5 update ...  (sudo apt update then sudo apt upgrade)
"""
import os
import json
from lightning_crawler.inspect.update_db import UpdateRoleDatabaseWrapper
from lightning_crawler.crawler_core.downloadv2 import DownloadV2
from lightning_crawler.inspect.build_db import get_roles_dict
from concurrent.futures import ThreadPoolExecutor
from lightning_crawler.inspect.database_inspector import DatabaseInspector
from lightning_crawler.inspect.update_db import UpdateRoleDatabase
from lightning_crawler.util.view_json import view_json
from lightning_crawler.crawler_core.download import Download
from lightning_crawler.inspect.build_db import RoleDict
from lightning_crawler.inspect.build_db import get_role_database_dict
from lightning_crawler.inspect.inspector import Inspector
from lightning_crawler.crawler_core.downloadV3 import DownloadV3
from lightning_crawler.inspect.build_db_from_search import RoleDictSearch
from lightning_crawler.inspect.update_db import UpdateRoleDatabaseSearch


def update_database_all():
    a = UpdateRoleDatabaseWrapper(path_to_json='../lightning_crawler/',
                                  path_to_dist='../')
    a.update_all()


# update_database_all()

def update_album_all():
    roles_dict = get_roles_dict(path_to_json='../lightning_crawler/')
    with ThreadPoolExecutor(2) as t:
        for k, v in roles_dict['homepage'].items():
            downloadv2 = DownloadV2(role_url=v, role_path=k)
            t.submit(downloadv2.start)

        for k, v in roles_dict['search'].items():
            downloadv2 = DownloadV2(role_url=v, role_path=k)
            t.submit(downloadv2.start)


def inspect_database_all():
    a = DatabaseInspector(path_to_json='../lightning_crawler/')
    a.database_inspect()


def inspect_database_role(role_path):
    role_dict = get_role_database_dict(path_to_json='../lightning_crawler/', role_path=role_path)
    a = DatabaseInspector(path_to_json='../lightning_crawler/')
    a.fix_personal_database(role_path + '.json', role_dict)


def inspect_album_all():
    roles_dict = get_roles_dict(path_to_json='../lightning_crawler/')
    with ThreadPoolExecutor(8) as t:
        for k, v in roles_dict['homepage'].items():
            fixer = Inspector(role_path=k, role_url=v)
            t.submit(fixer.inspect_image_num)

        for k, v in roles_dict['search'].items():
            fixer = Inspector(role_path=k, role_url=v)
            t.submit(fixer.inspect_image_num)


# a = FixIndex(role_path='何嘉颖_HeJiaying',path_to_json='../lightning_crawler/', path_to_dist='../')
# a.fix_index()

def inspect_album_role(role_path):
    roles_dict = get_roles_dict(path_to_json='../lightning_crawler/')
    source = get_source(role_path)
    role_url = roles_dict[source][role_path]
    fixer = Inspector(role_path=role_path, role_url=role_url)
    fixer.inspect_image_num()


def get_source(role_path):
    roles_dict = get_roles_dict(path_to_json='../lightning_crawler/')
    if role_path in roles_dict['homepage']:
        return 'homepage'
    elif role_path in roles_dict['search']:
        return 'search'
    else:
        print(role_path + " not in the rolesV3")
        return False


def update_database_role(role_path):
    roles_dict = get_roles_dict(path_to_json='../lightning_crawler/')
    source = get_source(role_path)
    if source:
        if source == 'homepage':
            role_url = roles_dict[source][role_path]
            a = UpdateRoleDatabase(role_path=role_path, role_url=role_url, path_to_json='../lightning_crawler/',
                                   path_to_dist='../')
            a.update()
        if source == 'search':
            role_url = roles_dict[source][role_path]
            a = UpdateRoleDatabaseSearch(role_path=role_path, role_url=role_url, path_to_json='../lightning_crawler/',
                                         path_to_dist='../')
            a.update()


def update_album_role(role_path):
    roles_dict = get_roles_dict(path_to_json='../lightning_crawler/')
    source = get_source(role_path)
    if source and source == 'homepage':
        role_url = roles_dict['homepage'][role_path]
    elif source and source == 'search':
        role_url = roles_dict['search'][role_path]

    a = DownloadV2(role_path=role_path, role_url=role_url)
    a.start()


def list_roles():
    roles_dict = get_roles_dict(path_to_json='../lightning_crawler/')
    print(json.dumps(roles_dict, ensure_ascii=False, indent=4))


def list_role_json(role_path):
    view_json('../lightning_crawler/json/database/' + role_path + '.json')


def add_role(role_path, role_url):
    a = Download(role_url=role_url, role_path=role_path)
    _, access = a.get_all_album_link_wrapper()
    if access:
        roles_dict = get_roles_dict(path_to_json='../lightning_crawler/')
        if role_path in roles_dict['homepage'].keys():
            print(role_path + ' have exist in rolesV3.json')
        else:
            roles_dict['homepage'].update({role_path: role_url})
            with open('../lightning_crawler/json/rolesV3.json', 'w', encoding='utf8') as f:
                json.dump(roles_dict, f, ensure_ascii=False)

            # build = input('build ' + role_path + " database (Y/es) or (N/o)")
            # if build == 'Y' or build == 'Yes':
            print("please wait to build database")
            role_db = RoleDict(role_path=role_path, role_url=role_url, path_to_json='../lightning_crawler/')
            role_db.build_personal_db_dict()
            # else:
            #     role_db = {}
            #     with open('../lightning_crawler/json/database/' + role_path + ".json", "w") as f:
            #         json.dump(role_db, f, ensure_ascii=False)
            #     print(role_path + ' database would build later')
    else:
        print("this url is broken, please check again")


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


def anonymous_url_down(role_url):
    anon = get_role_database_dict('../lightning_crawler/', role_path='anonymous')
    if role_url in anon.keys():
        print(role_url + ' have already in anonymous')
    else:
        anon.update({role_url: ""})
        with open('../lightning_crawler/json/database/anonymous.json', 'w', encoding='utf8') as f:
            json.dump(anon, f, ensure_ascii=False)
        anonymous = Download(role_url, "anonymous")
        anonymous.start()
        # download_anon_album(role_url, "anonymous")


def remove_role(role_path):
    roles_dict = get_roles_dict(path_to_json='../lightning_crawler/')
    source = get_source(role_path)
    if source:
        if source == 'homepage':
            roles_dict['homepage'].pop(role_path)
            with open('../lightning_crawler/json/rolesV3.json', "w") as f:
                json.dump(roles_dict, f, ensure_ascii=False)
            os.remove('../lightning_crawler/json/database/' + role_path + '.json')
            print("success remove " + role_path)

        elif source == 'search':
            roles_dict['search'].pop(role_path)
            with open('../lightning_crawler/json/rolesV3.json', "w") as f:
                json.dump(roles_dict, f, ensure_ascii=False)
            os.remove('../lightning_crawler/json/database/' + role_path + '.json')
            print("success remove " + role_path)
