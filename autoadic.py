import sys, subprocess, parameter
import matplotlib.pyplot as plt
from math import ceil

top, p, multiplier = 64, 2, 1
top, p = parameter.handle(sys.argv, (top, True), (p, True))
y, y1, y2 = [], [], []
if len(sys.argv) > 3:
    if "." in sys.argv[3]:
        multiplier = float(sys.argv[3])
    else:
        multiplier = int(sys.argv[3])

for i in range(1, ceil(multiplier*top) + 1):
    for j in range(1, top + 1):
        if j % p == 0:
            continue
        result = subprocess.run(['python', 'p-adicconv.py', str(i), str(j), str(p), "q"],
                stdout=subprocess.PIPE)
        result = str(result.stdout, 'utf-8').split("\t")
        y.append(int(result[0]))
        y1.append(int(result[1][2:]))
        y2.append(int(result[2][2:]))

fig, ax = plt.subplots(nrows=1, ncols=3)
ax[0].plot(range(len(y)), y)
ax[0].set_title("Total Length")
ax[0].axhline(16, color="green", linestyle="--")
ax[0].axhline(32, color="yellow", linestyle="--")
ax[0].axhline(64, color="red", linestyle="--")

ax[1].plot(range(len(y1)), y1)
ax[1].set_title("Infinite Portion")

ax[2].plot(range(len(y2)), y2)
ax[2].set_title("Finite Portion")

plt.suptitle(f"{p}-adic p/q lengths with combinations up to {top}\nwith a top multiplier of {multiplier}")
plt.show()
