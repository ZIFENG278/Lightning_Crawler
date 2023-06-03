from lightning_crawler.inspect import BuildDataBase
from lightning_crawler.inspect.database_inspector import DatabaseInspector
from lightning_crawler.runtime.update_runtime import update_runtime
#
# a = BuildDataBase(path_to_json="../lightning_crawler/")
# a.update_database()
#
# a = DatabaseInspector(path_to_json='../lightning_crawler/')
# a.database_inspect()

update_runtime('../lightning_crawler/')