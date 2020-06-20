#!/usr/bin/python3

import sys
import subprocess
# Cygwin
#process = subprocess.Popen('cat /dev/clipboard'.split(), stdout=subprocess.PIPE,stderr=subprocess.PIPE)

# WSL
process = subprocess.Popen('powershell.exe -command Get-Clipboard'.split(), stdout=subprocess.PIPE,stderr=subprocess.PIPE)
output, error = process.communicate()

clip = str(output)
clip = clip.split('\\r\\n')
clip = iter(clip)

ini = sys.argv[1][2]
out_name = './sample_'+ini+'.txt'
out = open(out_name,'w')

flag = 1
for line in clip:
    #print(len(line),line, line=="Copy")
    if line == "Copy":
        if flag == 1:
            print("Input")
            out.write("Input\n")
        else:
            print("Output")
            out.write("Output\n")
        flag *= -1
        next(clip)
        for data in clip:
            data = data.strip()
            if data:
                print(data)
                out.write(data+"\n")
            else:
                break


