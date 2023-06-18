import json
import os


def all_key_value_to_json(path=None):
    big_dict = {}
    dist_folders_list = os.listdir(path + "dist")
    dist_folders_list.remove('anonymous')
    # dist_folders_list.remove('update_log.md')

    for folder in dist_folders_list:
        #print(folder)
        small_dict = {}
        albums = os.listdir(path + "dist/" + folder)
        for album in albums:
            small_dict[album[3:]] = album[:3]
        big_dict[folder] = dict(sorted(small_dict.items(), key=lambda item: item[1]))

        # big_dict = sorted(big_dict)

    #print(big_dict)
    # print(big_dict)

    # print(os.path.abspath(os.path.dirname(__file__)))

    # print(dist_folders_list)
    with open('albums_key_value.json', 'w', encoding='utf8') as f:
        json.dump(big_dict, f, ensure_ascii=False)

    with open('albums_key_value.json', 'r') as f:
        a = json.load(f)
    # print(a['优优_Yoo'])
    # print(json.dumps(a, indent=4))
    # print(type(a))
    print(json.dumps(a, ensure_ascii=False, indent=4))


def update_single_role_json(role_path=None, path=None):  # TODO implement and chaek the path
    f = open(path + 'albums_key_value.json', 'r')
    big_dict = json.load(f)
    #print(type(big_dict))
    f.close()
    small_dict = {}
    albums = os.listdir(path + 'dist/' + role_path)
    for album in albums:
        small_dict[album[3:]] = album[:3]
    big_dict[role_path] = dict(sorted(small_dict.items(), key=lambda item: item[1]))
    with open(path + 'albums_key_value.json', 'w', encoding='utf-8') as f:
        json.dump(big_dict, f, ensure_ascii=False)
        print("update albums_key_value.json success")
        # print(json.dumps(big_dict, ensure_ascii=False, indent=4))


# all_key_value_to_json(path='../../')

# update_single_role_json(role_path='月音瞳_YueYintong', path="../")