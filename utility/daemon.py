import schedule, time
from utility.reporter import send_report
from utility.collectors import collect_system_state

last_state = None

def job():
    print(f"Job triggered at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    global last_state
    state = collect_system_state()

    if state != last_state:
        send_report(state)
        last_state = state

def start_daemon(interval):
    job()
    schedule.every(interval).minutes.do(job)
    while True:
        schedule.run_pending()
        time.sleep(5)
