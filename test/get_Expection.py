import requests
from bs4 import BeautifulSoup

role_path = '芝芝_Booty'
role_url = 'https://www.xsnvshen.com/girl/22899'
header = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
}
def get_all_album_link():  # done
    role_main_resp = requests.get(role_url, headers=header)
    role_main_resp.encoding = 'utf-8'
    # print(ycc_main_resp.text)
    role_main_resp_bs = BeautifulSoup(role_main_resp.text, "html.parser")
    find_main_class = role_main_resp_bs.find("div", class_="star-mod entryAblum")  # 返回string
    # print(find_main_class)
    role_childs = find_main_class.find_all("a")
    # print(ycc_child_name)
    # ycc_folders_list = []
    role_href_list = []
    for role_child in role_childs:
        # title = ycc_child.get('title')
        # print(title)
        # ycc_folders_list.append(title)
        href = role_child.get('href')
        # print(href)
        role_href_list.append(main_url + href)

    role_main_resp.close()
    return role_href_list

get_all_album_link()