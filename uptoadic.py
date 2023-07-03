import sys, subprocess

top = 5
p = 2
if len(sys.argv) > 1:
    top = int(sys.argv[1])
if len(sys.argv) > 2:
    p = int(sys.argv[2])

results = []
for i in range(1, top):
    result = subprocess.run(['python', 'p-adicconv.py', str(i), str(top), str(p)],
            stdout=subprocess.PIPE)
    result = str(result.stdout, 'utf-8').split("\n")
    result = result[-2][1:result[-2].find("]")].replace(", ", "").replace("\'", "")
    results.append(result)

#maximum = len(max(results, key = len))
results_dict = {}
for i, result in enumerate(results):
    results_dict[f"{i + 1}/{top}"] = result.replace('1', "\033[91m1\033[00m")
results_dict = dict(sorted(results_dict.items(), key = lambda x:x[1]))
for key,values in results_dict.items():
    print(f"{key}\t{values}")
