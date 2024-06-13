import tkinter
import tkinter as tk
from tkinter import *
import tkinter.ttk
import os
# Horrible code by Devyat, I will let these #texts bacause can help noobs like me :)

# Whatever you want for the START button
def script_start():
    print('do something')


# Create a event for the title bar to move, later bind in mouse click.
def move_window(event):
    gui.geometry('+{0}+{1}'.format(event.x_root, event.y_root))

# Active background and foreground(text).
class HoverButton(tk.Button):
    def __init__(self, master, **kw):
        tk.Button.__init__(self,master=master,**kw)
        self.defaultBackground = self["background"]
        self.defaultForeground = self["foreground"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        
    def on_enter(self, e):
        self['background'] = self['activebackground']
        self['foreground'] = self['activeforeground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground
        self['foreground'] = self.defaultForeground

class Interface(Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        self.pack(fill = BOTH, expand = 1)
        self.interface()
        
    def start_move_window(self, event):
        self.x = event.x
        self.y = event.y
        
    def stop_move_window(self, event):
        self.x = None
        self.y = None
        
    def moving_window(self, event):
        x = (event.x_root - self.x - self.gui_title_bar.winfo_rootx() + self.gui_title_bar.winfo_rootx())
        y = (event.y_root - self.y - self.gui_title_bar.winfo_rooty() + self.gui_title_bar.winfo_rooty())
        gui.geometry("+%s+%s" % (x, y))
        
    def frame_mapped(self, event):
        gui.update_idletasks()
        gui.overrideredirect(True)
        gui.state('normal')
    
    def minimize(self, event=None):
        gui.update_idletasks()
        gui.overrideredirect(False)
        gui.state('iconic')
    
    def close_app(self):
        os._exit(0)
    def interface(self):
        # Make a frame for the title bar.
        self.gui_title_bar = Frame(gui, bg='#2e2e2e', relief='flat', bd=0, highlightthickness=0, highlightbackground='#2e2e2e')
        
        # Put a close button on the title bar
        self.gui_close_button = HoverButton(self.gui_title_bar, text='X', command=self.close_app, bg="#2e2e2e", padx=2, pady=2, activebackground='red', activeforeground='white', bd=0, font="bold", fg='white', highlightthickness=0)
        self.gui_minimize_button = HoverButton(self.gui_title_bar, text='‒', command=self.minimize, bg='#2e2e2e', activebackground='#bbc1b9', activeforeground='black', bd=0, font="bold", fg="white", highlightthickness=0)

        # Pack the widgets
        self.gui_title_bar.pack(side=TOP, fill=X)
        self.gui_title_bar.pack_propagate(True)
        #self.gui_title_bar.pack(expand=1, fill=X)
        self.gui_close_button.pack(side=RIGHT)
        self.gui_minimize_button.pack(side=RIGHT)
        
        # A canvas for the main area of the window
        self.gui_window = Canvas(gui, bg='#1c1c1c', relief='flat', highlightthickness=0, bd=0,)
        self.gui_window.pack(expand=1, fill=BOTH)

        # Inside gui_window, fill with what you want
        self.gui_window_text = Label(self.gui_window, text="Definity bad code and englishu", bg='#1c1c1c', fg='white')
        self.gui_window_text.place(y=50, x=30)
        self.gui_window_text2 = Label(self.gui_window, text="if works dont ask how, accept and continue coding :3", bg='#1c1c1c', fg='white')
        self.gui_window_text2.place(y=90, x=30)
        self.gui_window_credit = Label(self.gui_window, text="By Devyat", bg='#1c1c1c', fg='white')
        self.gui_window_credit.place(y=247, x=342)

        # Button 1 - important stuff in sequence : text, text color, background color and text color change on mouse hover , command=will do something 
        self.button_start = HoverButton(self.gui_window, text="Start", fg='white', bg='#373737', activebackground='#bbc1b9', activeforeground='black', command=script_start, height=3, width=12, borderwidth=0)
        self.button_start.place(y=210, x=90)

        # Button 2 - 
        self.button_cancel = HoverButton(self.gui_window, text="Close", fg='white', bg='#373737', activeforeground='black', activebackground='red', command=gui.destroy, height=3, width=12, borderwidth=0)
        self.button_cancel.place(y=210, x=200)
        
        # Bind moving gui_title_bar
        self.gui_title_bar.bind("<Button-1>", self.start_move_window)
        self.gui_title_bar.bind("<ButtonRelease-1>", self.stop_move_window)
        self.gui_title_bar.bind("<B1-Motion>", self.moving_window)
        self.gui_title_bar.bind("<Map>", self.frame_mapped)

gui = tk.Tk()
gui.overrideredirect(True) # Turns off title bar and geometry for a custom one.
gui.geometry('400x300+10+10') # Sizes ("widthXheight").
gui.configure(background='#1c1c1c') # Fixes white color below title bar, need be SAME color as gui_window.
app = Interface(gui)
gui.mainloop()