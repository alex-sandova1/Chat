import tkinter as tk


window = tk.Tk()
window.title("Homepage")
window.geometry("500x500")
window.configure(background="grey", padx=10, pady=10)
window.resizable(True, True)

input = tk.Entry(window, width=25)
input.place(x=125, y=100)
label = tk.Label(window, text="Enter your message: ")
label.place(x=175, y=75)

#add button

window.mainloop()