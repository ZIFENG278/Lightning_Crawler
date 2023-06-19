from lightning_crawler.inspect.fix_index import FixIndex
from lightning_crawler.inspect.build_db import get_roles_dict
from concurrent.futures import ThreadPoolExecutor



def fix_all_index(path_to_json):
    roles_dict = get_roles_dict(path_to_json=path_to_json)
    with ThreadPoolExecutor(8) as t:
        for k, v in roles_dict.items():
            fixer = FixIndex(role_path=k, path_to_json=path_to_json, path_to_dist='../')
            t.submit(fixer.fix_index)
# a = FixIndex(role_path='何嘉颖_HeJiaying',path_to_json='../lightning_crawler/', path_to_dist='../')
# a.fix_index()


fix_all_index('../lightning_crawler/')