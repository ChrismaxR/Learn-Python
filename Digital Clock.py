from time import strftime
import tkinter as tk

#======= Configuring window =========
window = tk.Tk()
window.title("digital clock")
window.geometry("200x200")
window.resizable(False, False)
'''window.attributes('-zoomed', True)'''

#============ Logic lives here =======

clock_label = Label(window, bg="red", fg="white", font = ("Times", 30), relief='flat')
clock_label.place(x = 20, y = 20)

def update_label():
    current_time = strftime('%H: %M: %S')
    clock_label.configure(text = current_time)
    clock_label.after(80, update_label)

update_label()

window.mainloop()