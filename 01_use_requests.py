import requests


response = requests.get('https://ncov.dxy.cn/ncovh5/view/pneumonia')
# print(response)
# response.encoding = 'utf-8'
# print(response.text)
# print(response.encoding)
print(response.content.decode())  # 二进制解码


