# ToolKit

## Overview

**ToolKit** is a modular and extensible command-line framework designed to streamline and automate various tasks in cybersecurity, penetration testing, and bug bounty hunting. It brings together a curated set of open-source tools and custom scripts, providing a unified interface for reconnaissance, enumeration, vulnerability scanning, subdomain discovery, and more.

The main goal of ToolKit is to accelerate the workflow of security professionals by offering a single entry point for running, chaining, and managing multiple tools, reducing repetitive manual steps and improving efficiency.

---

## Features

- **Unified CLI Interface:** Run dozens of popular security tools from a single menu-driven interface.
- **Reconnaissance & Enumeration:** Automate information gathering on domains, subdomains, DNS, infrastructure, and endpoints.
- **Vulnerability Scanning:** Integrate scanners for web vulnerabilities, WordPress, APIs, and more.
- **Subdomain Discovery:** Use multiple engines and techniques for comprehensive subdomain enumeration and validation.
- **Fuzzing & Exploitation:** Automate parameter fuzzing, endpoint discovery, and exploitation tasks.
- **Reporting & Documentation:** Generate structured reports and use built-in templates for vulnerability documentation.
- **Extensible & Modular:** Easily add or update tools and scripts as needed.
- **Cross-Platform Support:** Installation instructions for both Debian-based and Arch-based Linux distributions.

---

## Main Modules & Tools

ToolKit organizes its features into several categories, each grouping related tools:

### 1. Enumeration
- **gf, arjun, unfurl, paramspider, subjs, anti-burl, amass, metabigor:** Tools for parameter discovery, endpoint enumeration, and information extraction.

### 2. Information Gathering
- **host, whois, censys, dnsenum, dnsrecon, nmap, wafw00f:** Collect infrastructure, DNS, and network information.

### 3. Scanners
- **jsql, dotdotpwn, searchsploit, wpscan, burpsuite:** Scan for vulnerabilities in web applications, WordPress, and more.

### 4. Structure & Automation
- **xargs, nuclei, dalfox, katana:** Automate command execution, vulnerability scanning, and crawling.

### 5. Subdomain & API Discovery
- **kiterunner, github-search, GitDorker, wfuzz, ffuf, feroxbuster, gauplus, waymore, httpx, httprobe, aquatone:** Discover subdomains, APIs, and endpoints using various techniques.

### 6. Options & Utilities
- **Manuals, Info, Reports, Python tools, Step-by-step guides, Install scripts:** Access documentation, reporting templates, and installation helpers.

---

## Usage

### Running ToolKit

1. **Start the toolkit:**
   ```bash
   uv run main.py
   ```
2. **Follow the interactive menu:**
   - Enter the target domain or URL when prompted.
   - Select the desired tool or module by its number.
   - Provide additional options or parameters as required by the tool.

### Example Workflow

- **Enumerate parameters:** Use `gf`, `arjun`, or `paramspider` to find interesting parameters.
- **Gather information:** Run `whois`, `nmap`, or `dnsenum` for infrastructure details.
- **Scan for vulnerabilities:** Use `nuclei`, `dalfox`, or `wpscan` to identify weaknesses.
- **Discover subdomains:** Combine `amass`, `gauplus`, and `httpx` for comprehensive coverage.
- **Generate a report:** Use the built-in reporting template to document findings.

---

## Installation

### Quick Start (Recommended)

Follow these steps to quickly set up ToolKit using [uv](https://github.com/astral-sh/uv) for fast dependency management.

#### 1. Clone the Repository

```bash
git clone https://github.com/k1ll-chain/Bounty-ToolKit.git
cd Bounty-ToolKit/ToolKit
```

#### 2. Install `uv`

If you don't have `uv` installed, install it with:

```bash
sudo apt install uv
```

Or, for the latest version:

```bash
curl -Ls https://astral.sh/uv/install.sh | sh
```

#### 3. Install Dependencies

```bash
uv pip install
```

#### 4. Run ToolKit

```bash
uv run main.py
```

Or, if you want to activate the environment and run manually:

```bash
uv venv
source .venv/bin/activate
python main.py
```

---

### Dependencies

- Python 3.13+
- Go (Golang)
- pipx
- Various system packages (see below)

### Automated Installation (Legacy)

#### Debian/Ubuntu

```bash
apt update -y
apt upgrade -y
apt install gccgo-go golang-go pipx -y
pipx ensurepath
pip install hackerhelp
# ... (see Config/Options/main_opt.py for full script)
```

#### Arch/BlackArch

```bash
sudo pacman -Syu
sudo pacman -S --noconfirm blackarch gcc go pipx seclists
sudo pipx ensurepath
sudo pipx install hackerhelp
# ... (see Config/Options/main_opt.py for full script)
```

### Manual Installation

If you prefer, you can install each tool individually. Refer to the "Manual" section in the toolkit for step-by-step commands for each dependency.

---

## Contributing

ToolKit is designed to be extensible. If you want to add new tools or improve existing modules:

1. Fork the repository.
2. Add your tool or script under the appropriate module in `Config/`.
3. Update the main menu and documentation as needed.
4. Submit a pull request.

---

## Disclaimer

ToolKit is intended for educational and authorized security testing purposes only. Always obtain proper permission before testing any system or network.

---

## Credits

ToolKit integrates and automates a wide range of open-source security tools. Please refer to each tool's repository for individual credits and licenses.

---
