# coding=utf-8
'''
Created on 2019年04月02日
@author: quqiao
第五课：BeautifulSoup库的使用
'''

# 快速使用
# from bs4 import BeautifulSoup
# html = '''
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>
#
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
# <p class="story">...</p>
# '''
# soup = BeautifulSoup(html, 'lxml')
# print(soup.prettify())
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.parent.name)
# print(soup.p)
# print(soup.p["class"])
# print(soup.p.attrs['class'])
# print(soup.a)
# print(soup.find_all('a'))
# print(soup.find_all(id="link3"))
# for link in soup.find_all('a'):
#     print(link.get('href'))
# print(soup.get_text())
# print(soup.p.contents)

# 解析器：Beautiful Soup支持Python标准库中的HTML解析器，还支持一些第三方的解析器
#         1)Python标准库 BeautifulSoup(markup,"html.parser")
#         2)lxml HTML解析器 BeautifulSoup(markup,"lxml")
#         3)lxml XML解析器 BeautifulSoup(markup, "xml")
#         4)html5lib   BeautifulSoup(markup, "html5lib")

# 基本使用：
# 1)标签选择器：通过soup.标签名，获取这个标签的内容，如果文档中有多个这样的标签，返回的结果是第一个标签的内容
# 2)获取名称：通过soup.title.name可以获得该title标签的名称
# 3)获取属性：soup.p.attrs['name']和soup.p['name']
# 4)获取内容：soup.p.string
# 5)嵌套选择：soup.head.title.string
# 6)子节点和子孙节点：contents的使用
#   children的使用：soup.p.children是一个迭代对象，而不是列表，只能通过循环的方式获取素有的信息
#   soup.descendants：获取子孙节点，获取的结果也是一个迭代器
# 7)父节点和祖先节点：soup.a.parent获取父节点的信息
#   通过list(enumerate(soup.a.parents))可以获取祖先节点
# 8)兄弟节点：soup.a.next_siblings:获取后面的兄弟节点
#             soup.a.previous_sibling:获取前面的兄弟节点
#             soup.a.next_sibling:获取下一个兄弟标签
#             soup.a.previous_sibling:获取上一个兄弟标签

# 标准选择器
# find_all:可以根据标签名，属性，内容查找文档
# html = '''
# <div class="panel">
#     <div class="panel-heading">
#         <h4>Hello</h4>
#     </div>
#     <div class="panel-body">
#         <ul class="list" id="list-1">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#             <li class="element">Jay</li>
#         </ul>
#         <ul class="list list-small" id="list-2">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#         </ul>
#     </div>
# </div>
# '''
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, "lxml")
# print(soup.find_all('ul'))
# print(type(soup.find_all('ul')[0]))
# print(soup.find_all(attrs={'id': 'list-1'}))
# print(soup.find_all(attrs={'class': 'element'}))
# print(soup.find_all(text='Foo'))
# find:返回匹配结果的第一个元素
# find_parents():返回所有祖先节点
# find_parent():返回直接父节点
# find_next_siblings():返回后面所有兄弟节点
# find_next_sibling():返回后面第一个兄弟节点
# find_previous_siblings():返回前面所有兄弟节点
# find_previous_sibling():返回前面第一个兄弟节点
# find_all_next():返回节点后所有符合条件的节点
# find_next():返回第一个符合条件的节点
# find_all_previous():返回节点后所有符合条件的节点
# find_previous():返回第一个符合条件的节点

# CSS选择器：通过select()直接传入CSS选择器完成选择
html = '''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# print(soup.select('.panel .panel-heading'))
# print(soup.select('ul li'))
# print(soup.select('#list-2 .element'))
# print(soup.select('ul')[1])
# for li in soup.select('li'):
#     print(li.get_text())
# for ul in soup.select('ul'):
#     print(ul['id'])
    # print(ul.attrs['id'])