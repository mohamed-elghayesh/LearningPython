# A basic calculator using tkinter
# partial is used to stop auto calling of the commands until clicking the controls
from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import font
from functools import partial

# Main Settings
main_form = Tk()
main_form.geometry('400x300')
app_font = font.Font(family='Helvetica', size=16, weight='bold')

# global variable that writes to the display label
existing = ""

# concatenates every thing typed into one string 
# TODO check if a number is written after updating the "existing"
# TODO check the case of clear then press equal
def type_exp(exp):
    global existing
    existing+=exp
    lbl_result.config(text=existing)

# evaluates the concatenated string after replacing the x --> * if found
def get_result():
    global existing
    equation = existing.replace("x","*")
    existing = str(eval(equation))
    lbl_result.config(text=existing)

# clears previous calculations
def clear():
    global existing
    existing = ""
    lbl_result.config(text=existing)

# control definitions
lbl_empty = Label(main_form, font=app_font, background="black", text="")
lbl_result = Label(main_form, font=app_font, background="light green", width=25, anchor="w", text="")
btn_add = Button(main_form, font=app_font, text="+", command=partial(type_exp,"+"))
btn_sub = Button(main_form, font=app_font, text="-", command=partial(type_exp,"-"))
btn_mult = Button(main_form, font=app_font, text="x", command=partial(type_exp,"x"))
btn_div = Button(main_form, font=app_font, text="/", command=partial(type_exp,"/"))
btn_zero = Button(main_form, font=app_font, text="0", command=partial(type_exp,"0"))
btn_one = Button(main_form, font=app_font, text="1", command=partial(type_exp,"1"))
btn_two = Button(main_form, font=app_font, text="2", command=partial(type_exp,"2"))
btn_three = Button(main_form, font=app_font, text="3", command=partial(type_exp,"3"))
btn_four = Button(main_form, font=app_font, text="4", command=partial(type_exp,"4"))
btn_five = Button(main_form, font=app_font, text="5", command=partial(type_exp,"5"))
btn_six = Button(main_form, font=app_font, text="6", command=partial(type_exp,"6"))
btn_seven = Button(main_form, font=app_font, text="7", command=partial(type_exp,"7"))
btn_eight = Button(main_form, font=app_font, text="8", command=partial(type_exp,"8"))
btn_nine = Button(main_form, font=app_font, text="9", command=partial(type_exp,"9"))
btn_equal = Button(main_form, font=app_font, text="=", command=partial(get_result))
btn_clear = Button(main_form, font=app_font, text="c", command=partial(clear))

# grid layout
lbl_result.grid(row=0,columnspan=9)
btn_zero.grid(row=1,column=0)
btn_one.grid(row=1,column=1)
btn_two.grid(row=1,column=2)
btn_three.grid(row=1,column=3)
btn_four.grid(row=1,column=4)
btn_five.grid(row=2,column=0)
btn_six.grid(row=2,column=1)
btn_seven.grid(row=2,column=2)
btn_eight.grid(row=2,column=3)
btn_nine.grid(row=2,column=4)
lbl_empty.grid(row=1,column=5, rowspan=2)
btn_add.grid(row=1,column=6)
btn_sub.grid(row=1,column=7)
btn_mult.grid(row=2,column=6)
btn_div.grid(row=2,column=7)
btn_equal.grid(row=1, column=8)
btn_clear.grid(row=2,column=8)

main_form.mainloop()