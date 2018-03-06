#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def logtiqu(sourcefile='F:\\tongjisx.txt',objectfile='F:\\log.txt'):
    '提取日志中需要的内容'
    tongjifile=open(sourcefile,'r')
    n = open(objectfile,'w')
    lines=tongjifile.readlines()
    for line in lines:
        if 'timeout' in line:
            n.write(line.replace('\n',''))
            n.write('\n')
        else:
            if len(line) >4:
                try:
                    if 'ExecuteThread' not in line:
                        a=line.split(']')[1].replace('\n','')
                        n.write(a)
                        n.write('\n')
                except:
                    print line
    tongjifile.close()
    n.close()

tx=open('F:\\log.txt')
lines=tx.readlines()
dd={}
for line in lines:
    a=line.split(':')
    dd.setdefault(a[0],[])
    if a[1].replace('\n','')=='timeout':
        pass
    elif float(a[1].replace('\n','')) > 10 :
        dd[a[0]].append(a[1].replace('\n',''))

tx.close()

for key in dd.keys():
    # dd[key].sort()
    print key,len(dd[key])


