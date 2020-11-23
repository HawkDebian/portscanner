import socket
import sys


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)
sys.ps1 = '\033[01;32m '
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

port1 = 80


def scan(port1):
    if s.connect_ex((target, port1)):
        print(port1, "port is closed")
    else:
        print(port1, " port is open")
    

scan(port1)

port2 = 443


def scan(port2):
    if s.connect_ex((target, port2)):
        print(port2, "port is closed")
    else:
        print(port2, " port is open")
    

scan(port2)


port3 = 22


def scan(port3):
    if s.connect_ex((target, port3)):
        print(port3, "port is closed")
    else:
        print(port3, " port is open")
    

scan(port3)



port4 = 21


def scan(port4):
    if s.connect_ex((target, port4)):
        print(port4, "port is closed")
    else:
        print(port4, " port is open")
    

scan(port4)



port5 = 25


def scan(port5):
    if s.connect_ex((target, port5)):
        print(port5, "port is closed")
    else:
        print(port5, " port is open")
    

scan(port5)



port6 = 23


def scan(port6):
    if s.connect_ex((target, port6)):
        print(port6, "port is closed")
    else:
        print(port6, " port is open")
    

scan(port6)


port7 = 20


def scan(port7):
    if s.connect_ex((target, port7)):
        print(port7, "port is closed")
    else:
        print(port7, " port is open")
    

scan(port7)

port8 = 3389


def scan(port8):
    if s.connect_ex((target, port8)):
        print(port8, "port is closed")
    else:
        print(port8, " port is open")
    

scan(port8)



port9 = 21


def scan(port9):
    if s.connect_ex((target, port9)):
        print(port9, "port is closed")
    else:
        print(port9, " port is open")
    

scan(port9)


port10 = 143


def scan(port10):
    if s.connect_ex((target, port10)):
        print(port10, "port is closed")
    else:
        print(port10, " port is open")
    

scan(port10)


port11 = 53


def scan(port11):
    if s.connect_ex((target, port11)):
        print(port11, "port is closed")
    else:
        print(port11, " port is open")
    

scan(port11)


port12 = 67


def scan(port12):
    if s.connect_ex((target, port12)):
        print(port12, "port is closed")
    else:
        print(port12, " port is open")
    

scan(port12)


port13 = 68


def scan(port13):
    if s.connect_ex((target, port13)):
        print(port13, "port is closed")
    else:
        print(port13, " port is open")
    

scan(port13)

port14 = 110


def scan(port14):
    if s.connect_ex((target, port14)):
        print(port14, "port is closed")
    else:
        print(port14, " port is open")
    

scan(port14)
