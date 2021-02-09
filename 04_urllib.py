from urllib.request import urlopen
import re

html = urlopen("https://ncov.dxy.cn/ncovh5/view/pneumonia").read().decode('utf-8')
# print(html)
res = re.findall(r'<body>(.*?)</body>', html, re.DOTALL)
print(res[0])
