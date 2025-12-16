import threading
import socket

#Port scanning function
def run_port_scan(ip_add, min_port, max_port, results_queue):
    
    for i in range(min_port, max_port + 1):        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.05) #Sets timeout to speed up performance
        try:
            s.connect((ip_add, i)) 
            request = f"GET / HTTP/1.1\r\nHost: {s}\r\nConnection: close\r\n\r\n" #Basic HTTP request
            s.sendall(request.encode())
            response_bytes = s.recv(1024)
            response_decoded = response_bytes.decode("UTF-8")
            header_information = response_decoded.split("\r\n")
            results_queue[i] = header_information[0] #"Returns" port to results queue if the connection works.
            s.close()
        except:
            pass #Does nothing if connection fails
    

#Breaks up the request from the UI into 8 threads and kicks off each thread
def run(ip_add, min_port, max_port):
    thread_size = ((max_port - min_port + 1)//8) + 1 #Set number of ports to scan in each thread
    #results_queue = set() #Initialize empty set to return list of open ports
    results_queue = {}
    #Thread initialization
    thread_1 = threading.Thread(target=run_port_scan, args=(ip_add, min_port + (thread_size * 0), min_port + (thread_size * 1), results_queue))
    thread_2 = threading.Thread(target=run_port_scan, args=(ip_add, min_port + (thread_size * 1), min_port + (thread_size * 2), results_queue))
    thread_3 = threading.Thread(target=run_port_scan, args=(ip_add, min_port + (thread_size * 2), min_port + (thread_size * 3), results_queue))
    thread_4 = threading.Thread(target=run_port_scan, args=(ip_add, min_port + (thread_size * 3), min_port + (thread_size * 4), results_queue))
    thread_5 = threading.Thread(target=run_port_scan, args=(ip_add, min_port + (thread_size * 4), min_port + (thread_size * 5), results_queue))
    thread_6 = threading.Thread(target=run_port_scan, args=(ip_add, min_port + (thread_size * 5), min_port + (thread_size * 6), results_queue))
    thread_7 = threading.Thread(target=run_port_scan, args=(ip_add, min_port + (thread_size * 6), min_port + (thread_size * 7), results_queue))
    thread_8 = threading.Thread(target=run_port_scan, args=(ip_add, min_port + (thread_size * 7), min_port + (thread_size * 8), results_queue))



    thread_1.start()
    thread_2.start()
    thread_3.start()
    thread_4.start()
    thread_5.start()
    thread_6.start()
    thread_7.start()
    thread_8.start()


    thread_1.join()
    thread_2.join()
    thread_3.join()
    thread_4.join()
    thread_5.join()
    thread_6.join()
    thread_7.join()
    thread_8.join()


    return results_queue
    