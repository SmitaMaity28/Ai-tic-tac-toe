from tkinter import *
from tkinter import messagebox
import random
import time

p1=""
root = Tk()
root.title('Tic-Tac-Toe')
check=[]
winner=False
clicked = True
count = 0
turn=0
ai=1
player = 'X'
bot = 'O'
def  disable_all_buttons():
    
    root.quit()
def cdrow():
    for key in board.keys():
        if (board[key] == ' '):
            return False
    return True
    
# def randomizer():
    
#     while TRUE:
#         nuv=random.randint(1,9)
#         if not nuv in check:
#             break
#     return nuv       
def winch(mark):
    if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False
def compMove():
    bscor = -800
    bmov = 0
    for key in board.keys():
        if (board[key] == ' '):
            board[key] = bot
            score = minimax(board, 0, False)
            board[key] = ' '
            if (score > bscor):
                bscor = score
                bmov = key
    return bmov           
def minimax(board, depth, isMaximizing):
    if (winch(bot)):
        return 1
    elif (winch(player)):
        return -1
    elif (cdrow()):
        return 0

    if (isMaximizing):
        bscor = -800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = bot
                score = minimax(board, depth + 1, False)
                board[key] = ' '
                if (score > bscor):
                    bscor = score
        return bscor

    else:
        bscor = 800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                if (score < bscor):
                    bscor = score
        
        return bscor
def comp():
    # time.sleep(2)
    but=compMove()
       
    if(but==1):
        b_click(b1,1)
    elif(but==2):
        b_click(b2,2)
    elif(but==3):
        b_click(b3,3)
    elif(but==4):
        b_click(b4,4)
    elif(but==5):
        b_click(b5,5)
    elif(but==6):
        b_click(b6,6)
    elif(but==7):
        b_click(b7,7)
    elif(but==8):
        b_click(b8,8)
    elif(but==9):
        b_click(b9,9)
             


    
def checkifwon():
    
    
    winnner =False
    p1=name1_var.get()+" win"
    # print(ai)
    if ai==1:
        p2="COMPUTER WIN"
    elif ai==0:    
        p2=name2_var.get()+" win"
    if b1["text"] =="X" and b2["text"] =="X" and  b3["text"] =="X":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner = True
        messagebox.showinfo("result",p1)
        
        disable_all_buttons()

        
    elif b4["text"] =="X" and b5["text"] =="X" and  b6["text"] =="X":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner = True
        messagebox.showinfo("result",p1)
        
        disable_all_buttons()

        
    elif b7["text"] =="X" and b8["text"] =="X" and  b9["text"] =="X":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("result",p1)
        
        disable_all_buttons()

        
    elif b1["text"] =="X" and b4["text"] =="X" and  b7["text"] =="X":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("result",p1)
        
        disable_all_buttons()

    
    elif b2["text"] =="X" and b5["text"] =="X" and  b8["text"] =="X":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner = True
        messagebox.showinfo("result",p1)
        
        disable_all_buttons()

    
    elif b3["text"] =="X" and b6["text"] =="X" and  b9["text"] =="X":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("result",p1)
        
        disable_all_buttons()

    
    elif b1["text"] =="X" and b5["text"] =="X" and  b9["text"] =="X":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("result",p1)
        
        disable_all_buttons()

    
    elif b3["text"] =="X" and b5["text"] =="X" and  b7["text"] =="X":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("result",p1)
        
        disable_all_buttons()

    
    
    
    elif b4["text"] =="O" and b5["text"] =="O" and  b6["text"] =="O":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner = True
        messagebox.showinfo("result",p2)
        
        disable_all_buttons()

        
    elif b7["text"] =="O" and b8["text"] =="O" and  b9["text"] =="O":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("result",p2)
        
        disable_all_buttons()

        
    elif b1["text"] =="O" and b4["text"] =="O" and  b7["text"] =="O":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("result",p2)
        
        disable_all_buttons()

    
    elif b2["text"] =="O" and b5["text"] =="O" and  b8["text"] =="O":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner = True
        messagebox.showinfo("result",p2)
        
        disable_all_buttons()

    
    elif b3["text"] =="O" and b6["text"] =="O" and  b9["text"] =="O":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("result",p2)
        disable_all_buttons()
    
    elif b1["text"] =="O" and b5["text"] =="O" and  b9["text"] =="O":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("result",p2)
        
        disable_all_buttons()

    
    elif b3["text"] =="O" and b5["text"] =="O" and  b7["text"] =="O":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner=True
        messagebox.showinfo("result",p2)
        
        disable_all_buttons()
    elif(count==9):
        draw()
    elif(count%2!=0 and ai==1):
        comp()    
        

def draw():
    messagebox.showinfo("result","match draw")
    disable_all_buttons()
    
board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}


def b_click(b,num):
    global clicked, count
    checks=[]
    check.append(num)
    
    if b["text"] ==" " and clicked == True:
        b["text"] ="X"
        board[num] ="X"
        clicked = False
        count +=1
        checkifwon()
        
    elif b["text"] ==" " and clicked == False:
        b["text"] ="O"
        board[num] ="O"
        clicked = True
        count +=1
        checkifwon()
        
    else:
        messagebox.showerror("Tic tac toe ","hey! thatbox is already been selected \npick another box.....")
        
    
        
    
    

        
      
              
f = Frame(root, height=400, width=400, bg="yellow")  
f.propagate(0)
f.pack()     
# f1 = Frame(root, height=800, width=800, bg="yellow")       
b1 = Button(f,text=" ", font=("heleveltica",20),height=3, width=6,bg="Blue",command=lambda: b_click(b1,1))
b2 = Button(f,text=" ", font=("heleveltica",20),height=3, width=6,bg="Blue",command=lambda: b_click(b2,2))
b3 = Button(f,text=" ", font=("heleveltica",20),height=3, width=6,bg="Blue",command=lambda: b_click(b3,3))
b4 = Button(f,text=" ", font=("heleveltica",20),height=3, width=6,bg="Blue",command=lambda: b_click(b4,4))
b5 = Button(f,text=" ", font=("heleveltica",20),height=3, width=6,bg="Blue",command=lambda: b_click(b5,5))
b6 = Button(f,text=" ", font=("heleveltica",20),height=3, width=6,bg="Blue",command=lambda: b_click(b6,6))
b7 = Button(f,text=" ", font=("heleveltica",20),height=3, width=6,bg="Blue",command=lambda: b_click(b7,7))
b8 = Button(f,text=" ", font=("heleveltica",20),height=3, width=6,bg="Blue",command=lambda: b_click(b8,8))
b9 = Button(f,text=" ", font=("heleveltica",20),height=3, width=6,bg="Blue",command=lambda: b_click(b9,9))
# f1.pack()
l1 = Label(f, text="PLAYER1 NAME")
l2 = Label(f, text="PLAYER2 NAME")
# l1.place(x=50, y=150)
# l2.place(x=50, y=200)
name1_var = StringVar()
name2_var = StringVar()

e1 = Entry(f, width=20, fg="yellow",bg="grey", textvariable=name1_var,font=("Arial,15"))
e2 = Entry(f, width=20, fg="yellow",bg="grey",textvariable=name2_var ,font=("Arial,15"))
# e1.place(x=200, y=150)
# e2.place(x=200, y=200)
bx = Button(f,text="START THE GAME ", font=("heleveltica",10),height=2, width=15,bg="Blue",command=lambda: pak())
# bx.place(x=200,y=250)
# p1=name1_var.get()
# print(p1)
# print(name1_var.get())
# p2=name2_var.get()
bn = Button(f,text="MULTIPLAYER", font=("heleveltica",10),height=2, width=15,bg="Blue",command=lambda: multi())
bn2 = Button(f,text="WITH_COMPUTER", font=("heleveltica",10),height=2, width=15,bg="Blue",command=lambda: sing())
bn.place(x=50,y=170)
bn2.place(x=220,y=170)

def multi():
    bn.destroy()
    bn2.destroy()
    global ai
    ai=ai-1
    e1.place(x=200, y=150)
    e2.place(x=200, y=200)
    l1.place(x=50, y=150)
    l2.place(x=50, y=200)
    bx.place(x=200,y=250)
def sing():
    bn.destroy()
    bn2.destroy()
    e1.place(x=200, y=150)
    # e2.place(x=200, y=200)
    l1.place(x=50, y=150)
    # l2.place(x=50, y=200)
    bx.place(x=200,y=250)
    


def pak():
    l1.destroy()
    l2.destroy()
    e1.destroy()
    e2.destroy()
    bx.destroy()
    # f.pack()
    b1.grid(row=0,column=0)
    b2.grid(row=0,column=1)
    b3.grid(row=0,column=2)

    b4.grid(row=1,column=0)
    b5.grid(row=1,column=1)
    b6.grid(row=1,column=2)

    b7.grid(row=2,column=0)
    b8.grid(row=2,column=1)
    b9.grid(row=2,column=2)
    

root.mainloop()