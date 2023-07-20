import sys, os
import prime, parameter

n = 5
n = parameter.handle(sys.argv, (n, True))

command = "clear"

for i in range(1, n + 1):
    m = 2*i + 1
    if not prime.isprime(m):
        continue
        #command += " && echo -n \"P \""
    command += f" && python binary.py {m} && python uptoadic.py {m}"
os.system(command)
