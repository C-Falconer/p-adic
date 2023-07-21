import sys, parameter
from color import *

n, ending, dec = 0, "\n", False
n, ending = parameter.handle(sys.argv, (n, True), ending)
if len(sys.argv) > 3:
    dec = sys.argv[3] == 'd'

if dec:
    print(int(str(n), 2))
else:
    print(bincolor(n))
