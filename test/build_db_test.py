from lightning_crawler.inspect.build_db import RoleDict
from lightning_crawler.inspect.build_db import BuildDataBase

# test_role = RoleDict(role_path='杨晨晨_Yome', role_url='https://www.xsnvshen.com/girl/22162', path_to_json='../lightning_crawler/')
# test_role.build_personal_db_dict()

a = BuildDataBase(path_to_json="../lightning_crawler/")
a.build_database()
# a.create_roles_database_json()