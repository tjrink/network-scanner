import threading
import socket

def run_port_scan(min_port, max_port, thread):
    for i in range(min_port, max_port):
        if(i%2 == thread):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.1)
            try:
                s.connect(("localhost", i))
                request = f"GET / HTTP/1.1\r\nHost: {s}\r\nConnection: close\r\n\r\n"
                s.sendall(request.encode())

                response_bytes = s.recv(1024)
                response_decoded = response_bytes.decode("UTF-8")

                print (f"Port {i} response: {response_decoded[0:26].rstrip()}")
                s.close()
            except:
                print (f"Port {i} cannot be reached")



def run(min_port, max_port):
    thread_evens = threading.Thread(target=run_port_scan, args=(min_port, max_port, 0))
    thread_odds = threading.Thread(target=run_port_scan, args=(min_port, max_port, 1))
    thread_evens.start()
    thread_odds.start()