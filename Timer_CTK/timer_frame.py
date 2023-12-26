import customtkinter as ctk
import datetime as dt
from plyer import notification


class TimerFrame(ctk.CTkFrame):
    def __init__(self, master, on_timer_complete=None, **kwargs):
        super().__init__(master, **kwargs)
        
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.on_timer_complete = on_timer_complete
        
        self.remaining_time = dt.time(self.hours, self.minutes, self.seconds)
        
        self.timer_running = False
        self.notify = True
        
        self.timer_lable = ctk.CTkLabel(master=self, text=self.remaining_time.strftime("%H:%M:%S"), fg_color='transparent', font=("Cascadia Mono SemiBold", 65))
        self.timer_lable.place(x=33, y=65)
        
        #self.after(1000, self.update_timer)
        
    def update_timer(self):
        if not self.timer_running:
        # Если таймер остановлен, не обновляем время и не вызываем функцию снова
                return

        self.seconds -= 1
        if self.seconds < 0:
            self.minutes -= 1
            self.seconds = 59
            if self.minutes < 0:
                self.hours -= 1
                self.minutes = 59
                if self.hours < 0:
                    # Обнуляем таймер и останавливаем его
                    self.hours = 0
                    self.minutes = 0
                    self.seconds = 0
                    self.timer_running = False
                    self.send_notify()
                    if self.on_timer_complete:
                        self.on_timer_complete()

        self.remaining_time = dt.time(self.hours, self.minutes, self.seconds)
        self.timer_lable.configure(text=self.remaining_time.strftime("%H:%M:%S"))

        if self.timer_running:
        # Планируем следующее обновление только если таймер активен
            self.after(1000, self.update_timer)
            
    def plus_timer(self, minutes_inc):
        if self.minutes + minutes_inc >= 0:
            self.minutes += minutes_inc
            if self.minutes > 59:
                self.hours += 1
                self.minutes = self.minutes % 60
                if self.hours >= 24:
                    self.hours = 23
                    self.minutes = 59
                    
        self.remaining_time = dt.time(self.hours, self.minutes, self.seconds)
        self.timer_lable.configure(text=self.remaining_time.strftime("%H:%M:%S"))  
                    
    def minus_timer(self, minutes_dec):
        if self.minutes - minutes_dec < 0:
            self.minutes = 60 + self.minutes - minutes_dec
            self.hours -= 1
            if self.hours < 0:
                self.hours = 0
                self.minutes = 0
        else:
            self.minutes -= minutes_dec
            
        self.remaining_time = dt.time(self.hours, self.minutes, self.seconds)
        self.timer_lable.configure(text=self.remaining_time.strftime("%H:%M:%S"))    
        
    def update_timer_from_slider(self, slider_value):
        self.hours = int(slider_value / 60)
        self.minutes = int(slider_value % 60)
        if self.hours >= 24:
            self.hours = 23
            self.minutes = 59
            
        self.remaining_time = dt.time(self.hours, self.minutes, self.seconds)
        self.timer_lable.configure(text=self.remaining_time.strftime("%H:%M:%S"))
        
    def clear_timer(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.notifi = False
        self.timer_running = False
        
        self.remaining_time = dt.time(self.hours, self.minutes, self.seconds)
        self.timer_lable.configure(text=self.remaining_time.strftime("%H:%M:%S"))
        
        if self.on_timer_complete:
            self.on_timer_complete()
        
    def send_notify(self):
        if self.notify:
            notification.notify(
                                title='Timer',
                                message='Time is out!',
                                app_name='Timer',
                                app_icon = 'images/app_logo_32x32.ico',
                                timeout = 100
                                )
        self.notify = True
    