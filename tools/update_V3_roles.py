import json
from lightning_crawler.inspect.build_db import get_roles_dict

def update_V3_roles(path_to_json='../lightning_crawler/'):
    roles_dict = get_roles_dict(path_to_json=path_to_json)

    roles_V3 = {"homepage": roles_dict,
                "search": {}}

    with open(path_to_json + "json/" + "rolesV3.json", "w") as f:
        json.dump(roles_V3, f, ensure_ascii=False)
        print("database success write in")

update_V3_roles()