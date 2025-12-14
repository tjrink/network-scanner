import tkinter as tk

root = tk.Tk()
root.title("Network Scanner")
root.state("zoomed")

frm_min_port = tk.Frame(root, bg="blue")

lbl_min_port = tk.Label(frm_min_port, height=1, text="Min Port")
txt_min_port = tk.Text(frm_min_port, height=1, width=30)
lbl_min_port.pack(side="left")
txt_min_port.pack(side="right")

frm_max_port = tk.Frame(root, bg="red")
lbl_max_port = tk.Label(frm_max_port, height=1, text="Max Port")
txt_max_port = tk.Text(frm_max_port, height=1, width=30)
lbl_max_port.pack(side="left")
txt_max_port.pack(side="right")


frm_min_port.pack()
frm_max_port.pack()
root.mainloop()
