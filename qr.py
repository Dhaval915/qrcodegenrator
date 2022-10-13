#---------------Pramukh Tech-------------
#First Install qrcode and tkinter using cmd = pip install qrcode/tkinter

import qrcode
from tkinter import *

cp = Tk()
cp.title('www.youtube.com/pramukhtech')
cp.geometry('700x250')
cp.config(bg='#ADD8E6')

def generate():
    img = qrcode.make(msg.get())
    type(img)
    img.save(f'{save_name.get()}.png')
    Label(cp, text='File Saved!', bg='#ADD8E6' , fg='black', font=('Arial Black', 8)).pack()

def show():
    img = qrcode.make(msg.get())
    type(img)
    img.show()

frame = Frame(cp, bg='#ADD8E6')
frame.pack(expand=True)

#-------------------ENTER THE TEXT OR URL------------------

Label(frame, text='Enter the Text or URL : ', font=('Arial Black', 16),
      bg='#ADD8E6').grid(row=0, column=0, sticky='w')

msg = Entry(frame)
msg.grid(row=0, column=1)

#-------------------ENTER THE FILE NAME------------------

Label(frame, text='File Name(Save As) : ', font=('Arial Black', 16),
      bg='#ADD8E6').grid(row=1, column=0, sticky='w')

save_name = Entry(frame)
save_name.grid(row=1, column=1)

#------------------BUTTONS TO SHOW OR SAVE QRCODE------------------

btn = Button(cp, text='Show QR code', bd='2', command=show, width=15)
btn.pack()

btn = Button(cp, text='Save QR code', command=generate, bd='2', width=15)
btn.pack()
cp.mainloop()