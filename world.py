# coding: utf-8
from jinja2 import Template
template = Template('Hello {{ name }} !')
print template.render(name='Haoran Feng')

m = Template(u"{% set a, b = 'foo', 'föö' %}").module
print type(m.a), m.a
print type(m.b), m.b.encode('utf-8')
