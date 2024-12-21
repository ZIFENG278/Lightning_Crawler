from lightning_crawler.crawler_core.download import *
from lightning_crawler.inspect.build_db import get_role_database_dict
from lightning_crawler.util.get_folder_num import get_need_update_num_from_db
from lightning_crawler.util.get_folder_num import get_need_update_from_dbV2
from tqdm import tqdm
class DownloadV2(Download):
    """
    Download image class base on database, can not install anonymous album
    if you need download anonymous please use downloadV1
    upgrade and download and find miss
    """
    def __init__(self, role_url=None, role_path=None):
        super().__init__(role_url=role_url, role_path=role_path)
        self.role_database = get_role_database_dict('../lightning_crawler/', self.role_path)


    async def get_tasksV2(self, index_str):
        folder_name = index_str + self.role_database['album'][index_str]["folder_name"]
        harf_link = self.role_database['album'][index_str]["harf_link"]
        folder_path = mkdir_with_new("../dist/" + self.role_path + "/" + folder_name)
        image_num = self.role_database['album'][index_str]["image_num"]
        album_url = self.role_database['album'][index_str]["album_url"]
        tasks = []
        for i in range(image_num):
            full_link = harf_link + str(i).rjust(3, '0') + '.jpg'
            img_name = full_link.split("/")[-1]
            # tasks.append(full_link)
            tasks.append(self.aiodownload(full_link, img_name, folder_path, album_url))

        for coro in tqdm(asyncio.as_completed(tasks), total=image_num, desc=folder_name[:3]):
            await coro

        print(folder_name)


        # print(tasks)


    def down_one_albumV2(self, index_str):
        asyncio.run(self.get_tasksV2(index_str))


    def start(self):  # both update and start
        # all_href, access = self.get_all_album_link_wrapper()
        access = True
        if access:  ## TODO change the need_update_num by index loss from  StartV3 :: finish
            need_update_index_str = get_need_update_from_dbV2(path=self.role_path, role_db=self.role_database)
            # need_update_zips = list(zip(need_update_href, need_update_index_str))
            # print(len(need_update_href))
            # print(self.role_path + str(need_update_index_str))
            if len(need_update_index_str) == 0:
                print(self.role_path + " no need to update")
            else:
                # need_update_index = []
                # for i in range(self.role_database['online_total'] -1,
                #                self.role_database['online_total'] - need_update_num -1,
                #                -1):
                #     index = str(i).rjust(3, '0')
                #     need_update_index.append(index)
                # print(need_update_index)

            # add_index = str(self.role_database['online_total'] - 1).rjust(3, '0')

                # need_update_info = self.role_database['album'][add_index]
                # print(need_update_info)
                # print(need_update_num)
                with ThreadPoolExecutor(4) as t:  # 更改线程池数量
                    for i in need_update_index_str:
                        t.submit(self.down_one_albumV2, index_str=i)
                        # time.sleep(60)
                    print(self.role_path + "\tupdate: " + str(len(need_update_index_str)))
