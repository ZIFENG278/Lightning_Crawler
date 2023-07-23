import json


anon = {
    "https://www.xsnvshen.com/album/40963": "",
    "https://www.xsnvshen.com/album/40967": "",
    "https://www.xsnvshen.com/album/40991": "",
    "https://www.xsnvshen.com/album/40982": "",
    "https://www.xsnvshen.com/album/40980": "",
    "https://www.xsnvshen.com/album/40948": "",
    "https://www.xsnvshen.com/album/40947": "",
    "https://www.xsnvshen.com/album/40946": "",
    "https://www.xsnvshen.com/album/40944": "",
    "https://www.xsnvshen.com/album/40936": "",
    "https://www.xsnvshen.com/album/40935": "",
    "https://www.xsnvshen.com/album/40933": "",
    "https://www.xsnvshen.com/album/40931": "",
    "https://www.xsnvshen.com/album/40926": "",
    "https://www.xsnvshen.com/album/40918": "",
    "https://www.xsnvshen.com/album/40914": "",
    "https://www.xsnvshen.com/album/40913": "",
    "https://www.xsnvshen.com/album/40912": "",
    "https://www.xsnvshen.com/album/40908": "",
    "https://www.xsnvshen.com/album/40906": "",
    "https://www.xsnvshen.com/album/40905": "",
    "https://www.xsnvshen.com/album/40903": "",
    "https://www.xsnvshen.com/album/40902": "",
    "https://www.xsnvshen.com/album/40900": "",
    "https://www.xsnvshen.com/album/40899": "",
    "https://www.xsnvshen.com/album/40898": "",
    "https://www.xsnvshen.com/album/40896": "",
    "https://www.xsnvshen.com/album/40894": "",
    "https://www.xsnvshen.com/album/40883": "",
    "https://www.xsnvshen.com/album/40876": "",
    "https://www.xsnvshen.com/album/41043": "",
    "https://www.xsnvshen.com/album/41047": "",
    "https://www.xsnvshen.com/album/41106": "",
}

with open('./database/anonymous.json', 'w', encoding='utf8') as f:
    json.dump(anon, f, ensure_ascii=False)





