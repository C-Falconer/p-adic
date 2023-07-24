import os, sys, subprocess
import parameter
from color import *

n = parameter.handle(sys.argv, (10, True))

result = subprocess.run(['python3', 'infinitetagger.py', str(n), "qh"], stdout=subprocess.PIPE)
result = str(result.stdout, 'utf-8').split("\n")[:-1]
print(colors.UNDERLINE + "n\tTag Half" + colors.END, flush=True)
last_denom = 0
denoms = []
converted_halves = []
for item in result:
    denom = item.split(" ")[0]
    tag = item.split(" ")[1]
    tag_half = tag[len(tag)//2:]
    print(denom, end = "\t", flush=True)
    sub_result = subprocess.run(['python3', 'binary.py', tag_half, "\"\"", "d"], stdout=subprocess.PIPE)
    sub_result = str(sub_result.stdout, 'utf-8')
    converted_halves.append(int(sub_result))
    print(converted_halves[-1], end = "\t", flush=True)
    if denom == last_denom:
        dif = converted_halves[-1] - converted_halves[-2]
        print(dif, end="\t", flush=True)
        os.system("python3 binary.py " + str(dif))
    else:
        last_denom = denom
        print(flush=True)
    
