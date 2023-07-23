import sys
import argparse
from module_runtime import *
description = "Lightning_Crawler"

def lightning_crawler():
    print(f'argv: {sys.argv}')
    # the cwd must be the root of the respository
    # if os.path.split(os.getcwd())[-1] == 'scripts':
    #     os.chdir('../')
    #

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-u', '--update', action='store_true', help='Update ')
    parser.add_argument('-i','--inspect', action='store_true', help='Inspect')
    parser.add_argument('-d','--database', action='store_true', help='Database')
    parser.add_argument('-l','--album', action='store_true', help='Album')
    parser.add_argument('--all', action='store_true', help='Select all')
    parser.add_argument('-ls', '--list', action='store_true', help='List all roles in default')
    parser.add_argument('-a', '--add_role', action='store_true', help='Add role')
    parser.add_argument('-anon','--anonymous', action='store_true', help='Download anonymous album')
    parser.add_argument('--role_path', type=str, help='Add role path')
    parser.add_argument('--role_url', type=str, help='Add role url')
    args = parser.parse_args()


    if ((args.update or args.inspect) and not (args.database or args.album)) and not (args.all or args.role_path):
        parser.error('Your command has insufficient parameters\n'
                     'example:\n'
                     'python3 lightning_crawler.py -u --database -all\n'
                     'python3 lightning_crawler.py -i --album --role_path xxx_xxx')

    if args.update and args.database and args.all:
        """update database all"""
        update_database_all()

    if args.inspect and args.database and args.all:
        """inspect database all"""
        inspect_database_all()

    if args.update and args.database and args.role_path:
        """update database role"""
        update_database_role(role_path=args.role_path)

    if args.inspect and args.database and args.role_path:
        """inspect database role"""
        inspect_database_role(args.role_path)

    if args.update and args.album and args.all:
        """update album all"""
        update_album_all()

    if args.inspect and args.album and args.all:
        """inspect album all"""
        inspect_album_all()

    if args.update and args.album and args.role_path:
        """update album role"""
        update_album_role(role_path=args.role_path)

    if args.inspect and args.album and args.role_path:
        """inspect album role """
        inspect_album_role(args.role_path)


    if args.list and not args.role_path:
        list_roles()

    if args.list and args.role_path:
        list_role_json(args.role_path)

    if args.add_role and not (args.role_path and args.role_url):
        parser.error('Your command has insufficient parameters\n'
                     'example:\n'
                     'python3 lightning_crawler.py -a --role_path xxx -- role_url xxx.com\n')

    if args.add_role and args.role_path and args.role_url:
        add_role(args.role_path, args.role_url)

    if args.anonymous and not args.role_url:
        parser.error('Your command has insufficient parameters\n'
                     'example:\n'
                     'python3 lightning_crawler.py -anon --role_path xxx -- role_url xxx.com\n')

    if args.anonymous and args.role_url:
        anonymous_url_down(args.role_url)


lightning_crawler()
