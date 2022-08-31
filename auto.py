import os
import time
from termcolor import colored
lines = 0
_Counter = 0 
def _sh(x):
    with open('script.sh','w') as sh:
        if x == 1:
            sh.write('go run main.go "$1" > "$2"')
        if x == 0:
            try:
                os.mkdir('domains')
                with open('script.sh','w') as sh:
                    sh.write('go run main.go "$1" > domains/"$2"')
            except FileExistsError:
                with open('script.sh','w') as sh:
                    sh.write('go run main.go "$1" > domains/"$2"')


def _Counting():
    global lines
    with open('domains.txt','r') as f:
        for i in f:
            lines += 1
def _run_script(x):
    _Counter = 0
    if x == 1:
        with open('domains.txt','r') as f:
            print('number of Lines: ', lines)
            f.seek(0)
            for rd in f: 
                line_strip = rd.strip()
                print("Process on: "+line_strip)
                _Command = 'bash script.sh '+ line_strip +' '+str(_Counter+1)+'.way'
                os.system(_Command)
                _Counter += 1
                print (colored('Line ('+ str(_Counter) +') Completed; ','green')+colored(line_strip,'red'))
    if x == 0:
        with open('domains.txt','r') as f:
            print('number of Lines: ', lines)
            f.seek(0)
            for rd in f: 
                line_strip = rd.strip()
                _Command = 'bash script.sh '+ line_strip +' '+ line_strip
                os.system(_Command)
                _Counter += 1
                print (colored('Line ('+ str(_Counter) +') Completed; ','green')+colored(line_strip,'red'))
def _end(x):
    if x == 1:
        _Command = "cat *.way > merged-links.txt;rm *.way;rm script.sh"
        os.system(_Command)
        print("Your links are here: "+colored("merged-links.txt","green"))
    if x == 0:
        os.system('rm script.sh')

def delay_print(s):
    for c in s:
        print(c,end='')
        time.sleep(0.015)

delay_print('__        ___     _ _             _     _ _  _        _\n')
delay_print("\ \      / / |__ (_) |_ ___      | |__ | | || |   ___| | __\n")
delay_print(" \ \ /\ / /| '_ \| | __/ _ \_____| '_ \| | || |_ / __| |/ /\n")
delay_print("  \ V  V / | | | | | ||  __/_____| |_) | |__   _| (__|   <\n")
delay_print("   \_/\_/  |_| |_|_|\__\___|     |_.__/|_|  |_|  \___|_|\_\ \n")
delay_print("https://white_bl4ck.t.me\n")
print('-----------------------------------------------------------\n\n')

try:
    _what = int(input('separately saving = 0 \nmerge all = 1\nWhat to do? '))
    if _what == 1 :
        _sh(_what)
        _Counting()
        _run_script(_what)
        _end(_what)
    elif _what == 0:
        _sh(_what)
        _Counting()
        _run_script(_what)
        _end(_what)
    else:
        print('Wrong value; try again. :)')
except ValueError:
    print('Wrong value; try again. :)')
except ImportError:
    input('It seems you have Termcolor library.\n press any key to install or ctrl+c for stop')
    os.system('pip3 install termcolor')
