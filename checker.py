#!/usr/bin/python3
import platform
import sys
import subprocess
from time import time
from subprocess import PIPE

# Windows
#PYEXE = "/cygdrive/d/application/Anaconda3/python.exe" 
# WSL
PYEXE = "/usr/bin/python3"

script = sys.argv[1]
num = int(sys.argv[2])
if len(sys.argv) > 3:
    ts = float(sys.argv[3])
else:
    ts = 3.0
print("test:{} with sample{}".format(script,num))

Qs = []
As = []
ini=script[2]
sample_file="sample_"+ini+'.txt'
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
# n = 1
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
