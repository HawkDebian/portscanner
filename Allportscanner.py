import socket
import sys
import os

os.system('clear')



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
choose = input("do you want to scan UDP ports or TCP?: ")


    

print("scanning please wait. it gonna take a while\n")
def TCP():
    for i in range(100000000):
        port = i
        def scan(port):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if s.connect_ex((target, port)):
                pass
            else:
                print(port, " port is open")
        scan(port)

def UDP():
    for j in range(100000000):
        port1 = j
        def scan(port1):
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            if s.connect_ex((target, port1)):
                pass
                
            else:
                print(port1, " port is open")
        scan(port1)
        
l = choose.upper()

if "TCP" in l:
    TCP()
elif "UDP" in l:
    UDP()

else:
    print("dude select a valid option!")
    sys.exit()
