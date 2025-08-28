import platform
import subprocess
import os
import string

def check_disk_encryption():
    os_type = platform.system()

    if os_type == "Windows":
        try:
            for drive in get_drives_windows():
                result = subprocess.run(
                    ["manage-bde", "-status", drive],
                    capture_output=True,
                    text=True,
                    check=False
                )
                output = result.stdout
                if not ("Percentage Encrypted: 100" in output or "Fully Encrypted" in output):
                    return False
            return True
        except Exception as e:
            return f"Error checking BitLocker: {e}"

    elif os_type == "Darwin":  # macOS
        try:
            output = subprocess.check_output(
                ["fdesetup", "status"], text=True
            )
            return "FileVault is On" in output
        except Exception as e:
            return f"Error checking FileVault: {e}"

    elif os_type == "Linux":
        try:
            output = subprocess.check_output(
                ["lsblk", "-o", "NAME,MOUNTPOINT,FSTYPE"], text=True
            )
            return "crypt" in output or "luks" in output
        except Exception as e:
            return f"Error checking LUKS: {e}"
    else:
        return "Unsupported OS"


def get_drives_windows():
    drives = []
    for letter in string.ascii_uppercase:
        drive = f"{letter}:"
        if os.path.exists(drive + "\\"):
            drives.append(drive)
    return drives