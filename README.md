# Spide Keeper
Security password keeper with CLI interface. 

#### Features
- **Mobility**. The data is stored in one file.
- **Security**. The application uses AES256 encryption.
- **Easy-to-use**. Minimal dependencies and easy to use.
- **Strength Highlights.** Bad, medium and good passwords.

#### Installation o system (not necessary)
- `chmod +x install.sh && ./install.sh`

#### Command usage
- `skeeper --help` – help page.
- `skeeper init` – create new store file (`default.skeep`) in current directory.
- `skeeper init <path>` – create new store file with the specified path.
- `skeeper open` – open `default.skeep` from current directory.
- `skeeper open <path>` – open the specified store file.

#### Interface usage
- `ls` – name, date, description of all your passwords.
- `add <name>` – create new password.
- `addrand <name> <length>` – create new random password.
- `remove <name>` – delete the specified password.
- `copy <name>` – copy to clipboard the specified password.
- `rand <length>` – generate to clipboard new random password.
- `export <format>` – export passwords to file with the specified format (csv or json).
- `change` – change password for encrypted file.
- `quit` – save and close program.
- `clear` – clear terminal.

### Warning!
The program **DOES NOT** save passwords in real time; to do this you need to close the application. (`exit` or `Ctrl + C`)

In addition, it does not accept data with line breaks.

I will also ask you to make backups.

Tested on Python 3.11.
