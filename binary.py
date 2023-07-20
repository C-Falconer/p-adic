import sys, parameter
from color import *

n, ending = 0, "\n"
n, ending = parameter.handle(sys.argv, (n, True), ending)
print(bincolor(n))
