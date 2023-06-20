import asyncio
import json
import os
import time
import aiohttp
from lightning_crawler.crawler_core.download import *
from lightning_crawler.util import mkdir
from concurrent.futures import ThreadPoolExecutor
from lightning_crawler.util.get_folder_num import get_folder_num

class RoleDictZhizhi(Download):
    """
    RoleDict use to build role database json
    """
    def __init__(self, role_path=None, role_url=None, path_to_json=None, roles_dict=None):
        super().__init__(role_url=role_url, role_path=role_path)
        self.album_index_dict = {}
        self.path_to_json = path_to_json
        self.header_with_referer = {
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
            "Referer": "https://www.xsnvshen.com/album/33499"
        }
        self.fix_role_url = "https://www.xsnvshen.com/album/33499"
        # mkdir(path_to_json + 'json/database')

        # if roles_dict is None:
        #     self.roles_dict = self.get_roles_dict()
        # else:
        #     self.roles_dict = roles_dict
    # def init_album_index_dict(self):
    #     files = os.listdir(self.path_to_json + 'json/database')
    #     if self.role_path + '.json' in files:
    #         return get_role_database_dict(self.path_to_json, self.role_path)
    #     else:
    #         return {}

    def get_all_album_link(self):  # done
        with open(self.path_to_json + "/html/zhizhi_html.txt", "r") as f:
            full_html = f.read()
        # print(full_html)

        role_main_resp_bs = BeautifulSoup(full_html, "html.parser")
        find_main_class = role_main_resp_bs.find_all("div", class_="show_box_1083")  # 返回string
        # print(find_main_class)
        find_main_class = find_main_class[1]

        # find_main_class.find_all()
        # role_main_resp_bs_2 = BeautifulSoup(str(find_main_class), "html.parser")
        # find_main_class = role_main_resp_bs_2.find_all("div", class_="show_box_1083")
        # print(find_main_class)
        role_childs = find_main_class.find_all("a")
        #
        role_href_list = []
        for i in range(0, len(role_childs), 2):
            href = role_childs[i].get('href')
            role_href_list.append(self.main_url + href)

        # role_main_resp.close()
        # print(role_href_list)
        # print(len(role_href_list))
        return role_href_list

    def get_all_album_link_wrapper(self):
        access = True
        all_href = None
        try:
            all_href = self.get_all_album_link()

        except:
            print('\033[93m' + self.role_path + " url broken. can not access the url. FAIL" + '\033[0m')
            access = False
        finally:
            return all_href, access
    async def aio_get_album_info(self, href, index_str):
        async with aiohttp.ClientSession() as session:
            async with session.get(href, headers=self.header_with_referer) as resp:
                page_content = await resp.text()
                # print(page_content)
                #['https://img.xsnvshen.com/album/0/40883/', '[XiuRen]高清写真图 2023.04.14 No.6577 林珊珊 芭提雅旅拍秀人网性感清新黑丝 女神私房照_秀色女神', 86]
                data = self.get_pre_data(resp_text=page_content)
                album_info_dict = {'folder_name': data[1],
                                   'image_num': data[2],
                                   'album_url': href,
                                   'index': index_str,
                                   'harf_link': data[0]
                                   }  # TODO add half link :: finish
                print(album_info_dict)
                self.album_index_dict[index_str] = album_info_dict
            resp.close()
        await session.close()

        # pass

    async def get_album_tasks(self, all_href, len_all_href, state=None, miss_index_str=None):
        """
        :param index_str: use to fix the db which not full
        :param state: to judge is it update or build db
        :param all_href: all_need_update href
        :param len_all_href: update need to calculate index
        :return:
        """
        # tasks = []
        split_num = 100
        if len(all_href) > 450:
            all_href = all_href[:450]
            print(self.role_path + "all href bigger then 500, it must need use db inspect to keep complete ")

        num_tasks = len(all_href) // split_num + 1 if len(all_href) % split_num != 0 else len(all_href) // split_num
        print(num_tasks)
        for i in range(num_tasks):
            split_hrefs = all_href[split_num*i: split_num*i+split_num]
            print("begin " + str(i + 1), "total: " + str(num_tasks))
            tasks = []
            for index, href in enumerate(split_hrefs):
                # index_str = str(len(all_href) - 1 - index).rjust(3, '0')
                if miss_index_str is None:
                    index_str = str(len_all_href - 1 - (split_num * i) - index).rjust(3, '0')
                else:
                    index_str = miss_index_str[i * num_tasks + index]
                # print(index_str)
                tasks.append(self.aio_get_album_info(href, index_str))

            await asyncio.wait(tasks)
            print("stop crawler for 15 seconds")
            if state is None:
                time.sleep(0.1)

    def get_albums_info(self, all_href, len_all_href, state=None, miss_index_str=None):
        asyncio.run(self.get_album_tasks(all_href=all_href, len_all_href=len_all_href, state=state, miss_index_str=miss_index_str))
        # asyncio.run(self.)

    def save_role_database_json(self, middle_dict):
        with open(self.path_to_json + "json/database/" + self.role_path + ".json", "w") as f:
            json.dump(middle_dict, f, ensure_ascii=False)
            print(self.role_path + " database success write in")

    def build_personal_db_dict(self):
        """
        role : {
                'url': 'xxx',
                'role_name': 'self.role_path',
                'online_total': int
                'album':{
                        '000' : {
                                'folder_name' : 'xxx',
                                'img_num': int,
                                'index': '000',
                                'url': 'xxx'
                                }
                        'xxx':{...}
                        }
                }

        """
        # middle_dict = {}

        all_href, access = self.get_all_album_link_wrapper()
        if access:
            middle_dict = {'role_name': self.role_path,
                            'url': self.role_url,
                           'online_total': len(all_href)
                           }
            self.get_albums_info(all_href, len(all_href))

        # for index, href in enumerate(all_href):
        #     index_str = str(len(all_href) - 1 - index).rjust(3, '0')
        #
        #     data = self.get_pre_data(href)
        #     album_info_dict = {'folder_name': data[1],
        #                        'image_num': data[2],
        #                        'album_url': href,
        #                        'index': index_str
        #                        }
        #     print(album_info_dict)
        #
        #     album_index_dict[index_str] = album_info_dict
        # album_index_dict = sorted(album_index_dict)

            middle_dict['album'] = dict(sorted(self.album_index_dict.items(), key=lambda item: item[0]))
            # dict(sorted(small_dict.items(), key=lambda item: item[1]))
            # print(json.dumps(middle_dict, ensure_ascii=False, indent=4))
            self.save_role_database_json(middle_dict)
            # return middle_dict