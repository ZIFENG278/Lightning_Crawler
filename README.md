# Lightning Crawler

> A professional website assistant for downloading photo albums, simple, efficient, and fast, download the photo albums you need.

> Photo website: https://www.xsnvshen.com/

[中文 Chinese](https://github.com/ZIFENG278/Lightning_Crawler/blob/rebuild/README.md)

[English](https://github.com/ZIFENG278/Lightning_Crawler/blob/rebuild/README.md)

## Setup

> ***python>=3.7***

- **Clone the repository**

```bash
git clone https://github.com/ZIFENG278/Greaseheads_share.git
```
- Alternatively, download the zip archive
```bash
wget https://github.com/ZIFENG278/Greaseheads_share/archive/refs/heads/master.zip
```
- **Install the required environment**

```bash
cd Lightning_Crawler
./setup.sh
```

## Usage
```bash
cd Lightning_Crawler
. start_env.sh
cd ./crawler_scripts
```

### Parameter Description

```bash
python3 Lightning_crawler --help
```

**-u, --update** Update

**-i, --inspect** Inspect

**-d, --database** Database

**-l, --album** Photo Albums

**-a, --add_role** Add a new role

**-anon, --anonymous** Anonymous photos

**-ls, --list** List all

**--name** Role name

**--url** Role homepage or anonymous photo album URL

### Examples

> Software logic:
>
> 1. Enter the name of the role to be downloaded and the role's homepage URL. The database will be automatically created after entry.
> 
> 2. Check the integrity of the local database.
>
> 3. Download photo albums.
>
> 4. Check the integrity of the photo albums.
>
> If you encounter IP blocking, try using a mobile hotspot. When creating or updating the database encounters IP blocking, simply enable airplane mode, then check the database to automatically repair the missing database.

- List all currently entered role names and website URLs

  ```bash
  python3 Lightning_crawler -ls
  ```

- View the role database

  ```bash
  python3 Lightning_crawler -ls --name name_of_role
  ```

- Add a new role

  ```bash
  python3 Lightning_crawler -a --name XXX --url www.XXX.com
  ```

- Update the database

  ```bash
  python3 Lightning_crawler -u -d --all # update all
  python3 Lightning_crawler -u --database --name XXX # update specify role
  ```

- Check the database (ensure the database integrity, as network issues may cause partial loss)

  ```bash
  python3 Lightning_crawler -i -d --all # inspect all
  python3 Lightning_crawler -i --database --name XXX # inspect specify role
  ```

- Download all photo albums of a role

  ```bash
  python3 Lightning_crawler -u -l -all # update all roles album
  python3 Lightning_crawler -u --album --name # update specify role album
  ```

- Check the integrity of the image library (ensure the image library integrity, as network issues may cause partial loss)

  ```bash
  python3 Lightning_crawler -i -l -all # inspect all roles album
  python3 Lightning_crawler -i --album --name # inspect specify role album
  ```

- Download anonymous photos (photo albums without a role homepage or for separate storage)

  ```bash
  python3 Lightning_crawler -anon --url www.XXX.com
  ```