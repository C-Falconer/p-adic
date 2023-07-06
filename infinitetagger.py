import color
import prime
import subprocess, sys, math

n = 5
if len(sys.argv) > 1:
    n = int(sys.argv[1])

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

def isSameTag(tag1, tag2):
    tags = map(str, [tag1, tag2])
    sizes = map(len, tags)
    shapes = [[], []]
    for i, tag in enumerate(tags):
        index = 0
        one = tag[0] == "1"
        #print(tag)
        while tag.find(str(int(one)), index) != -1:
            shapes[i].append(str(int(one)) + str(tag.count(str(int(one)), index, tag.find(str(int(not one)), index))))
            one = not one
            index = tag.find(str(int(one)), index)
            #print(tag[index:], shapes[i])
        shapes[i][-1] = shapes[i][-1][0] + str(int(shapes[i][-1][1:]) + 1)
        if tag[0] == tag[-1]:
            tagtype = shapes[i][0][0]
            newfirst = tagtype + str(int(shapes[i][0][1:]) + int(shapes[i][-1][1:]))
            shapes[i][0] = newfirst
            shapes[i].pop()
    #print(shapes[0], shapes[1])
    for i in range(len(shapes[0])):
        if swap(shapes[0], i) == shapes[1]:
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
        #CHECK THIS
        returnval = returnval and isSameTag(tags[comb[0]], tags[comb[1]])
    return returnval

for i in range(n + 1):
    m = 2*i + 1
    if not prime.isprime(m):
        continue
    result = subprocess.run(['python', 'uptoadic.py', str(m)], stdout=subprocess.PIPE)
    result = str(result.stdout, 'utf-8').split("\n")
    #print(result)
    tags = []
    for item in result[:-1]:
        item = item.split("\t")
        item[2] = color.color(color.decolor(item[2])[:-2])
        tags.append(color.decolor(item[2]))
        [print(x, end="\t") for x in item]
        print()
    if tags == []:
        continue
    print(checkalltags(tags))
#print(isSameTag("100011", "110101"))
#print(isSameTag("010111", "110101"))
#print(isSameTag("101000", "110101"))
#print(isSameTag("1110", "1111"))
#print(isSameTag("1111", "1110"))
