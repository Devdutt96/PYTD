from tkinter import *
import tkinter as tk
from pytube import YouTube

root = Tk()


def useless():
    print("it does nothing")

def edit():
    status = Label(root, text="you clicked undo", relief=SUNKEN)
    status.grid(row=5, column=0, columnspan=4)

def copy():

    status = Label(root, text="you CLICK  COPY", relief=SUNKEN)
    status.grid(row=5, column=0, columnspan=4)
    status.delete(0,END)
def you():

    status = Label(root, text="you are AWSOME", relief=SUNKEN)
    status.grid(row=5, column=0, columnspan=4)


def get_path(arg=None):
    path = mypath.get()

myurl= Entry(root)
myurl.focus()



def get_url(arg=None):
    yt = myurl.get()


myurl.bind("<Return>", get_url)
myurl.grid(row=1,column=3)


mypath=Entry(root)
mypath.bind("<Return>", get_path)
mypath.grid(row=2 , column=3)


blankmenu = Menu(root)
root.config(menu=blankmenu)


filemenu = Menu(blankmenu)
blankmenu.add_cascade(label="File", menu= filemenu )
filemenu.add_command(label="New project", command = useless)
filemenu.add_command(label="New..", command = useless)
filemenu.add_separator()
filemenu.add_command(label="Exit", command= quit)


editmenu =Menu(blankmenu)
blankmenu.add_cascade(labe="Edit", menu = editmenu)
editmenu.add_command(label = "Undo", command= edit)
editmenu.add_command(label = "cut", command = copy )
editmenu.add_command(label = "copy", command = you)
editmenu.add_command(label = "Redo", command= useless)


formatmenu =Menu(blankmenu)
formatmenu.add_command(label="indent region", command =lambda: print("done"))
formatmenu.add_command(label="format graph", command= lambda:print("xyz"))


#  *----------------------------------menus finished------------------------------------*

img = PhotoImage(file = '68.gif')
smallimage= PhotoImage.subsample(img, x=3, y=5)


imglabel =Label(root, image= smallimage)
imglabel.grid(row=1, column=1, rowspan=2)  # for image


url_text = Label(root, relief = 'groove',  text = "       Enter URL       ")
url_text.grid(row=1, column=2, sticky="E",padx=2)  # url label box
pathlabel = Label(root,relief = 'groove',text = "     Specify path      " )
pathlabel.grid(row=2, column=2, sticky="E")  # path label box

resultLabel = Label(root,text="")
resultLabel.grid(row=5, column=0, columnspan=4)

dbutton = Button(root, text= "Download  single video")
dbutton.grid(row=4, column=2, columnspan=2, pady=5)  # single video download button
#dbutton.bind("<Button-1>", get_url)

pbutton = Button(root, text="Download full Playlist")
pbutton.grid(row=3, column=2, columnspan=2, pady=5)  # playlist download button

root.title("Welcome to Dev's YTD")
root.resizable(0,0)


status = Label(root,width=50, text=edit(), relief=SUNKEN)
status.grid(row=5, column=0, columnspan=4)

var=tk.StringVar(root)

choices=['1080p', '720p','420p']
varl= tk.StringVar()
drop = OptionMenu(root,varl,*choices)
drop.grid(row=6,column=0)
#  *_____________________________________________GUI Finished______________________________________________*




root.mainloop()
