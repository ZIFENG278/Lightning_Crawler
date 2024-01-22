# Lightning Crawler 
> 一款专业写真网站辅助下载软件，简单，高效，极速，下载你所需要的写真集
> 
> 写真网址 https://www.xsnvshen.com/


[中文 Chinese](https://github.com/ZIFENG278/Lightning_Crawler/blob/rebuild/README.md)

[英文 English](https://github.com/ZIFENG278/Lightning_Crawler/blob/rebuild/README.md)


## Setup

> ***python>=3.7***

- **抓取分支**

```bash
git clone https://github.com/ZIFENG278/Lightning_Crawler.git
```
- 或者下载zip压缩包
```bash
wget https://github.com/ZIFENG278/Lightning_Crawler/archive/refs/heads/master.zip
```
- **安装所需环境**

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
### 参数解析
```bash
python3 Lightning_crawler --help
```
**-u, --updata** 更新

**-i, --inspect** 检查

**-d, --database** 数据库

**-l, --album** 写真集

**-a, --add_role** 录入新角色

**-anon, --anonymous** 匿名写真

**-ls, --list** 列出

**--name** 角色名字

**--url** 角色主页或匿名写真集URL



### Examples

> 软件使用逻辑 ：
> 
> 1 录入向下载的角色名字与角色主页URL 录入后会自动创建数据库
>
> 2 检查本地数据库完整性
>
> 3 下载写真集
>
> 4 检查写真集完整性
>
> 如遇到IP封禁，尝试使用手机热点，数据库创建或更新遇到IP封禁时，只需开关飞行模式，然后检查一次数据库就可自动修复丢失的数据库

- 列出当前所有已经录入的角色名字和网站URL

  ```bash
  python3 Lightning_crawler -ls
  ```

- 查看角色数据库

  ```bash
  python3 Lightning_crawler -ls --name name_of_role
  ```

- 录入新角色

  ```bash
  python3 Lightning_crawler -a --name XXX --url www.XXX.com
  ```

- 更新数据库

  ```bash
  python3 Lightning_crawler -u -d --all # update all
  python3 Lightning_crawler -u --database --name XXX #update specify role
  ```

- 检查数据库（确保数据库完整，因网络问题影响可能造成部分丢失）

  ```bash
  python3 Lightning_crawler -i -d --all # inspect all
  python3 Lightning_crawler -i --database --name XXX #inspect specify role
  ```

- 下载角色所有写真

  ```bash
  python3 Lightning_crawler -u -l -all # update all roles album
  python3 Lightning_crawler -u --album --name # update specify role album
  ```

- 检查图库完整性（确保图库完整，因网络问题影响可能造成部分丢失）

  ```bash
  python3 Lightning_crawler -i -l -all # inspect all roles album
  python3 Lightning_crawler -i --album --name # inspect specify role album
  ```

- 下载匿名写真（无角色主页的写真集或只想单独保存）

  ```bash
  python3 Lightning_crawler -anon --url www.XXX.com
  ```
