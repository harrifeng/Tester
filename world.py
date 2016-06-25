# coding: utf-8
import sys
from jinja2 import Template
template = Template('Hello {{ name }} !')
print template.render(name='Haoran Feng')

m = Template(u"{% set a, b = 'foo', 'föö' %}").module
print m.a
reload(sys)
sys.setdefaultencoding('utf-8')
print m.b
