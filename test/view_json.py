import json


def view_json(path):
    with open(path, 'r') as f:
        a = json.load(f)
    # print(a['优优_Yoo'])
    # print(json.dumps(a, indent=4))
    print(json.dumps(a, ensure_ascii=False, indent=4))

view_json('../lightning_crawler/json/database/roles_database.json')