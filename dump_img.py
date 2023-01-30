from os import listdir
import requests
from faker import Faker
import re

XZ_MD_PATH = "./xz.aliyun.com.md/"
TTTANG_MD_PATH = "./tttang.com.md/"
SEEBUG_MD_PATH = "./paper.seebug.org.md/"

def output_list(file_path):
    all_img = []
    file_list = listdir(file_path)
    for file_name in file_list:
        try:
            with open(file_path + file_name, "r") as f:
                text = f.read()
                # 匹配 https://xzfile.aliyuncs.com开头的所有格式图片链接
                # img_list = re.findall(r'(https://xzfile.aliyuncs.com.*?\.(png|jpg|jpeg|gif))', text)
                # 匹配 https://storage.tttang.com开头的图片链接
                # img_list = re.findall(r'(https://storage.tttang.com.*?\.(png|jpg|jpeg|gif))', text)
                # 匹配 https://images.seebug.org开头的图片链接
                # img_list = re.findall(r'(https://images.seebug.org.*?)-w331s', text)
                img_list = re.findall(r'(http://images.sebug.net.*?)\)', text)
            # for i in img_list:
            #     all_img.append(i[0])
            # print(img_list)
            all_img.extend(img_list)
            print("%s ok: %d" % (file_name, len(img_list)))
        except Exception as e:
            print('%s error: %s' %(file_name, e))
            continue

    # 去重
    all_img = list(set(all_img))
    # 写入文件
    with open("seebug_old_img.txt", "w") as f:
        for url in all_img:
            f.write(url + "\n")
    # print(all_img)
    print("write ok: %d" % len(all_img))
    

def dump_img(url, file_path):
    # headers = {
    #         'Host': 'xzfile.aliyuncs.com',
    #         'User-Agent': Faker().user_agent(),
    #         'Accept': '*/*',
    #         'Accept-Language': 'en',
    #         'Referer': 'https://xz.aliyun.com/',
    #         'Connection': 'close'
    #     }
    # headers = {
    #         'Host': 'storage.tttang.com',
    #         'User-Agent': Faker().user_agent(),
    #         'Accept': '*/*',
    #         'Accept-Language': 'en',
    #         'Referer': 'https://tttang.com/',
    #         'Connection': 'close'
    #     }
    headers = {
            'Host': 'images.seebug.org',
            'User-Agent': Faker().user_agent(),
            'Accept': '*/*',
            'Accept-Language': 'en',
            'Referer': 'https://paper.seebug.org/',
            'Connection': 'close'
        }
    try:
        resp = requests.get(url, headers=headers, timeout=3)
        with open(file_path, 'wb') as f:
            f.write(resp.content)
            print("%s ok" % url)
            return True
    except Exception as e:
        print("%s error: %s" % (url, e))
        return False

def dump_from_list(img_list, file_path):
    with open (img_list, "r") as f:
        urls = f.readlines()
        for url in urls:
            url = url.strip()
            file_name = url.split("/")[-1]
            file_dir = file_path + "img/" + file_name
            dump_img(url, file_dir)
        


if __name__ == '__main__':
    # output_list(XZ_MD_PATH)
    # output_list(TTTANG_MD_PATH)
    # output_list(SEEBUG_MD_PATH)

    # dump_from_list("tttang_img.txt", TTTANG_MD_PATH)
    dump_from_list("seebug_new_img.txt", SEEBUG_MD_PATH)
    # dump_from_list("seebug_old_img.txt", SEEBUG_MD_PATH)