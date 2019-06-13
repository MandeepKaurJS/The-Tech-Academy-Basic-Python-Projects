# myCal_Expt1.py
from tkinter import *
from decimal import *

#key press function
def click(btn_text):
    display.insert(END, btn_text)


#### main :

window = Tk()
window.title("My Calculator")

#create top_row frame

top_row = Frame(window)
top_row.grid(row=0, column=0, columnspan=2, sticky=N)

# use Entry for an editable display

display = Entry(top_row, width=45, bg= "light green")
display.grid()

#create num_pad_frame

num_pad = Frame(window)
num_pad.grid(row=1, column=0, sticky= W)

# provide a list of keys for the number pad:

num_pad_list = [
'7', '8', '9',
'4', '5', '6',
'1', '2', '3',
'0', '.', '=' ]
# create operator_frame

operator = Frame(window)
operator.grid(row=1, column=1, sticky=E)
operator_list = [ '*', '/', '+', '-', '(', ')', 'C' ]

# create operator buttons with a loop

r = 0
c = 0
for btn_text in operator_list:
    def cmd(x=btn_text):
        click(x)
    Button( operator, text=btn_text, width=3, command=cmd).grid(row=r,column=c)
    c = c + 1
    if c > 1:
       c = 0
       r = r + 1

# create num_oad buttons with a for loop

r = 0 # row counter
c = 0 # column counter

for btn_text in num_pad_list:
    def cmd(x=btn_text):
            click(x)
    Button(num_pad, text = btn_text , width=3, command=cmd).grid(row=r, column=c)
    c = c+1
    if c > 2:
        c = 0
        r = r + 1

# Adding another Frame
last_row = Frame(window)
last_row.grid(row = 2, column = 0, columnspan=2, sticky = S)

#adding another button(HERE!)

Button( last_row, text = "last", width= 45, command = click).grid(row = 0,     column = 0)

#### Run mainloop
window.mainloop()

