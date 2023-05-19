from lightning_crawler.inspect import RoleDict
from lightning_crawler.inspect import BuildDataBase

# test_role = RoleDict(role_path='周九九_JojoBaby', role_url='https://www.xsnvshen.com/girl/28306')
# test_role.build_personal_db_dict()

a = BuildDataBase(path_to_json="../lightning_crawler/")
a.update_database()