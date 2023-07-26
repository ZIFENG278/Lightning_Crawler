from lightning_crawler.inspect.build_db_from_search import RoleDictSearch


a = RoleDictSearch(role_path='幼幼_YouYou', role_url='https://www.xsnvshen.com/search?w=%E5%B9%BC%E5%B9%BC', path_to_json="../lightning_crawler/")
# print(type(a.path_to_json))
a.build_personal_db_dict()