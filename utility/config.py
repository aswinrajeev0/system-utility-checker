import os
import sys
from dotenv import load_dotenv
from utility.utils.machine_id import get_machine_id

if getattr(sys, 'frozen', False):
    base_dir = sys._MEIPASS
else:
    base_dir = os.path.dirname(os.path.abspath(__file__))

load_dotenv(os.path.join(base_dir, '.env'))

API_URL = os.getenv("API_URL", "")
MACHINE_ID = get_machine_id()
CHECK_INTERVAL = 15