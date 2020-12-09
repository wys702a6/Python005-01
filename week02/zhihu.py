import requests
from lxml import etree


url = "https://www.zhihu.com/question/377547324/answer/1516614122"

header = {
    "User-Agent": r"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Mobile Safari/537.36"
}

s = requests.Session()
response = s.get(url, headers=header)

selector = etree.HTML(response.text)
my_xpath = "//div[@class='RichContent-inner']/span/p/text()"

res = selector.xpath(my_xpath)

for i in res:
    print(i)
