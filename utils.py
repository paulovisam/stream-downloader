import os
from pyrogram import Client
from colorama import Fore
import pyfiglet
import random

session_name = "user_session"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

async def authenticate():
    async def get_credentials():
        api_id = input("Digite seu API ID: ")
        api_hash = input("Digite seu API Hash: ")
        return api_id, api_hash

    if not os.path.exists(f"{session_name}.session"):
        api_id, api_hash = await get_credentials()
        async with Client(session_name, api_id=api_id, api_hash=api_hash) as app:
            print("Você está autenticado!")
    else:
        print("Usando sessão existente.")


class Banner:
    def __init__(self, banner):
        self.banner = banner
        self.lg = Fore.LIGHTGREEN_EX
        self.w = Fore.WHITE
        self.cy = Fore.CYAN
        self.ye = Fore.YELLOW
        self.r = Fore.RED
        self.n = Fore.RESET

    def print_banner(self):
        colors = [self.lg, self.r, self.w, self.cy, self.ye]
        f = pyfiglet.Figlet(font='slant')
        banner = f.renderText(self.banner)
        print(f'{random.choice(colors)}{banner}{self.n}')
        print(f'{self.r}  Version: v1.0 \n  Author: https://github.com/viniped \n{self.n}')

def show_banner():
    banner = Banner('Stream-Down')
    banner.print_banner()
