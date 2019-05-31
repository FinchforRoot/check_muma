import re
import requests
from bs4 import BeautifulSoup


def getHTML(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
    }
    try:
        if ('http' not in url):
            pass
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''


# txt = 'basfkjbjkafsbkjabskjfbasjk'
txt = getHTML('http://qd.blkbx.cn//7')
# str = 'bfqwjbajkbajsb replace doreplace  eval'
pattern = re.compile(r'\biframe\b.+src=(http|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?|document.location|document.write|install|Install|fromCharCode|eval|unescape|replace|\\x|%u')
result = re.findall(pattern, txt)
if result!=[] :
    print('有')
else:
    print('无')