from lightning_crawler.crawler_core.download import *
from lightning_crawler.inspect.build_db import get_role_database_dict
from lightning_crawler.util.get_folder_num import get_need_update_num_from_db

class DownloadV2(Download):
    """
    Download image class base on database, can not install anonymous album
    if you need download anonymous please use downloadV1
    """
    def __init__(self, role_url=None, role_path=None):
        super().__init__(role_url=role_url, role_path=role_path)
        self.role_database = get_role_database_dict('../lightning_crawler/', self.role_path)


    async def get_tasksV2(self, index):
        folder_name = self.role_database['album'][index]["index"] + self.role_database['album'][index]["folder_name"]
        harf_link = self.role_database['album'][index]["harf_link"]
        folder_name = mkdir_with_new("../dist/" + self.role_path + "/" + folder_name)
        image_num = self.role_database['album'][index]["image_num"]
        tasks = []
        for i in range(image_num):
            full_link = harf_link + str(i).rjust(3, '0') + '.jpg'
            img_name = full_link.split("/")[-1]
            # tasks.append(full_link)
            tasks.append(self.aiodownload(full_link, img_name, folder_name))
        await asyncio.wait(tasks)
        print(folder_name)

        # print(tasks)


    def down_one_albumV2(self, index):
        asyncio.run(self.get_tasksV2(index))


    def start(self):  # both update and start
        all_href, access = self.get_all_album_link_wrapper()
        if access:
            need_update_num = get_need_update_num_from_db(path=self.role_path, role_db=self.role_database)
            if need_update_num == 0:
                print(self.role_path + " no need to update")
            else:
                need_update_index = []
                for i in range(self.role_database['online_total'] -1,
                               self.role_database['online_total'] - need_update_num -1,
                               -1):
                    index = str(i).rjust(3, '0')
                    need_update_index.append(index)
                # print(need_update_index)

            # add_index = str(self.role_database['online_total'] - 1).rjust(3, '0')
                #
                # need_update_info = self.role_database['album'][add_index]
                # print(need_update_info)
                # print(need_update_num)
                with ThreadPoolExecutor(8) as t:  # 更改线程池数量
                    for i in need_update_index:
                        t.submit(self.down_one_albumV2, index=i)
                        # time.sleep(60)
                    print(self.role_path + "\tupdate: " + str(need_update_num) + "\tTotal: " + str(len(all_href)))
