# from lightning_crawler.inspect.build_db import UpdateRoleDatabase
import os
import sys
from lightning_crawler.inspect.update_db import UpdateRoleDatabaseWrapper
from lightning_crawler.inspect.update_db import UpdateRoleDatabase
from lightning_crawler.inspect.update_db import UpdateRoleDatabaseSearch
# a = UpdateRoleDatabase(role_path='茜茜_Kimi', role_url='https://www.xsnvshen.com/girl/22149',
#                        path_to_json='../lightning_crawler/', path_to_dist='../')
#
# a.update()
#
a = UpdateRoleDatabaseWrapper(path_to_json='../lightning_crawler/',
                              path_to_dist='../')
#
a.update_all()

# a = UpdateRoleDatabaseSearch(role_path='幼幼_YouYou', role_url='https://www.xsnvshen.com/search?w=%E5%B9%BC%E5%B9%BC', path_to_json='../lightning_crawler/', path_to_dist='../' )
# a.update()


