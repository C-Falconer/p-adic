import sys, os

lis = sys.argv[1:]

for item in lis:
    os.system("python binary.py {0}".format(int(item.replace(",", ""))))
