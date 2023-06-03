from lightning_crawler.crawler_core import Download
import os
class Inspector(Download):
    def __init__(self, role_path=None, role_url=None):
        super().__init__(role_url=role_url, role_path=role_path)

    def inspect_update(self, null=None):
        try:
            all_href = self.get_all_album_link()
            #print(len(all_href))
            all_href_num = len(all_href)
            need_update_num = get_need_update_num(self.role_path, all_href_num)
            local_num = all_href_num - need_update_num
            print(self.role_path + "\tneed update: " + str(need_update_num) +\
                  "\tTotal: " + str(all_href_num), "\tLocal: " + str(local_num))
            return all_href, all_href_num, local_num
        except:
            print('\033[93m' + self.role_path + " url broken. can not access the url. FAIL" + '\033[0m')
            return null
        # return
        # for i in range(all_href - 1, -1, -1)
        #     add_index = str(index).rjust(3, '0')
        #     data = self.get_pre_data(i)
        #     if add_index + data[1] in os.listdir(self.role_path) and data[2] != len(os.listdir(self.role_path + "/" + data[1])):
        #             os.

    def redownload(self, url, small_dict): # TODO redownload the special img, don't download hold album to decrease the stream
        data = self.get_pre_data(url)
        if data[1] in small_dict:   # TODO continues
            # print(data[1])
            full_album_name = small_dict[data[1]] + data[1]
            img_num = len(os.listdir("dist/" + self.role_path + "/" + full_album_name))
            # print(img_num)
            if img_num != data[2]:
                print("find " + full_album_name + " not match img num, auto fix")
                shutil.rmtree("dist/" + self.role_path + "/" + full_album_name)
                self.down_one_album(url=url, index=small_dict[data[1]])


    def inspect_image_num(self, small_dict):   # TODO consider a data structural use JSON big O2 is too slow use mutil thread
        all_href, all_href_num, local_num = self.inspect_update()
        # print(type(big_dict))
        if all_href is not None or all_href_num is not None and local_num != 0:
            with ThreadPoolExecutor(8) as t:
                 for i in all_href:
                     t.submit(self.redownload, url=i, small_dict=small_dict)
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