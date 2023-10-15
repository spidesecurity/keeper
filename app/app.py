#!/usr/bin/python3
from modules.show import show
from modules.interface import interface
from modules.encryption import EncryptionFile

from utils.exceptions import *
from utils.functions import *

import click
import os


@click.group()
def main(): ...


@click.command(name="version")
def version():
    """ Show Spide Keeper and Python version. """
    show.version()


@click.command(name="open")
@click.argument("file", default="default.skeep")
def open_file(file):
    """ Open encrypted file for next work with passwords. """
    encrypt = None

    try:
        if not file or not os.path.isfile(file):
            raise FileNotFoundError
        
        passwd = show.password()
        encrypt = EncryptionFile(file, passwd)

        interface.setup_encryption_file(encrypt)
        interface.run(encrypt.read())

        encrypt.write()
    
    except FileNotFoundError:
        show.error("file not found")
        
    except InvalidPasswordError:
        show.error("invalid password")
    
    except KeyboardInterrupt:
        show.clear()
        show.info("keyboard exited")

        if encrypt:
            encrypt.write()


@click.command(name="init")
@click.argument("file", default="default.skeep")
def init_file(file):
    """ Initialize new password encrypted file. """
    encrypt = None

    try:
        if file and os.path.exists(file):
            raise PathExistsError
        
        encrypt = EncryptionFile(file, password())
        encrypt.write({})

        interface.setup_encryption_file(encrypt.data)
        interface.run(encrypt.data)

        encrypt.write()
    
    except PathExistsError:
        show.error("path exists")
    
    except PasswordNotEqualsError:
        show.error("password mistmatch")
    
    except KeyboardInterrupt:
        show.clear()
        show.info("keyboard exited")

        if encrypt:
            encrypt.write()


main.add_command(open_file)
main.add_command(init_file)
main.add_command(version)


if __name__ == "__main__":
    main()
