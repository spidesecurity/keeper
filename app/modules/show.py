from datetime import datetime, timedelta
from colorama import Fore, Style
from getpass import getpass

import platform
import sys
import os


APP_VERSION = "1.0.0"


class Show:
    def __init__(self, is_time: bool = False):
        self.is_time = is_time
    
    def clear(self):
        os.system("clear")
    
    def now(self):
        return f"({(datetime.now() + timedelta(hours=3)).strftime('%H:%M:%S')}) " if self.is_time else ""

    def success(self, text: str):
        print(f"{Style.BRIGHT}{self.now()}{Fore.GREEN}[success]{Style.RESET_ALL}", text)
    
    def info(self, text: str):
        print(f"{Style.BRIGHT}{self.now()}{Fore.CYAN}[info]{Style.RESET_ALL}", text)
    
    def warn(self, text: str):
        print(f"{Style.BRIGHT}{self.now()}{Fore.YELLOW}[warn]{Style.RESET_ALL}", text)
    
    def error(self, text: str):
        print(f"{Style.BRIGHT}{self.now()}{Fore.RED}[error]{Style.RESET_ALL}", text)
    
    def default(self, text: str):
        print(text)
    
    def success_answer(self, text: str):
        print(f"{Fore.GREEN}>{Style.RESET_ALL} {text}")
    
    def error_answer(self, text: str):
        print(f"{Fore.RED}>{Style.RESET_ALL} {text}")
    
    def enter(self):
        return input(f"{Style.BRIGHT}{Fore.BLUE}spide@keeper {Fore.CYAN}${Style.RESET_ALL} ")

    def password(self, text: str = "Password: "):
        return getpass(text)
    
    def exactly(self, text: str = "Are you sure?"):
        answer = input(f"{text} [y/N]: ")
        return answer.lower() == "y"
    
    def version(self):
        print(f"Spide Keeper {APP_VERSION}, Python {platform.python_version()}")


show = Show()
