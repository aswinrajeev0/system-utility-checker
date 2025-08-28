import platform
import subprocess
import shutil

def check_antivirus():
    os_type = platform.system()

    try:
        if os_type == "Windows":
            output = subprocess.check_output(
                ["powershell", "-Command",
                 "Get-CimInstance -Namespace root/SecurityCenter2 -ClassName AntivirusProduct"],
                text=True
            )
            return "displayName" in output and "pathToSignedProductExe" in output
        elif os_type == "Darwin":
            if shutil.which("xprotectupdater") or \
               shutil.which("MRT"):
                return True

            # Check common 3rd party processes
            output = subprocess.check_output(["ps", "aux"], text=True).lower()
            common_avs = ["sophos", "malwarebytes", "avast", "symantec", "bitdefender"]
            return any(av in output for av in common_avs)
        elif os_type == "Linux":
            av_binaries = ["clamscan", "clamdscan", "savscan", "bdscan"]
            for av in av_binaries:
                if shutil.which(av):
                    return True

            # Check running processes
            output = subprocess.check_output(["ps", "aux"], text=True).lower()
            common_avs = ["clamd", "savd", "f-secure", "eset", "mcafee"]
            return any(av in output for av in common_avs)
    except Exception as e:
        return f"Error checking antivirus: {e}"