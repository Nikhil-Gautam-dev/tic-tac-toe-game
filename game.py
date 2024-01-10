from numpy import zeros
from random import randint
from tkinter import *
from tkinter import messagebox

'''
    NIKHIL MALHOTRA
    PROJECT: TIC TAC TOE (GUI)


'''


base=zeros((3,3),dtype=str)
keys={1:'.!button',2:'.!button2',3:'.!button3',4:'.!button4',5:'.!button5',6:'.!button6',7:'.!button7',8:'.!button8',9:'.!button9'}

pos={1:(0,0),2:(0,1),3:(0,2),4:(1,0),5:(1,1),6:(1,2),7:(2,0),8:(2,1),9:(2,2)}

rpos={(0,0):1,(0,1):2,(0,2):3,(1,0):4,(1,1):5,(1,2):6,(2,0):7,(2,1):8,(2,2):9}

pl="X"
cpl="O"
w=0
counter=0
check=True

def startgamewithcomputer(player):
    global B1,B2,B3,B4,B5,B6,B7,B8,B9,base,zeros,keys,pos,rpos,pl,cpl,w,counter,root
    if player=="X":
        pl='X'
        cpl='O'
    elif player=="O":
        pl='O'
        cpl='X'

    root=Tk()
    title=Label(root,text="Tic-tac-toe",font=('Arial',15))
    title.grid(row=0,column=0)

    turn=Label(root,text='x-turn',font=('Arial',15))
    turn.grid(row=0,column=2)
    B1=Button(root,text="",font=('Arial',20,'bold'),fg="black",bg="white",width=5,height=2,command=lambda : basevalues(B1))
    B1.grid(row=1,column=0)
    B2=Button(root,text="",font=('Arial',20,'bold'),fg="black",bg="white",width=5,height=2,command=lambda : basevalues(B2))
    B2.grid(row=1,column=1)
    B3=Button(root,text="",font=('Arial',20,'bold'),fg="black",bg="white",width=5,height=2,command=lambda : basevalues(B3))
    B3.grid(row=1,column=2)

    B4=Button(root,text="",font=('Arial',20,'bold'),fg="black",bg="white",width=5,height=2,command=lambda : basevalues(B4))
    B4.grid(row=2,column=0)
    B5=Button(root,text="",font=('Arial',20,'bold'),fg='black',bg='white',width=5,height=2,command=lambda : basevalues(B5))
    B5.grid(row=2,column=1)
    B6=Button(root,text="",font=('Arial',20,'bold'),fg="black",bg="white",width=5,height=2,command=lambda : basevalues(B6))
    B6.grid(row=2,column=2)

    B7=Button(root,text="",font=('Arial',20,'bold'),fg="black",bg="white",width=5,height=2,command=lambda : basevalues(B7))
    B7.grid(row=3,column=0)
    B8=Button(root,text="",font=('Arial',20,'bold'),fg="black",bg="white",width=5,height=2,command=lambda : basevalues(B8))
    B8.grid(row=3,column=1)
    B9=Button(root,text="",font=('Arial',20,'bold'),fg="black",bg="white",width=5,height=2,command=lambda : basevalues(B9))
    B9.grid(row=3,column=2)

    mymenu=Menu(root)
    mymenu.add_command(label="restart",command=restart_with_comp)
    mymenu.add_command(label="quit",command=quit_game)
    mymenu.add_command(label="home",command=home)
    root.config(menu=mymenu)


    root.mainloop()

def basevalues(b):
    global base,keys,pos,rpos,pl,cpl,ls,w,counter
    k=str(b)
    for i in range(1,10):
        x=keys[i]
        if k==x:
            p=pos[i]
            if base[p]==pl or base[p]==cpl:
                messagebox.showerror(message="place already occupied")
                break

            else:
                base[p]=pl
                b['text']=pl
                cv=cvalues(base,pl,cpl)
                if cv=='clear' :
                    for i in range(5):
                        rd=randint(1,9)
                        bv=pos[rd]
                        if base[bv]==pl or base[bv]==cpl:
                            continue
                        else:
                            bk=buttons(rd)
                            base[bv]=cpl
                            bk['text']=cpl
                            break
                elif cv!='clear':
                    if base[cv]==pl or base[cv]==cpl:
                        for i in range(5):
                            rd=randint(1,9)
                            bv=pos[rd]
                            if base[bv]==pl or base[bv]==cpl:
                                continue
                            else:
                                bk=buttons(rd)
                                base[bv]=cpl
                                bk['text']=cpl
                                break
                    else:
                        bv=rpos[cv]
                        bk=buttons(bv)
                        base[cv]=cpl
                        bk['text']=cpl

                win=winner(base,pl,cpl)
                if win!='clear':
                    try:
                        colorchange(win)
                        disablebutton()
                        if colorchange(win)['text']==pl:
                            new_game=messagebox.askyesno(message="You Win!\n Do you Want to play again ?")
                            if new_game==True:
                                try:
                                    restart_with_comp()
                                except:
                                    pass
                            elif new_game==False:
                                quit_game()
                        if colorchange(win)['text']==cpl:
                            new_game=messagebox.askyesno(message="Computer Win!\n Do you Want to play again ?")
                            if new_game:
                                try:
                                    restart_with_comp()
                                except:
                                    pass
                            elif new_game==False:
                                quit_game()

                        break
                    except:
                        pass
                elif win=='clear':
                    counter=counter+1
                    if counter==5 or counter>5:
                        new_game=messagebox.askyesno(message="Draw!\n Do you Want to play again ?")
                        if new_game==True:
                            restart_with_comp()
                        elif new_game==False:
                            quit_game()

                break

def startcustumgame(player):
    global B1,B2,B3,B4,B5,B6,B7,B8,B9,turn,base,zeros,keys,pos,rpos,pl,cpl,w,counter,root2
    if player=="X":
        pl='X'
        cpl='O'
    elif player=="O":
        pl='O'
        cpl='X'

    root2=Tk()
    title=Label(root2,text="Tic-tac-toe",font=('Arial',15))
    title.grid(row=0,column=0)

    turn=Label(root2,text='Player1',font=('Arial',15))
    turn.grid(row=0,column=2)
    B1=Button(root2,text="",font=('Arial',20,'bold'),fg="black",bg="white",width=5,height=2,command=lambda : click(B1))
    B1.grid(row=1,column=0)
    B2=Button(root2,text="",font=('Arial',20,'bold'),fg="black",bg="white",width=5,height=2,command=lambda : click(B2))
    B2.grid(row=1,column=1)
    B3=Button(root2,text="",font=('Arial',20,'bold'),fg="black",bg="white",width=5,height=2,command=lambda : click(B3))
    B3.grid(row=1,column=2)

    B4=Button(root2,text="",font=('Arial',20,'bold'),fg="black",bg="white",width=5,height=2,command=lambda : click(B4))
    B4.grid(row=2,column=0)
    B5=Button(root2,text="",font=('Arial',20,'bold'),fg='black',bg='white',width=5,height=2,command=lambda : click(B5))
    B5.grid(row=2,column=1)
    B6=Button(root2,text="",font=('Arial',20,'bold'),fg="black",bg="white",width=5,height=2,command=lambda : click(B6))
    B6.grid(row=2,column=2)

    B7=Button(root2,text="",font=('Arial',20,'bold'),fg="black",bg="white",width=5,height=2,command=lambda : click(B7))
    B7.grid(row=3,column=0)
    B8=Button(root2,text="",font=('Arial',20,'bold'),fg="black",bg="white",width=5,height=2,command=lambda : click(B8))
    B8.grid(row=3,column=1)
    B9=Button(root2,text="",font=('Arial',20,'bold'),fg="black",bg="white",width=5,height=2,command=lambda : click(B9))
    B9.grid(row=3,column=2)

    mymenu=Menu(root2)
    mymenu.add_command(label="restart",command=restart)
    mymenu.add_command(label="quit",command=quit_custum_game)
    mymenu.add_command(label="home",command=home2)
    root2.config(menu=mymenu)


    root2.mainloop()

def click(b):
    global B1,B2,B3,B4,B5,B6,B7,B8,B9,turn,base,zeros,keys,pos,rpos,pl,cpl,win,counter,check

    str_b=str(b)
    for i in range(1,10):
        get_button=keys[i]
        if str_b==get_button:
            get_coordinate=pos[i]
            if check==True:
                if base[get_coordinate]==pl or base[get_coordinate]==cpl:
                    messagebox.showerror(message='already occupied !')
                    break
                else:
                    base[get_coordinate]=pl
                    b['text']=pl
                    check=False 
                    turn['text']='Player2'
                    
            elif check==False:
                if base[get_coordinate]==pl or base[get_coordinate]==cpl:
                    messagebox.showerror(message='already occupied !')
                    break
                else:
                    base[get_coordinate]=cpl
                    b['text']=cpl
                    check=True
                    turn['text']='Player1'
            win=winner(base,pl,cpl)
            if win=='clear':
                counter=counter+1
                if counter==9 or counter>9:
                    new_game=messagebox.askyesno(message='Draw ! \n do want to play agian')
                    if new_game==True:
                        restart()
                    elif new_game==False:
                        quit_custum_game()
                    break
            elif win!='clear':
                winner_button=colorchange(win)
                disablebutton()
                if winner_button['text']==pl:
                    turn['text']='Player1'
                    new_game=messagebox.askyesno(message='Player1 win\n Do you want play again')
                elif winner_button['text']==cpl:
                    turn['text']='Player2'
                    new_game=messagebox.askyesno(message='Player2 win\n Do you want play again')
                if new_game==True:
                    restart()
                elif new_game==False:
                    quit_custum_game()
                
            break


def checker(arr):
    i=1 
    while i<2:
        if arr[0]==arr[1]:
            if arr[0]=='':
                pass
            else:
                return 2
        elif arr[0]==arr[2]:
            if arr[0]=='':
                pass
            else:
                return 1
        elif arr[1]==arr[2]:
            if arr[1]=='':
                pass
            else:
                return 0
        else:
            break
        i=i+1
    return 'True'

def buttons(val):
    global B1,B2,B3,B4,B5,B6,B7,B8,B9
    ls=[B1,B2,B3,B4,B5,B6,B7,B8,B9]
    try:
        x=int(val)-1
        return ls[x]
    except:
        pass
def cvalues(base,pl,cpl):
    cq='True'
    for i in range(0,3):
        arr=list(base[i])
        v=checker(arr)
        if v==cq:
            continue
        elif base[i,v]==pl or base[i,v]==cpl:
            continue
        else:
            return (i,v)
            

    for i in range(0,3):
        arr=list(base[:,i])
        v=checker(arr)
        if v==cq:
            continue
        elif base[v,i]==pl or base[v,i]==cpl:
            continue
        else:
            return (v,i)
    
    d1=[base[0,0],base[1,1],base[2,2]]
    d2=[base[0,2],base[1,1],base[2,0]]

    for i in range(0,1):
        v=checker(d1)
        if v==cq:
            break
        elif v==pl or v==cpl:
            break
        else:
            if v==0:
                return (0,0)
            elif v==1:
                return (1,1)
            elif v==2:
                return (2,2)

    for i in range(0,1):
        v=checker(d2)
        if v==cq:
            break
        elif v==pl or v==cpl:
            break
        else:
            if v==0:
                return (0,2)
            elif v==1:
                return (1,1)
            elif v==2:
                return (2,0)

    return "clear"

def winner(base,pl,cpl):
    for i in range(0,3):
        arr=list(base[i])
        l=len(arr)
        e=arr[0]
        if arr.count(e)==l:
            if e=='' or e== None:
                continue
            else:
                return (1,i) 

    for i in range(0,3):
        arr=list(base[:,i])
        l=len(arr)
        e=arr[0]
        if arr.count(e)==l:
            if e=='' or e== None:
                continue
            else:
                return (2,i) 

    d1=[base[0,0],base[1,1],base[2,2]]
    d2=[base[0,2],base[1,1],base[2,0]]
    for i in range(1):
        if d1.count(d1[0])==3:
            if d1[0]=='' or d1[0]==None:
                continue
            else:
                return (3)
    for i in range(1):
        if d2.count(d2[0])==3:
            if d2[0]=='' or d2[0]==None:
                continue
            else:
                return (4)
    return 'clear'
    
def colorchange(win):
    global B1,B2,B3,B4,B5,B6,B7,B8,B9
    if win==(1,0):
        B1.config(fg='red',bg='red')
        B2.config(fg='red',bg='red')
        B3.config(fg='red',bg='red')
        return B1
    elif win==(1,1):
        B4.config(fg='red',bg='red')
        B5.config(fg='red',bg='red')
        B6.config(fg='red',bg='red')
        return B4
    elif win==(1,2):
        B7.config(fg='red',bg='red')
        B8.config(fg='red',bg='red')
        B9.config(fg='red',bg='red')
        return B7

    elif win==(2,0):
        B1.config(fg='red',bg='red')
        B4.config(fg='red',bg='red')
        B7.config(fg='red',bg='red')
        return B1
    elif win==(2,1):
        B2.config(fg='red',bg='red')
        B5.config(fg='red',bg='red')
        B8.config(fg='red',bg='red')
        return B2
    elif win==(2,2):
        B3.config(fg='red',bg='red')
        B6.config(fg='red',bg='red')
        B9.config(fg='red',bg='red')
        return B9

    elif win==(3):
        B1.config(fg='red',bg='red')
        B5.config(fg='red',bg='red')
        B9.config(fg='red',bg='red')
        return B9
    elif win==(4):
        B3.config(fg='red',bg='red')
        B5.config(fg='red',bg='red')
        B7.config(fg='red',bg='red')
        return B7

def disablebutton():
    global B1,B2,B3,B4,B5,B6,B7,B8,B9
    B1.config(state=DISABLED)
    B2.config(state=DISABLED)
    B3.config(state=DISABLED)
    B4.config(state=DISABLED)
    B5.config(state=DISABLED)
    B6.config(state=DISABLED)
    B7.config(state=DISABLED)
    B8.config(state=DISABLED)
    B9.config(state=DISABLED)


def restart():
    global B1,B2,B3,B4,B5,B6,B7,B8,B9,base,w,counter,turn,check
    ls=[B1,B2,B3,B4,B5,B6,B7,B8,B9]
    w=0
    counter=0
    turn['text']='Player1'
    check=True
    for button in ls:
        button.config(text="",state=ACTIVE,fg='black',bg='white')

    for i in range(0,3):
        for j in range(0,3):
            base[i,j]=''

def restart_with_comp():
    global B1,B2,B3,B4,B5,B6,B7,B8,B9,base,w,counter
    ls=[B1,B2,B3,B4,B5,B6,B7,B8,B9]
    w=0
    counter=0
    for button in ls:
        button.config(text="",state=ACTIVE,fg='black',bg='white')

    for i in range(0,3):
        for j in range(0,3):
            base[i,j]=''


def xclick():
    window.destroy()
    startcustumgame('X')

def yclick():
    window.destroy()
    x=startgamewithcomputer('X')

def main():
    global window
    window=Tk()
    window.geometry('288x293')
    window.config(bg='#73a580')
    title=Label(window,text='Tic-tac toe',font=('Arial',30,'bold'),fg='black',bg='#73a580')

    title.pack(anchor=CENTER,pady=10)

    choose=Label(window,text='Choose your player',font=('Arial',10,'bold'),bg='#73a580')
    choose.place(relx=0.5,rely=0.3,anchor=CENTER)

    X=Button(window,text='Custom',font=('Arial',10,'bold'),command=xclick)
    X.place(relx=0.5,rely=0.5,anchor=CENTER,width=120,height=40)

    y=Button(window,text='With computer',font=('Arial',10,'bold'),command=yclick)
    y.place(relx=0.5,rely=0.7,anchor=CENTER,width=120,height=40)

    quitbutton=Button(window,text='quit',font=('Arial',10,'bold'),command=quit)
    quitbutton.place(relx=0.5,rely=0.9,anchor=CENTER,width=120,height=40)

    window.mainloop()


def home():
    root.destroy()
    main()
def home2():
    root2.destroy()
    main()

def quit_game():
    root.destroy()

def quit_custum_game():
    root2.destroy()
main()



