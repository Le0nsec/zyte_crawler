import requests
import re
from os import rename, chdir
from faker import Faker

def main():
    with open("tmp_no_title.txt", "r") as f:
        names = f.readlines()
        print(len(names))
    
    chdir("./tttang.com.md/")
    for name in names:
        num = name.split("-")[0]
        url = "https://tttang.com/archive/{}/".format(num)
        # print(url)
        title = get_title(url)
        if title:
            new_name = clean_file_name("{}-{}.md".format(num, title))
            rename(name.strip(), new_name)
            print("rename {} to {}".format(name.strip(), new_name))
        else:
            print("get title failed: {}".format(url))
            continue
            
            
def clean_file_name(filename):
    invalid_chars='[\\\/:*?"<>|]'
    replace_char=''
    return re.sub(invalid_chars,replace_char,filename)      

def get_title(url):
    headers = {
        'Host': 'tttang.com',
        'User-Agent': Faker().user_agent(),
        'Accept': '*/*',
        'Accept-Language': 'en',
        'Referer': 'https://tttang.com/',
        'Connection': 'close'
    }
    try:
        resp = requests.get(url, headers=headers, timeout=3)
        title = re.findall(r'<title>(.*?)</title>', resp.text)[0]
        # print(title)
        return title
    except Exception as e:
        print("%s error: %s" % (url, e))
        return None

if __name__ == "__main__":
    main()