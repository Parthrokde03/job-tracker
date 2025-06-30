import tkinter as tk
from tkinter import messagebox
import os
import json
from datetime import datetime


data_file = "job_list.json"

if not os.path.exists(data_file):
    with open(data_file, 'w') as file:
        json.dump([], file)
        
def save_job():
    company = company_entry.get().strip()
    role = role_entry.get().strip()
    date = date_entry.get().strip()
    status = status_var.get()
    
    if not company or not role or not date or not status:
        messagebox.showerror("Error","Please fill all fields")
        return
    
    job_data = {
        'company' : company,
        'role' : role,
        'date' : date,
        'status' : status
    }
    
    try:
        with open(data_file, 'r') as file:
            data = json.load(file)
        
    except json.JSONDecodeError:
        data = []    

    data.append(job_data)
    
    with open(data_file, 'w') as file:
        json.dump(data ,file, indent=4)
        
    messagebox.showinfo("Saved", "Job application saved!")
    company_entry.delete(0,tk.END)
    role_entry.delete(0,tk.END)
    date_entry.delete(0,tk.END)
    status_entry.delete(0,tk.END)
     
# GUI
root = tk.Tk()
root.title("JobTarcker")      
root.geometry("400x400")
root.resizable(False,False)

tk.Label(root,text="Company Name").pack()
company_entry = tk.Entry(root,width=40)
company_entry.pack()

tk.Label(root,text="Role Applied For").pack()
role_entry = tk.Entry(root,width=40)
role_entry.pack()

tk.Label(root,text="Date Applied (YYYY-MM-DD)").pack()
date_entry = tk.Entry(root, width=40)
date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))
date_entry.pack()

tk.Label(root,text="Application Status").pack()
# status_entry = tk.Entry(root,width=40)
status_var = tk.StringVar()
status_option = ["Applied", "Interviewed", "Rejected", "Accepted", "Offer Received"]
status_menu = tk.OptionMenu(root,status_var, *status_option)
status_menu.pack()

tk.Button(root,text="Save Application",command=save_job).pack(pady=5)

root.mainloop()
