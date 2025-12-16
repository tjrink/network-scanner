import tkinter as tk
import port_scanner
from tkinter import font as tkfont #Import font module for styling

#Send port scan options to scanner
def send_info_to_scanner():
    #Update results label to show scan running
    lbl_results.config(text="Scanning...", fg="orange")
    
    #Gets key values from input fields
    ip_add = txt_ip.get()
    min_str = txt_min_port.get()
    max_str = txt_max_port.get()


    try:
        min_port = int(min_str)
        max_port = int(max_str)
        
        #Call the port scanner function
        port_results = port_scanner.run(ip_add, min_port, max_port)
        print(port_results)
        
        #Display the results
        if port_results:
            sorted_ports = sorted(list(port_results.keys()))
            results_text = f"Scan Complete. Open ports ({len(sorted_ports)})"
            lbl_results.config(text=results_text, fg="green")

            for port in sorted_ports:
                port_descriptor = f"Port {port}: {port_results[port]}"
                lbl_port = tk.Label(frm_results, text=port_descriptor)
                lbl_port.pack()


        else:
            lbl_results.config(text="Scan Complete. No open ports found in range.", fg="red")
            
    except ValueError:
        lbl_results.config(text="Error: Port numbers must be integers.", fg="red")
    except Exception as e:
        lbl_results.config(text=f"Scan Error: {e}", fg="red")


#UI Setup
root = tk.Tk()
root.title("Network Scanner")

TITLE_FONT = tkfont.Font(family="Helvetica", size=14, weight="bold")
LABEL_FONT = tkfont.Font(family="Helvetica", size=10)

GLOBAL_PADX = 10
GLOBAL_PADY = 5

#Main input frame
frm_main_input = tk.Frame(root, padx=GLOBAL_PADX*2, pady=GLOBAL_PADY*2, 
                         bd=2, relief=tk.GROOVE)
frm_main_input.grid(row=0, column=0, padx=GLOBAL_PADX, pady=GLOBAL_PADY)


lbl_title = tk.Label(frm_main_input, text="Port Scanner Configuration", font=TITLE_FONT)
lbl_title.grid(row=0, column=0, columnspan=2, pady=(0, GLOBAL_PADY*2))


#IP Input
lbl_ip = tk.Label(frm_main_input, text="Target IP Address:", anchor="w", font=LABEL_FONT)
lbl_ip.grid(row=1, column=0, padx=GLOBAL_PADX, pady=GLOBAL_PADY, sticky="w")
txt_ip = tk.Entry(frm_main_input, width=30)

#Sets default value
txt_ip.insert(0, "127.0.0.1") 
txt_ip.grid(row=1, column=1, padx=GLOBAL_PADX, pady=GLOBAL_PADY)


#Minimum port input 
lbl_min_port = tk.Label(frm_main_input, text="Min Port:", anchor="w", font=LABEL_FONT)
lbl_min_port.grid(row=2, column=0, padx=GLOBAL_PADX, pady=GLOBAL_PADY, sticky="w")

txt_min_port = tk.Entry(frm_main_input, width=30)
txt_min_port.insert(0, "1") #Sets default min port
txt_min_port.grid(row=2, column=1, padx=GLOBAL_PADX, pady=GLOBAL_PADY)


#Max port input
lbl_max_port = tk.Label(frm_main_input, text="Max Port:", anchor="w", font=LABEL_FONT)
lbl_max_port.grid(row=3, column=0, padx=GLOBAL_PADX, pady=GLOBAL_PADY, sticky="w")

txt_max_port = tk.Entry(frm_main_input, width=30)
txt_max_port.insert(0, "1024") #Sets default max port
txt_max_port.grid(row=3, column=1, padx=GLOBAL_PADX, pady=GLOBAL_PADY)


#Run button
btn_run_scan = tk.Button(
    frm_main_input, 
    text="Run Port Scan", 
    command=send_info_to_scanner, 
    font=TITLE_FONT, 
    bg="lightblue", 
    fg="darkblue"
)
btn_run_scan.grid(row=4, column=0, columnspan=2, pady=GLOBAL_PADY*3, sticky="ew")


#Results Frame
frm_results = tk.Frame(root, padx=GLOBAL_PADX, pady=GLOBAL_PADY)
frm_results.grid(row=1, column=0, padx=GLOBAL_PADX, pady=GLOBAL_PADY)

#Results Label
lbl_results = tk.Label(frm_results, text="Enter configuration and click 'Run Scan'.", justify=tk.LEFT, wraplength=400, font=LABEL_FONT)
lbl_results.pack(fill="both", expand=True)

#Run loop
root.mainloop()