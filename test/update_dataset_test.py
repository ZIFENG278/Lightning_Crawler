# from lightning_crawler.inspect.build_db import UpdateRoleDatabase
from lightning_crawler.inspect.build_db import UpdateRoleDatabaseWrapper
from lightning_crawler.inspect.build_db import UpdateRoleDatabase
# a = UpdateRoleDatabase(role_path='茜茜_Kimi', role_url='https://www.xsnvshen.com/girl/22149',
#                        path_to_json='../lightning_crawler/', path_to_dist='../')
#
# a.update()
#
a = UpdateRoleDatabaseWrapper(path_to_json='../lightning_crawler/',
                              path_tp_dist='../')

a.update_all()

# a = UpdateRoleDatabase(role_path='诗诗_Kiki', role_url='https://www.xsnvshen.com/girl/19550', path_to_json='../lightning_crawler/', path_to_dist='../' )
# a.update()


