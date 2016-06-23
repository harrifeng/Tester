from jinja2 import Environment, PackageLoader
from Tester import Mamalls

env = Environment(loader=PackageLoader("Tester", "templates"))
print env

m = Mamalls()
m.printMember()
