import tkinter as tk
import port_scanner

def send_info_to_scanner():
    min_str = txt_min_port.get()
    max_str = txt_max_port.get()

    port_scanner.run(int(min_str), int(max_str))

root = tk.Tk()
root.title("Network Scanner")
root.state("zoomed")

frm_min_port = tk.Frame(root, bg="blue")

lbl_min_port = tk.Label(frm_min_port, height=1, text="Min Port")
txt_min_port = tk.Entry(frm_min_port, width=30)
lbl_min_port.pack(side="left")
txt_min_port.pack(side="right")

frm_max_port = tk.Frame(root, bg="red")
lbl_max_port = tk.Label(frm_max_port, height=1, text="Max Port")
txt_max_port = tk.Entry(frm_max_port, width=30)
lbl_max_port.pack(side="left")
txt_max_port.pack(side="right")

btn_run_scan = tk.Button(root, text="Run Port Scan", command=send_info_to_scanner)


frm_min_port.pack()
frm_max_port.pack()
btn_run_scan.pack()
root.mainloop()


