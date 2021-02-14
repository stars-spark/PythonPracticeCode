# Countdown using Tkinter 
from tkinter import *
import time
import tkinter.messagebox
  
class App:
 def __init__(self,master):
  frame = Frame(master)
  frame.pack()
  self.entryWidget = Entry(frame)
  self.entryWidget["width"] = 15
  self.entryWidget.pack(side=LEFT)
  self.hi_there = Button(frame, text="开始", command=self.start)
  self.hi_there.pack(side=LEFT)
  self.button = Button(frame, text="退出", fg="red", command=frame.quit)
  self.button.pack(side=LEFT)
   
 def start(self):
  text = self.entryWidget.get().strip()
  if text != "":
   num = int(text)
   self.countDown(num)
   
 def countDown(self,seconds):
  lbl1.config(bg='yellow')
  lbl1.config(height=3, font=('times', 20, 'bold'))
  for k in range(seconds, 0, -1):
   if k == 30:
    print("\a")
   if k== 29:
    print("\a")
   if k== 28:
    print("\a")
   lbl1["text"] = k
   root.update()
   time.sleep(1)
  lbl1.config(bg='red')
  lbl1.config(fg='white')
  lbl1["text"] = "时间到！"
  tkMessageBox.showinfo("时间到！","时间到！")
  
 def GetSource():
  get_window = Tkinter.Toplevel(root)
  get_window.title('Source File?')
  Tkinter.Entry(get_window, width=30,
      textvariable=source).pack()
  Tkinter.Button(get_window, text="Change",
      command=lambda: update_specs()).pack()
  
root = Tk()
root.title("Countdown")
lbl1 = Label()
lbl1.pack(fill=BOTH, expand=1)
app = App(root)
root.mainloop()