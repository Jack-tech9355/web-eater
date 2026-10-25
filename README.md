```markdown
<h1 align="center">🕸️ Web Eater v2.1.0</h1>

<p align="center">
  <b>An advanced, blazing-fast Directory Fuzzer built in Python.</b><br>
  Created with ❤️ by <a href="https://github.com/Jack-tech9355">Jack-tech9355</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Version-2.1.0-blue?style=for-the-badge&logo=appveyor" alt="Version">
  <img src="https://img.shields.io/badge/Python-3.x-yellow?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Platform-Termux%20%7C%20Kali%20Linux-green?style=for-the-badge&logo=linux" alt="Platform">
  <img src="https://img.shields.io/badge/License-MIT-red?style=for-the-badge" alt="License">
</p>

---

## 📖 About The Tool
**Web Eater** is a powerful, multi-threaded directory and file fuzzer designed for penetration testers, bug bounty hunters, and ethical hackers. It is built to discover hidden directories, files, and endpoints on web servers efficiently. With its real-time progress bar, WAF bypassing techniques, and smart filtering, Web Eater makes web enumeration faster and more reliable.

## 🚀 Features
- ⚡ **Blazing Fast:** Multi-threading support for lightning-fast scans.
- 📊 **Live Progress Bar:** A sleek, colorful real-time progress bar to track your scans visually.
- 🎯 **Status Code Filtering:** Filter results by specific HTTP status codes (e.g., `200, 301, 403`).
- 🔄 **Recursive Scanning:** Automatically scans inside newly discovered directories.
- 🛡️ **WAF Bypass:** Rotates User-Agents randomly to avoid getting blocked by Web Application Firewalls.
- ⏱️ **Rate Limiting:** Add delays between requests (`-d 0.5`) to prevent server overload.
- 💾 **Output Saving:** Save your findings directly to a text file for later reporting.
- 🕵️ **Fake Page Filter:** Exclude specific response sizes to ignore custom 404/error pages.

---

## 📦 Installation

### Prerequisites
- Python 3.x
- Termux (Android) or Kali Linux / Debian-based OS

### For Termux / Kali Linux
```bash
# 1. Clone the repository
git clone https://github.com/Jack-tech9355/web-eater.git

# 2. Navigate into the directory
cd web-eater

# 3. Make the installer executable
chmod +x install.sh

# 4. Run the automatic installer
./install.sh
```

---

💻 Usage

```bash
python3 webeater.py -u <URL> -w <WORDLIST> [OPTIONS]
```

⚙️ Options:

Flag Description
-u, --url Target URL (e.g., https://example.com)
-w, --wordlist Path to wordlist file (e.g., common.txt)
-e, --extensions File extensions to check (e.g., php,html,js)
-t, --threads Number of threads for speed (default: 10)
-sc, --status Filter by status codes (e.g., "200,403")
-d, --delay Delay between requests in seconds (e.g., 0.5)
-o, --output Save output to a file (e.g., result.txt)
-rec, --recursive Enable recursive directory scanning
-m, --method HTTP Method (GET/POST)
--exclude Exclude response size (to filter fake pages)

🎯 Example Scans:

1. Basic Scan:

```bash
python3 webeater.py -u https://target.com -w common.txt -e php,html -t 20
```

2. Advanced Scan (Filter 200 OK, Save to file, Bypass WAF):

```bash
python3 webeater.py -u https://target.com -w common.txt -sc "200" -d 0.5 -o results.txt -rec
```

3. Filtering Fake Pages (Excluding size 9121):

```bash
python3 webeater.py -u https://target.com -w common.txt --exclude 9121
```

---

⚠️ Disclaimer

This tool is created for educational purposes and authorized penetration testing only. 
Do not use this tool on any website without prior mutual consent. The author (Jack-tech9355) is not responsible for any misuse or damage caused by this program. Hacking without permission is illegal.

---

<p align="center">
  <i>If you like this tool, don't forget to ⭐ star the repository!</i>
</p>
```
