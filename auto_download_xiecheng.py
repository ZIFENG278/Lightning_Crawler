import requests
import re
import asyncio
import aiohttp
import aiofiles
import os
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
# import time

# 同步  1.打开图包页，获得所有jpg的子链接
# 异步下载到文件中

url_ycc_main = "https://www.xsnvshen.com/girl/17424"   # 此处更改角色的主页
url_2 = "https://www.xsnvshen.com"

header = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
}

header2 = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
    "Referer": url_ycc_main

}

get_title = re.compile(r'<title>(?P<title>.*?)</title>', re.S)

find_num_picture = re.compile(r'更新.*?<span style.*?共 (?P<num_picture>.*?) 张', re.S)

# get_half_jpg_link = re.compile(r'(?P<half_link>.*?)000.jpg')


def mkdir(path):
    while True:
        folder = os.path.exists(path)
        if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
            os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
            print("---  new folder...  ---")
            # print("---  OK  ---")
            break
        else:
            print("---  There already have this folder!  ---")
            path = path + "new"
            continue

    return path


def get_pre_data(url):
    data = []  # order: jpg_half_link, title, num_picture
    resp = requests.get(url, headers=header)
    resp.encoding = 'utf-8'
    # print(resp.text)
    resp_bs = BeautifulSoup(resp.text, "html.parser")
    first_picture_href = resp_bs.find("div", class_="swpt-full-wrap").find("a").get('href')
    # print(first_picture_href)
    full_first_jpg_link = 'https:' + first_picture_href
    # jpg_half_link = get_half_jpg_link.search(full_first_jpg_link).group("half_link")
    jpg_half_link = full_first_jpg_link.rsplit("/", 1)[0] + "/"
    data.append(jpg_half_link)
    title = get_title.search(resp.text).group("title")
    # print(title)
    data.append(title)
    picture_num = int(find_num_picture.search(resp.text).group("num_picture"))
    # print(picture_num)
    data.append(picture_num)
    print(data)
    resp.close()
    return data


async def aiodownload(full_link, img_name, folder_name):
    async with aiohttp.ClientSession() as session:
        async with session.get(full_link, headers=header2) as resp:
            jpg_content = await resp.read()
            # print(type(jpg_content), img_name)
            async with aiofiles.open(folder_name + "/" + img_name, 'wb') as f:
                await f.write(jpg_content)
                f.close()
        resp.close()
    print(img_name + " over!")


async def get_tasks(url):
    data = get_pre_data(url)
    folder_name = mkdir("wangxinyao_example/" + data[1])  # 更改路径
    tasks = []
    for jpgs in range(data[2]):
        full_link = data[0] + str(jpgs).rjust(3, '0') + '.jpg'
        # print(full_link)
        img_name = full_link.split("/")[-1]
        tasks.append(aiodownload(full_link, img_name, folder_name))

    await asyncio.wait(tasks)


def down_one_album(url):
    # signal_album_url = 'https://www.xsnvshen.com/album/39192'
    # get_pre_data(url)
    asyncio.run(get_tasks(url))


def get_all_album_link(url):
    ycc_main_resp = requests.get(url, headers=header)
    ycc_main_resp.encoding = 'utf-8'
    # print(ycc_main_resp.text)
    ycc_main_resp_bs = BeautifulSoup(ycc_main_resp.text, "html.parser")
    find_main_class = ycc_main_resp_bs.find("div", class_="star-mod entryAblum")  # 返回string
    # print(find_main_class)
    ycc_childs = find_main_class.find_all("a")
    # print(ycc_child_name)
    # ycc_folders_list = []
    ycc_href_list = []
    for ycc_child in ycc_childs:
        # title = ycc_child.get('title')
        # print(title)
        # ycc_folders_list.append(title)
        href = ycc_child.get('href')
        # print(href)
        ycc_href_list.append(url_2 + href)

    ycc_main_resp.close()
    return ycc_href_list


if __name__ == '__main__':
    all_href = get_all_album_link(url_ycc_main)
    with ThreadPoolExecutor(8) as t:  # 更改线程池数量
        for i in range(len(all_href) - 1, -1, -1):
            t.submit(down_one_album, url=all_href[i])
            # time.sleep(60)
