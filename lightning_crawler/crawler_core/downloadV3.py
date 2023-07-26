from lightning_crawler.crawler_core.download import *


class DownloadV3(Download):
    """
    Download V3 can download form search result
    this class can download role albums without person homepage
    """
    def __init__(self, role_url=None, role_path=None):
        self.from_search = True
        super().__init__(role_url=role_url, role_path=role_path)

    def get_all_album_link(self):
        role_main_resp = requests.get(self.role_url, headers=self.header)
        role_main_resp.encoding = 'utf-8'
        # print(ycc_main_resp.text)
        role_main_resp_bs = BeautifulSoup(role_main_resp.text, "html.parser")
        find_main_class = role_main_resp_bs.find("div", class_="index_listc longConWhite")  # 返回string
        # print(find_main_class)
        role_childs = find_main_class.find_all("a")
        # print(ycc_child_name)
        # ycc_folders_list = []
        role_href_list = []
        for index, role_child in enumerate(role_childs):
            # title = ycc_child.get('title')
            # print(title)
            # ycc_folders_list.append(title)
            index += 1
            if index % 2 != 0:
                href = role_child.get('href')
                # print(href)
                if href[:6] == '/album':
                    role_href_list.append(self.main_url + href)

        role_main_resp.close()
        # print(role_href_list)
        # print(len(role_href_list))
        return role_href_list



#
# a = DownloadV3(role_path="幼幼_YouYou", role_url="https://www.xsnvshen.com/search?w=%E5%B9%BC%E5%B9%BC" )
# a.get_all_album_link_wrapper()