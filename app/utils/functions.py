from modules.show import show

from utils.exceptions import *

from datetime import date

import pyperclip
import secrets
import string
import json
import csv
import re


special_chars = "@_!#$%&*()<>|}{:[]\."


def random_password(length: int):
    """ Generate random password """
    alphabet = string.ascii_letters + string.digits + special_chars
    return ''.join(secrets.choice(alphabet) for i in range(length))


def password(text1: str = "Password: ", text2: str = "Repeat password: "):
    """ Get new password """
    password1 = show.password(text1)
    password2 = show.password(text2)

    if password1 == password2:
        return password1
    
    raise PasswordNotEqualsError


def export_to_json(filename: str, data: dict):
    """ Export data to JSON """
    with open(filename, "w") as file:
        file.write(json.dumps(data, indent=4))


def export_to_csv(filename: str, data: dict):
    """ Export data to CSV """
    fields = ["name", "password", "description", "date"]

    with open(filename, "w") as file:
        writer = csv.DictWriter(file, fieldnames=fields, delimiter=",", quotechar="\"")
        writer.writeheader()

        for passwd in data:
            writer.writerow({
                "name": passwd, 
                "password": data[passwd]["password"], 
                "date": data[passwd]["date"], 
                "description": data[passwd]["description"]
            })


def copy(text: str):
    """ Copy text to clipboard """
    pyperclip.copy(text)


def now():
    """ Today in text """
    return date.today().strftime("%Y-%m-%d")


def has_special_symbols(text: str):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:\[\]\.;№\-\–\=\+]')
    return regex.search(text) is not None


def get_unique(text: str):
    """ Count of unique symbols in text """
    uniques = {}

    for symbol in text:
        uniques[symbol] = True
    
    return len(uniques.keys())


def get_password_strength(text: str):
    """ Check password strength 0, 1, 2 – bad, medium, good """
    uniques = get_unique(text)
    has_upper = text.lower() != text
    has_lower = text.upper() != text
    has_special = has_special_symbols(text)

    if not text.isdigit() and len(text) >= 50 and uniques >= 5:
        return 2

    if text.isdigit() or len(text) < 10 or uniques <= 3 or not has_upper or not has_lower:
        return 0
    
    if len(text) < 16 or not has_special:
        return 1
    
    if has_special and has_upper and has_lower and len(text) >= 16:
        return 2
    
    return 1
