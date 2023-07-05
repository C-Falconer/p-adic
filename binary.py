import sys

n = 0
ending = "NULL"
if len(sys.argv) > 1:
    n = int(sys.argv[1])
if len(sys.argv) > 2:
    ending = sys.argv[2]

if ending == "NULL":
    ending = "\n"
print(bin(n)[2:].replace("1", "\033[91m1\033[00m"), end=ending)
