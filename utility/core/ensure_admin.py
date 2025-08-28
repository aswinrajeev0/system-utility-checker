import os
import sys
import platform
import ctypes
import subprocess

def ensure_admin():
    system = platform.system()

    if system == "Windows":
        try:
            # Check admin
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        except:
            is_admin = False

        if not is_admin:
            # Relaunch as admin
            params = " ".join([f'"{arg}"' for arg in sys.argv])
            ctypes.windll.shell32.ShellExecuteW(
                None, "runas", sys.executable, params, None, 1
            )
            sys.exit(0)

    elif system == "Darwin":  # macOS
        if os.geteuid() != 0:
            # Relaunch using AppleScript admin prompt
            script = f'do shell script "python3 {sys.argv[0]}" with administrator privileges'
            subprocess.call(["osascript", "-e", script])
            sys.exit(0)

    elif system == "Linux":
        if os.geteuid() != 0:
            print("⚠️  This tool requires root privileges. Please run with: sudo " + " ".join(sys.argv))
            sys.exit(1)

    else:
        print(f"Unsupported OS: {system}")
        sys.exit(1)
