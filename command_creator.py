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
    else:
        print("Not supported script type")
        exit()

    return preprocess, command
    



