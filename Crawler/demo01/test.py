# coding=utf-8
'''
Created on 2019年04月10日
@author: quqiao
弄来测试用的
'''

from bs4 import BeautifulSoup
import requests

url = "http://image.baidu.com/"
response = requests.get(url)
html = response.text
# print(html)
baidu = BeautifulSoup(html, 'lxml')
print(baidu.select('a img'))
# # for link in baidu.select('a img'):
# #     print(link.get('src'))

# html='''
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
# soup = BeautifulSoup(html, 'lxml')
# # print(soup.select('.panel .panel-heading'))
# # print(soup.select('ul li'))
# print(soup.select('#list-2 .element'))
# # print(type(soup.select('ul')[0]))