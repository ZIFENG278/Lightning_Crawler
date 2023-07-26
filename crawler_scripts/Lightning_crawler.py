import sys
import argparse
from module_runtime import *
description = "Lightning Crawler is a professional website assistant for downloading photo albums, simple, efficient, and fast, " \
              "download the photo albums you need.\nPhoto website: https://www.xsnvshen.com/"


def lightning_crawler():
    print(f'argv: {sys.argv}')
    # if os.path.split(os.getcwd())[-1] == 'scripts':
    #     os.chdir('../')

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-u', '--update', action='store_true', help='Update ')
    parser.add_argument('-i','--inspect', action='store_true', help='Inspect')
    parser.add_argument('-d','--database', action='store_true', help='Database')
    parser.add_argument('-l','--album', action='store_true', help='Album')
    parser.add_argument('--all', action='store_true', help='Select all')
    parser.add_argument('-ls', '--list', action='store_true', help='List all roles in default')
    parser.add_argument('-a', '--add_role', action='store_true', help='Add role from homepage')
    parser.add_argument('-s', '--add_search', action='store_true', help='Add role from search')
    parser.add_argument('-anon','--anonymous', action='store_true', help='Download anonymous album')
    parser.add_argument('-r', '--remove', action='store_true', help='Remove role from list')
    parser.add_argument('--name', type=str, help='Role name')
    parser.add_argument('--url', type=str, help='URL')
    args = parser.parse_args()


    if ((args.update or args.inspect) and not (args.database or args.album)) and not (args.all or args.name):
        parser.error('Your command has insufficient parameters\n'
                     'example:\n'
                     'python3 lightning_crawler.py -u --database -all\n'
                     'python3 lightning_crawler.py -i --album --name xxx_xxx')

    if args.update and args.database and args.all:
        """update database all"""
        update_database_all()

    if args.inspect and args.database and args.all:
        """inspect database all"""
        inspect_database_all()

    if args.update and args.database and args.name:
        """update database role"""
        update_database_role(role_path=args.name)

    if args.inspect and args.database and args.name:
        """inspect database role"""
        inspect_database_role(args.name)

    if args.update and args.album and args.all:
        """update album all"""
        update_album_all()

    if args.inspect and args.album and args.all:
        """inspect album all"""
        inspect_album_all()

    if args.update and args.album and args.name:
        """update album role"""
        update_album_role(role_path=args.name)

    if args.inspect and args.album and args.name:
        """inspect album role """
        inspect_album_role(args.name)


    if args.list and not args.name:
        list_roles()

    if args.list and args.name:
        list_role_json(args.name)

    if args.add_role and not (args.name and args.url):
        parser.error('Your command has insufficient parameters\n'
                     'example:\n'
                     'python3 lightning_crawler.py -a --name xxx -- url xxx.com\n')

    if args.add_role and args.name and args.url and not args.add_search:
        add_role(args.name, args.url)

    if args.add_role and args.add_search and args.name and args.url:
        add_search_role(args.name, args.url)

    if args.anonymous and not args.url:
        parser.error('Your command has insufficient parameters\n'
                     'example:\n'
                     'python3 lightning_crawler.py -anon --name xxx -- url xxx.com\n')

    if args.anonymous and args.url:
        anonymous_url_down(args.url)

    if args.remove and args.name:
        remove_role(args.name)

    if args.remove and not args.name:
        parser.error('Your command has insufficient parameters\n'
                     'example:\n'
                     'python3 lightning_crawler.py -r --name xxx\n')


lightning_crawler()
