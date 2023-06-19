from lightning_crawler.crawler_core.downloadv2 import *
from lightning_crawler.inspect.build_db import get_role_database_dict

import os
class Inspector(DownloadV2):
    """
    Inspector base on local database to inspect the album miss or img miss
    """
    def __init__(self, role_path=None, role_url=None):
        super().__init__(role_url=role_url, role_path=role_path)
        # self.role_database = get_role_database_dict('../lightning_crawler/', self.role_path)

    # def inspect_update(self, null=None):
    #     try:
    #         all_href = self.get_all_album_link()
    #         #print(len(all_href))
    #         all_href_num = len(all_href)
    #         need_update_num = get_need_update_num(self.role_path, all_href_num)
    #         local_num = all_href_num - need_update_num
    #         print(self.role_path + "\tneed update: " + str(need_update_num) +\
    #               "\tTotal: " + str(all_href_num), "\tLocal: " + str(local_num))
    #         return all_href, all_href_num, local_num
    #     except:
    #         print('\033[93m' + self.role_path + " url broken. can not access the url. FAIL" + '\033[0m')
    #         return null

        # return
        # for i in range(all_href - 1, -1, -1)
        #     add_index = str(index).rjust(3, '0')
        #     data = self.get_pre_data(i)
        #     if add_index + data[1] in os.listdir(self.role_path) and data[2] != len(os.listdir(self.role_path + "/" + data[1])):
        #             os.

    # def redownload(self, url, small_dict):
    #     data = self.get_pre_data(url)
    #     if data[1] in small_dict:
    #         # print(data[1])
    #         full_album_name = small_dict[data[1]] + data[1]
    #         img_num = len(os.listdir("dist/" + self.role_path + "/" + full_album_name))
    #         # print(img_num)
    #         if img_num != data[2]:
    #             print("find " + full_album_name + " not match img num, auto fix")
    #             shutil.rmtree("dist/" + self.role_path + "/" + full_album_name)
    #             self.down_one_album(url=url, index=small_dict[data[1]])


    async def get_tasksV2(self, index, loss_images):
        folder_name = self.role_database['album'][index]["index"] + self.role_database['album'][index]["folder_name"]
        harf_link = self.role_database['album'][index]["harf_link"]
        folder_name = "../dist/" + self.role_path + "/" + folder_name
        # image_num = self.role_database['album'][index]["image_num"]
        tasks = []
        for i in loss_images:
            full_link = harf_link + i
            img_name = i
            # tasks.append(full_link)
            tasks.append(self.aiodownload(full_link, img_name, folder_name))
        await asyncio.wait(tasks)
        print(folder_name)


    def fix_loss_image(self, index, loss_images):
        asyncio.run(self.get_tasksV2(index, loss_images))

    def inspect_image_num(self):
        files = os.listdir('../dist/' + self.role_path)
        for i in files:
            local_image_list = os.listdir('../dist/' + self.role_path + '/' + i)
            local_image_num = len(local_image_list)
            file_index = i[:3]
            db_image_num = self.role_database['album'][file_index]['image_num']
            if local_image_num != db_image_num:
                print(i + " image num is not collect automatic fix " + str(db_image_num - local_image_num))
                loss_images = []
                for i in range(db_image_num):
                    file_name = str(i).rjust(3, '0') + '.jpg'
                    if file_name not in local_image_list:
                        loss_images.append(file_name)
                self.fix_loss_image(index=file_index, loss_images=loss_images)




        # all_href, all_href_num, local_num = self.inspect_update()
        # # print(type(big_dict))
        # if all_href is not None or all_href_num is not None and local_num != 0:
        #     with ThreadPoolExecutor(8) as t:
        #          for i in all_href:
        #              t.submit(self.redownload, url=i, small_dict=small_dict)
            # data = self.get_pre_data(i)
            # if data[1] in small_dict:   # TODO continues
            #     # print(data[1])
            #     full_album_name = small_dict[data[1]] + data[1]
            #     img_num = len(os.listdir("dist/" + self.role_path + "/" + full_album_name))
            #     # print(img_num)
            #     if img_num != data[2]:
            #         print("find " + full_album_name + " not match img num, auto fix")
            #         shutil.rmtree("dist/" + self.role_path + "/" + full_album_name)
            #         self.down_one_album(url=i, index=small_dict[data[1]])
            # print(data[1])
            # for n in ls:
            #     # print("==========================")
            #     # print(n[3:])
            #     if data[1] == n[3:]:
            #         # print(n[3:])
            #         # print("find")
            #         f = len(os.listdir("dist/" + self.role_path + "/" + n))
            #         if f != data[2]:
            #             print("find " + n + " not match img num, auto fix")
            #             shutil.rmtree("dist/" + self.role_path + "/" + n)  # 递归删除文件夹，即：删除非空文件夹
            #             self.redownload(url=i, index=n[:3]) # TODO add fix
            #         break
            # f = os.listdir("dist/" + self.role_path + "/" + r'\d{3}' + data[1])
            # print(len(f))
            # if len(f) != data[3]:
            #     print("you wen ti")