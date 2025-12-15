import threading
import socket

def run_port_scan(ip_add, min_port, max_port, thread, results_queue):
    open_ports = set()
    for i in range(min_port, max_port + 1):
        if(i%4 == thread):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.05)
            try:
                s.connect((ip_add, i))
                request = f"GET / HTTP/1.1\r\nHost: {s}\r\nConnection: close\r\n\r\n"
                s.sendall(request.encode())

                response_bytes = s.recv(1024)
                response_decoded = response_bytes.decode("UTF-8")
                results_queue.add(i)
                s.close()
            except:
                pass



def run(ip_add, min_port, max_port):
    results_queue = set()
    thread_1 = threading.Thread(target=run_port_scan, args=(ip_add, min_port, max_port, 0, results_queue))
    thread_2 = threading.Thread(target=run_port_scan, args=(ip_add, min_port, max_port, 1, results_queue))
    thread_3 = threading.Thread(target=run_port_scan, args=(ip_add, min_port, max_port, 2, results_queue))
    thread_4 = threading.Thread(target=run_port_scan, args=(ip_add, min_port, max_port, 3, results_queue))

    thread_1.start()
    thread_2.start()
    thread_3.start()
    thread_4.start()

    thread_1.join()
    thread_2.join()
    thread_3.join()
    thread_4.join()

    return results_queue
    