import sys
import parameter
from color import *

r, q = 1, 1
r, q = parameter.handle(sys.argv, (r, True), (q, True))

print(bincolor(r), "%", bincolor(q), "=", bincolor(r % q))
