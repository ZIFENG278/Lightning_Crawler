from lightning_crawler.crawler_core.download import *

class DownloadV2(Download):
    """
    Download image class base on database, can not install anonymous album
    if need download anonymous please use downloadV1
    """
    def __init__(self, role_url=None, role_path=None):
        super().__init__(role_url=role_url, role_path=role_path)


    def start(self):  # both update and start
        all_href, access = self.get_all_album_link_wrapper()
        if self.role_path == "anonymous":
            print(
                '\033[93m' + "downloading in " + self.role_path + '\033[0m')  # TODO waring consider sometime url broken
            self.down_one_album(self.role_url, index='')

        elif access and self.role_path != "anonymous":
            need_update_num = get_need_update_num(self.role_path, len(all_href))
            with ThreadPoolExecutor(8) as t:  # 更改线程池数量
                for i in range(need_update_num - 1, -1, -1):
                    t.submit(self.down_one_album, url=all_href[i], index=len(all_href) - 1 - i)
                    # time.sleep(60)
                print(self.role_path + "\tupdate: " + str(need_update_num) + "\tTotal: " + str(len(all_href)))