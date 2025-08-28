from utility.checks.updates import check_os_updates
from utility.checks.antivirus import check_antivirus
from utility.checks.sleep import check_sleep_settings
from utility.checks.disk import check_disk_encryption
from utility.core.ensure_admin import ensure_admin

ensure_admin()

def collect_system_state():
    return {
        "disk_encryption": check_disk_encryption(),
        "os_update": check_os_updates(),
        "antivirus": check_antivirus(),
        "sleep_settings": check_sleep_settings(),
    }