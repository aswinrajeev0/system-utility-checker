import platform
import subprocess

def check_os_updates():
    os_type = platform.system()

    try:
        if os_type == "Windows":
            result = subprocess.run(
                ["powershell", "-Command",
                 "$updateSession = New-Object -ComObject Microsoft.Update.Session; "
                 "$searcher = $updateSession.CreateUpdateSearcher(); "
                 "$result = $searcher.Search('IsInstalled=0'); "
                 "if ($result.Updates.Count -gt 0) { Write-Output 'UpdatesAvailable' } else { Write-Output 'NoUpdates' }"
                 ],
                capture_output=True,
                text=True,
                check=False
            )
            return "UpdatesAvailable" in result.stdout

        elif os_type == "Darwin":  # macOS
            output = subprocess.check_output(["softwareupdate", "-l"], text=True)
            return "No new software available." not in output

        elif os_type == "Linux":
            # Debian/Ubuntu
            try:
                output = subprocess.check_output(
                    ["apt-get", "-s", "upgrade"], text=True
                )
                return "0 upgraded" not in output
            except:
                return "Check manually: dnf/yum/zypper"
    except Exception as e:
        return f"Error checking updates: {e}"
