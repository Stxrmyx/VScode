import socket
import tqdm
from multiprocessing.pool import ThreadPool


PORTS_COUNT = 2**16
HOST = "127.0.0.1"
TIMEOUT = 0.1

def is_opened_port (port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(TIMEOUT)
        return None if sock.connect_ex((HOST, port)) else port

if __name__ == '__main__':
   pool = ThreadPool(7500)
   scanned = list(
      tqdm.tqdm( pool.imap(is_opened_port, range(1, PORTS_COUNT)), total=PORTS_COUNT-1, desc=f'Scaninh {HOST}'))
   print([port for port in scanned if port])
