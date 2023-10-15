from modules.show import show
from utils.exceptions import *

from tabulate import tabulate
import sys


def get_args(command: list, obj: dict):
    if obj["args"] and len(obj["args"]) != len(command[1:]):
        use = [f"<{arg}>" for arg in obj["args"]]
        show.default(f"use: {command[0]} {' '.join(use)}")
        return False
    
    args = {}
    for_command = command[1:]
    for i in for_command:
        args[obj["args"][for_command.index(i)]] = i
    
    return args


class Interface:
    def __init__(self):
        self.commands = {}
        self.active = True
        self.encrypt = None
    
    def setup_encryption_file(self, encrypt):
        self.encrypt = encrypt
    
    def run(self, data: dict):
        show.clear()
        show.default("Try `help` to get a list of commands.")

        try:
            while self.active:
                command = show.enter().strip().split(" ")
                cmd = command[0].strip()

                if cmd == "":
                    continue

                if cmd == "help":
                    self.help()
                    continue

                if cmd not in self.commands:
                    show.error_answer(f"{cmd}: command not found")
                    continue

                args = get_args(command, self.commands[cmd])

                if args is not False:
                    self.commands[cmd]["wrapper"](data, args)
        
        except ValueError: ...
        
        return data
    
    def help(self):
        grid = []

        for command in self.commands:
            args = [f"<{arg}>" for arg in self.commands[command]["args"]]
            cmd = f"{command} {' '.join(args)}"

            grid.append([cmd, self.commands[command]["description"]])

        show.default(tabulate(grid, tablefmt="plain"))

    def command(self, name: str, use: list = [], description: str = None):
        def function(handler):
            def wrapper(*args, **kwargs):
                try:
                    return handler(*args, **kwargs)
                
                except ChangePasswordException as e:
                    if self.encrypt:
                        self.encrypt.key = str(e)
                        show.success_answer(f"password for encrypted file successfully changed!")

                    else:
                        show.error_answer(f"error: password not changed")

                except KeyboardInterrupt:
                    self.active = False
                
                except CommandError as e:
                    show.error_answer(f"error: {e}")
                
            self.commands[name] = {
                "wrapper": wrapper,
                "description": description,
                "args": use
            }
            return wrapper

        return function


interface = Interface()
