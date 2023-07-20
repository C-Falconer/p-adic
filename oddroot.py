import matplotlib.pyplot as plt
import sys, parameter

n = 5
n = parameter.handle(sys.argv, (n, True))

y = []
for i in range(1, n + 1):
    num = i
    if num % 2 != 0:
        y.append(0)
        continue
    while num % 2 == 0:
        num //= 2
    y.append(num)

plt.plot(range(1, n+1), y)
plt.show()
