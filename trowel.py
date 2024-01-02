#!/usr/bin/python3
import subprocess
import os
x = open('trowelib')
y = []
subprocess.run(['cat', 'trowelib'])
for line in x:
    z = line.split()[0]
    y.append(z)
print('create file-name')
e = input()
print('input a number which is before the address to apply that gadget to your code')
while 1 < 6:
    a = int(input())
    os.system('echo ' + str(y[a]) + '>>' + e)
    print('gadget added to code')
