import tkinter as tk
import shadowTk
import platform

root = tk.Tk()

# place a label on the root window
message = tk.Label(root, text="Hello, World!",bg='#ccffcc',fg='#000000',font=('Arial', 30))
shadowTk.Shadow(message,color='#ccffcc', size=1.3, offset_x=-5,onhover={'color':'#88cc88'})

message2 = tk.Label(root, text="Hello, World!",bg='#ccffcc',fg='#000000',font=('Arial', 30))
shadowTk.Shadow(message2,color='#1565C0', size=1.3, offset_x=-5,onhover={'color':'#3265C0'})
message2.pack()
if(platform.system()=='Windows'):    
    from ctypes import windll
    try:
        windll.shcore.SetProcessDpiAwareness(1)
    finally:
        root.mainloop()
else:
    root.mainloop()