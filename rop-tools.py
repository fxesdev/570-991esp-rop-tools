#!/usr/bin/python3
import os
import subprocess
print('rop tools by u68')
def printf(stuff):
    subprocess.run(['printf', str(stuff)])
while 1 < 2:
    printf('\e[1;35m> ')
    x = input().split(' ')
    if (x[0] == 'help'):
        os.system('./help.py')
    if (x[0] == 'gadget-to-hex'):
        # print('somethings-right!')
        os.system('./gadget-to-hex.py ' + x[1])
        #print('somethings-wrong!', x)
    if (x[0] == 'trowel'):
        os.system('./trowel.py')
