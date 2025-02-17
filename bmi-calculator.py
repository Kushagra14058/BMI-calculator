# Demo
from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk


root=Tk()
root.title("BMI CALCULATOR")
root.geometry("470x580+300+200")
root.resizable(False,False)
root.configure(bg="lightblue")

def reset_entry():
    height.delete(0,'end')
    weight.delete(0,'end')
    slider.set(0)
    slider2.set(0)

def BMI():
    h=float(Height.get())
    w=float(Weight.get())

#convert hieght into meter
    m=h/100
    bmi=round(float(w/m**2),1)
    labell1.config(text=bmi)

    if bmi < 18.5:
        labell2.config(text="underwieght!")
        labell3.config(text="you have normal weight than the \n normally body")
    elif (bmi > 18.5) and (bmi < 24.9):
        labell2.config(text="Normal")
        labell3.config(text="you are healthy! \n you don't need any diet")
    elif (bmi > 24.9) and (bmi < 29.9):
        labell2.config(text="overwieght")
        labell3.config(text="it indicates that a person is \n slightly overwieght!\n A doctor may advise to lose some \n weight ")
    elif (bmi > 29.9):
        labell2.config(text="obese!")
        labell3.config(text="Health may be at risk,if they do not \n lose weight!")


#icon
image_icon=PhotoImage(file="C:\\project2\\icon.png")
root.iconphoto(False,image_icon)

#top
top=PhotoImage(file="C:\\project2\\top.png")
top_image=Label(root,image=top,background="black")
top_image.place(x=-10,y=-10)

#bottom box
Label(root,width=72,height=18,bg="lightgreen").pack(side=BOTTOM)

#two boxes
box=PhotoImage(file="C:\\project2\\box.png")
Label(root,image=box).place(x=20,y=100)
Label(root,text="Height",font="arial 20 bold",bg="white").place(x=80,y=110)
Label(root,image=box).place(x=240,y=100)
Label(root,text="Weight",font="arial 20 bold",bg="white").place(x=300,y=110)

#scale
scale=PhotoImage(file="C:\\project2\\scale.png")
Label(root,image=scale,bg="white").place(x=20,y=310)

##slider code 1
current_value = tk.DoubleVar()
def get_current_value():
    return'{: .2f}' .format(current_value.get())
def slider_changed(event):
    Height.set(get_current_value())

    size=int(float(get_current_value()))
    img= (Image.open("c:\\project2\\man.png"))
    resized_image=img.resize((50,10+size))
    photo2=ImageTk.PhotoImage(resized_image)
    secondimage.configure(image=photo2)
    secondimage.place(x=70,y=550-size)
    secondimage.image=photo2

style = ttk.Style()
style.configure("TScale",background="white")
slider= ttk.Scale(root,from_=0, to =220,orient='horizontal',style="TScale",command=slider_changed,variable=current_value)
slider.place(x=80,y=250)

#slider code 2
current_value2 = tk.DoubleVar()
def get_current_value2():
    return'{: .2f}' .format(current_value2.get())
def slider_changed2(event):
    Weight.set(get_current_value2())

style2 = ttk.Style()
style2.configure("TScale",background="white")
slider2= ttk.Scale(root,from_=0, to =200,orient='horizontal',style="TScale",command=slider_changed2,variable=current_value2)
slider2.place(x=300,y=250)

#Entry box
Height=StringVar()
Weight=StringVar()
height=Entry(root,textvariable=Height,width=5,font='arial 50',bg="#fff",justify=CENTER)
height.place(x=35,y=160)
Height.set(get_current_value())

weight=Entry(root,textvariable=Weight,width=5,font='arial 50',bg="#fff",justify=CENTER)
weight.place(x=255,y=160)
Weight.set(get_current_value2())

#man image
secondimage=Label(root,bg="lightblue")
secondimage.place(x=70,y=530)

#button

labell1=Label(root,font="arial 30 bold",bg="lightgreen")
labell1.place(x=125,y=340)

Button(root,text="view report",width=15,height=2,font="arial 10 bold ",bg="yellow",command=BMI).place(x=280,y=340)

labell2=Label(root,font="arial 20 bold",bg="lightgreen")
labell2.place(x=280,y=430)

labell3=Label(root,font="arial 10 bold",bg="lightgreen")
labell3.place(x=200,y=500)

reset_btn = Button(
    root,
    text='Reset',
    command=reset_entry,
    height=1,width=7,
    bg="red"
)
reset_btn.pack(side=LEFT)
reset_btn.place(x=410,y=15)

def openNewWindow():
     
    newWindow = Toplevel(root)

    newWindow.title("DIET")
 
    newWindow.geometry("700x700")
 
    Label(newWindow, 
          text ="HEALTHY DIET PLAN",font='arial 20 bold underline').place(x=200,y=10)
    
    diet_plan=ImageTk.PhotoImage(file="C:\\project2\\diet_plan.png")
    Label(newWindow,image=diet_plan).place(x=100,y=60)

    newWindow.mainloop()
 
 
btn = Button(root, 
             text ="DIET", 
             bg="green",
             command = openNewWindow)
btn.place(x=10,y=15)


root.mainloop()
