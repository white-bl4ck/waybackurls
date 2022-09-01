import os
import time
import sys

def install(package):
    os.system('pip3 install '+package)
    
try:
    import pip
except ImportError:
    try:
        input("No module named 'pip' found. press any key to install..[using sudo for installing it. 'sudo apt update; sudo apt install python3-pip']")
        os.system('sudo apt update; sudo apt install python3-pip')
        print('Run again;')
        exit()
    except:
        print('You got error try installing manual [module "pip"]')
        print('Run again;')
        exit()

try:
    from termcolor import colored 
except ImportError:
    try:
        input("No module named 'termcolor' found. press any key to install..")
        install('termcolor')
        print('Run again;')
        exit()
    except:
        print('You got error try installing manual [module "termcolor"]')
        print('Run again;')
        exit()
# defines ;

def create_bash_script(x):
    with open('script.sh','w') as file_sh:
        if x == 1:
            file_sh.write('go run main.go "$1" > "$2"')
        if x == 0:
            try:
                os.mkdir('domains')
                with open('script.sh','w') as file_sh:
                    file_sh.write('go run main.go "$1" > domains/"$2"')
            except FileExistsError:
                with open('script.sh','w') as file_sh:
                    file_sh.write('go run main.go "$1" > domains/"$2"')

def count_all_lines():
    lines = 0
    with open('domains.txt','r') as file_domain:
        for i in file_domain:
            lines += 1
    return lines

def count_lines_for_way(_Counter):
    lines = 0
    with open(str(_Counter)+'.way','r') as file_way:
        for i in file_way:
            lines += 1
    return lines


def _run_script(x,lines):
    _Counter = 0
    _lines = 0
    if x == 1:
        with open('domains.txt','r') as file_domain:
            print('number of Lines: ', lines)
            file_domain.seek(0)
            for rd in file_domain: 
                line_strip = rd.strip()
                print("Process on: "+line_strip)
                _Command = 'bash script.sh '+ line_strip +' '+str(_Counter+1)+'.way'
                os.system(_Command)
                _Command = "wc "+str(_Counter+1)+".way | cut -d ' ' -f 2"
                lines = count_lines_for_way(_Counter+1)
                print (colored('Line ('+ str(_Counter) +') Completed; ','green')+colored(line_strip,'red')+' '+str(lines)+' lines discovered. ')
                _Counter += 1        
    if x == 0:
        with open('domains.txt','r') as file_domain:
            print('number of Lines: ', lines)
            file_domain.seek(0)
            for rd in file_domain: 
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

def banner():
    return '''
            

 █     █░▓█████  ▄▄▄▄      ▄▄▄█████▓▓█████ ▄▄▄       ███▄ ▄███▓
▓█░ █ ░█░▓█   ▀ ▓█████▄    ▓  ██▒ ▓▒▓█   ▀▒████▄    ▓██▒▀█▀ ██▒
▒█░ █ ░█ ▒███   ▒██▒ ▄██   ▒ ▓██░ ▒░▒███  ▒██  ▀█▄  ▓██    ▓██░
░█░ █ ░█ ▒▓█  ▄ ▒██░█▀     ░ ▓██▓ ░ ▒▓█  ▄░██▄▄▄▄██ ▒██    ▒██ 
░░██▒██▓ ░▒████▒░▓█  ▀█▓     ▒██▒ ░ ░▒████▒▓█   ▓██▒▒██▒   ░██▒
░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒     ▒ ░░   ░░ ▒░ ░▒▒   ▓▒█░░ ▒░   ░  ░
  ▒ ░ ░   ░ ░  ░▒░▒   ░        ░     ░ ░  ░ ▒   ▒▒ ░░  ░      ░
  ░   ░     ░    ░    ░      ░         ░    ░   ▒   ░      ░   
    ░       ░  ░ ░                     ░  ░     ░  ░       ░   
                      ░                                                                   '''
        
def delay_print(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)

print(colored(banner(),'red'))
delay_print("https://white_bl4ck.t.me\n")
delay_print('-----------------------------------------------------------\n\n')

try:
    _what = int(input('separately saving = 0 \nmerge all = 1\nWhat to do? '))
    if _what == 1 :
        create_bash_script(_what)
        lines = count_all_lines()
        _run_script(_what,lines)
        _end(_what)
    elif _what == 0:
        create_bash_script(_what)
        lines = count_all_lines()
        _run_script(_what,lines)
        _end(_what)
    else:
        print('Wrong value; try again. :)')
except ValueError:
    print('Wrong value; try again. :)')
except ImportError:
    input('It seems you have Termcolor library.\n press any key to install or ctrl+c for stop')
    os.system('pip3 install termcolor')
