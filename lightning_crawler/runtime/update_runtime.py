from lightning_crawler.crawler_core.download import Download
import json
from concurrent.futures import ThreadPoolExecutor

def update_runtime():
    with open('../json/roles.json', 'r') as f:
        roles_dict = json.load(f)

    # a = roles_dict.items()
    # print(type(a))

    print("++++++++++update start++++++++++")
    with ThreadPoolExecutor(8) as t:
        for k, v in roles_dict.items():
            # print(k, v)
            role = Download(role_url=v, role_path=k)
            t.submit(role.start)

    #     role = Download(role_url=roles_dict.get('王馨瑶_Yanni'), role_path='王馨瑶_Yanni')
    #
    # role.start()

# update_runtime()