import customtkinter as ctk
from PIL import Image, ImageTk, Image
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

from mini_timer_frame import MiniTimerFrame

class MiniTimer(ctk.CTkToplevel):
    def __init__(self, hours=0, minutes=0, seconds=0, timer_runing=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.geometry('300x65')
        self.resizable(False, False)
        self.title('Timer')
        self.configure(fg_color='#0f0f0f')
        #self.overrideredirect(True) 
        
        self.is_override = False
        self.facten_btn_image = ImageTk.PhotoImage(Image.open('images/fasten_btn_icon.png'))
        self.expand_btn_image = ImageTk.PhotoImage(Image.open('images/expand_btn_icon.png'))
        
        self.mimi_timer = MiniTimerFrame(master=self, width=165,
                                     height=45,
                                     border_color='white',
                                     border_width=2,
                                     hours=hours,
                                     minutes=minutes,
                                     seconds=seconds,
                                     timer_runing=timer_runing
                                     )
        
        self.expand_win_btn = ctk.CTkButton(master=self, width=48,
                                            height=45,
                                            text='',
                                            image=self.expand_btn_image,
                                            command=self.expand_win
                                            )
        
        self.fasten_win_btn = ctk.CTkButton(master=self, width=48,
                                            height=45,
                                            text='',
                                            image=self.facten_btn_image,
                                            command=self.fasten_win,
                                            ) 
        
        self.mimi_timer.place(x=68, y=10)
        self.expand_win_btn.place(x=242, y=10)
        self.fasten_win_btn.place(x=10, y=10)
        
        
    def expand_win(self):
        self.master.deiconify()
        self.withdraw()
        
    def fasten_win(self):
        if self.is_override:
            self.overrideredirect(False)
            self.attributes('-topmost', False)
            self.is_override = False
        elif not self.is_override:
            self.overrideredirect(True)
            self.attributes('-topmost', True)
            self.is_override = True