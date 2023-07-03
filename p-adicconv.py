import sys

r = -1
q = 3
p = 2
quiet = False
if len(sys.argv) > 1:
    r = int(sys.argv[1])
if len(sys.argv) > 2:
    q = int(sys.argv[2])
if len(sys.argv) > 3:
    p = int(sys.argv[3])
if len(sys.argv) > 4:
    quiet = sys.argv[4] == "q"

if q % p == 0:
    print(f"Can only handle denominators without a factor of p({p}).")
    sys.exit(0)

k = range(p)
adic = []
remainders = []
done = False
while not done:
    for ki in k:
        if abs(r - q*ki) % p == 0:
            ri = (r - q*ki) // p
            if not quiet: print(f"{r}/{q} = {ki} + {p}({ri}/{q})")
            adic.insert(0, ki)
            if ri in remainders:
                adic.insert(remainders.index(ri) + 1, "_")
                done = True
                break
            remainders.insert(0, ri)
            r = ri
            break
while adic[0] == 0:
    adic.pop(0)

if len(adic) - len(adic[:adic.index("_")]) == 2 and adic[-1] == 0:
    adic = adic[:-1]

if len(adic[adic.index("_") + 1:]) == 1 and adic[adic.index("_") - 1] == adic[-1]:
    adic.pop()

if not quiet: print(adic, end=" ")
print("{0}\tL:{1}\tR:{2}".format(len(adic) - 1, adic.index("_"), len(adic) - adic.index("_") - 1))
