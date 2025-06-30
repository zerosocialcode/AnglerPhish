# AnglerPhish: Advanced Web Cloning & Exposure Toolkit

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**AnglerPhish** is a modular, extensible research toolkit for web cloning, local hosting, and public exposure via secure tunneling. Designed for both researchers and enthusiasts, it features a universal launcher (`Gateway`) that auto-discovers and executes tools within the `tools/` directory. The toolkit currently includes modules for webpage mirroring (`AnglerCloning`) and serving/exposing cloned sites (`AnglerPhish`).

---

**Developed & maintained by [zerosocialcode](https://github.com/zerosocialcode)**

---

## Table of Contents

1. [Features](#features)
2. [Why Cloudflared First?](#why-cloudflared-first)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
    - [Linux](#linux-installation)
    - [Termux (Android)](#termux-installation)
    - [Windows](#windows-installation)
5. [Project Structure](#project-structure)
6. [Universal Launcher (Gateway)](#universal-launcher-gateway)
7. [Usage](#usage)
8. [Dependencies](#dependencies)
9. [External Tools](#external-tools)
10. [Contributing](#contributing)
11. [License](#license)

---

## Features

- **Universal Launcher (`Gateway`):** Auto-detect and execute any tool module dropped into `tools/`.
- **Website Cloning (`AnglerCloning`):** Effortlessly mirror any website for offline or analytical purposes.
- **Local Hosting (`AnglerPhish`):** Serve static cloned content via a robust Flask-based server.
- **Public Exposure via Tunnels:** Seamlessly expose your local server using Cloudflared (fully tested).  
  > **Note:** Only **Cloudflared** is fully tested. Support for **Ngrok** and **LocalTunnel** is planned, but these methods are not fully implemented or tested yet.
- **Colorized Terminal UI:** Enhanced UX with clear, color-coded prompts and outputs.
- **Plug-and-Play Architecture:** Add new tools by simply placing them in the `tools/` directory—no core modification required.

---

## Why Cloudflared First?

**Cloudflared** is selected as the primary and recommended tunneling method for public exposure because:
- **Stability & Reliability:** Cloudflared consistently offers stable, high-uptime tunnels with minimal downtime or throttling.
- **Bypasses Most NAT/Firewall Restrictions:** It directly connects through Cloudflare's global edge network, making it more robust in restrictive environments.
- **No Account/Token Required:** Unlike some alternatives, Cloudflared does not require prior registration or API keys for basic tunnel usage.
- **Security:** Traffic is proxied through Cloudflare's network, benefitting from their DDoS protection and security features.
- **Performance:** Low latency and high throughput are maintained even under heavy load.
- **Widely Trusted:** Used by organizations worldwide for secure, production-grade tunneling.
- **Cross-platform Support:** Runs on Linux, Windows, macOS, and ARM-based devices (including Android/Termux).

> For these reasons, **Cloudflared** is the only exposure method fully tested and supported in AnglerPhish at this time. Ngrok and LocalTunnel are included for future support, but are not fully implemented or tested yet.

---

## Prerequisites

- **Python 3.8 or newer**
- **pip** (Python package manager)
- **wget** (for deep web cloning)
- **Tunnel CLIs:**  
    - `cloudflared` (fully tested)
    - `ngrok` (not fully implemented)
    - `lt` (localtunnel) (not fully implemented)  
> **Note:** Tunnel CLIs must be installed and have executable permission in your environment.

---

## Installation

The toolkit supports installation on **Linux**, **Termux (Android)**, and **Windows**.  
Follow the instructions for your environment:

---

### Linux Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/zerosocialcode/AnglerPhish.git
   cd AnglerPhish
   ```

2. **Install Python & pip**  
   On Debian/Ubuntu:
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   ```

3. **Install Python Dependencies**
   ```bash
   pip3 install -r requirements.txt
   ```

4. **Install wget**
   ```bash
   sudo apt install wget
   ```

5. **Ensure tunnel tools (`cloudflared`, `ngrok`, `lt`) are installed and have executable permission.**

---

### Termux Installation (Android)

1. **Update & Install Packages**
   ```bash
   pkg update
   pkg install python wget git nodejs
   ```

2. **Clone the Repository**
   ```bash
   git clone https://github.com/zerosocialcode/AnglerPhish.git
   cd AnglerPhish
   ```

3. **Install Python Dependencies**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Ensure wget is installed and tunnel tools (`cloudflared`, `ngrok`, `lt`) are installed and have executable permission.**

---

### Windows Installation

1. **Install Python 3.x and pip**
   - Download from [python.org](https://www.python.org/downloads/) and check “Add Python to PATH” during installation.

2. **Install Git**
   - Download from [git-scm.com](https://git-scm.com/download/win)

3. **Open Command Prompt (CMD) or PowerShell and run:**
   ```bash
   git clone https://github.com/zerosocialcode/AnglerPhish.git
   cd AnglerPhish
   pip install -r requirements.txt
   ```

4. **Install wget**
   - Download Windows binary and add `wget.exe` to your PATH or place it in the project folder.

5. **Ensure tunnel tools (`cloudflared`, `ngrok`, `lt`) are installed and have executable permission.**

> **Tip:** For all environments, make sure all executables (`wget`, `cloudflared`, `ngrok`, `lt`) are in your `PATH` or present in the project directory.

---

## Project Structure

```
AnglerPhish/
├── main.py                   # Universal launcher (Gateway)
├── credentials/              # Captured data storage (per tool)
└── tools/                    # Tool modules loaded by Gateway
    ├── AnglerCloning/        # Website cloning script (cloner.py)
    └── AnglerPhish/          # Hosting server and tunnel exposers
        ├── main.py
        └── expose/
            ├── cloudflared.py
            ├── ngrok.py
            └── localtunnel.py
```

---

## Universal Launcher (Gateway)

The `main.py` script in the root directory serves as the **Gateway**. It dynamically scans the `tools/` directory, lists all available modules (any subfolder with a `main.py`), and allows you to interactively select and execute them.

**To start:**
```bash
python main.py
```
Follow the prompts to select and launch available tools (e.g., `AnglerCloning`, `AnglerPhish`).

---

## Usage

- **AnglerCloning:** Clone any website for offline analysis or research.  
- **AnglerPhish:** Host previously cloned content locally and, if desired, expose it publicly via a secure tunnel.

> **Only Cloudflared is fully tested for public exposure.  
> Ngrok and LocalTunnel are included for planned future support, but are not yet fully implemented or tested.**

---

## Dependencies

**Python Packages:**
- `requests`
- `beautifulsoup4`
- `termcolor`
- `Flask`

Install all dependencies:
```bash
pip install -r requirements.txt
```

---

## External Tools

- **wget** (for deep web cloning)
- **cloudflared** (secure tunnel, fully tested)
- **ngrok** (alternative tunnel, not fully implemented)
- **lt (LocalTunnel)** (alternative tunnel, not fully implemented)

> These must be installed manually and have executable permission in your environment.

---

## Contributing

Contributions are welcome! To add a new tool, simply create a new subdirectory under `tools/` containing a `main.py`. The Gateway will auto-detect and list it for use.

**Example Tool Structure:**
```
tools/
└── YourToolName/
    └── main.py
```

### How to Contribute

1. **Fork the repository**
2. **Create a feature branch:**  
   `git checkout -b feature/your-tool`
3. **Add your tool under `tools/`**
4. **Commit and push your changes**
5. **Submit a pull request**

---

## License

This project is released under the [MIT License](LICENSE).

---

**Developer:** [zerosocialcode](https://github.com/zerosocialcode)
