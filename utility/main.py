from utility.config import CHECK_INTERVAL
from utility.config import MACHINE_ID
from utility.daemon import start_daemon

def main():
    print(f"Starting system utility daemon (Machine ID: {MACHINE_ID})")
    print(f"Check interval: {CHECK_INTERVAL} minutes")
    
    start_daemon(interval=CHECK_INTERVAL)

if __name__ == "__main__":
    main()
