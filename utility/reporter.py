import requests
from utility.config import API_URL
from utility.config import MACHINE_ID
import platform

def send_report(data):
    os_type = platform.system()
    payload = {
        "machine_id": MACHINE_ID,
        "os_type": os_type,
        **data
    }
    print(payload)
    try:
        r = requests.post(API_URL, json=payload, timeout=5)
        r.raise_for_status()
    except Exception as e:
        print("Error reporting:", e)
