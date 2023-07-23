import os
import sys
# 获取根目录
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)) + '/../')
# # 将根目录添加到path中
# sys.path.append(BASE_DIR)

import argparse
from module_runtime import *
description = "Lightning_Crawler"

def crawler():
    print(f'argv: {sys.argv}')
    # the cwd must be the root of the respository
    if os.path.split(os.getcwd())[-1] == 'scripts':
        os.chdir('../')
    #

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-u', '--update', action='store_true', help='Update ')
    parser.add_argument('-i','--inspect', action='store_true', help='Inspect')

    parser.add_argument('-d','--database', action='store_true', help='database')
    parser.add_argument('-l','--album', action='store_true', help='local image')
    parser.add_argument('--all', action='store_true', help='select all')

    parser.add_argument('-a', '--add_role', action='store_true', help='Add role')
    parser.add_argument('--role_path', type=str, help='Add role path')
    parser.add_argument('--role_url', type=str, help='Add role url')
    args = parser.parse_args()


    if ((args.update or args.inspect) and not (args.database or args.album)) and not (args.all or args.role_path):
        parser.error('Your command has insufficient parameters\n'
                     'example:\n'
                     'python3 crawler.py -u --database -all\n'
                     'python3 crawler.py -i --album --role_path xxx_xxx')

    if args.update and args.database and args.all:
        update_database_all()
    update_database_all()

    # print(args.role_path)
    # print(args)

    # kwargs = vars(args)
    # # print("+++++kwargs++++++++")
    # # print(kwargs)
    # # exit(1)
    # if 'session_type_dict' in kwargs:
    #     kwargs['session_type_dict'] = utils.str_to_dict(kwargs['session_type_dict'])
    # #
    # print("++++==cmd.settings_file+++++++")
    # print(cmds.settings_file)
    # settings = config_settings.ConfigSettings(cmds.settings_file, **kwargs)  # settings_import_on_pc.yaml
    # print("++++++settings++++")
    # # print(f'settings: {settings}')
    # # print(type(settings))
    # sys.stdout.flush() # force output all the buffer in std output
    #
    # work_dir = os.path.join(settings.modelartifacts_path, f'{settings.tensor_bits}bits')
    # print(f'work_dir: {work_dir}')   # work_dir: ./work_dirs/modelartifacts/8bits
    #
    # # run the accuracy pipeline
    # tools.run_accuracy(settings, work_dir)

crawler()
