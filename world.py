# coding: utf-8
from jinja2 import Template
template = Template('Hello {{ name }} !')
print template.render(name='Haoran Feng')

m = Template(u"{% set a, b = 'foo', 'föö' %}").module
print type(m.a), m.a
print type(m.b), m.b.encode('utf-8')
# UTF-8对于单字节的符号，字节的第一位设为0，后面7位为这个符号的unicode码。
# 因此对于英语字母，UTF-8编码和ASCII码是相同的。
print type(m.a), m.a.encode('utf-8')
