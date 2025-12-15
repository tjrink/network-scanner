import tkinter as tk
import port_scanner

def send_info_to_scanner():
    lbl_results.config(text="Scanning")
    ip_add = txt_ip.get()
    min_str = txt_min_port.get()
    max_str = txt_max_port.get()

    port_set = port_scanner.run(ip_add, int(min_str), int(max_str))
    results_text = "Open ports: "
    for port in port_set:
        results_text+= port + " "
    
    lbl_results.config(text=results_text)

root = tk.Tk()
root.title("Network Scanner")
root.state("zoomed")

frm_ip_add = tk.Frame(root)
lbl_ip = tk.Label(frm_ip_add, text="IP Address")
txt_ip = tk.Entry(frm_ip_add, width=30)
lbl_ip.pack()
txt_ip.pack()


frm_min_port = tk.Frame(root)

lbl_min_port = tk.Label(frm_min_port, height=1, text="Min Port")
txt_min_port = tk.Entry(frm_min_port, width=30)
lbl_min_port.pack(side="left")
txt_min_port.pack(side="right")

frm_max_port = tk.Frame(root)
lbl_max_port = tk.Label(frm_max_port, height=1, text="Max Port")
txt_max_port = tk.Entry(frm_max_port, width=30)
lbl_max_port.pack(side="left")
txt_max_port.pack(side="right")

btn_run_scan = tk.Button(root, text="Run Port Scan", command=send_info_to_scanner)

frm_results = tk.Frame(root)
lbl_results = tk.Label(frm_results)
lbl_results.pack()

frm_ip_add.pack()
frm_min_port.pack()
frm_max_port.pack()
btn_run_scan.pack()
frm_results.pack()
root.mainloop()


