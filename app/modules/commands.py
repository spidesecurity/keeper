from modules.show import show
from modules.interface import interface

from utils.exceptions import *
from utils.functions import *

from tabulate import tabulate
from colorama import Fore

import os


@interface.command("ls", description="List of your passwords.")
def list_password(data, args):
    table = []
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN]

    for passwd in data:
        table.append([f"{colors[get_password_strength(data[passwd]['password'])]}{passwd}", data[passwd]["date"], data[passwd]["description"] + Fore.RESET])
    
    show.default(tabulate(table, headers=["Name", "Date", "Description"]))


@interface.command("add", use=["name"], description="Create new password.")
def add_password(data, args):
    if args["name"] in data.keys():
        raise CommandError("name exists")

    data[args["name"]] = {
        "description": input("Description: "),
        "date": now(),
        "password": show.password()
    }

    show.success_answer("password added!")


@interface.command("addrand", use=["name", "length"], description="Create new random password.")
def addrand_password(data, args):
    if args["name"] in data.keys():
        raise CommandError("name exists")
    
    password = random_password(int(args["length"]))
    data[args["name"]] = {
        "description": input("Description: "),
        "date": now(),
        "password": password
    }

    copy(password)
    show.success_answer("password added and copied!")


@interface.command("copy", use=["name"], description="Copy password to clipboard.")
def copy_password(data, args):
    if args["name"] not in data.keys():
        raise CommandError("password not found")
        
    copy(data[args["name"]]["password"])
    show.success_answer("password copied!")


@interface.command("remove", use=["name"], description="Remove password from store.")
def remove_password(data, args):
    if args["name"] not in data.keys():
        raise CommandError("password not found")
    
    answer = show.exactly()

    if answer:
        del data[args["name"]]
        show.success_answer("password successfully removed!")


@interface.command("rand", use=["length"], description="Generate password to clipboard.")
def generate_password(data, args):
    if not args["length"].isdigit():
        raise CommandError("length is number")

    copy(random_password(int(args["length"])))
    show.success_answer("new password copied!")


@interface.command("export", use=["format"], description="Export passwords (csv, json).")
def export(data, args):
    if args["format"].lower() == "csv":
        export_to_csv("export-skeeper.csv", data)
        show.success_answer(f"{len(data.keys())} passwords saved in export-skeeper.csv")

    elif args["format"].lower() == "json":
        export_to_json("export-skeeper.json", data)
        show.success_answer(f"{len(data.keys())} passwords saved in export-skeeper.json")
    
    else:
        raise CommandError("undefined format, use csv or json")


@interface.command("change", description="Change password for encrypted file.")
def change_password(data, args):
    try:
        new_password = password("Enter new password: ", "Repeat new password: ")
        raise ChangePasswordException(new_password)

    except PasswordNotEqualsError:
        raise CommandError("password not equals")


@interface.command("clear", description="Clear terminal.")
def clear(data, args):
    os.system("clear")


@interface.command("exit", description="Save and close keeper.")
def quit(data, args):
    raise KeyboardInterrupt
