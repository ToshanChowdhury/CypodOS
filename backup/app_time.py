import tkinter as tk
import time

def update():
    updated_time = time.strftime("%I:%M:%S %p")
    astime.config(text=updated_time)
    astime.after(1000, update)

window = tk.Tk()
window.title("Time Application")

get_time = time.strftime("%I:%M:%S %p")
get_date = time.strftime("%d/%m/%Y")

astime = tk.Label(text=get_time, font=("Segoe UI", 100), fg="green", bg="yellow")
astime.pack()

asdate = tk.Label(text=get_date, font=("Segoe UI", 30), fg="yellow", bg="lime")
asdate.pack()

update()

window.mainloop()