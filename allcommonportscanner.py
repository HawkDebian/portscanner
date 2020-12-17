import socket
import sys
import os




sys.ps1 = '\033[01;32m '
os.system('cls || clear')
print(sys.ps1)
print('''

 ####### ######   #####   #####  
    #    #     # #     # #     # 
    #    #     #       #       # 
    #    ######   #####   #####  
    #    #   #         #       # 
    #    #    #  #     # #     # 
    #    #     #  #####   #####  
                                 

''')



target = input("Enter The IP: ")

print('scanning ports, please wait...')

port1 = 80


def scan(port1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    if s.connect_ex((target, port1)):
        print(port1, "port is closed")
        s.close()
    else:
        print(port1, " port is open")
        s.close()
    

scan(port1)

port2 = 443


def scan(port2):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    if s.connect_ex((target, port2)):
        print(port2, "port is closed")
        s.close()
    else:
        print(port2, " port is open")
        s.close()
    

scan(port2)


port3 = 22


def scan(port3):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    if s.connect_ex((target, port3)):
        print(port3, "port is closed")
        s.close()
    else:
        print(port3, " port is open")
        s.close()
    

scan(port3)



port4 = 21


def scan(port4):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    if s.connect_ex((target, port4)):
        print(port4, "port is closed")
        s.close()
    else:
        print(port4, " port is open")
        s.close()
    

scan(port4)



port5 = 25


def scan(port5):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    if s.connect_ex((target, port5)):
        print(port5, "port is closed")
        s.close()
    else:
        print(port5, " port is open")
        s.close()
    

scan(port5)



port6 = 23


def scan(port6):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    if s.connect_ex((target, port6)):
        print(port6, "port is closed")
        s.close()
    else:
        print(port6, " port is open")
        s.close()
    

scan(port6)


port7 = 20


def scan(port7):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    if s.connect_ex((target, port7)):
        print(port7, "port is closed")
        s.close()
    else:
        print(port7, " port is open")
        s.close()
    

scan(port7)

port8 = 3389


def scan(port8):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    if s.connect_ex((target, port8)):
        print(port8, "port is closed")
        s.close()
    else:
        print(port8, " port is open")
        s.close()
    

scan(port8)



port9 = 21


def scan(port9):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    if s.connect_ex((target, port9)):
        print(port9, "port is closed")
        s.close()
    else:
        print(port9, " port is open")
        s.close()
    

scan(port9)


port10 = 143


def scan(port10):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    if s.connect_ex((target, port10)):
        print(port10, "port is closed")
        s.close()
    else:
        print(port10, " port is open")
        s.close()
    

scan(port10)


port11 = 53


def scan(port11):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    if s.connect_ex((target, port11)):
        print(port11, "port is closed")
        s.close()
    else:
        print(port11, " port is open")
        s.close()
    

scan(port11)


port12 = 67


def scan(port12):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    if s.connect_ex((target, port12)):
        print(port12, "port is closed")
        s.close()
    else:
        print(port12, " port is open")
        s.close()
    

scan(port12)


port13 = 68


def scan(port13):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    if s.connect_ex((target, port13)):
        print(port13, "port is closed")
        s.close()
    else:
        print(port13, " port is open")
        s.close()
    

scan(port13)

port14 = 110


def scan(port14):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    if s.connect_ex((target, port14)):
        print(port14, "port is closed")
        s.close()
    else:
        print(port14, " port is open")
        s.close()
    

scan(port14)


port15 = 8080


def scan(port15):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    if s.connect_ex((target, port15)):
        print(port15, "port is closed")
        s.close()
    else:
        print(port15, " port is open")
        s.close()
        
scan(port15)


port16 = 111


def scan(port16):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    if s.connect_ex((target, port16)):
        print(port16, "port is closed")
        s.close()
    else:
        print(port16, " port is open")
        s.close()
        
scan(port16)

port17 = 6999


def scan(port17):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    if s.connect_ex((target, port17)):
        print(port17, "port is closed")
        s.close()
    else:
        print(port17, " port is open")
        s.close()
        
scan(port17)


port18 = 3076


def scan(port18):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    if s.connect_ex((target, port18)):
        print(port18, "port is closed")
        s.close()
    else:
        print(port18, " port is open")
        s.close()
        
scan(port18)

port19 = 8810


def scan(port19):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    if s.connect_ex((target, port19)):
        print(port19, "port is closed")
        s.close()
    else:
        print(port19, " port is open")
        s.close()
        
scan(port19)

port20 = 8925


def scan(port20):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    if s.connect_ex((target, port20)):
        print(port20, "port is closed")
        s.close()
    else:
        print(port20, " port is open")
        s.close()
        
scan(port20)
