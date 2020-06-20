#!/usr/bin/python3
import os
import sys
import subprocess
from time import time
from subprocess import PIPE
# Windows
#PYEXE="/cygdrive/d/application/Anaconda3/python.exe" 
# WSL
PYEXE="/usr/bin/python3"
print(os.name,PYEXE)
script = sys.argv[1]
print("test:{}".format(script))

ini=script[2]
sample_file="sample_"+ini+'.txt'
Qs = []
As = []
with open(sample_file,'r') as f:
    data = []
    for line in f:
        if "Input" in line:
            As.append(data[:])
            data = []
            continue
        if "Output" in line:
            Qs.append(data[:])
            data = []
            continue
        data.append(line)
    As.append(data[:])
As = As[1:]
test = []
times = []
for n,(Q,A) in enumerate(zip(Qs,As)):
    print("s{}".format(n+1))
    p = subprocess.Popen([PYEXE,script],stdout=PIPE,stdin=PIPE,stderr=PIPE)
    data = str.encode("".join(Q))
    start = time()
    out, error = p.communicate(input=data)
    elapsed = time() - start
    times.append(elapsed)
    print("time:{:>4.0f}[ms]".format(elapsed*1000))
    if error:
        print("ERROR : wrong input")
        test.append("RE")
        continue

    out = out.decode().split('\n')[:-1]

    if not len(out) == len(A):
        print("ERROR : wrong output size")
        test.append("WA")
        continue

    correct = True 
    for o,a in zip(out,A):
        a = a.strip()
        if o == a:
            print("  {} == {}".format(o,a))
        else:
            print("  {} <> {}".format(o,a))
            correct = False
    if correct:
        test.append("AC")
    else:
        test.append("WA")

for n,(result,ts) in enumerate(zip(test,times)):
    print("sapmle {} : {} : {:>4.0f}ms".format(n+1,result,ts*1000))

    
