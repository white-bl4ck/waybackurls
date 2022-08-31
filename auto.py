import os
from termcolor import colored
lines = 0
_Counter = 0 
with open('domains.txt','r') as f:
    for i in f:
        lines+= 1
    print('number of Lines: ', lines)
    f.seek(0)
    for rd in f: 
        line_strip = rd.strip()
        print("Procces on: "+line_strip)
        _Command = 'bash s.sh '+ line_strip +' '+str(_Counter+1)+'.way'
        os.system(_Command)
        _Counter += 1
        print (colored('Line ('+ str(_Counter) +') Completed; ','green')+colored(line_strip,'red'))
_Command = "cat *.way > merged-links.txt;rm *.way"
os.system(_Command)
print("Your links are here: "+colored("merged-links.txt","green"))

