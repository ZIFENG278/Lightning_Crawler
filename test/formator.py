import os
import shutil
import requests
import re
import asyncio
import aiohttp
import aiofiles
from bs4 import BeautifulSoup
from lightning_crawler.util.mkdir import mkdir_with_new
from lightning_crawler.util.get_folder_num import get_need_update_num
from concurrent.futures import ThreadPoolExecutor
import imghdr
from PIL import Image
from io import BytesIO






def aiodownload1(full_link, album_url=None):
    header_with_url_referer = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
        "Referer": album_url
    }

    resp = requests.get(full_link, headers=header_with_url_referer)
    img_type = imghdr.what(None, resp.content)
    print(img_type)
    if resp.status_code == 200:
        # Get the content type from the "Content-Type" header
        # print(resp.text)
        content_type = resp.headers.get('Content-Type', '')
        print(content_type)

        # Check if the content type indicates JPEG or WebP format
        if 'image/jpeg' in content_type:

            print("The response is in JPEG format.")
            with open('000.jpg', 'wb') as file:
                if img_type == 'webp':
                    webp_image = Image.open(BytesIO(resp.content))
                    webp_image = webp_image.convert('RGB')
                    webp_image.save('000.jpg', 'JPEG')
                    print('save jpg')
                # Write the response content to the file
                else:
                    file.write(resp.content)
                    print(f"Image saved")
        elif 'image/webp' in content_type:
            print("The response is in WebP format.")
        else:
            print(f"The response is in an unexpected format: {content_type}")
    else:
        print(f"Failed to fetch the image. Status code: {resp.status_code}")

    # print(img_name + " over!")



async def aiodownload(self, full_link, img_name, folder_name, album_url=None):
    header_with_url_referer = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
        "Referer": album_url
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(full_link, headers=header_with_url_referer) as resp:
            jpg_content = await resp.read()
            # print(type(jpg_content), img_name)
            async with aiofiles.open(folder_name + "/" + img_name, 'wb') as f:
                await f.write(jpg_content)
                await f.close()
                # print(folder_name)
        resp.close()
    # print(img_name + " over!")
    await session.close()

async def get_tasks(self, url, index):
    data = self.get_pre_data(url)
    add_index = ''
    if index != '':
        add_index = str(index).rjust(3, '0')
    folder_name = mkdir_with_new("../dist/" + self.role_path + "/" + add_index + data[1])  # 更改路径
    tasks = []
    for jpgs in range(data[2]):
        full_link = data[0] + str(jpgs).rjust(3, '0') + '.jpg'
        # print(full_link)
        img_name = full_link.split("/")[-1]
        tasks.append(self.aiodownload(full_link, img_name, folder_name))

    await asyncio.wait(tasks)
    print(folder_name)

def down_one_album(self, url, index):
    # print('down_one')
    # signal_album_url = 'https://www.xsnvshen.com/album/39192'
    # get_pre_data(url)
    asyncio.run(self.get_tasks(url, index))


url = 'https://www.xsnvshen.com/album/42317'
index = '000'



# link = 'https://img.xsnvshen.com/album/22162/42317/000.jpg'
# album_url = 'https://www.xsnvshen.com/album/42317'
#
# link2 = 'https://img.xsnvshen.com/album/22162/41685/000.jpg'
# url2 = 'https://www.xsnvshen.com/album/41685'
# aiodownload1(link, album_url)
# aiodownload1(link2, url2)