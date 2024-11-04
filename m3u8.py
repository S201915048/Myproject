import requests
import subprocess
import os

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
 
 
def main():
    Second_url=""
    Second_url_head = ""
    

    current_folder = os.getcwd() + "\\vedio1"
    #存了第二次m3u8的文件
    resp = requests.get(Second_url)
    with open("m3u8.txt",mode="wb") as f:
        f.write(resp.content)

    with open("m3u8.txt",mode="r",encoding="utf-8") as f:
        for line in f:
            if line.startswith("#"):
                continue
            line = line.strip()
            ts_url = Second_url_head + line
            file_path = os.path.join(current_folder, line)
            print(file_path)
            download_ts(ts_url,file_path)
    #merge_ts()
    

if __name__ == '__main__':
    main()