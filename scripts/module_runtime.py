"""
0 add role_path and role json
1 build db
2 inspect the db (or update) must
    2.5 optional fix index,
3 DownloadV2(all role album) or Download(anonymous)
4 inspect local image
5 update ...  (sudo apt update then sudo apt upgrade)
"""
from lightning_crawler.inspect.build_db import UpdateRoleDatabaseWrapper


def update_database_all():
    a = UpdateRoleDatabaseWrapper(path_to_json='../lightning_crawler/',
                                  path_to_dist='../')

    a.update_all()

# update_database_all()