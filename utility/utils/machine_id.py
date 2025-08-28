import uuid, hashlib, socket

def get_machine_id():
    node = uuid.getnode()
    hostname = socket.gethostname()
    raw_id = f"{node}-{hostname}"
    return hashlib.sha256(raw_id.encode()).hexdigest()[:16]