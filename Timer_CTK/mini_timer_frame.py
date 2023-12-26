import customtkinter as ctk
import datetime as dt

class MiniTimerFrame(ctk.CTkFrame):
    def __init__(self, master, hours, minutes, seconds, timer_runing, **kwargs):
        super().__init__(master, **kwargs)
        
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        
        self.remaining_time = dt.time(self.hours, self.minutes, self.seconds)
        
        self.timer_running = timer_runing
        
        self.timer_lable = ctk.CTkLabel(master=self, text=self.remaining_time.strftime("%H:%M:%S"), fg_color='transparent', font=("Cascadia Mono SemiBold", 30))
        self.timer_lable.place(x=10, y=2)
        
        self.after(1000, self.update_timer)
        
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
    

        self.remaining_time = dt.time(self.hours, self.minutes, self.seconds)
        self.timer_lable.configure(text=self.remaining_time.strftime("%H:%M:%S"))

        if self.timer_running:
        # Планируем следующее обновление только если таймер активен
            self.after(1000, self.update_timer)