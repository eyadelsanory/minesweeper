from tkinter import *
from tkinter import messagebox
from cell import cell
import settings
import sizefunc
import tkinter
import os

#-----------------------window setting-----------------------
root=Tk()
root.configure(bg='whitesmoke')
root.title('NU MineSweaper')
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.resizable(False,False)
#-----------------------window setting-----------------------

#---------------------------frames--------------------------------
top_frame=Frame(root,width=sizefunc.wi(100),height=sizefunc.hi(15),bg='black')
top_frame.place(x=0,y=0)

left_frame=Frame(root,width=sizefunc.wi(25),height=sizefunc.hi(85),bg='silver')
left_frame.place(x=0,y=sizefunc.hi(15))

game_frame=Frame(root,width=sizefunc.wi(71),height=sizefunc.hi(80),bg='skyblue')
game_frame.place(x=sizefunc.wi(27),y=sizefunc.hi(17))
#---------------------------frames-----------------------------------
#--------------------------cell class object-------------------------
for x in range (settings.col):
    for y in range (settings.row):
        c=cell(x,y)
        c.creat_btn(game_frame)
        c.btn.grid(row=y,column=x)
        
cell.random_mine()

cell.cell_left_count(left_frame)
cell.cell_count.place(x=0,y=10)

cell.mine_left_count(left_frame)
cell.mine_counter.place(x=0,y=60)


    
def restart():
    root.destroy()
    os.startfile("C:\\Users\\PF\\Desktop\\minesweaper proj\\root.pyw")

def about_us_fun():
    messagebox.showinfo(message='EYAD ESSAM ELSNORY ')

    
restartbtn=Button(left_frame,bg='skyblue',width=12,height=2,text='restart game',font=('MV Boli',17,'bold'),command=restart)
restartbtn.place(x=0,y=120)

name=Label(top_frame,text='NU MINESWEAPER',font=('Showcard Gothic',12,'bold'),fg='white',bg='black')
name.place(x=50,y=20)


about_us=Button(left_frame,bg='skyblue',width=12,height=2,text='About us',font=('MV Boli',17,'bold'),command=about_us_fun)
about_us.place(x=0,y=280)

exit_btn=Button(left_frame,bg='skyblue',width=12,height=2,text='Exit Game',font=('MV Boli',17,'bold'),command=root.quit)
exit_btn.place(x=0,y=500)









root.mainloop()
    



