import tkinter as tk

root = tk.Tk()
root.title('Market Update Emailer')

tk.Label(root, text='Manual Time Interval:', font='Arial 11 bold').grid(row=0, padx=8)
tk.Entry(root, width = 8).grid(row=0, column=1, sticky=tk.N, pady=8, padx=8)
tk.Button(root, text='Submit').grid(row=1, column=1, sticky=tk.N)

root.mainloop()


