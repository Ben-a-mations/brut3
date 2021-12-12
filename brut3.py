import math
import time
import os
import sys
from tqdm import tqdm
import time

print('Starting Brut3-Framework..')  

for i in tqdm (range (101), 
               desc="Loading…", 
               ascii=False, ncols=75):
    time.sleep(0.07)

time.sleep(1)

def main():

    os.system('clear')

    print('''__________                __ ________  
\______   \_______ __ ___/  |\_____  \ 
 |    |  _/\_  __ \  |  \   __\_(__  < 
 |    |   \ |  | \/  |  /|  | /       >
 |______  / |__|  |____/ |__|/______  /
        \/                          \/ ''')

    print('')
    print('[1] Hashcat   [2] Hydra   [3] Hydra-GUI\n')
    print('     [4] Metasploit   [5] BurpSuite')
    print('-----------------------------------------')
    print('       [I] IP ADDR   [A] Arp-Scan')
    print('-----------------------------------------')


    cmd()

def cmd():
    c = input("~$ ")
    if c == '':
        cmd()
    elif c == 'Q':
        print('Bye!! (;-;)')
        time.sleep(1.2)
        sys.exit()
    elif c == 'q':
        print('Bye!! (;-;)')
        time.sleep(1.2)
        sys.exit()
    elif c == '1':
        hash = input('Hash File:>> ')
        words = input('Wordlist:>> ')
        out = input('Out File:>> ')
        OS = input('OS (Num):>> ')
        print('Executing..')
        time.sleep(1)
        os.system(f'sudo hashcat -a 0 -m {OS} -o {out} {hash} {words}')
        time.sleep(4)
        main()
    elif c == '2':
        user = input("Victim Username:>> ")
        words = input('Wordlist:>> ')
        ftp = input('Connection (ex:ssh):>> ')
        ip = input("IP ADDR:>> ")
        print("Executing..")
        time.sleep(1)
        os.system(f'sudo hydra -l "{user}" -P "{words}" {ip} {ftp}')
        time.sleep(4)
        main()
    elif c == '3':
        os.system('xhydra')
        main()
    elif c == '4':
        os.system('sudo msfconsole')
        main()
    elif c == '5':
        os.system('sudo burpsuite')
        main()
    elif c == 'I':
        os.system("ip addr")
        time.sleep(4)
        main()
    elif c == 'i':
        os.system("ip addr")
        time.sleep(4)
        main()
    elif c == 'A':
        os.system('sudo arp-scan -l')
        time.sleep(4)
        main()
    elif c == 'a':
        os.system('sudo arp-scan -l')
        time.sleep(4)
        main()
    else:
        print('Unkown Command..')
        time.sleep(2)
        main()

main()
if '__name__' == '__main__':
    main()