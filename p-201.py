from tkinter import *

window = Tk()

def calculate_interest():
    p=float(principle.get())
    r=float(rate.get())
    t=float(time.get())
    i=(p*r*t)/100
    interest=round(i,2)
    p_message=""

    showLabel.destroy()

    message=Label(resultFrame,text="Your SI is "+str(interest)+" "+p_message)
    message.place(x=50, y=270)
    message.pack()

window.title("SI calculator")
window.geometry("400x400")
window.config(bg="lightcyan")   

appLabel = Label(window, text="SI calculator", fg="black",bg="lightcyan", font=("monospace", 20))
appLabel.place(x=90, y=20)

principleLabel = Label(window, text="enter the principle:", fg="black",bg="lightcyan", font=("monospace", 15))
principleLabel.place(x=50, y=70)

principle = Entry(window, text="", bd=5,width=25)
principle.place(x=220, y=70)

roiLabel= Label(window, text="enter the rate:",fg="black", bg="lightcyan", font=("monospace", 15))
roiLabel.place(x=20, y=120)

rate = Entry(window, text="", bd=5,width=25)
rate.place(x=220, y=120)

timeLabel = Label(window, text="enter the time:",fg="black", bg="lightcyan", font=("monospace", 15))
timeLabel.place(x=20, y=170)

time = Entry(window, text="", bd=5,width=25)
time.place(x=220, y=170)

SIbutton = Button(window, text="CALCULATE", fg="black",bg="yellow", bd=4, command=calculate_interest)
SIbutton.place(x=150, y=220)

showLabel = Label(window, text=" ", bg="lightcyan",font=("monospace", 15), fg="black")
showLabel.place(x=50, y=270)
showLabel.pack()

resultFrame = LabelFrame(window, text="Result",bg="lightcyan", font=("monospace", 15), fg="black")
resultFrame.pack(padx=20, pady=20)
resultFrame.place(x=20, y=290)

window.mainloop()
