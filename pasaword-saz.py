from optparse import OptionValueError
import random
import time
import pyfiglet
from time import sleep
from colorama import Fore,Back,Style
import sys
import os
print("\033[34m")
print(f"""


⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⠿⠿⠿⠿⠿⠿⠿⠿⢷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠁⠀⠀⠀⠀⠀⣀⣠⣤⣶⣶⣶⣶⣶⣶⣤⣄⣀⠀⠀⠀⠀⠀⠀⢿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣏⠀⠀⣤⣴⣾⣿⠿⠛⠉⠁⠀⠀⠀⠀⠀⠉⠛⠻⢿⣷⣶⣤⡄⠀⢸⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣆⠀⠉⠉⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠈⠉⠁⢠⣾⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣼⣿⣧⡀⠀⢻⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⣰⣿⣿⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣰⣾⠟⠛⠋⠉⠈⢻⣷⡄⠘⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⠏⢀⣼⡿⠁⠉⠉⠛⠻⢿⣦⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣰⣿⠃⠀⣀⣀⣀⣀⣀⣹⣿⣆⣈⣿⣷⣦⣄⣀⣀⣀⣀⣠⣤⣾⣿⣋⣠⣾⣟⣀⣀⣀⣀⣀⡀⠈⢿⣧⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⣿⠃⢰⣿⠟⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⣿⡇⠈⢿⣆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⣿⠏⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠘⣿⣆⠀⠀⠀⠀
⠀⠀⠀⢠⣿⡟⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣶⠿⠿⣷⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠸⣿⣆⠀⠀⠀
⠀⠀⢀⣾⡟⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⡟⠉⠀⠀⠀⠀⠈⠻⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠹⣿⡄⠀⠀
⠀⢀⣾⡟⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡏⠀⣴⣄⠀⠀⣠⣤⡄⠸⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠹⣿⡄⠀
⠀⣼⡟⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣇⠀⠈⠻⠇⠐⠿⠋⠀⢠⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠹⣷⡀
⢸⣿⠁⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⣷⣦⡄⠀⠀⠀⣤⣶⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⣿⡧
⠈⠻⣷⣦⡀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣷⣤⣤⣴⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⢀⣠⣾⡿⠃
⠀⠀⠈⠙⢿⣷⣄⡀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⣠⣴⡿⠛⠁⠀⠀
⠀⠀⠀⠀⠀⠈⠻⢿⣾⣿⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⢀⣀⣀⣀⣿⣿⣿⠟⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠀⠀⠘⠛⠛⠛⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀


\033[33m]
	github.com/mr-abron
	
""")
print("\033[31m")
print(pyfiglet.figlet_format("Password list",font='epic'))
x = input("\033[32mWhat letters should we use? »\033[33m")
v = input("\033[32mWhat number should we use? »\033[33m")
z = int(input ("\033[32mThe number of characters in the password »\033[33m"))
b = int(input("\033[32mNumber of passwords »\033[33m"))
a =(f"{x}{v}")
with open('passworld.txt','a') as f:
    for i in range(b):
        print("\033[32m")
        f.write(''.join(random.sample(a,z))+'\n')
        print(''.join(random.sample(a,z))+'\n')
        time.sleep(0.01)

mi =[f"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣴⣶⣶⣶⣶⣦⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⠏⠁⠀⢶⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀
⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⡿⠿⣿⠀⠀⠀⠀⣿⠿⢿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀
⠀⢠⣾⣿⣿⣿⣿⣿⡿⠋⣠⣴⣿⣷⣤⣤⣾⣿⣦⣄⠙⢿⣿⣿⣿⣿⣿⣷⡄⠀
⠀⣼⣿⣿⣿⣿⣿⡏⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⢹⣿⣿⣿⣿⣿⣧⠀
⢰⣿⣿⣿⣿⣿⡿⠀⣾⣿⣿⣿⣿⠟⠉⠉⠻⣿⣿⣿⣿⣷⠀⢿⣿⣿⣿⣿⣿⡆
⢸⣿⣿⣿⣿⣿⣇⣰⣿⣿⣿⣿⡇⠀⠀⠀⠀⢸⣿⣿⣿⣿⣆⣸⣿⣿⣿⣿⣿⡇
⠸⣿⣿⣿⡿⣿⠟⠋⠙⠻⣿⣿⣿⣦⣀⣀⣴⣿⣿⣿⣿⠛⠙⠻⣿⣿⣿⣿⣿⠇
⠀⢻⣿⣿⣧⠉⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠈⣿⣿⣿⡟⠀
⠀⠘⢿⣿⣿⣷⣦⣤⣴⣾⠛⠻⢿⣿⣿⣿⣿⡿⠟⠋⣿⣦⣤⠀⣰⣿⣿⡿⠃⠀
⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣄⣈⣁⣠⣤⣶⣾⣿⣿⣷⣾⣿⣿⡿⠁⠀⠀
⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠻⠿⠿⠿⠿⠟⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
""","""

⠀⠀⡇⠀⠀⠀⠀⢀⣴⣿⡿⠿⢿⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣇
⠀⠉⡏⠁⠀⠀⣴⣿⡿⠋⢙⡆⢀⣧⠀⠉⠛⢿⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠘⠀
⠀⠀⠀⠀⠀⣼⣿⢛⣁⡴⣋⣴⣿⣿⣷⣄⣀⠀⠈⣻⣿⣿⣿⣶⣶⣶⣶⣤⡀⠀
⠀⠀⠀⠀⢰⣿⣿⠏⣹⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠈⠉⠻⣿⡄
⠀⠀⠀⢠⣾⣿⣟⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⢻⣿
⠀⢀⣴⣿⣿⡿⠋⠉⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⢸⣿
⣠⣿⣿⣿⣿⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⠋⠁⠀⠀⠉⢿⣿⣿⣿⣿⣿⣿⡇
⣿⣿⠉⢹⣿⣦⡀⠀⠀⣀⣾⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠈⣿⣿⣷⣿⣿⠟⠀
⢿⣿⣆⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⢀⣼⣿⣿⣿⠿⠋⠀⠀
⠈⠻⣿⣶⣍⣻⣿⣿⣿⣿⠿⠛⠛⠛⢿⣿⣿⣿⣿⣶⣶⣿⣿⡿⠛⠁⠀⠀⡀⠀
⠀⠀⠈⠙⠻⢿⣿⣿⣿⣧⣤⣤⣤⣤⣤⣼⡿⠿⢿⡿⠛⠋⠁⠀⠀⠀⠀⠀⠈⠏
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⢹⣿⡆⠀⠀⠀⢸⣿⠀⠀⠀⠀⣀⣆⡄⠀⠀⠀
⠀⠀⠀⠀⠀⣰⣀⠀⠀⠀⠀⠀⢸⣿⠀⠀⡠⠄⢸⣿⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⠀⠀⠀⠀⠀⠀⢾⣇⠀⠀⠀⠀⢸⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣦⣤⣴⡿⠃⠀⠀⠀⠀⠀⠁⠀⠀⠀⠄
""","""

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⡀⠒⠒⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣤⣶⡾⠿⠿⠿⠿⣿⣿⣶⣦⣄⠙⠷⣤⡀⠀⠀⠀⠀
⠀⠀⠀⣠⡾⠛⠉⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣿⣷⣄⠘⢿⡄⠀⠀⠀
⠀⢀⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠐⠂⠠⢄⡀⠈⢿⣿⣧⠈⢿⡄⠀⠀
⢀⠏⠀⠀⠀⢀⠄⣀⣴⣾⠿⠛⠛⠛⠷⣦⡙⢦⠀⢻⣿⡆⠘⡇⠀⠀
⠀⠀⠀⠀⡐⢁⣴⡿⠋⢀⠠⣠⠤⠒⠲⡜⣧⢸⠄⢸⣿⡇⠀⡇⠀⠀
⠀⠀⠀⡼⠀⣾⡿⠁⣠⢃⡞⢁⢔⣆⠔⣰⠏⡼⠀⣸⣿⠃⢸⠃⠀⠀
⠀⠀⢰⡇⢸⣿⡇⠀⡇⢸⡇⣇⣀⣠⠔⠫⠊⠀⣰⣿⠏⡠⠃⠀⠀⢀
⠀⠀⢸⡇⠸⣿⣷⠀⢳⡈⢿⣦⣀⣀⣀⣠⣴⣾⠟⠁⠀⠀⠀⠀⢀⡎
⠀⠀⠘⣷⠀⢻⣿⣧⠀⠙⠢⠌⢉⣛⠛⠋⠉⠀⠀⠀⠀⠀⠀⣠⠎⠀
⠀⠀⠀⠹⣧⡀⠻⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡾⠃⠀⠀
⠀⠀⠀⠀⠈⠻⣤⡈⠻⢿⣿⣷⣦⣤⣤⣤⣤⣤⣴⡾⠛⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠙⠶⢤⣈⣉⠛⠛⠛⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""]
print("\r [*]                                         ",end="",flush=False)
print ()
print ()
print (Fore.GREEN +"")
print("\r[~] ălert > 5s",end="",flush=False) 
time.sleep(1)
print("\r[~] ălert >> 4s",end="",flush=False)
time.sleep(1) 
print("\r[~] ălert >>> 3s",end="",flush=False) 
time.sleep(1)
print("\r[~] ălert >>>> 2s",end="",flush=False) 
time.sleep(1)
print("\r[~] ălert >>>>> 1s",end="",flush=False)
time.sleep(0.1)
print ()
def slow_print(Str):
    for char in Str:
        print(char, end='', flush=True)
        sleep(.02)
def clear():
    system('' if name == 'posix' else 'cls')
# -------------------------------------------------

soheil = """\033[31m
  ________________________________________________                
 |>>>-----------------------------------------<<<|
 |>\033[32mDo you want to start the script from scratch?\033[31m<|
 \033[36m|>>>—————————————————————————————————————————<<<|
 |>>>			    	              <<<|
 |>>>             \033[31m[\033[32mY\033[31m] \033[33mYES\033[36m                     <<<|
 |>>>             \033[31m[\033[32mN\033[31m] \033[33mNO\033[36m                      <<<|
 |>>>                                         <<<|
 |>>>—————————————————————————————————————————<<<|
\033[31m |>>>-----------------------------------------<<<|
 |>>>-----------------------------------------<<<|  
 —————————————————————————————————————————————————"""
banner = (random.choice(mi))

#
#
for i in banner:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.007)
print (Fore.BLUE + "")
print()
for i in soheil:
	sleep(0.005)
	print(i,end='',flush=True)
print()

shah = input(Fore.CYAN+"     \033[41m[?]\33[1;0m"+"\33[1; \033[31mSelect\033[32m◈─━─━─━─━\033[34m❯❯❯  \033[93m"+Fore.RED+"")
#
if(str(shah) == "y"):
  os.system("python Mail-Hack.py")
  os.system("clear")
#
if shah == "n":
	print("ok ")



        