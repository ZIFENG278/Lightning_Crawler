from lightning_crawler.crawler_core import Download
from lightning_crawler.inspect.build_db import get_roles_dict
from lightning_crawler.inspect.build_db import BuildDataBase
import json
import os

class DatabaseInspector(BuildDataBase):
    """
    This class to fix thr personal db if the db is not full
    """
    def __init__(self, path_to_json=None):
        super().__init__(path_to_json)

    def fix_personal_database(self, file, person_dict):
        role_downloader = Download(role_url=person_dict['url'], role_path=person_dict['role_name'])
        all_href, access = role_downloader.get_all_album_link_wrapper()
        person_dict['online_total'] = len(all_href)

        for i in range(len(all_href)):
            index_str = str(i).rjust(3, '0')
            if index_str not in person_dict['album'].keys():
                index = len(all_href) - 1 - i
                data = role_downloader.get_pre_data(url=all_href[index])
                album_info_dict = {'folder_name': data[1],
                                   'image_num': data[2],
                                   'album_url': all_href[index],
                                   'index': index_str,
                                   'harf_link': data[0]
                                   }
                person_dict['album'][index_str] = album_info_dict
        person_dict['album'] = dict(sorted(person_dict['album'].items(), key=lambda item: item[0]))

        with open(self.path_to_json + 'json/database/' + file, "w") as f:
            json.dump(person_dict, f, ensure_ascii=False)

        with open(self.path_to_json + 'json/database/' + file, 'r') as f:
            a = json.load(f)
        # print(a['优优_Yoo'])
        # print(json.dumps(a, indent=4))
        print(json.dumps(a, ensure_ascii=False, indent=4))



    def database_inspect(self):
        # roles_dict = get_roles_dict()
        files = os.listdir(self.path_to_json + 'json/database')
        files.remove('roles_database.json')

        for file in files:
            f = open(self.path_to_json + 'json/database/' + file, 'r')
            person_dict = json.load(f)
            f.close()

            if person_dict['online_total'] != len(person_dict['album'].keys()):
                print(file + " not correct" + " online " + str(person_dict['online_total']) + " : database " + str(len(person_dict['album'].keys())))
                print("fix now")
                self.fix_personal_database(file, person_dict)


            else:
                print(file + " correct")

                # print()
                # print(json.dumps(dict, ensure_ascii=False, indent=4))


        # self.create_roles_database_json()