import platform
import subprocess
import re

def check_sleep_settings(max_seconds=600):
    os_type = platform.system()

    try:
        if os_type == "Windows":
            output = subprocess.check_output(
                ["powercfg", "-query"], text=True, errors="ignore"
            )

            ac_match = re.search(r"Current AC Power Setting Index:\s*0x([0-9a-fA-F]+)", output)
            dc_match = re.search(r"Current DC Power Setting Index:\s*0x([0-9a-fA-F]+)", output)

            ac_val = int(ac_match.group(1), 16) if ac_match else None
            dc_val = int(dc_match.group(1), 16) if dc_match else None

            return (ac_val is not None and ac_val <= max_seconds) or \
                   (dc_val is not None and dc_val <= max_seconds)
                   
        elif os_type == "Darwin":
            output = subprocess.check_output(["pmset", "-g"], text=True, errors="ignore")
            for line in output.splitlines():
                if line.strip().startswith(" sleep "):
                    try:
                        val = int(line.split()[-1])
                        return val * 60 <= max_seconds
                    except:
                        return False
            return False
        
        elif os_type == "Linux":
            try:
                output = subprocess.check_output(
                    ["gsettings", "get", "org.gnome.settings-daemon.plugins.power", "sleep-inactive-ac-timeout"], 
                    text=True, errors="ignore"
                )
                val = int(output.strip())
                return val <= max_seconds
            except:
                return False

        return False
    except Exception as e:
        print(f"Error checking sleep settings: {e}")
        return False