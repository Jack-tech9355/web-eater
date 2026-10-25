#!/usr/bin/env python3
import requests
import sys
import argparse
import time
import os
import random
from concurrent.futures import ThreadPoolExecutor, as_completed
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Disable SSL warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# ==========================================
# TOOL CONFIGURATION
# ==========================================
AUTHOR = "Jack-tech9355"
GITHUB_REPO = "https://github.com/Jack-tech9355/web-eater"
VERSION = "2.1.0"

# Clean ASCII ART BANNER
BANNER = """
\033[91m
██╗    ██╗███████╗██████╗     ███████╗ █████╗ ████████╗███████╗██████╗ 
██║    ██║██╔════╝██╔══██╗    ██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
██║ █╗ ██║█████╗  ██████╔╝    █████╗  ███████║   ██║   █████╗  ██████╔╝
██║███╗██║██╔══╝  ██╔══██╗    ██╔══╝  ██╔══██║   ██║   ██╔══╝  ██╔══██╗
╚███╔███╔╝███████╗██████╔╝    ███████╗██║  ██║   ██║   ███████╗██║  ██║
 ╚══╝╚══╝ ╚══════╝╚═════╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
\033[0m
\033[96m    [+] Tool Name : Web Eater (v2.1.0)
    [+] Author    : Jack-tech9355
    [+] GitHub    : https://github.com/Jack-tech9355/web-eater
\033[0m
\033[93m    >> Advanced Features: Status Filter, Recursive, WAF Bypass, Save Output <<
\033[0m
"""

USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1'
]

# Global variables
EXCLUDE_LENGTH = 0
total_words = 0
completed_words = 0
found_count = 0
output_file = None
allowed_status = []
recursive_dirs = []

def print_progress():
    global completed_words, total_words
    if total_words == 0: return
    percent = (completed_words / total_words) * 100
    bar_length = 30
    filled_length = int(bar_length * completed_words // total_words)
    bar = '\033[92m█\033[0m' * filled_length + '\033[91m-\033[0m' * (bar_length - filled_length)
    sys.stdout.write(f'\r\033[96m[Progress]\033[0m |{bar}| {percent:.2f}% ({completed_words}/{total_words}) ')
    sys.stdout.flush()

def save_to_file(text):
    if output_file:
        with open(output_file, "a") as f:
            f.write(text + "\n")

def check_url(base_url, word, extensions, method, delay):
    global EXCLUDE_LENGTH, completed_words, found_count
    
    for ext in extensions:
        path = f"{word}.{ext}" if ext else word
        test_url = f"{base_url.rstrip('/')}/{path}"
        
        # WAF Bypass: Random User-Agent
        headers = {'User-Agent': random.choice(USER_AGENTS)}
        
        try:
            # Rate Limiting
            if delay > 0: time.sleep(delay)

            if method.upper() == 'POST':
                response = requests.post(test_url, headers=headers, timeout=8, allow_redirects=False, verify=False)
            else:
                response = requests.get(test_url, headers=headers, timeout=8, allow_redirects=False, verify=False)
            
            status = response.status_code
            length = len(response.content)

            if length == EXCLUDE_LENGTH:
                pass
            else:
                # Status Code Filter
                if allowed_status and str(status) not in allowed_status:
                    pass
                else:
                    if status in [200, 301, 302, 401, 403]:
                        color = "\033[92m" if status == 200 else "\033[93m" if status in [301,302] else "\033[95m" if status == 401 else "\033[91m"
                        output = f"{color}[+] {status} | Size: {length:<6} | {test_url}\033[0m"
                        print(f"\n{output}")
                        save_to_file(f"{status} | Size: {length} | {test_url}")
                        found_count += 1
                        
                        # Recursive Scan ke liye save karna (sirf 200 OK folders)
                        if status == 200 and (test_url.endswith('/') or not ext):
                            recursive_dirs.append(test_url)
                
        except requests.exceptions.RequestException:
            pass 
        finally:
            if ext == extensions[-1]:
                completed_words += 1
                print_progress()

def main():
    global EXCLUDE_LENGTH, total_words, completed_words, found_count, output_file, allowed_status, recursive_dirs
    
    print(BANNER)
    
    parser = argparse.ArgumentParser(description="Web Eater v2.1 - Advanced Fuzzer")
    parser.add_argument("-u", "--url", required=True, help="Target URL")
    parser.add_argument("-w", "--wordlist", required=True, help="Path to wordlist")
    parser.add_argument("-e", "--extensions", default="", help="Extensions (php,html,js)")
    parser.add_argument("-t", "--threads", type=int, default=10, help="Threads (default 10)")
    parser.add_argument("-sc", "--status", default="", help="Filter status codes (e.g., 200,301,403)")
    parser.add_argument("-d", "--delay", type=float, default=0, help="Delay between requests in seconds")
    parser.add_argument("-o", "--output", default="", help="Save output to file")
    parser.add_argument("-rec", "--recursive", action="store_true", help="Enable recursive directory scan")
    parser.add_argument("-m", "--method", default="GET", help="HTTP Method (GET/POST)")
    parser.add_argument("--exclude", type=int, default=0, help="Exclude response size")
    args = parser.parse_args()

    EXCLUDE_LENGTH = args.exclude
    output_file = args.output
    if output_file:
        open(output_file, "w").close() # Clear file if exists

    if args.status:
        allowed_status = [s.strip() for s in args.status.split(",")]

    ext_list = [ext.strip() for ext in args.extensions.split(",") if ext.strip()]
    if ext_list:
        ext_list.append("")

    print(f"\033[96m[*] Target URL  : {args.url}")
    print(f"[*] Wordlist    : {args.wordlist}")
    print(f"[*] Threads     : {args.threads}")
    print(f"[*] Delay       : {args.delay}s")
    print(f"[*] Status Code : {args.status if args.status else 'All'}")
    print(f"[*] Recursive   : {'Enabled' if args.recursive else 'Disabled'}")
    if output_file: print(f"[*] Saving to   : {output_file}")
    print("-" * 75)

    try:
        with open(args.wordlist, "r", encoding="latin-1") as f:
            words = [line.strip() for line in f if line.strip()]
        
        total_words = len(words)
        print(f"\033[96m[*] Total Words : {total_words}\033[0m\n")
        
        start_time = time.time()
        scan_queue = [(args.url, words)] # List of (base_url, wordlist)

        # Main Scan Loop
        while scan_queue:
            current_url, current_words = scan_queue.pop(0)
            print(f"\n\033[94m[Scanning] -> {current_url}\033[0m")
            
            if args.recursive:
                total_words = len(current_words) # Reset total for progress
                completed_words = 0

            with ThreadPoolExecutor(max_workers=args.threads) as executor:
                for word in current_words:
                    executor.submit(check_url, current_url, word, ext_list, args.method, args.delay)

            # Agar recursive hai, toh jo naye folders mile hain unko queue mein daalo
            if args.recursive and recursive_dirs:
                for d in recursive_dirs:
                    if d not in [q[0] for q in scan_queue]: # Avoid duplicates
                        scan_queue.append((d, words))
                recursive_dirs.clear()

        print("\n")
        print("-" * 75)
        print(f"\033[92m[+] Scan Finished in {round(time.time() - start_time, 2)} seconds!\033[0m")
        print(f"\033[92m[+] Total Paths Found: {found_count}\033[0m")

    except FileNotFoundError:
        print(f"\n\033[91m[-] Error: Wordlist file '{args.wordlist}' not found!\033[0m")
    except KeyboardInterrupt:
        print("\n\033[93m[-] Scan stopped by user (CTRL+C).\033[0m")

if __name__ == "__main__":
    main()