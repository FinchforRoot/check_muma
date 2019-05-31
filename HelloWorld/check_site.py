# _*_ coding: utf-8 _*_
import requests
from bs4 import BeautifulSoup
import re


'''
根据给出的URL获取它的源代码
'''
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

'''
根据给出的URL将其保存在某个文件下
以URL的名字作为文件名
意外错误：需要用正则表达式剔除
/*等非法字符，保留剩下的字符串
'''
def save_html(url):
    try:
        text = getHTML(url)
        url = re.sub('\.', '_', url)
        url = re.sub(':', '_', url)
        url = re.sub('/', '', url)
        url = re.sub('=', '', url)
        with open(url + '.txt', 'w', encoding='utf-8') as fw:
            fw.write(text)
        print(url + '.txt保存成功')
    except:
        print(url + '.txt保存失败')


'''
检测网站所有网页是否有被挂马的
'''
def check_security(url):
    dict = get_dict(url)
    pattern = re.compile(r'\biframe\b.+src=(http|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?|document.location|document.write|fromCharCode|eval|unescape|replace|\\x|%u')
    for key in dict:
        if re.findall(pattern, dict[key]):
            print(key+'被挂马')
        else:
            print(key+'安全')


'''
根据初始网站获取字典存储URL及相对应的源代码
'''
def get_dict(url):
    text = getHTML(url)
    urlList = getAllUrl(text)
    textList = []
    for item in urlList:
        html = getHTML(item)
        textList.append(html)
    dictionary = dict(zip(urlList, textList))
    return dictionary


'''
根据第一个给出的URL获取到的源代码
提取出符合规则的URL组
进行各个URL源码的获取
返回一个关于源代码的列表
'''
def getAllUrl(text):
    soup = BeautifulSoup(text, 'html.parser')
    urlList = []
    newUrlList = []
    for link in soup.find_all('a'):
        urlList.append(link.get('href'))
    for i in urlList:
        if i:
            if 'http' not in i:
                pass
            else:
                newUrlList.append(i)
    return newUrlList


if __name__ == '__main__':
    # txt = 'document.location'
    # pattern = re.compile(r'\biframe\b.+src=(http|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?|document.location|document.write|fromCharCode|eval|unescape|replace|\\x|%u')
    # result = re.findall(pattern, txt)
    # print(result)
    # check_security('http://news.sohu.com')
    check_security('http://www.sylu.edu.cn/sylusite')
    # time1 = time.perf_counter()
    # text = getHTML('http://news.sohu.com')
    # urlList = getAllUrl(text)
    # textList = []
    # for item in urlList:
    #     html = getHTML(item)
    #     textList.append(html)
    # time2 = time.perf_counter()
    # time = (time2 - time1) / 60
    # print('总共爬去花费{}分钟'.format(time))
    # print(len(urlList))
    # print(len(textList))
    # dicti = dict(zip(urlList, textList))
    # for url in urlList:
    #     save_html(url)