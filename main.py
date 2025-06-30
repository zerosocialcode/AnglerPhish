import json
import os
import shutil
import subprocess
import sys
import textwrap

CONFIG_FILE = ".config.json"
TOOLS_DIR = "tools"

# Theme Styles
class Style:
    CYAN = "\033[96m"
    AQUA = "\033[36m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    RESET = "\033[0m"
    BOLD = "\033[1m"
    GRAY = "\033[90m"

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def get_terminal_width():
    try:
        return shutil.get_terminal_size((80, 20)).columns
    except Exception:
        return 80

def display_header():
    width = get_terminal_width()
    # Split the banner into lines for control
    banner_lines = [
        "  ____       _            ",
        " / ___| __ _| |_ _____      ____ _ _   _ ",
        "| |  _ / _` | __/ _ \\ \\ /\\ / / _` | | | |",
        "| |_| | (_| | ||  __/\\ V  V / (_| | |_| |",
        " \\____|\\__,_|\\__\\___| \\_/\\_/ \\__,_|\\__, |",
        "                                   |___/ "
    ]
    slogan = f"{Style.GREEN}{Style.BOLD}Everything starts here.{Style.RESET}"
    devline = f"{Style.GRAY}developer: zerosocialcode{Style.RESET}"
    # Print all banner lines except the last
    for line in banner_lines[:-1]:
        print(f"{Style.CYAN}{Style.BOLD}{line}{Style.RESET}")
    # Print last line with slogan appended
    print(f"{Style.CYAN}{Style.BOLD}{banner_lines[-1]} {slogan}{Style.RESET}")
    print(f"{devline}\n")
    disclaimer = "This tool is provided as-is. Use responsibly—you assume all risks."
    for line in textwrap.wrap(disclaimer, width=width):
        print(f"{Style.YELLOW}{line}{Style.RESET}")
    print()  # Blank line after disclaimer

def load_config():
    if not os.path.exists(CONFIG_FILE):
        print(f"{Style.RED}❌ Missing config file: {CONFIG_FILE}{Style.RESET}")
        sys.exit(1)
    with open(CONFIG_FILE, "r") as f:
        return json.load(f).get("tools", [])

def print_row(num, name, desc, col_widths, show_desc):
    num_width, name_width, desc_width = col_widths
    if show_desc:
        desc_lines = textwrap.wrap(desc, width=desc_width) if desc else [""]
        print(
            f"{Style.CYAN}{str(num):<{num_width}}{Style.RESET}  "
            f"{Style.AQUA}{name:<{name_width}}{Style.RESET}  "
            f"{desc_lines[0]}"
        )
        for line in desc_lines[1:]:
            print(" " * (num_width + 2 + name_width + 2) + line)
    else:
        print(
            f"{Style.CYAN}{str(num):<{num_width}}{Style.RESET}  "
            f"{Style.AQUA}{name:<{name_width}}{Style.RESET}"
        )

def display_menu(tools):
    display_header()
    width = get_terminal_width()
    num_width = 3
    name_width = min(24, max((len(tool['name']) for tool in tools), default=12) + 2)
    show_desc = any(tool.get('description', '').strip() for tool in tools)
    desc_width = width - (num_width + 2 + name_width + (2 if show_desc else 0))
    if show_desc:
        print(f"{'No.':<{num_width}}  {'Tool Name':<{name_width}}  {'Description'}")
    else:
        print(f"{'No.':<{num_width}}  {'Tool Name':<{name_width}}")
    print()
    for i, tool in enumerate(tools, start=1):
        desc = tool.get('description', '')
        print_row(i, tool['name'], desc, (num_width, name_width, desc_width), show_desc)
        print()
    if show_desc:
        print(f"{Style.CYAN}{'0':<{num_width}}{Style.RESET}  {Style.RED}Exit{Style.RESET}\n")
    else:
        print(f"{Style.CYAN}{'0':<{num_width}}{Style.RESET}  {Style.RED}Exit{Style.RESET}\n")

def run_script(entry):
    script_path = os.path.join(TOOLS_DIR, entry)
    if not os.path.exists(script_path):
        print(f"{Style.RED}❌ Script not found: {script_path}{Style.RESET}")
        return
    script_dir = os.path.dirname(script_path)
    script_file = os.path.basename(script_path)
    print(f"{Style.AQUA}🚀 Launching {entry}...{Style.RESET}\n")
    subprocess.run([sys.executable, script_file], cwd=script_dir)

def main():
    tools = load_config()
    if not tools:
        print(f"{Style.RED}No tools found in config.{Style.RESET}")
        return
    while True:
        clear_screen()
        display_menu(tools)
        choice = input(f"{Style.BOLD}➤ Select a tool: {Style.RESET}").strip()
        if choice == "0":
            print(f"\n{Style.CYAN}👋 Exiting the lab...{Style.RESET}\n")
            break
        if not choice.isdigit() or not (1 <= int(choice) <= len(tools)):
            print(f"{Style.RED}❌ Invalid choice. Try again.{Style.RESET}")
            input("\nPress Enter to continue...")
            continue
        selected = tools[int(choice) - 1]
        run_script(selected["entry"])
        input(f"\n{Style.GRAY}Press Enter to return to the lab...{Style.RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Style.CYAN}👋 Interrupted. Exiting the lab gracefully...{Style.RESET}\n")
        sys.exit(0)
