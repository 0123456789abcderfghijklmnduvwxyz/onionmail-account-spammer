#!/usr/bin/env python3
import os
import platform
import shutil
import subprocess
import sys

def run(cmd, shell=False):
    print(f"[*] Running: {' '.join(cmd) if isinstance(cmd, list) else cmd}")
    subprocess.check_call(cmd, shell=shell)

def ensure_uv():
    if shutil.which("uv"):
        print("[*] uv already installed.")
        return

    system = platform.system().lower()
    if system == "windows":
        print("[*] Installing uv on Windows...")
        run(["powershell", "-Command", "irm https://astral.sh/uv/install.ps1 | iex"], shell=True)
    else:
        print("[*] Installing uv on Linux/macOS...")
        run("curl -LsSf https://astral.sh/uv/install.sh | sh", shell=True)

    if not shutil.which("uv"):
        print("[!] uv installation failed. Please install manually: https://astral.sh/uv/")
        sys.exit(1)

def main():
    ensure_uv()

    # Create virtual environment
    if not os.path.exists(".venv"):
        run(["uv", "venv", ".venv"])
    else:
        print("[*] Virtual environment already exists.")

    # Install requirements
    if not os.path.exists("requirements.txt"):
        print("[!] requirements.txt not found. Please create it first.")
        sys.exit(1)

    run(["uv", "pip", "install", "-r", "requirements.txt"])

    # Install Playwright browsers
    run([os.path.join(".venv", "Scripts" if platform.system() == "Windows" else "bin", "playwright"), "install"])

    print("\n[+] Setup finished!")
    if platform.system() == "Windows":
        print("Activate venv with: .venv\\Scripts\\activate")
    else:
        print("Activate venv with: source .venv/bin/activate")

if __name__ == "__main__":
    main()
