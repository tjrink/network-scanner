import socket

min_port = 0
max_port = 444

for i in range(min_port, max_port):
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
