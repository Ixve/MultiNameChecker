import os, time, requests
from threading import Thread
from colorama import init, Fore
init()

os.system("title MultiChecker")
cwd = os.path.dirname(os.path.realpath(__file__))
names = open(f"{cwd}\\usernames.txt", 'r').read().splitlines()

def logo():
    os.system('cls;clear')
    print("""
 /$$      /$$           /$$   /$$     /$$                             
| $$$    /$$$          | $$  | $$    |__/                             
| $$$$  /$$$$ /$$   /$$| $$ /$$$$$$   /$$                             
| $$ $$/$$ $$| $$  | $$| $$|_  $$_/  | $$                             
| $$  $$$| $$| $$  | $$| $$  | $$    | $$                             
| $$\  $ | $$| $$  | $$| $$  | $$ /$$| $$                             
| $$ \/  | $$|  $$$$$$/| $$  |  $$$$/| $$                             
|__/     |__/ \______/ |__/   \___/  |__/                             
                                                                      
                                                                      
                                                                      
  /$$$$$$  /$$                           /$$                          
 /$$__  $$| $$                          | $$                          
| $$  \__/| $$$$$$$   /$$$$$$   /$$$$$$$| $$   /$$  /$$$$$$   /$$$$$$ 
| $$      | $$__  $$ /$$__  $$ /$$_____/| $$  /$$/ /$$__  $$ /$$__  $$
| $$      | $$  \ $$| $$$$$$$$| $$      | $$$$$$/ | $$$$$$$$| $$  \__/
| $$    $$| $$  | $$| $$_____/| $$      | $$_  $$ | $$_____/| $$      
|  $$$$$$/| $$  | $$|  $$$$$$$|  $$$$$$$| $$ \  $$|  $$$$$$$| $$      
 \______/ |__/  |__/ \_______/ \_______/|__/  \__/ \_______/|__/      
                                                                      
 Created with ♥ by synth#7222 || https://github.com/edgyandcoolname
   """.replace('█', Fore.WHITE + '█' + Fore.LIGHTMAGENTA_EX))
logo()

print(" KIK CHECKER WILL ONLY CHECK ON WS2.KIK.COM")

def kik(name):
    r1 = requests.get(f"https://ws2.kik.com/user/{name}", headers={'User-Agent': 'Mozilla/5.0'})
    if r1.status_code == 404:
        print(f"{Fore.MAGENTA} [ KIK WS2", r1.status_code, f"] {Fore.GREEN}[{Fore.LIGHTGREEN_EX}AVAILABLE{Fore.GREEN}]{Fore.WHITE} {name}")
        with open('available_kik.txt', 'a') as (f):
            f.write(name + '\n')
    else:
        print(f"{Fore.MAGENTA} [ KIK WS2", r1.status_code, f"] {Fore.RED}[{Fore.LIGHTRED_EX}UNAVAILABLE{Fore.RED}]{Fore.WHITE} {name}")


def instagram(name):
    r2 = requests.get(f"https://instagram.com/{name}", headers={'User-Agent': 'Mozilla/5.0'})
    if r2.status_code == 404:
        print(f"{Fore.MAGENTA} [ INSTAGRAM", r2.status_code, f"] {Fore.GREEN}[{Fore.LIGHTGREEN_EX}AVAILABLE{Fore.GREEN}]{Fore.WHITE} {name}")
        with open('available_instagram.txt', 'a') as (f):
            f.write(name + '\n')
    else:
        print(f"{Fore.MAGENTA} [ INSTAGRAM", r2.status_code, f"] {Fore.RED}[{Fore.LIGHTRED_EX}UNAVAILABLE{Fore.RED}]{Fore.WHITE} {name}")


def solo(name):
    r3 = requests.get(f"https://solo.to/{name}", headers={'User-Agent': 'Mozilla/5.0'})
    if r3.status_code == 404:
        print(f"{Fore.MAGENTA} [ SOLO.TO", r3.status_code, f"] {Fore.GREEN}[{Fore.LIGHTGREEN_EX}AVAILABLE{Fore.GREEN}]{Fore.WHITE} {name}")
        with open('available_solo.txt', 'a') as (f):
            f.write(name + '\n')
    else:
        print(f"{Fore.MAGENTA} [ SOLO.TO", r3.status_code, f"] {Fore.RED}[{Fore.LIGHTRED_EX}UNAVAILABLE{Fore.RED}]{Fore.WHITE} {name}")

def pastebin(name):
    r4 = requests.get(f"https://pastebin.com/u/{name}", headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0'})
    if r4.status_code == 404:
        print(f"{Fore.MAGENTA} [ PASTEBIN", r4.status_code, f"] {Fore.GREEN}[{Fore.LIGHTGREEN_EX}AVAILABLE{Fore.GREEN}]{Fore.WHITE} {name}")
        with open('available_pastebin.txt', 'a') as (f):
            f.write(name + '\n')
    else:
        print(f"{Fore.MAGENTA} [ PASTEBIN", r4.status_code, f"] {Fore.RED}[{Fore.LIGHTRED_EX}UNAVAILABLE{Fore.RED}]{Fore.WHITE} {name}")

def github(name):
    r5 = requests.get(f"https://github.com/{name}", headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0'})
    if r5.status_code == 404:
        print(f"{Fore.MAGENTA} [ GITHUB", r5.status_code, f"] {Fore.GREEN}[{Fore.LIGHTGREEN_EX}AVAILABLE{Fore.GREEN}]{Fore.WHITE} {name}")
        with open('available_github.txt', 'a') as (f):
            f.write(name + '\n')
    else:
        print(f"{Fore.MAGENTA} [ GITHUB", r5.status_code, f"] {Fore.RED}[{Fore.LIGHTRED_EX}UNAVAILABLE{Fore.RED}]{Fore.WHITE} {name}")


threads = []
for name in names:
    threads.append(Thread(target=kik, args=[name]))
    threads.append(Thread(target=instagram, args=[name]))
    threads.append(Thread(target=solo, args=[name]))
    threads.append(Thread(target=pastebin, args=[name]))
    threads.append(Thread(target=github, args=[name]))

for t in threads:
    t.start()
    time.sleep(0.25)
    t.join()
