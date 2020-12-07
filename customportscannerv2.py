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



target = sys.argv[1]

if (target == None):
                    print('''
                    please give a valid value
                    for example:
            
        python3 alltcpscan2.py example.com
                             ''')
                    
elif (target == False):

                    print('''
                    please give a valid value
                    for example:
            
        python3 alltcpscan2.py example.com
                             ''')
                    

elif (target == ""):

                    print('''
                    please give a valid value
                    for example:
            
        python3 alltcpscan2.py example.com
                             ''')
                    

elif(target == " "):

                    print('''
                    please give a valid host
                    for example:
            
        python3 alltcpscan2.py example.com
                             ''')
                   

else:
     print('scanning ports, please wait...')

port = int(input('Enter the port you want to scan : '))

def scan(port):
    if s.connect_ex((target, port)):
        print(port, "port is closed")
    else:
        print(port, " port is open")
    

scan(port)
