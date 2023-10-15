#!/bin/bash

# Check root
if [[ $EUID -ne 0 ]]; then
	echo "This script must be run as root"
    exit 1
fi

# Uninstallation
sudo rm -rf /usr/local/lib/skeeper
sudo rm /usr/local/bin/skeeper

# Installation
pip3 install -r requirements.txt
sudo mkdir /usr/local/lib/skeeper
sudo cp -r app/* /usr/local/lib/skeeper/

sudo touch /usr/local/bin/skeeper
sudo echo "#!/bin/bash" >> /usr/local/bin/skeeper
sudo echo 'python3 /usr/local/lib/skeeper/app.py "$@"' >> /usr/local/bin/skeeper

sudo chmod +x /usr/local/bin/skeeper
