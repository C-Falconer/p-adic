import sys, os

n = 5
if len(sys.argv) > 1:
    n = int(sys.argv[1])

command = "clear"

for i in range(1, n + 1):
    m = 2*i + 1
    command += f" && python binary.py {m} && python uptoadic.py {m}"

os.system(command)
