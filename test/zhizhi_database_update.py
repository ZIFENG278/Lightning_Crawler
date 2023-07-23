from lightning_crawler.inspect.zhizhi_database_update import UpdateZhiZhiDB
from lightning_crawler.inspect.build_db import get_role_database_dict
a = UpdateZhiZhiDB(path_to_json='../lightning_crawler/')
a.update()

# a = get_role_database_dict(path_to_json='../lightning_crawler/', role_path='芝芝_Booty')
# print(a['online_total'])