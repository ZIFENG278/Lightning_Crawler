from lightning_crawler.inspect.inspector import Inspector
from lightning_crawler.inspect.build_db import get_roles_dict
from concurrent.futures import ThreadPoolExecutor

# a = Inspector(role_path='何嘉颖_HeJiaying', role_url='https://www.xsnvshen.com/girl/21790', )
#
# a.inspect_image_num()

def fix_all_local_image_miss(path_to_json):
    roles_dict = get_roles_dict(path_to_json=path_to_json)
    with ThreadPoolExecutor(8) as t:
        for k, v in roles_dict.items():
            fixer = Inspector(role_path=k, role_url=v)
            t.submit(fixer.inspect_image_num)
# a = FixIndex(role_path='何嘉颖_HeJiaying',path_to_json='../lightning_crawler/', path_to_dist='../')
# a.fix_index()


fix_all_local_image_miss('../lightning_crawler/')