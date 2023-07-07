import color
import prime
import subprocess, sys, math

n = 5
printing = True
if len(sys.argv) > 1:
    n = int(sys.argv[1])
if len(sys.argv) > 2:
    printing = sys.argv[2] != "q"

def swap(lis, amount):
    if amount == 0:
        return lis
    length = len(lis)
    for j in range(amount):
        old, old2 = lis[0], -1
        for i in range(length):
            nextind = (i + 1) % length
            old2 = lis[nextind]
            lis[nextind] = old
            old = old2
    return lis

def isSameTag(tag1, tag2, quiet=True):
    tags = map(str, [tag1, tag2])
    shapes = [[], []]
    for i, tag in enumerate(tags):
        index = 0
        one = tag[0] == "1"
        if not quiet: print(tag)
        while tag.find(str(int(one)), index) != -1:
            shapes[i].append(str(int(one)) + str(tag.count(str(int(one)), index, tag.find(str(int(not one)), index))))
            one = not one
            index = tag.find(str(int(one)), index)
        shapes[i][-1] = shapes[i][-1][0] + str(int(shapes[i][-1][1:]) + 1)
        if tag[0] == tag[-1]:
            tagtype = shapes[i][0][0]
            newfirst = tagtype + str(int(shapes[i][0][1:]) + int(shapes[i][-1][1:]))
            shapes[i][0] = newfirst
            shapes[i].pop()
    if not quiet: print(shapes[0], shapes[1])
    if len(shapes[0]) != len(shapes[1]):
        if not quiet: print("Skipping due to different lengths")
        return False
    for i in range(len(shapes[0])):
        newshape = swap(shapes[0], 1)
        if not quiet: print(newshape)
        if newshape == shapes[1]:
            return True
    return False        

def C(n):
    returnlist = []
    for i in range(n):
        for j in range(i + 1, n):
            returnlist.append((i, j))
    return returnlist

def checkalltags(tags):
    returnval = True
    for comb in C(len(tags)):
        returnval = returnval and isSameTag(tags[comb[0]], tags[comb[1]])
    return returnval

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    y = []
    y2 = []
    last_m = -1
    for i in range(n + 1):
        m = 2*i + 1
        if not prime.isprime(m):
            continue
        result = subprocess.run(['python', 'uptoadic.py', str(m)], stdout=subprocess.PIPE)
        result = str(result.stdout, 'utf-8').split("\n")
        tags = []
        for item in result[:-1]:
            item = item.split("\t")
            item[2] = color.color(color.decolor(item[2])[:-2])
            tags.append(color.decolor(item[2]))
            if printing: [print(x, end="\t") for x in item]; print()
        if tags == []:
            continue
        alltagsequal = checkalltags(tags)
        if printing: print(alltagsequal, len(tags[0]))
        if alltagsequal:
            y.append(len(tags[0]))
        else:
            y2.append(len(tags[0]))
        last_m = m
    plt.plot(y, label="Equal Tags")
    plt.plot(y2, label="Non-Equal Tags")
    plt.xlabel("Amount of Tags")
    plt.ylabel("Size of Tags")
    plt.title(f"Sizes of Infinite Portions (Tags) for Prime Denominators > 2\nup to {last_m}")
    plt.axhline(16, ls="--", color="green")
    plt.axhline(32, ls="--", color="yellow")
    plt.axhline(64, ls="--", color="red")
    plt.legend()
    plt.show()
