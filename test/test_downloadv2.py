from lightning_crawler.crawler_core.downloadv2 import DownloadV2
from lightning_crawler.inspect.build_db import get_roles_dict
from concurrent.futures import ThreadPoolExecutor

# a = DownloadV2(role_url='https://www.xsnvshen.com/girl/28192', role_path='77_Qiqi')
#
# a.start()



def update_all(path_to_json):
    roles_dict = get_roles_dict(path_to_json=path_to_json)
    with ThreadPoolExecutor(2) as t:
        for k, v in roles_dict.items():
            downloadv2 = DownloadV2(role_url=v, role_path=k)
            t.submit(downloadv2.start)
# a = FixIndex(role_path='何嘉颖_HeJiaying',path_to_json='../lightning_crawler/', path_to_dist='../')
# a.fix_index()


update_all('../lightning_crawler/')