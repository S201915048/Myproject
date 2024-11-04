import requests
import os
from Crypto.Cipher import AES

def download_ts(url,name):
    resp = requests.get(url)
    with open(name,mode="wb") as f:
        f.write(resp.content)

def dec_ts(name,name2,key):
    aes = AES.new(key=key, IV=b"0000000000000000",mode=AES.MODE_CBC)
    with open(name,mode="rb") as f1:
        with open(name2,mode="wb") as f2:
            bs = f1.read()
            print(len(bs)%16)
            f2.write(aes.decrypt(bs))

def main():
    Second_url=""
    Second_url_head = ""
    key = b"d7f8039aea88af8b"

    current_folder = os.getcwd() + "\\vedio1"
    current_folder2= os.getcwd() + "\\vedio2"
    #存了第二次m3u8的文件
    resp = requests.get(Second_url)
    #with open("m3u8.txt",mode="wb") as f:
        #f.write(resp.content)

    with open("m3u8.txt",mode="r",encoding="utf-8") as f:
        for line in f:
            if line.startswith("#"):
                continue
            line = line.strip()
            ts_url = Second_url_head + line
            name = line.replace(line[:30]," ")
            name = name.strip()   
            file_path = os.path.join(current_folder, name)
            name2 = os.path.join(current_folder2, name)
            download_ts(ts_url,file_path)
            print(file_path)
            print(name2)
            dec_ts(file_path,name2,key)



if __name__ == '__main__':
    main()