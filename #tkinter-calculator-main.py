#tkinter-calculator-output-to-input-branch

from tkinter import *
import tkinter as ttk
#from tkinter import font

NBPX = 20 #Normal button padx value
NBPY = 15 #Normal button pady value

BROPR = 4 #Button row operators
BR789 = 5 #Button row 7, 8, 9
BR456 = 6 #Button row 4, 5, 6
BR123 = 7 #Button row 1, 2, 3
BR0DP = 8 #Button row 0 & decimal point



Calculator = ttk.Tk()



def clearHeader():
    inputDisplay.config(text = "")    #Set input box to null
    outputDisplay.config(text = "")   #Set output box to null

def appendHeader(val): 
    cur = inputDisplay.cget("text")   #Get the current value stored in the input box
    new = str(cur) + str(val)         #Create a new var that has the new value at the end
    inputDisplay.config(text = new)   #Write the new value

def backSpace():
    cur = inputDisplay.cget("text")   #Get current value stored in the input box
    newB = cur[:-1]                   #Create new var based of cur with the last char cut off
    inputDisplay.config(text = newB)  #Write the updated value

def computeInput():                   
    cur = inputDisplay.cget("text")   #Get current value stored in the input box
    Ecur = eval(cur)
    outputDisplay.config(text = Ecur)


#Headers
#Input
inputHeader = ttk.Label(
    text = "Input:",
    background = "Grey"
    )
#Output
outputHeader = ttk.Label(
    text = "Output:",
    background = "Grey"
    )


#Display
#Input
inputDisplay = ttk.Label(
    text = ""
    )
#Output
outputDisplay = ttk.Label(
    text = ""
    )


#Operator Buttons

#Addition
BA = ttk.Button(
    text = "+",
    padx = NBPX,
    pady = NBPY,
    command = lambda : appendHeader("+"),
    activebackground = "grey"
    ) 

#Subtraction
BS = ttk.Button(
    text = "-",
    padx = NBPX,
    pady = 15,
    command = lambda : appendHeader("-"),
    activebackground = "grey"
    )  

#Multiplication
BM = ttk.Button(
    text = "*",
    padx = NBPX,
    pady = 15,
    command = lambda : appendHeader("*"),
    activebackground = "grey"
    ) 

#Division
BD = ttk.Button(
    text = "÷",
    padx = NBPX,
    pady = NBPY,
    command = lambda : appendHeader("/"),
    activebackground = "grey"
    )

#Decimal Point
BDP = ttk.Button(
    text = ".",
    padx = NBPX,
    pady = NBPY,
    command = lambda : appendHeader("."),
    activebackground = "grey"
    )

#Enter
BE = ttk.Button(
    text = "Enter",
    padx = NBPX,
    pady = NBPY,
    activebackground = "grey",
    command = computeInput
    )

#Back
BB = ttk.Button(
    text = "Back",
    padx = NBPX,
    pady = NBPY,
    activebackground = "grey",
    command = lambda : backSpace()
    )

#Clear
BC = ttk.Button( 
    text = "Clear",
    padx = NBPX,
    pady = NBPY,
    activebackground = "grey",
    command = lambda : clearHeader()

)


#Number Buttons

B1 = ttk.Button(
    text = "1",
    padx = NBPX,
    pady = NBPY,
    command = lambda : appendHeader(1),
    activebackground = "grey"
    )

B2 = ttk.Button(
    text = "2",
    padx = NBPX,
    pady = NBPY,
    command = lambda : appendHeader(2),
    activebackground = "grey"
    )

B3 = ttk.Button(
    text = "3",
    padx = NBPX,
    pady = NBPY,
    command = lambda : appendHeader(3),
    activebackground = "grey"
    )

B4 = ttk.Button(
    text = "4",
    padx = NBPX,
    pady = NBPY,
    command = lambda : appendHeader(4),
    activebackground = "grey"
    )

B5 = ttk.Button(
    text = "5",
    padx = NBPX,
    pady = NBPY,
    command = lambda : appendHeader(5),
    activebackground = "grey"
    )

B6 = ttk.Button(
    text = "6",
    padx = NBPX,
    pady = NBPY,
    command = lambda : appendHeader(6),
    activebackground = "grey"
    )

B7 = ttk.Button(
    text = "7",
    padx = NBPX,
    pady = NBPY,
    command = lambda : appendHeader(7),
    activebackground = "grey"
    )

B8 = ttk.Button(
    text = "8",
    padx = NBPX,
    pady = NBPY,
    command = lambda : appendHeader(8),
    activebackground = "grey"
    )

B9 = ttk.Button(
    text = "9",
    padx = NBPX,
    pady = NBPY,
    command = lambda : appendHeader(9),
    activebackground = "grey"
    )

B0 = ttk.Button(
    text = "0",
    padx = NBPX,
    pady = NBPY,
    command = lambda : appendHeader(0),
    activebackground = "grey"
    )  


Calculator.grid

#Operator Buttons Grid
BA.grid(
    column = 0,
    row = BROPR,
    sticky = "NSEW"
    )

BS.grid(
    column = 1,
    row = BROPR,
    sticky = "NSEW"
    )

BM.grid(
    column = 2,
    row = BROPR,
    sticky = "NSEW"
    )

BD.grid(
    column = 3,
    row = BROPR,
    sticky = "NSEW"
    )

BDP.grid(
    column = 2,
    row = BR0DP,
    sticky = "NSEW"
    )

BE.grid(
    column = 3,
    row = BR123,
    rowspan = 2,
    sticky = "NSEW"
    )

BB.grid(
    column = 3,
    row = BR789,
    sticky = "NSEW")

BC.grid(
    column = 3,
    row = BR456,
    sticky = "NSEW"
)

#Number Buttons Grid
B1.grid(
    column = 0,
    row = BR123,
    sticky = "NSEW"
    )

B2.grid(
    column = 1,
    row = BR123,
    sticky = "NSEW"
    )

B3.grid(
    column = 2,
    row = BR123,
    sticky = "NSEW"
    )

B4.grid(
    column = 0,
    row = BR456,
    sticky = "NSEW"
    )

B5.grid(
    column = 1,
    row = BR456,
    sticky = "NSEW"
    )

B6.grid(
    column = 2,
    row = BR456,
    sticky = "NSEW"
    )

B7.grid(
    column = 0,
    row = BR789,
    sticky = "NSEW"
    )

B8.grid(
    column = 1,
    row = BR789,
    sticky = "NSEW"
    )

B9.grid(
    column = 2,
    row = BR789,
    sticky = "NSEW"
    )

B0.grid(
    column = 0,
    columnspan = 2,
    row = BR0DP,
    sticky = "NSEW"
    )

inputHeader.grid(
    columnspan = 5,
    row = 0,
    sticky = "NSEW"
)

inputDisplay.grid(
    columnspan = 5,
    row = 1,
    sticky = "NSEW"
    )

outputHeader.grid(
    columnspan = 5,
    row = 2,
    sticky = "NSEW"
)

outputDisplay.grid(
    columnspan = 5,
    row = 3,
    sticky = "NSEW"
    )


Calculator.mainloop()
