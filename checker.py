#!/usr/bin/python3
import sys
import subprocess
from time import time
from subprocess import PIPE
PYEXE = "/cygdrive/d/application/Anaconda3/python.exe" 
script = sys.argv[1]
num = int(sys.argv[2])
if len(sys.argv) > 3:
    ts = float(sys.argv[3])
else:
    ts = 3.0
print("test:{} with sample{}".format(script,num))

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
n = 1
Q = Qs[num-1]
A = As[num-1]
print("example {}/{}".format(num,len(Qs)))
print("input:")
print("".join(Q).strip())
print("answer:")
print("".join(A).strip())

p = subprocess.Popen([PYEXE,script],stdout=PIPE,stdin=PIPE,stderr=PIPE)
data = str.encode("".join(Q))
start = time()
try:
    out, error = p.communicate(input=data,timeout=ts)
except subprocess.TimeoutExpired:
    p.kill()
    out, error = p.communicate()
    print("- TimeOUT!")
elapsed = time() - start
print("time:{:>4.0f}[ms]".format(elapsed*1000))
print("output:")
print(out.decode())
print("error:")
print(error.decode())
