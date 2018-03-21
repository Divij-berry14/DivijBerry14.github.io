from tkinter import *

def btnClick(numbers):
    global operator
    operator=operator+str(numbers)
    text_input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_input.set("")

def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    operator=""
    
calci=Tk()
calci.title("CALCULATOR")
operator=""
text_input=StringVar()

Textdisplay=Entry(calci,font=('Adobe Gothic Std B',20), textvariable=text_input,bd=20, insertwidth=10,bg="light GREY",justify='left').grid(columnspan=4)

btn1=Button(calci,padx=12,bd=5,fg="black",relief="raised",font=('Adobe Gothic Std B',20,'bold'),text="1",command=lambda:btnClick(1)).grid(row=1,column=0)
btn2=Button(calci,padx=12,bd=5,fg="black",relief="raised",font=('Adobe Gothic Std B',20,'bold'),text="2",command=lambda:btnClick(2)).grid(row=1,column=1)
btn3=Button(calci,padx=12,bd=5,fg="black",relief="raised",font=('Adobe Gothic Std B',20,'bold'),text="3",command=lambda:btnClick(3)).grid(row=1,column=2)
btnADD=Button(calci,padx=10,bd=5,fg="black",relief="raised",font=('Adobe Gothic Std B',20,'bold'),text="+",command=lambda:btnClick("+")).grid(row=1,column=3)

#_____________________________________________________________________________________________________________________________________

btn6=Button(calci,padx=12,bd=5,fg="black",relief="raised",font=('Adobe Gothic Std B',20,'bold'),text="6",command=lambda:btnClick(6)).grid(row=2,column=0)
btn5=Button(calci,padx=12,bd=5,fg="black",relief="raised",font=('Adobe Gothic Std B',20,'bold'),text="5",command=lambda:btnClick(5)).grid(row=2,column=1)
btn4=Button(calci,padx=12,bd=5,fg="black",relief="raised",font=('Adobe Gothic Std B',20,'bold'),text="4",command=lambda:btnClick(4)).grid(row=2,column=2)
btnMinus=Button(calci,padx=14,bd=5,fg="black",relief="raised",font=('Adobe Gothic Std B',20,'bold'),text="-",command=lambda:btnClick("-")).grid(row=2,column=3)

#_____________________________________________________________________________________________________________________________________

btn7=Button(calci,padx=12,bd=5,fg="black",relief="raised",font=('Adobe Gothic Std B',20,'bold'),text="7",command=lambda:btnClick(7)).grid(row=3,column=0)
btn8=Button(calci,padx=12,bd=5,fg="black",relief="raised",font=('Adobe Gothic Std B',20,'bold'),text="8",command=lambda:btnClick(8)).grid(row=3,column=1)
btn9=Button(calci,padx=12,bd=5,fg="black",relief="raised",font=('Adobe Gothic Std B',20,'bold'),text="9",command=lambda:btnClick(9)).grid(row=3,column=2)
btnmultiply=Button(calci,padx=12,bd=5,fg="black",relief="raised",font=('Adobe Gothic Std B',20,'bold'),text="*",command=lambda:btnClick("*")).grid(row=3,column=3)


#_______________________________________________________________________________________________________________________________________

btnclear=Button(calci,padx=12,bd=5,fg="black",relief="raised",font=('Adobe Gothic Std B',20,'bold'),text="C",command=btnClearDisplay).grid(row=4,column=0)
btn0=Button(calci,padx=12,bd=5,fg="black",relief="raised",font=('Adobe Gothic Std B',20,'bold'),text="0",command=lambda:btnClick(0)).grid(row=4,column=1)
btnresult=Button(calci,padx=12,bd=5,fg="black",relief="raised",font=('Adobe Gothic Std B',20,'bold'),text="=",command=btnEqualsInput).grid(row=4,column=2)
btndivison=Button(calci,padx=14,bd=5,fg="black",relief="raised",font=('Adobe Gothic Std B',20,'bold'),text="/",command=lambda:btnClick("/")).grid(row=4,column=3)



calci.mainloop()
