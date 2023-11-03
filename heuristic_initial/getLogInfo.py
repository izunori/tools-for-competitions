import sys

args = sys.argv

log = args[1]

dic = {}
for arg in args[2:]:
    dic[arg] = ""

with open(log, 'r') as f:
    for line in f:
        if ':' in line:
            tag, value = line.split(':')
            tag = tag[1:].strip()
            value = value[1:].strip()
            if tag in dic:
                dic[tag] = value

out = []
for arg in args[2:]:
    out.append(dic[arg])

print(",".join(out))
