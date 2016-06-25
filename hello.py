from jinja2 import Environment, PackageLoader
from Tester import Mamalls

env = Environment(loader=PackageLoader("Tester", "templates"))
print env

template = env.get_template('mytemplate.html')
print template.render(the='variable', go='here')

m = Mamalls()
m.printMember()
