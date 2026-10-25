#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

echo -e "${CYAN}[*] Starting Web Eater Installation...${NC}"

# Check if Python is installed
if command -v python3 &>/dev/null; then
    echo -e "${GREEN}[+] Python3 is already installed.${NC}"
else
    echo -e "${CYAN}[*] Python3 not found. Installing...${NC}"
    # Check if running in Termux or Debian based system
    if [ -d "/data/data/com.termux" ]; then
        pkg install python -y
    else
        sudo apt update && sudo apt install python3 python3-pip -y
    fi
fi

# Install requirements
echo -e "${CYAN}[*] Installing required Python packages...${NC}"
pip install -r requirements.txt

# Make the main script executable
chmod +x webeater.py

echo -e "${GREEN}[+] Installation Complete!${NC}"
echo -e "${GREEN}[+] Run the tool using: python3 webeater.py -h${NC}"