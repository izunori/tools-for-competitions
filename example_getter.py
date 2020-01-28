#!/usr/bin/python3

import subprocess
process = subprocess.Popen('cat /dev/clipboard'.split(), stdout=subprocess.PIPE,stderr=subprocess.PIPE)
output, error = process.communicate()

clip = str(output)
clip = clip.split('\\r\\n')
clip = iter(clip)

out = open('./example.txt','w')
for line in clip:
    #print(len(line),line, line=="Copy")
    if line == "Copy":
        next(clip)
        for data in clip:
            data = data.strip()
            if data:
                print(data)
                out.write(data+"\n")
            else:
                print()
                out.write("\n")
                break


