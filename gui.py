import tkinter
import tkinter as tk
from tkinter import *
import tkinter.ttk
# Horrible code by Devyat, I will let these #texts bacause can help noobs like me :)

gui = tk.Tk()
gui.overrideredirect(True) # Turns off title bar and geometry for a custom one.
gui.geometry('400x300+10+10') # Sizes ("widthXheight").
gui.configure(background='#1c1c1c') # Fixes white color below title bar, need be SAME color as gui_window.

# Create a event for the title bar to move, later bind in mouse click.
def move_window(event):
    gui.geometry('+{0}+{1}'.format(event.x_root, event.y_root))

# Active background and foreground(text).
class hoverbutton(tk.Button):
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

# Whatever you want for the START button
def script_start():
    print('do something')

# Make a frame for the title bar.
gui_title_bar = Frame(gui, bg='#2e2e2e', relief='flat', bd=2,highlightthickness=0)

# Put a close button on the title bar
gui_close_button = hoverbutton(gui_title_bar, text='X', command= gui.destroy,bg = "#2e2e2e",padx = 2,pady = 2,activebackground='red',activeforeground='white',bd = 0,font="bold",fg='white',highlightthickness=0)

# A canvas for the main area of the window
gui_window = Canvas(gui, bg='#1c1c1c',highlightthickness=0)

# Pack the widgets
gui_title_bar.pack(expand=1, fill=X)
gui_close_button.pack(side=RIGHT)
gui_window.pack(expand=1,fill=BOTH)
xwin=None
ywin=None

# Inside gui_window, fill with what you want
gui_window_text = Label(gui_window, text="Definity bad code and englishu")
gui_window_text.place(y=50, x=30)
gui_window_text2 = Label(gui_window, text="if works dont ask how, accept and continue codding :3")
gui_window_text2.place(y=90, x=30)
gui_window_credit = Label(gui_window, text="By Devyat")
gui_window_credit.place(y=247, x=342)


# Button 1 - important stuff in sequence : text, text color, background color and text color change on mouse hover , command=will do something 
button_start= hoverbutton(gui_window, text="Start",fg='white',bg='#373737',activebackground='#bbc1b9', activeforeground='black', command=script_start, height= 3, width=12, borderwidth=0)
button_start.place(y=210, x=90)

# Button 2 - 
button_cancel = hoverbutton(gui_window, text="Close", fg='white', bg='#373737', activeforeground='black', activebackground='red', command=gui.destroy, height= 3, width=12, borderwidth=0)
button_cancel.place(y=210, x=200)
    
gui_title_bar.bind('<B1-Motion>', move_window) # Remenber the event on the start :)
gui.mainloop()