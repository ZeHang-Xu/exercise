import requests
import re
from bs4 import BeautifulSoup

response = requests.get('https://ncov.dxy.cn/ncovh5/view/pneumonia')
home_page = response.content.decode()
print(home_page)
# 提取疫情数据
# soup = BeautifulSoup(home_page, 'lxml')
# script = soup.find(id="getAreaStat", recursive=True)
# print(script.text)
# print(script)
# text = script.text
# print(script.string)

# 使用正则提取json字符串
# json_str = re.findall(r'(\[.*\])', script.string)
# print(json_str)
