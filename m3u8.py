import requests
import subprocess
import os
import asyncio
import aiofiles
import aiohttp

async def download_ts(url,name,session):
    async with session.get(url) as resp:
        async with aiofiles.open(name,mode="wb") as f:
            await f.write(await resp.content.read())


async def aio_download(url_head,current_folder,i):
    tasks = []
    async with aiohttp.ClientSession() as session:
        async with aiofiles.open("m3u8.txt",mode="r",encoding="utf-8") as f:
            async for line in f:
                if line.startswith("#"):
                    continue
                line = line.strip()
                ts_url = url_head + line
                name = str(i).zfill(4) + ts_url[-3:]
                file_path = os.path.join(current_folder, name)
                task = asyncio.create_task(download_ts(ts_url,file_path,session))
                print(file_path)
                i += 1
                tasks.append(task)
            await asyncio.wait(tasks)

def merge_ts_windows():
    os.system('copy /b E:\\CODE\\pachong\\Myproject\\vedio1\\*.ts E:\\CODE\\pachong\\Myproject\\vedio2\\output.mp4')

def main():
    i = 0
    Second_url=""
    Second_url_head = ""
    current_folder = os.getcwd() + "\\vedio1"
    resp = requests.get(Second_url)
    with open("m3u8.txt",mode="wb") as f:
        f.write(resp.content)
    asyncio.run(aio_download(Second_url_head,current_folder,i))
    merge_ts_windows()

'''
def download_ts(url,name):
    resp = requests.get(url)
    with open(name,mode="wb") as f:
        f.write(resp.content)

def merge_ts():
    lst = []
    with open("m3u8.txt",mode="r",encoding="utf-8") as f:
        for line in f:
            if line.startswith("#"):
                continue
            line = line.strip()
            lst.append(line)
    s = "+".join(lst)
    cmd = ['ffmpeg', '-i', s, '-c', 'copy', "output.mp4"]
    subprocess.run(cmd)

def merge_ts_windows():
    os.system('copy /b E:\\CODE\\pachong\\Myproject\\vedio1\\*.ts E:\\CODE\\pachong\\Myproject\\vedio2\\output.mp4')
 
def main():
    Second_url=""
    Second_url_head = ""

    current_folder = os.getcwd() + "\\vedio1"
    #存了第二次m3u8的文件
    resp = requests.get(Second_url)

    i = 0
    with open("m3u8.txt",mode="wb") as f:
      f.write(resp.content)

    with open("m3u8.txt",mode="r",encoding="utf-8") as f:
        for line in f:
            if line.startswith("#"):
                continue
            line = line.strip()
            ts_url = Second_url_head + line
            name = str(i).zfill(4) + ts_url[-3:]
            file_path = os.path.join(current_folder, name)
            #file_path = os.path.join(current_folder, str(i).zfill(4))
            print(file_path)
            download_ts(ts_url,file_path)
            i += 1
    #merge_ts()
    merge_ts_windows()

    
'''
if __name__ == '__main__':
    main()
