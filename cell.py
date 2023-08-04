
from tkinter import Button,Label, font
import random
from tkinter.constants import RAISED, SUNKEN
import settings
from tkinter import messagebox
import tkinter
import os





class cell:
    all=[]
    cell_left=settings.cell_left
    mines_count=settings.mines_count
    mines_left=settings.mines_count


    def __init__(self,x,y,is_mine=False):      #constuctor 
        self.is_mine=is_mine
        self.x=x
        self.y=y
        self.btn=None
        self.cell_count=None
        self.is_open=False
        self.is_marked=False
        self.mine_counter=None
        
        cell.all.append(self)
        
        

    def creat_btn(self,location):
        btn=Button(location,width=6,height=1)
        btn.bind('<Button-1>',self.left_click_action)            #bind function to creat action to the button  
        btn.bind('<Button-3>',self.right_click_action)              #bind function to creat action to the button  
        self.btn=btn

    @staticmethod
    def cell_left_count(location):
        lbl=Label(location,text=f"Cells Left:{cell.cell_left}",bg='silver',fg='black',font=("",20))
        cell.cell_count=lbl



    @staticmethod
    def mine_left_count(location):
        lbl1=Label(location,text=f"Cells Left:{cell.mines_left}",bg='silver',fg='black',font=("",20))
        cell.mine_counter=lbl1

    







    def left_click_action(self,event):          # event needs 2 parameter at least 
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_mines_number == 0:
                for not_bomb_surr_cels in self.surrounded_cells:
                    not_bomb_surr_cels.show_num()
            self.show_num()

        self.btn.unbind('<Button-1>')
        self.btn.unbind('<Button-3>')
        if self.cell_left ==0:
            messagebox.askyesnocancel(title='Boooooom',message='You won the Game')

    def get_cell_by_axis(self,x,y):
        for cel in cell.all:
            if cel.x==x and cel.y==y:
                return cel
    @property
    def surrounded_cells(self):
        surroundin_cells_list=[
            self.get_cell_by_axis(self.x -1,self.y -1),
            self.get_cell_by_axis(self.x -1,self.y),
            self.get_cell_by_axis(self.x -1,self.y +1),
            self.get_cell_by_axis(self.x,self.y -1),
            self.get_cell_by_axis(self.x+1,self.y-1),
            self.get_cell_by_axis(self.x+1,self.y),
            self.get_cell_by_axis(self.x+1,self.y+1),
            self.get_cell_by_axis(self.x,self.y+1)
                                                     ]

        surroundin_cells_list=[celll for celll in surroundin_cells_list if celll is not None]
        return surroundin_cells_list
        

    @property
    def surrounded_mines_number(self):
        mine_count=0
        for i in self.surrounded_cells:
            if i.is_mine:
                mine_count=mine_count+1
        return mine_count




    def show_num(self):
        if not self.is_open:
            cell.cell_left=cell.cell_left-1
            self.btn.configure(text=self.surrounded_mines_number,fg='green')
            # changing the left cells counter after every show num call
            if cell.cell_count:
                cell.cell_count.configure(text=f"Cells Left:{cell.cell_left}")
                self.is_open=True
                self.btn.configure(bg='SystemButtonFace')

        


    
    
    def show_mine(self):
        self.btn.configure(bg='red')
        user=messagebox.showinfo(title='Boooooom',message='You lost the game')
        for gg in cell.all:
            gg.btn.unbind('<Button-1>')
            gg.btn.unbind('<Button-3>')
            gg.btn.configure(bg='red')
        


    def right_click_action(self,event):          # event needs 2 parameter at leaset
        if not self.is_marked:
            self.btn.configure(bg='orange')
            self.is_marked=True
            cell.mines_left=cell.mines_left -1
            cell.mine_counter.configure(text=f"Cells Left:{cell.mines_left}")
        
            
        else:
            self.btn.configure(bg='SystemButtonFace')
            self.is_marked=False
            cell.mines_left=cell.mines_left +1
            cell.mine_counter.configure(text=f"Cells Left:{cell.mines_left}")
            
            
            
    @staticmethod
    def random_mine():
        mine_cells=random.sample(cell.all,settings.mines_count)
        for i in mine_cells:
            i.is_mine=True
           
            
    

    def __repr__(self):
        return f"cell({self.x},{self.y})"
    