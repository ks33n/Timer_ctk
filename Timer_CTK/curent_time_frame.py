import customtkinter as ctk
import datetime as dt

class CurentTimeFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.time = dt.datetime.now().time()
        
        self.time_lable = ctk.CTkLabel(self, text=self.time.strftime('%H:%M:%S'), fg_color='transparent', font=("Cascadia Mono SemiBold", 65))
        self.time_lable.place(x=33, y=65)
        
        self.after(1000, self.update_curent_time)
        
    def update_curent_time(self):
        self.time = dt.datetime.now().time()
        self.time_lable.configure(text=self.time.strftime('%H:%M:%S'))
        
        self.after(1000, self.update_curent_time)
