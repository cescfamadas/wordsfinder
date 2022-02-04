import re
file1 = open('net.txt', 'r')
lines = file1.readlines()
r=re.compile("(^.i.a.$)")
for l in lines:
    l=l.rstrip().lower()
    if(len(l)==5):
        if(r.match(l)):
            print(l)
