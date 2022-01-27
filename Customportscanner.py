import socket
import sys



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)
sys.ps1 = '\033[01;32m '
print(sys.ps1)

print('''

████████╗██╗  ██╗███████╗██████╗ ███████╗██████╗ ██╗ █████╗ ███╗   ██╗
╚══██╔══╝██║  ██║██╔════╝██╔══██╗██╔════╝██╔══██╗██║██╔══██╗████╗  ██║
   ██║   ███████║█████╗  ██║  ██║█████╗  ██████╔╝██║███████║██╔██╗ ██║
   ██║   ██╔══██║██╔══╝  ██║  ██║██╔══╝  ██╔══██╗██║██╔══██║██║╚██╗██║
   ██║   ██║  ██║███████╗██████╔╝███████╗██████╔╝██║██║  ██║██║ ╚████║
   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═════╝ ╚══════╝╚═════╝ ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
                                                                      

                                  
                                                                        
''')


target = input("Enter The IP: ")

port = int(input("Enter the port you wanna scan: "))


def scan(port):
    if s.connect_ex((target, port)):
        print(port, "port is closed")
    else:
        print(port, " port is open")
    

scan(port)
             
