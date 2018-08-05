from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import os

root=Tk()
root.title("TextPad")
root.geometry("1000x600+200+50")

file=None

#****************************************************************************************MENU FUNCTIONALITY************************************************************

def openFile():
        global file 
        file = askopenfilename(defaultextension=".txt",
                                      filetypes=[("All Files","*.*"),
                                        ("Text Documents","*.txt")])
        if file == "":
            file = None
        else:
            root.title(os.path.basename(file) + " - Notepad")
            txtarea.delete(1.0,END)
            f = open(file,"r")
            txtarea.insert(1.0,f.read())
            f.close()

def NewFile():
    global file
    root.title("untitled - TextPad")
    file=""
    txtarea.delete('1.0','end')
    
def Save():
    global file
    if file == "":
            file = asksaveasfilename(initialfile='Untitled.txt',
                                            defaultextension=".txt",
                                            filetypes=[("All Files","*.*"),
                                                ("Text Documents","*.txt")])
            if file == "":
                file = None
            else:
                f = open(file,"w")
                f.write(txtarea.get(1.0,END))
                f.close()
                root.title(os.path.basename(file) + " - Notepad")
    else:
        f = open(file,"w")
        f.write(txtarea.get(1.0,END))
        f.close()

def exits():
        global file
        p=0
        if file==None or file=="":
                t1=txtarea.get('1.0','end-1c')
                if t1=="":
                        root.destroy()
                else:
                        p=askquestion("Exit","Are you sure you want to exit without saving",icon='warning')
                if p=="yes":
                        root.destroy()
                        
        else:
                f=open(file,"r")
                txt1=f.read()
                text=txtarea.get('1.0','end-1c')
                if txt1==text:
                        root.destroy()
                else:
                        p=askquestion("Exit","Are you sure you want to exit without saving",icon='warning')
                        if p=="yes":
                                root.destroy()

def helps():
        import webbrowser
        webbrowser.open("first.txt", 'r')
    
def tut():
        import webbrowser
        webbrowser.open("first.txt", 'r')
    
#*************************************************************************MENU BAR*************************************************************************************

menu=Menu(root)
root.config(menu=menu)
SubMenu=Menu(menu)
menu.add_cascade(label="File",menu=SubMenu)
SubMenu.add_command(label="New File", accelerator="ctrl+n", font=("Helvetica",10), command=NewFile)
root.bind('<Control-n>', lambda e: NewFile())
SubMenu.add_command(label="Open...", accelerator="ctrl+o", font=("Helvetica",10), command=openFile)
root.bind('<Control-o>', lambda e: openFile())
SubMenu.add_command(label="Save...", accelerator="ctrl+s", font=("Helvetica",10), command=Save)
root.bind('<Control-s>', lambda e: Save())
SubMenu.add('separator')
SubMenu.add_command(label="Quit", accelerator="ctrl+q", font=("Helvetica",10), command=exits)
root.bind('<Control-q>', lambda e: exits())
root.bind('<Alt-F4>', lambda e: exits())
SubMenu.add('separator')

EditMenu=Menu(menu)
menu.add_cascade(label="Edit", menu=EditMenu)
EditMenu.add_command(label="Cut", accelerator="ctrl+x", font=("Helvetica",10), command=lambda : txtarea.event_generate("<<Cut>>"))
EditMenu.add_command(label="Copy", accelerator="ctrl+c", font=("Helvetica",10), command=lambda : txtarea.event_generate("<<Copy>>"))
EditMenu.add_command(label="Paste", accelerator="ctrl+v", font=("Helvetica",10), command=lambda : txtarea.event_generate("<<Paste>>"))
EditMenu.add('separator')

Help=Menu(menu)
menu.add_cascade(label="Help", menu=Help)
Help.add_command(label="Tutorial", accelerator="ctrl+h", font=("Helvetica",10), command=tut)
Help.add('separator')
Help.add_command(label="About", font=("Helvetica",10), command=helps)
Help.add('separator')

#****************************************************************************TEXT BOX**********************************************************************************

txtarea=Text(root, height=1000, width=600)
txtarea.pack()

root.mainloop()          #MAIN WINDOW CLOSE
