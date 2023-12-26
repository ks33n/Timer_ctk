import customtkinter as ctk
import datetime as dt
from PIL import Image, ImageTk
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

from curent_time_frame import CurentTimeFrame
from timer_frame import TimerFrame
from mini_timer import MiniTimer

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.geometry('800x600')
        self.resizable(False, False)
        self.configure(fg_color='#0f0f0f')
        self.title('Timer')
        self.iconbitmap('images/app_logo.ico')
        
        self.squeeze_btn_img = ImageTk.PhotoImage(Image.open('images/squeeze_btn_icon.png'))
        self.start_btn_image = ImageTk.PhotoImage(Image.open('images/start_btn_icon.png'))
        self.pause_btn_image = ImageTk.PhotoImage(Image.open('images/pause_btn_icon.png'))
        self.clear_btn_image = ImageTk.PhotoImage(Image.open('images/clear_btn_icon.png'))
        self.block_timer_img_unloced = ImageTk.PhotoImage(Image.open('images/block_timer_icon(unloced).png'))
        self.block_timer_img_loced = ImageTk.PhotoImage(Image.open('images/block_timer_icon(loced).png'))
        
        self.is_btns_blocked = False
        
        
        self.curent_time_frame = CurentTimeFrame(master=self, width=370, 
                                                 height=250,
                                                 border_color='white',
                                                 border_width=2
                                                 )
        
        self.timer_frame = TimerFrame(master=self, width=370,
                                      height=250,
                                      border_color='white', 
                                      border_width=2,
                                      on_timer_complete=self.block_btns
                                      )
        
        self.start_btn = ctk.CTkButton(master=self, width=240, 
                                       height=58,
                                       fg_color='#046921',
                                       hover_color='#074017', 
                                       text='',
                                       image=self.start_btn_image,  
                                       font=("Cascadia Mono SemiBold", 40), 
                                       command=self.start_timer
                                       )
        
        self.stop_btn = ctk.CTkButton(master=self, width=240,
                                      height=58,
                                      fg_color='#7a3e3e',
                                      hover_color='#4f2d2b',
                                      text='',
                                      image=self.pause_btn_image,
                                      font=("Cascadia Mono SemiBold", 40), 
                                      command=self.stop_timer
                                      )
        
        self.plus_ten_btn = ctk.CTkButton(master=self, width=175,
                                          height=40,
                                          text='+10',
                                          font=("Cascadia Mono SemiBold", 40),
                                          command=lambda: self.update_timer_and_slider(10, plus=True)
                                         )
        
        self.plus_30_btn = ctk.CTkButton(master=self, width=175,
                                          height=40,
                                          text='+30',
                                          font=("Cascadia Mono SemiBold", 40),
                                          command=lambda: self.update_timer_and_slider(30, plus=True)
                                         )
        
        self.minus_ten_btn = ctk.CTkButton(master=self, width=175,
                                          height=40,
                                          fg_color='#7a3e3e',
                                          hover_color='#4f2d2b',
                                          text='-10',
                                          font=("Cascadia Mono SemiBold", 40),
                                          command=lambda: self.update_timer_and_slider(10, minus=True)
                                         ) 
        
        self.minus_30_btn = ctk.CTkButton(master=self, width=175,
                                          height=40,
                                          fg_color='#7a3e3e',
                                          hover_color='#4f2d2b',
                                          text='-30',
                                          font=("Cascadia Mono SemiBold", 40),
                                          command=lambda: self.update_timer_and_slider(30, minus=True)
                                         )
        self.slider = ctk.CTkSlider(master=self, from_=0, to=1440, 
                                    width=700, height=15,
                                    border_width=5, 
                                    command=self.timer_frame.update_timer_from_slider
                                   )
        self.slider.set(0)
        
        
        self.block_timer = ctk.CTkButton(master=self.timer_frame, text='',
                                              image=self.block_timer_img_unloced,
                                              width=48,
                                              height=40,
                                              command=self.block_btns
                                              )
        
        self.squeeze_winbow_btn = ctk.CTkButton(master=self.timer_frame, text='',
                                                    width=48,
                                                    height=40,
                                                    #hover_color='#5e5e5e',
                                                    bg_color='transparent',
                                                    #fg_color='transparent',
                                                    image=self.squeeze_btn_img,
                                                    command=self.squeeze_winbow
                                                    )
        
        self.claer_timer_btn = ctk.CTkButton(master=self, text='',
                                             image=self.clear_btn_image, 
                                             width=240,
                                             height=58,
                                             font=("Cascadia Mono SemiBold", 40),
                                             command=lambda: self.update_timer_and_slider(clear=True)
                                            )
        
        self.curent_time_frame.place(x=20, y=20)
        self.timer_frame.place(x=410, y=20)
        self.start_btn.place(x=540, y=280)
        self.claer_timer_btn.place(x=280, y=280)
        self.stop_btn.place(x=20, y=280)
        self.plus_ten_btn.place(x=20, y=500)
        self.plus_30_btn.place(x=215, y=500)
        self.minus_ten_btn.place(x=410, y=500)
        self.minus_30_btn.place(x=605, y=500)
        self.slider.place(x=50, y=410)
        self.block_timer.place(x=307, y=195)
        self.squeeze_winbow_btn.place(x=15, y=195)
                                      
        
    def start_timer(self):
        if not self.timer_frame.timer_running:
            if self.timer_frame.seconds != 0 or self.timer_frame.minutes != 0 or self.timer_frame.hours != 0:
                self.timer_frame.timer_running = True
                self.timer_frame.update_timer()
        
    def stop_timer(self):
        self.timer_frame.timer_running = False
        
    def update_timer_and_slider(self, minutes=0, plus=False, minus=False, clear=False):
        if plus:
            self.timer_frame.plus_timer(minutes)
            self.slider.set(self.slider.get() + minutes)
        elif minus:
            self.timer_frame.minus_timer(minutes)
            self.slider.set(self.slider.get() - minutes)
        elif clear:
            self.timer_frame.clear_timer()
            self.slider.set(0)
    
    def block_btns(self):
        if self.is_btns_blocked == False and self.timer_frame.timer_running == True:
            self.start_btn.configure(state='disabled')
            self.stop_btn.configure(state='disabled')
            self.plus_ten_btn.configure(state='disabled')
            self.plus_30_btn.configure(state='disabled')
            self.minus_ten_btn.configure(state='disabled')
            self.minus_30_btn.configure(state='disabled')
            self.slider.configure(state='disabled')
            self.block_timer.configure(image=self.block_timer_img_loced, fg_color='#7a3e3e', state='disabled')
            self.is_btns_blocked = True
        elif self.is_btns_blocked == True and self.timer_frame.timer_running == False:
            self.start_btn.configure(state='normal')
            self.stop_btn.configure(state='normal')
            self.plus_ten_btn.configure(state='normal')
            self.plus_30_btn.configure(state='normal')
            self.minus_ten_btn.configure(state='normal')
            self.minus_30_btn.configure(state='normal')
            self.slider.configure(state='normal')
            self.block_timer.configure(image=self.block_timer_img_unloced, fg_color='#1a6096', state='normal')
            self.is_btns_blocked = False
       
    def squeeze_winbow(self):
        self.withdraw()
        self.mini_timer = MiniTimer(master=self, hours=self.timer_frame.hours, 
                                    minutes=self.timer_frame.minutes, 
                                    seconds=self.timer_frame.seconds,
                                    timer_runing=self.timer_frame.timer_running,
                                    )
        
if __name__ == '__main__':
    app = App()
    app.mainloop()
    