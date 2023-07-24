import color, prime, parameter
import subprocess, sys, math, time

n = 5
n = parameter.handle(sys.argv, (n, True))
printing = True
halfmode = False
if len(sys.argv) > 2:
    printing = sys.argv[2][0] != "q"
    if len(sys.argv[2]) > 1:
        halfmode = sys.argv[2][1] == "h"

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

def isSameTag(tag1, tag2, quiet=True, inverting=False):
    tags = map(str, [tag1, tag2])
    shapes = [[], []]
    for i, tag in enumerate(tags):
        index = 0
        tag = str(tag)
        tag = tag.replace("[", "").replace("]", "")
        one = tag[0] == "1"
        if not quiet: print(tag, inverting)
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

def checkalltags(tags, inv=False):
    returnval = True
    for comb in C(len(tags)):
        comb_bool = isSameTag(tags[comb[0]], tags[comb[1]])
        if inv:
            comb_bool = comb_bool or isSameTag(invert(tags[comb[0]]), tags[comb[1]])
        returnval = returnval and comb_bool
    return returnval

def invert(*tags):
    invtags = []
    for a in tags:
        a = str(a)
        b = ""
        for bit in a:
            b += str(int(not bool(int(bit))))
        invtags.append(b)
    if len(invtags) == 1:
        return invtags[0]
    return invtags

def checkhalves(tags):
    for tag in tags:
        tag = str(tag)
        if len(tag) % 2 != 0 or tag[len(tag)//2:] != invert(tag[:len(tag)//2]):
            return False
    return True

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    x, x2, x3, y, y2, y3 = [], [], [], [], [], []
    last_m = -1
    if not printing: percent_complete, times, starttime = 10, [0], time.time()
    for i in range(n + 1):
        m = 2*i + 1
        if not printing and 100 * i / n > percent_complete and not halfmode:
            percent_complete += 10
            times.append(time.time() - starttime)
            print(f"{percent_complete - 10}% ({times[-1]:.2f})s...", end = " ", flush=True)
        if not prime.isprime(m):
            continue
        result = subprocess.run(['python', 'uptoadic.py', str(m)], stdout=subprocess.PIPE)
        result = str(result.stdout, 'utf-8').split("\n")
        tags = []
        denom = -1
        for item in result[:-1]:
            item = item.split("\t")
            item[2] = color.color(color.decolor(item[2])[:-2])
            tags.append(color.decolor(item[2]))
            denom = int(item[1].split("/")[1])
            if printing: [print(x, end="\t") for x in item]; print()
        if tags == []:
            continue
        alltagsequal = checkalltags(tags)
        if alltagsequal and not checkhalves(tags):
            print("Not halves but equal", tags)
            break
        if printing: print(alltagsequal, len(tags[0]))
        if alltagsequal:
            if halfmode: [print(denom, x) for x in tags]
            x.append(denom)
            y.append(len(tags[0]))
        else:
            inverttagequal = checkalltags(tags, True)
            if printing: print(inverttagequal)
            if inverttagequal:
                x3.append(denom)
                y3.append(len(tags[0]))
            else:
                x2.append(denom)
                y2.append(len(tags[0]))
        last_m = m
    if halfmode: sys.exit(0)
    if not printing:
        times.append(time.time() - starttime); print(f"100% ({times[-1]:.2f})s")
        plt.plot(range(0, 110, 10), times); plt.xlabel("Percents"); plt.ylabel("Time Taken");
        plt.title("Time to run program"); plt.show()
    y = [x//2 if x % 2 == 0 else x for x in y]
    y3 = [x//2 if x % 2 == 0 else x for x in y3]
    plt.plot(x, y, label="Equal Tags", marker=".")
    plt.plot(x2, y2, label="Non-Equal Tags", marker=".")
    plt.plot(x3, y3, label="Invert Equal Tags", marker=".")
    plt.xlabel("Denominators")
    plt.ylabel("Size of Tags")
    plt.title(f"Sizes of Infinite Portions (Tags) for Prime Denominators > 2\nup to {last_m}")
    plt.axhline(16, ls="--", color="green")
    plt.axhline(32, ls="--", color="yellow")
    plt.axhline(64, ls="--", color="red")
    plt.legend()
    plt.show()
