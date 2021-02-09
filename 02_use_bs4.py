from bs4 import BeautifulSoup

html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>The Dormouse's story</title>
</head>
<body>
    <p> class="title">
        <b>The Dormouse's story</b>
    </p>
    <p> class="story">Once upon aa time there were three little sisters; and their names were
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>and
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        and they lived at the bottom of a well.
    </p>
    <p class="story">...</p>
</body>
</html>
'''

soup = BeautifulSoup(html, 'lxml')
# 查找title标签
# title = soup.find('title')
# print(title)

# 查找a标签
# a = soup.find('a')
# print(a)

# a_s = soup.find_all('a')
# print(a_s)

# 根据属性查找
a = soup.find(id='link1')
print(a.text)

# a = soup.find(attrs={'id': 'link1'})
# print(a)

# 根据文本内容查找
# text = soup.find(text='Elsie')
# print(text)
print(type(a))  # Tag 对象
# print('标签名: {}'.format(a.name))
print('标签属性: {}'.format(a.attrs))
# print('标签文本内容: {}'.format(a.text))