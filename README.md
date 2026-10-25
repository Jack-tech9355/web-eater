<h1 align="center">🕸️ Web Eater v2.1.0</h1>

<p align="center">
  <strong>An Advanced, High-Speed Directory Fuzzer Built with Python</strong><br>
  Created with ❤️ by <a href="https://github.com/Jack-tech9355">Jack-tech9355</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Version-2.1.0-blue?style=for-the-badge&logo=appveyor" alt="Version">
  <img src="https://img.shields.io/badge/Python-3.x-yellow?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Platform-Termux%20%7C%20Kali%20Linux-green?style=for-the-badge&logo=linux" alt="Platform">
  <img src="https://img.shields.io/badge/License-MIT-red?style=for-the-badge" alt="License">
</p>

---

## 📖 About Web Eater

**Web Eater** is a multithreaded directory and file fuzzing tool designed for security professionals, bug bounty researchers, and ethical hackers working within an authorized scope. It helps identify publicly reachable directories, files, and endpoints on web servers.

Features include real-time scan progress, configurable HTTP status-code filtering, recursive scanning, request delays, and output export to support efficient web enumeration.

## 🚀 Features

- ⚡ **Multithreaded Scanning** — Configure concurrent workers to speed up requests.
- 📊 **Live Progress Display** — Track scan progress with a real-time progress bar.
- 🎯 **HTTP Status Filtering** — Show only selected response codes, such as `200`, `301`, or `403`.
- 🔄 **Recursive Scanning** — Optionally scan directories discovered during a run.
- 🧭 **User-Agent Rotation** — Rotate User-Agent values to help test how a site responds to different clients. This does not guarantee WAF evasion.
- ⏱️ **Request Delay** — Add a delay between requests to reduce request rate and server load.
- 💾 **Save Results** — Export findings to a text file for later review.
- 🕵️ **Response-Size Filtering** — Exclude known response sizes to help filter custom error pages.

## 📦 Installation

### Requirements

- Python 3.x
- Termux on Android, or Kali Linux / another Debian-based Linux distribution
- Git

### Install on Termux or Linux

```bash
# 1. Clone the repository
git clone https://github.com/Jack-tech9355/web-eater.git

# 2. Enter the project directory
cd web-eater

# 3. Make the installer executable
chmod +x install.sh

# 4. Run the installer
./install.sh
```

## 💻 Usage

```bash
python3 webeater.py -u <URL> -w <WORDLIST> [OPTIONS]
```

### ⚙️ Command-Line Options

| Option | Description |
|---|---|
| `-u`, `--url` | Target URL, for example `https://example.com`. |
| `-w`, `--wordlist` | Path to a wordlist file, for example `common.txt`. |
| `-e`, `--extensions` | File extensions to test, such as `php,html,js`. |
| `-t`, `--threads` | Number of worker threads (default: `10`). |
| `-sc`, `--status` | Filter results by HTTP status codes, such as `"200,403"`. |
| `-d`, `--delay` | Delay between requests in seconds, such as `0.5`. |
| `-o`, `--output` | Save results to a file, such as `results.txt`. |
| `-rec`, `--recursive` | Enable recursive directory scanning. |
| `-m`, `--method` | HTTP method, such as `GET` or `POST`. |
| `--exclude` | Exclude responses with a specified size to help filter custom error pages. |

## 🎯 Example Scans

Run these examples only against systems you own or have explicit permission to test.

### 1. Basic Scan

```bash
python3 webeater.py -u https://example.com -w common.txt -e php,html -t 20
```

### 2. Filter Results and Save Output

```bash
python3 webeater.py -u https://example.com -w common.txt -sc "200" -d 0.5 -o results.txt -rec
```

### 3. Exclude a Known Response Size

```bash
python3 webeater.py -u https://example.com -w common.txt --exclude 9121
```

---

## ⚠️ Responsible Use

Web Eater is intended for educational use and authorized security testing only. Scan only websites and systems you own or have explicit permission to assess. Obtain authorization before testing, follow the target's rules and rate limits, and stop if your testing causes disruption.

The author, **Jack-tech9355**, is not responsible for misuse of this tool or damage caused by unauthorized activity. Unauthorized access or testing may violate applicable laws.

---

<p align="center">
  <em>If you find Web Eater useful, consider starring the repository ⭐</em>
</p>
