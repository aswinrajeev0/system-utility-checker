import requests
from utility.config import API_URL
from utility.config import MACHINE_ID

def send_report(data):
    payload = {
        "machine_id": MACHINE_ID,
        "data": data
    }
    print(payload)
    try:
        r = requests.post(API_URL, json=payload, timeout=5)
        r.raise_for_status()
    except Exception as e:
        print("Error reporting:", e)
