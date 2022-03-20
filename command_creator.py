import os
import subprocess
from config import *

def createCommand(script):
    root, ext = os.path.splitext(script)
    if ext == '.py':
        preprocess = lambda : ()
        command = f"{PYEXE} {script}"
    elif ext == '.kt':
        out = root+'.jar'
        preprocess = lambda : subprocess.run(f'kotlinc {script} -include-runtime -d {out}',shell=True)
        command = f"kotlin {out}"
    elif ext == '.fs':
        out = root+'.exe'
        preprocess = lambda : subprocess.run(f'fsharpc {script}',shell=True)
        command = f"mono {out}"
    elif ext == '.cpp':
        out = './cppout'
        run = f"g++ -O2 --std=gnu++17 {script} -o {out}"
        preprocess = lambda : subprocess.run(run,shell=True)
        command = f"{out}"

    else:
        print("Not supported script type")
        exit()

    print("command : ", command)
    return preprocess, command
    



