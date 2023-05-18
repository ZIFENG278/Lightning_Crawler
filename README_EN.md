# picture reptile tool

[中文 Chinese](https://github.com/ZIFENG278/Greaseheads_share)

[英文 English](https://github.com/ZIFENG278/Greaseheads_share/blob/master/README_EN.md)

> Reptile combat
>
> This time, I started with an unencrypted image website for non-client rendering. I found a third-party image website with fast update speed, perfect atlas and very suitable for crawling. [~~Click to jump~~]()
>
> Linux/Mac users can run directly after installing the required library, adding a folder and modifying the save path.
>
> Windows users need to modify the backslashes of the save path



## Linux/Mac Usage

> Recommended to use conda environment ***python>=3.7***

- **Grab the master branch (the main branch has no content)**

```bash
git clone https://github.com/ZIFENG278/Greaseheads_share.git
```
- Or download the zip archive
```bash
wget https://github.com/ZIFENG278/Greaseheads_share/archive/refs/heads/master.zip
```
- **Install the required environment**

```bash
pip3 install -r requirements.txt
```

- (option) Select the role you like and copy the url to url_ycc_main, otherwise the role is recommended by default, and in the same directory create a folder with the role name you like, and modify the path in the get_tasks function. 
If it is not changed, it is the default Example (refer to assets/image)


- **run the program**
```bash
python3 auto_download_xiecheng.py
```
- **For update the picture albums, put the character homepage url and the character path to the respective list, the url and character path sequence must be in one-to-one correspondence, ensure that the path is correct and run**
```bash
python3 auto_update_xiecheng.py
````
When viewing the folder, it is recommended to choose to sort by last modifide, the newer the better, and if you want to update the latest albums in the future, the approximate timeline will not be messed up.

The actual measurement of Ubuntu with above 8 threads has some segments too many open files. There is no problem with the actual measurement of 8. The default thread pool is 8.

Mac M1 chip is tested with 16 threads, too many open files are directly displayed at the beginning of the test and automatically terminated.

If the computer hardware is relatively high, you can try to use more threads. For example, high-speed writing of SSD should be avoided. Of course, you can also directly modify the value of the system open files maximum.

[too many open files Error solution can refer to](https://support.axway.com/kb/101749/language/en#:~:text=The%20%22Too%20many%20open%20files%22%20message%20means%20that%20the%20operating,command%20displays%20the%20current%20limit.)



