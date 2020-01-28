#!/usr/bin/python3
import sys
import subprocess
from time import time
from subprocess import PIPE
PYEXE = "/cygdrive/d/application/Anaconda3/python.exe" 
script = sys.argv[1]
print("test:{}".format(script))

Qs = []
As = []
with open('./example.txt','r') as f:
    for line in f:
        q = []
        a = []
        if line.strip():
            q.append(line)
            for line in f:
                if line.strip():
                    q.append(line)
                else:
                    break
            Qs.append(q)
            for line in f:
                if line.strip():
                    break
            a.append(line)
            for line in f:
                if line.strip():
                    a.append(line)
                else:
                    break
            As.append(a)
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

    out = out.decode().split('\r\n')[:-1]

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

    
