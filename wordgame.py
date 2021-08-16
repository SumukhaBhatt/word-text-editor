file="no"
def under():
    return(tx.index(INSERT))
def search(replace):
    def de(event):
        tx.tag_delete("wr")
    def yes1(replace):
        count=0
        sw=value.get()
        w=tx.get(0.0,END).split("\n")
        if replace:
            jk=(len(sw)-len(value1.get()))
        l=0
        for i in w :
            jkk=0
            l+=1
            k=0;
            for j in i:
                if j==sw[0] and i[k:k+len(sw):]==sw:
                    vv=str(l)+'.'+str(k-jkk)
                    vv1=str(l)+'.'+str(k+len(sw)-jkk)
                    if replace:
                        tx.delete(vv,vv1)
                        tx.insert(vv,value1.get())
                        jkk=jkk+jk
                    else:
                        tx.tag_add("wr", vv, vv1)
                        tx.tag_config("wr",background="orange")
                    count+=1
                k=k+1
        if(count):
            lb=Label(su1,text=str(count)+" Matching is found",).pack()
        else:
            lb=Label(su1,text="No matching is found",).pack()
    tx.bind('<Double-1>',de)
    su1=Toplevel(word)
    su1.title("Find")
    value=Entry(su1,)
    value.pack()
    if replace:
        value1=Entry(su1,)
        value1.pack()
        root1.title("Replace")
    b3=Button(su1,text="search",command=lambda :yes1(replace))
    b3.pack(side=RIGHT)
    if replace:
        b3.config(text="Replace")
def upper(lw):
    try:
        a=tx.get("sel.first","sel.last").split("\n")
        tx.delete("sel.first","sel.last")
        for i in a:
            if lw==0:
                tx.insert(INSERT,i.upper())
            elif lw==1:
                tx.insert(INSERT,i.lower())
            elif lw==2:
                tx.insert(INSERT,i.title())
            elif lw==3:
                for j in i.split('.'):
                    for k in j:
                        if k=='\t'or k==' ':
                            tx.insert(INSERT,k)
                        else:
                            tx.insert(INSERT,j[j.index(k)::].capitalize())
                            tx.insert(INSERT,".")
                            break
            tx.insert(INSERT,'\n')
    except:
        messagebox.showinfo("Imformation","Please select text")
        
def cpy():
    try:
        tx.clipboard_clear()
        tx.clipboard_append(tx.selection_get())
    except:
        messagebox.showinfo("Imformation","Please select text")
def ct():
    try:
        cpy()
        tx.delete("sel.first","sel.last")
    except:
        messagebox.showinfo("Imformation","Please select text")
def undo():
    try:
        tx.edit_undo()
    except:
        messagebox.showinfo("Imformation","Nothing to undo")
def redo():
    try:
        tx.edit_redo()
    except:
        messagebox.showinfo("Imformation","Nothing to redo")
def pst():
    try:
        tx.insert(INSERT,tx.clipboard_get())
    except:
        messagebox.showinfo("Imformation","Please select text")
def fnt(i,a):
    try:
        tx.tag_add("t1"+str(i),"sel.first","sel.last")
    except:
        tx.insert(a," ")
        tx.tag_add("t1"+str(i),a,END)
    tx.tag_config("t1"+str(i),font="normal "+str(i)+" normal")
def fntstyl(i,a):
    try:
        tx.tag_add("t1"+i,"sel.first","sel.last")
    except:
        tx.insert(a," ")
        tx.tag_add("t1"+i,a,END)
    tx.tag_config("t1"+i,font="normal "+str(fn.get())+" "+i)
def color(i,a,t):
    try:
        tx.tag_add("t1"+i,"sel.first","sel.last")
    except:
        tx.insert(a," ")
        tx.tag_add("t1"+i,a,END)
    if t:
        tx.tag_config("t1"+i,foreground=i)
    else:
        tx.tag_config("t1"+i,background=i)
def jr(a):
    try:
        tx.tag_add("jr","sel.first","sel.last")
    except:
        tx.insert(a," ")
        tx.tag_add("jr",a,END)
    tx.tag_config("jr",justify="right")
def jc(a):
    try:
        tx.tag_add("jc","sel.first","sel.last")
    except:
        tx.insert(a," ")
        tx.tag_add("jc",a,END)
    tx.tag_config("jc",justify="center")
def jl(a):
    try:
        tx.tag_add("jl","sel.first","sel.last")
    except:
        tx.insert(a," ")
        tx.tag_add("jl",a,END)
    tx.tag_config("jl",justify="left")
def togle(a):
    if b1.config('background')[-1]=="white":
        try:
            tx.tag_add("un","sel.first","sel.last")
        except:
            tx.insert(a," ")
            b1.config(background="lightblue")
            tx.tag_add("un",a,END)
        tx.tag_config("un",underline=1)
       
    else:
        b1.config(background="white")
        tx.tag_remove("un",INSERT,END)
def togle1(a):
    if b2.config('background')[-1]=="white":
        b2.config(background="lightblue")
        tx.insert(a," ")
        tx.tag_add("ov",a,END)
        tx.tag_config("ov",overstrike=1)
       
    else:
        b2.config(background="white")
        tx.tag_remove("ov",INSERT,END)
def spr(a):
    if b8.config('background')[-1]=="white":
        if b9.config("background")[-1]=="lightblue":
            tx.tag_remove("sub",INSERT,END)
            b9.config(background="white")
        try:
            tx.tag_add("spr","sel.first","sel.last")
        except:
            tx.insert(a," ")
            b8.config(background="lightblue")
            tx.tag_add("spr",a,END)
        tx.tag_config("spr",offset=7)
       
    else:
        b8.config(background="white")
        tx.tag_remove("spr",INSERT,END)
def sub(a):
    if b9.config('background')[-1]=="white":
        if b8.config("background")[-1]=="lightblue":
            tx.tag_remove("spr",INSERT,END)
            b8.config(background="white")
        try:
            tx.tag_add("sub","sel.first","sel.last")
        except:
            tx.insert(a," ")
            b9.config(background="lightblue")
            tx.tag_add("sub",a,END)
        tx.tag_config("sub",offset=-7)
       
    else:
        b9.config(background="white")
        tx.tag_remove("sub",INSERT,END)
def space2():
    def space11(i):
        try:
            tx.tag_add("sp"+str(i),"sel.first","sel.last")
            tx.tag_config("sp"+str(i),spacing2=i)
            c.destroy()
        except:
            messagebox.showinfo("Imformation","Please select text")
    c=Toplevel(word)
    c.title("1LS")
    a=range(1,11,1)
    b=StringVar(c)
    b.set(a[0])
    op=OptionMenu(c,b,*a,command=lambda i:space11(i)).pack()
def space1():
    def space12(i):
        try:
            tx.tag_add("sp"+str(i),"sel.first","sel.last")
            tx.tag_config("sp"+str(i),spacing1=i)
            c.destroy()
        except:
            messagebox.showinfo("Imformation","Please select text")
    c=Toplevel(word)
    c.title("1LS")
    a=range(10,40,5)
    b=StringVar(c)
    b.set(a[0])
    op=OptionMenu(c,b,*a,command=lambda i:space12(i)).pack()
def op():
    global file
    try:
        rt=filedialog.askopenfile(initialdir="f:/",title="open file",filetypes=(("text files","*.txt"),("all files","*.*")))
        if rt!=None:
            tx.delete("1.0",END)
            for i in rt:
                tx.insert(END,i)
            file=rt.name
            word.title(file)
            rt.close()
    except:
        pass
def saveas():
    global file
    f=filedialog.asksaveasfile(mode="w",defaultextension=".txt")
    if f is None:
        return
    texttosave=tx.get("1.0",END)
    f.write(texttosave)
    file=f.name
    word.title(file)
    f.close()
def save():
    global file
    if file=="no":
        saveas()
    else:
        f=open(file,"w+")
        f.write(tx.get("1.0",END))
        f.close()
def new(t):
    global file
    if messagebox.askyesno("Required","Do you want to save the file")==True:
        if file=="no":
            saveas()
        else:
            f=open(file,"w+")
            f.write(tx.get("1.0",END))
            f.close()
    if t==1:
        tx.delete(0.0,END)
        word.title("Untitled file")
        file="no"
    else:
            word.destroy()
def info(event,b,a):
    def info1(event):
        c.destroy()
    c=Toplevel(word)
    l=Label(c,text=a).pack()
    b.bind("<Leave>",lambda event:info1(event))
def showinfo():
    a=[b1,b2,b3,b4,b5,b6,b7,b8,b9]
    if b10.config('background')[-1]!='white':
        for i in a:
            i.unbind("<Enter>")
        b10.config(background="white")
    else:
        b1.bind("<Enter>",lambda event:info(event,b1,a="Underline text"))
        b2.bind("<Enter>",lambda event:info(event,b2,a="Strick through the text"))
        b3.bind("<Enter>",lambda event:info(event,b3,a="Spacing between lines"))
        b4.bind("<Enter>",lambda event:info(event,b4,a="Justify menu"))
        b5.bind("<Enter>",lambda event:info(event,b5,a="Font size"))
        b6.bind("<Enter>",lambda event:info(event,b6,a="Font style"))
        b7.bind("<Enter>",lambda event:info(event,b7,a="Font color"))
        b8.bind("<Enter>",lambda event:info(event,b8,a="Superscript"))
        b9.bind("<Enter>",lambda event:info(event,b9,a="Subscript"))
        b10.config(background="lightblue")
def date():
    def tm(i):
        tx.insert(INSERT,i)
        d.destroy()
    d=Toplevel(word)
    dat=[strftime("%d/%m/%y"),strftime("%d.%m.%y"),strftime("%H:%M:%S"),strftime("%H:%M"),strftime("%d/%m/%y-%H:%M:%S")]
    da=StringVar(word)
    da.set(dat[0])
    b13=OptionMenu(d,da,*dat,command=lambda i:tm(i))
    b13.pack()
    b13.config(background="white")
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from time import strftime
word=Tk()
word.geometry("1100x800")
word.minsize(width=1100,height=800)
word.title("Untitled file")
word.configure(background="white")
he=Frame(word)
he.pack()
head=Frame(he)
head.pack(side="left")
head1=Frame(he)
head1.pack(side="left")
foot=Frame(word)
foot.pack()
sc=Scrollbar(foot)
sc.pack(side="right",fill=Y)
tx=Text(foot,width="500",height="80",yscrollcommand=sc.set,undo=True)
tx.pack(side="right")
sc.config(command=tx.yview)
mb=Menubutton(head,text="Edit",activeforeground="orange",pady="5",padx="20",background="white")
mb.pack(side="right")
mb.menu=Menu(mb)
mb["menu"]=mb.menu
mb.menu.add_checkbutton(label="Undo",activebackground="Red",background="white",command=undo)
mb.menu.add_checkbutton(label="Redo",activebackground="Red",background="white",command=redo)
mb.menu.add_separator(background="white")
mb.menu.add_checkbutton(label="Find",activebackground="Red",background="white",command=lambda :search(0))
mb.menu.add_checkbutton(label="Replace",activebackground="Red",background="white",command=lambda:search(1))
mb.menu.add_separator(background="white")
mb.menu.add_checkbutton(label="Copy",activebackground="Red",background="white",command=cpy)
mb.menu.add_checkbutton(label="Cut",activebackground="Red",background="white",command=ct)
mb.menu.add_checkbutton(label="Paste",activebackground="Red",background="white",command=pst)
mb2=Menubutton(head,text="File",activeforeground="orange",pady="5",padx="20",background="white")
mb2.pack(side="right")
mb2.menu=Menu(mb2)
mb2["menu"]=mb2.menu
mb2.menu.add_checkbutton(label="New",activebackground="Red",background="white",command=lambda :new(1))
mb2.menu.add_checkbutton(label="Open",activebackground="Red",background="white",command=op)
mb2.menu.add_checkbutton(label="Save As",activebackground="Red",background="white",command=saveas)
mb2.menu.add_checkbutton(label="Save",activebackground="Red",background="white",command=save)
mb2.menu.add_checkbutton(label="Exit",activebackground="Red",background="white",command=lambda :new(0))
b1=Button(head1,text="U",background="white",padx="20",command=lambda :togle(under()))
b1.pack(side="left")
b8=Button(head1,text="super",background="white",padx="20",command=lambda :spr(under()))
b8.pack(side="left")
b9=Button(head1,text="sub",background="white",padx="20",command=lambda :sub(under()))
b9.pack(side="left")
b2=Button(head1,text="-S-",background="white",padx="20",command=lambda :togle1(under()))
b2.pack(side="left")
b3=Menubutton(head1,text="line spacing",background="white",padx="20")
b3.pack(side="left")
b3.menu=Menu(b3)
b3["menu"]=b3.menu
b3.menu.add_checkbutton(label="first line spacing",background="white",command=space1)
b3.menu.add_checkbutton(label="All line spacing",background="white",command=space2)
b4=Menubutton(head1,text="justify",background="white",padx="20")
b4.pack(side="left")
b4.menu=Menu(b4)
b4["menu"]=b4.menu
b4.menu.add_checkbutton(label="Left",background="white",command=lambda :jl(under()))
b4.menu.add_checkbutton(label="Center",background="white",command=lambda :jc(under()))
b4.menu.add_checkbutton(label="Right",background="white",command=lambda :jr(under()))
font=list(range(8,50))
fn=StringVar(word)
fn.set(font[0])
b5=OptionMenu(head1,fn,*font,command=lambda i:fnt(i,under()))
b5.config(bg="white")
b5.pack(side="left")
styl=["normal","bold","italic"]
sty=StringVar(word)
sty.set(styl[0])
b6=OptionMenu(head1,sty,*styl,command=lambda i:fntstyl(i,under()))
b6.config(bg="white")
b6.pack(side="left")
clrs=["black","red","orange","green","yellow","violet","indigo","blue","purple"]
clr=StringVar(word)
clr.set(clrs[0])
b7=OptionMenu(head1,clr,*clrs,command=lambda i:color(i,under(),1))
b7.config(bg="white")
b7.pack(side="left")
b11=Menubutton(head1,text="case",background="white",padx="20")
b11.pack(side="left")
b11.menu=Menu(b11)
b11["menu"]=b11.menu
b11.menu.add_checkbutton(label="Upper",background="white",command= lambda :upper(0))
b11.menu.add_checkbutton(label="Lower",background="white",command= lambda :upper(1))
b11.menu.add_checkbutton(label="Title",background="white",command= lambda :upper(2))
b11.menu.add_checkbutton(label="Gramer",background="white",command= lambda :upper(3))
clr=["white","black","red","orange","green","yellow","violet","indigo","blue","purple"]
cl=StringVar(word)
cl.set(clr[0])
b12=OptionMenu(head1,cl,*clr,command=lambda i:color(i,under(),0))
b12.config(bg="white")
b12.pack(side="left")
b14=Button(head1,text="Date",command=date)
b14.pack(side="left")
b14.config(background="white")
b10=Button(head1,text="Help",background="white",padx="20",command=showinfo)
b10.pack(side="left")
word.mainloop()
