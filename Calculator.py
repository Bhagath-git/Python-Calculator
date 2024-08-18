#TKinterCalculator
"""
Created by : Bhagath P Chandran 

Brototype malayalam (Youtube channel)
Python Basic Challenge (Playlist)
Episode 8 Tkinter calculator
"""

#importing Tkinter
from tkinter import *

#num1 & num2 are input variables, call is used for declare operation
num1 = ""
num2 = 0
call = int(0)


#Title and size
window = Tk()
window.title("Calculator")
window.geometry("424x545")
window.resizable(False,False)


#functions

#operating functions
def operate(text,a):
    
    global num1
    global num2
    global call
    
    num2 = float(num1)
    
    if(call == 0):
    
        if (a == 1):        
            call = 1
        
        elif (a == 2):        
            call = 2
        
        elif (a == 3):        
            call = 3
        
        elif (a == 4):        
            call = 4
    
    num2 = float(num1)
    num1 = num1+str(text)
    label.config(text = num1)
    num1 = ''
    
#result function
def result():
    
    global num1
    global num2
    global call
        
    label.config(text = "")
    
    if (call == 0):
        label.config(text = "")
    
    elif (call == 1):
        
        num2 = num2+float(num1)
        label.config(text = num2)
        
    elif (call == 2):
        
        num2 = num2-float(num1)
        label.config(text = num2)
        
    elif (call == 3):
        
        num2 = num2*float(num1)
        label.config(text = num2)
        
    elif (call == 4):
        
        num2 = num2/float(num1)
        label.config(text = num2)
    
    print("Result : "+str(num2))
    num1  = str(num2)
    num2 = 0
    call = 0
    
#show numbers function
def show(text):
    
    global num1
    global call
    
    num1 = num1+text
    print(num1)
    
    if (call == 0):
        label.config(text = num1)
        
    elif (call == 1):
        label.config(text = str(num2)+"+"+num1)
        
    elif (call == 2):
        label.config(text = str(num2)+"-"+num1)
        
    elif (call == 3):
        label.config(text = str(num2)+"x"+num1)
        
    elif (call == 4):
        label.config(text = str(num2)+"÷"+num1)
        
def clear():
    
    label.config(text = "")
    global num1
    global num2
    global call
    num1 = ""
    num2 = ""
    call = 0
    

#Frames for windows
top_frame = Frame(window, bg = "blue", width = 450, height = 50, pady = 0)
btm_frame = Frame(window, bg = "black", width = 450, height = 70, pady = 0)

top_frame.grid(row = 0, sticky = "ew")
btm_frame.grid(row = 1, sticky = "new")


#Labal, used to print input and results
label = Label(top_frame, text = "", width = 27, height = 3, font = ('helvetica 20'))
label.grid(row = 0, column = 0)


#Buttons for nums and operations
#button for nums
button7 = Button(btm_frame, bg = "#FFFF00", width = 6, height = 2, text = "7", font = ("helvetica 20"), command = lambda:show("7"))
button8 = Button(btm_frame, bg = "#FFFF00", width = 6, height = 2, text = "8", font = ("helvetica 20"), command = lambda:show("8"))
button9 = Button(btm_frame, bg = "#FFFF00", width = 6, height = 2, text = "9", font = ("helvetica 20"), command = lambda:show("9"))

button4 = Button(btm_frame, bg = "#FFFF00", width = 6, height = 2, text = "4", font = ("helvetica 20"), command = lambda:show("4"))
button5 = Button(btm_frame, bg = "#FFFF00", width = 6, height = 2, text = "5", font = ("helvetica 20"), command = lambda:show("5"))
button6 = Button(btm_frame, bg = "#FFFF00", width = 6, height = 2, text = "6", font = ("helvetica 20"), command = lambda:show("6"))

button1= Button(btm_frame, bg = "#FFFF00", width = 6, height = 2, text = "1", font = ("helvetica 20"), command = lambda:show("1"))
button2 = Button(btm_frame, bg = "#FFFF00", width = 6, height = 2, text = "2", font = ("helvetica 20"), command = lambda:show("2"))
button3 = Button(btm_frame, bg = "#FFFF00", width = 6, height = 2, text = "3", font = ("helvetica 20"), command = lambda:show("3"))

btn_Dot = Button(btm_frame, bg = "#FFFF00", width = 6, height = 2, text = ".", font = ("helvetica 20"), command = lambda:show("."))
button0 = Button(btm_frame, bg = "#FFFF00", width = 6, height = 2, text = "0", font = ("helvetica 20"), command = lambda:show("0"))
btn_per = Button(btm_frame, bg = "#FFFF00", width = 6, height = 2, text = "%", font = ("helvetica 20"))

#button for arithemetic operations
add_Btn = Button(btm_frame, bg = "#0E80F9", width = 6, height = 2, text = "+", font = ("helvetica 20"), command = lambda:operate("+",1))
sub_Btn = Button(btm_frame, bg = "#0E80F9", width = 6, height = 2, text = "-", font = ("helvetica 20"), command = lambda:operate("-",2))
mul_Btn = Button(btm_frame, bg = "#0E80F9", width = 6, height = 2, text = "x", font = ("helvetica 20"), command = lambda:operate("x",3))
div_Btn = Button(btm_frame, bg = "#0E80F9", width = 6, height = 2, text = "÷", font = ("helvetica 20"), command = lambda:operate("÷",4))

#button for sum and cleat
sum_Btn = Button(btm_frame, bg = "#1CF90E", width = 13, height = 2, text = "=", font = ("helvetica 20"), command = lambda:result())
clear_Btn = Button(btm_frame, bg = "#F02214", width = 13, height = 2, text = "Clear", font = ("helvetica 20"), command = lambda:clear())

#colors used for buttons
'''
colours
nums = #FFFF00
operator = #1CF90E
clear = #F02214
sum = #1CF90E

'''

#button for num grid
button7.grid(row = 0, column = 0)
button8.grid(row = 0, column = 1)
button9.grid(row = 0, column = 2)

button4.grid(row = 1, column = 0)
button5.grid(row = 1, column = 1)
button6.grid(row = 1, column = 2)

button1.grid(row = 2, column = 0)
button2.grid(row = 2, column = 1)
button3.grid(row = 2, column = 2)

btn_Dot.grid(row = 3, column = 0)
button0.grid(row = 3, column = 1)
btn_per.grid(row = 3, column = 2)

#button for operate grid
add_Btn.grid(row = 0, column = 3)
sub_Btn.grid(row = 1, column = 3)
mul_Btn.grid(row = 2, column = 3)
div_Btn.grid(row = 3, column = 3)

sum_Btn.grid(row=4, column=0, columnspan = 2)
clear_Btn.grid(row=4, column=2, columnspan = 2)


# layout all of the main containers,
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(0, weight=1)

#loop for continous usage
window.mainloop()
