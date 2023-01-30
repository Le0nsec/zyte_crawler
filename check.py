import requests

def main():
    arr = []
    url = 'https://tttang.com/archive/{}/'

    for i in range(2, 1877):
        page = url.format(i)
        result = check(page)
        if result:
            arr.append(i)

    print(arr)
        

def check(page):
    headers = {
            'Host': 'tttang.com',
            'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)',
            'Accept': '*/*',
            'Accept-Language': 'en',
            'Connection': 'close'
        }
    
    try:
        resp = requests.get(page, headers=headers, timeout=4)
        print('%s %s' % (page, resp.status_code))
        if resp.status_code == 200 and '>404 Not Found</h2>' in resp.text:
            return True
    except Exception as e:
        print('[!] %s error: %s' % (page, e))
        return False
    return False

if __name__ == '__main__':
    main()