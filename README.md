# 图片爬虫工具（油头党专用）
[中文 Chinese](https://github.com/ZIFENG278/Greaseheads_share)

[英文 English](https://github.com/ZIFENG278/Greaseheads_share/blob/master/README_EN.md)

> 爬虫实战
>
> 本次针对非客户端渲染的无加密的图片网站下手，该网站更新速度快，图册完善且非常适合爬取的第三方图片网[~~点击跳转~~]()，测试时在国外测试的，不清楚国内是否被墙，看具体情况科学上网。
>
> Linux/mac用户安装所需库后添加文件夹后修改保存路径后可直接运行
>
> windows用户需修改保存路径的反斜杠



## Linux/Mac Usage

> 推荐使用conda环境 ***python>=3.7***

- **抓取master分支（main分支无内容）**

```bash
git clone https://github.com/ZIFENG278/Greaseheads_share.git
```
- 或者下载zip压缩包
```bash
wget https://github.com/ZIFENG278/Greaseheads_share/archive/refs/heads/master.zip
```
- **安装所需环境**

```bash
pip3 install -r requirements.txt
```

- (option)挑选你喜欢的角色复制url到url_ycc_main处 否则默认推荐角色, 并代码同目录先新建一个你喜欢的角色名的文件夹，且在get_tasks函数处修改路径，不改则是默认Example（参考assets/image）


- **运行程序**
```bash
python3 auto_download_xiecheng.py
```
- **后续更新图集，在更新程序中放好角色主页url，与角色路径到各自的list中，url与人物路径顺序必须一一对应，确保路径无误后运行**
```bash
python3 auto_update_xiecheng.py
````
查看文件夹时建议选择以last modifide排序，越新越好看，并且以后想更新最新图集只需稍微改一下代码就可以补齐，大致时间线也不会乱

实测ubuntu开8线程以上也有部分段too many open files 实测8无问题，默认线程池为8

Mac M1芯片16线程测试时初段直接显示too many open files自动终止

如果电脑配置比较高可尝试使用更多线程，例如固态硬盘SSD高速写入应该会避免，当然也可以直接修改系统open files maximum的值

[too many open files 报错解决可参考](https://support.axway.com/kb/101749/language/en#:~:text=The%20%22Too%20many%20open%20files%22%20message%20means%20that%20the%20operating,command%20displays%20the%20current%20limit.)



## 开发思路

> python爬虫

1. 利用requests对人物的主页进行访问，获取源码后放进BeautifulSoup里，通过标签查找找出主页所有图册的href


2. 通过多线程对每个href先进行同步线程访问获取网页源码, 首先利用BeautifulSoup与正则表达式获取相册的名字以作文件夹名称与第一张jpg的url和单个图册的图片数,因为网页源码实质提供了所有低清预览，但有第一张高清预览图jpg的url, 需要简单拼接一下得到完整的单个高清图url, 所以需要提取前半段的url


3. 得到所有预处理数据后，利用协程进行异步访问与异步写入，用到asyncio，aiohttp ，aiofiles 三个库，~~因为网站有时候会存在相同名称的图集，所以遇到相同名称的后面加上new防止覆盖，宁可多下也不能错过~~（目前利用子href获取标题后修复了这个问题）

   **windows用户需要修改一下路径，改成反斜杠，mkdir函数不清楚windows用户是否能跑，可能要稍微改改**





