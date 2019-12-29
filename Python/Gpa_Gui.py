# GPA Calculator using tkinter (GUI)
from tkinter import Tk
from tkinter import Entry
from tkinter import Label
from tkinter import Button
from tkinter import messagebox
from tkinter import StringVar
from tkinter import font
from functools import partial

# Main Settings
main_form = Tk()
main_form.title("GPA Calculator")
main_form.geometry('800x500')
small_font = font.Font(family='Helvetica', size=14)
normal_font = font.Font(family='Helvetica', size=16, weight='bold')
large_font = font.Font(family='Helvetica', size=22, weight='bold')

# Write program's logic here

# global list to hold semester's marks
semester_marks = ["first",[],"second",[],"third",[],"fourth",[],"fifth",[],"sixth",[]]
textvar1 = StringVar()
textvar2 = StringVar()
textvar3 = StringVar()
textvar4 = StringVar()
textvar5 = StringVar()
textvar6 = StringVar()

# update the semester_marks from the changes in the course entries
def update_marks_entry1(semester):
    if (semester.split()[0]=="First"):
        semester_marks[1].append(lbl_course1["text"])
        semester_marks[1].append(textvar1.get())
        lbl_empty1["text"] = semester_marks[1][0]
        #textvar.set("")
    elif (semester.split()[0]=="Second"):
        semester_marks[3].append(lbl_course1["text"])
        semester_marks[3].append(textvar1.get())
        lbl_empty1["text"] = semester_marks[3][0]

def update_marks_entry2(semester):
    if (semester.split()[0]=="First"):
        semester_marks[1].append(lbl_course2["text"])
        semester_marks[1].append(textvar2.get())
        lbl_empty1["text"] = semester_marks[1][2]
        #textvar.set("")
    elif (semester.split()[0]=="Second"):
        semester_marks[3].append(lbl_course2["text"])
        semester_marks[3].append(textvar2.get())
        lbl_empty1["text"] = semester_marks[3][2]

def update_marks_entry3(semester):
    if (semester.split()[0]=="First"):
        semester_marks[1].append(lbl_course3["text"])
        semester_marks[1].append(textvar3.get())
        lbl_empty1["text"] = semester_marks[1][4]
        #textvar.set("")
    elif (semester.split()[0]=="Second"):
        semester_marks[3].append(lbl_course3["text"])
        semester_marks[3].append(textvar3.get())
        lbl_empty1["text"] = semester_marks[3][4]

def update_marks_entry4(semester):
    if (semester.split()[0]=="First"):
        semester_marks[1].append(lbl_course4["text"])
        semester_marks[1].append(textvar4.get())
        lbl_empty1["text"] = semester_marks[1][6]
        #textvar.set("")
    elif (semester.split()[0]=="Second"):
        semester_marks[3].append(lbl_course4["text"])
        semester_marks[3].append(textvar4.get())
        lbl_empty1["text"] = semester_marks[3][6]

def update_marks_entry5(semester):
    if (semester.split()[0]=="First"):
        semester_marks[1].append(lbl_course5["text"])
        semester_marks[1].append(textvar5.get())
        lbl_empty1["text"] = semester_marks[1][8]
        #textvar.set("")
    elif (semester.split()[0]=="Second"):
        semester_marks[3].append(lbl_course5["text"])
        semester_marks[3].append(textvar5.get())
        lbl_empty1["text"] = semester_marks[3][8]

def update_marks_entry6(semester):
    if (semester.split()[0]=="First"):
        semester_marks[1].append(lbl_course6["text"])
        semester_marks[1].append(textvar6.get())
        lbl_empty1["text"] = semester_marks[1][10]
        #textvar.set("")
    elif (semester.split()[0]=="Second"):
        semester_marks[3].append(lbl_course6["text"])
        semester_marks[3].append(textvar6.get())
        lbl_empty1["text"] = semester_marks[3][10]


# clear entries
def clear_entries():
    entry_first.delete(0,"end")
    entry_second.delete(0,"end")
    entry_third.delete(0,"end")
    entry_fourth.delete(0,"end")
    entry_fifth.delete(0,"end")
    entry_sixth.delete(0,"end")
    entry_search.delete(0,"end")

# first Semester method
def first_set():
    clear_entries()
    lbl_semester.config(text="First Semester")
    lbl_course1.config(text="LH135 : ESP I")
    lbl_course2.config(text="BA113 : Physics I")
    lbl_course3.config(text="BA103 : Calculus I")
    lbl_course4.config(text="AR115 : Visual Studies")
    lbl_course5.config(text="CS111 : Int. to Computers")
    lbl_course6.config(text="IS171 : Int. to Information Systems")

# second Semester method
def second_set():
    clear_entries()
    lbl_semester.config(text="Second Semester")
    lbl_course1.config(text="LH139 : ITA I")
    lbl_course2.config(text="CS119 : Computer Logics")
    lbl_course3.config(text="BA203 : Calculus II")
    lbl_course4.config(text="AR215 : Social Studies")
    lbl_course5.config(text="CS227 : Int. to Database")
    lbl_course6.config(text="IS211 : Int. to Artificial Intelligence")  

# third Semester method
def third_set():
    clear_entries()
    lbl_semester.config(text="Third Semester")
    lbl_course1.config(text="LH135 : ESP I")
    lbl_course2.config(text="BA113 : Physics I")
    lbl_course3.config(text="BA103 : Calculus I")
    lbl_course4.config(text="AR115 : Visual Studies")
    lbl_course5.config(text="CS111 : Int. to Computers")
    lbl_course6.config(text="IS171 : Int. to Information Systems")

# fourth Semester method
def fourth_set():
    clear_entries()
    lbl_semester.config(text="Fourth Semester")
    lbl_course1.config(text="LH135 : ESP I")
    lbl_course2.config(text="BA113 : Physics I")
    lbl_course3.config(text="BA103 : Calculus I")
    lbl_course4.config(text="AR115 : Visual Studies")
    lbl_course5.config(text="CS111 : Int. to Computers")
    lbl_course6.config(text="IS171 : Int. to Information Systems")

# fifth Semester method
def fifth_set():
    clear_entries()
    lbl_semester.config(text="Fifth Semester")
    lbl_course1.config(text="LH135 : ESP I")
    lbl_course2.config(text="BA113 : Physics I")
    lbl_course3.config(text="BA103 : Calculus I")
    lbl_course4.config(text="AR115 : Visual Studies")
    lbl_course5.config(text="CS111 : Int. to Computers")
    lbl_course6.config(text="IS171 : Int. to Information Systems")

# sixth Semester method
def sixth_set():
    clear_entries()
    lbl_semester.config(text="Sixth Semester")
    lbl_course1.config(text="LH135 : ESP I")
    lbl_course2.config(text="BA113 : Physics I")
    lbl_course3.config(text="BA103 : Calculus I")
    lbl_course4.config(text="AR115 : Visual Studies")
    lbl_course5.config(text="CS111 : Int. to Computers")
    lbl_course6.config(text="IS171 : Int. to Information Systems")

# seventh Semester method
def seventh_set():
    clear_entries()
    lbl_semester.config(text="Seventh Semester")
    lbl_course1.config(text="LH135 : ESP I")
    lbl_course2.config(text="BA113 : Physics I")
    lbl_course3.config(text="BA103 : Calculus I")
    lbl_course4.config(text="AR115 : Visual Studies")
    lbl_course5.config(text="CS111 : Int. to Computers")
    lbl_course6.config(text="IS171 : Int. to Information Systems")

# eighth Semester method
def eighth_set():
    clear_entries()
    lbl_semester.config(text="Eighth Semester")
    lbl_course1.config(text="LH135 : ESP I")
    lbl_course2.config(text="BA113 : Physics I")
    lbl_course3.config(text="BA103 : Calculus I")
    lbl_course4.config(text="AR115 : Visual Studies")
    lbl_course5.config(text="CS111 : Int. to Computers")
    lbl_course6.config(text="IS171 : Int. to Information Systems")

# term gpa method
def term_gpa():
    course1 = float(entry_first.get())
    course2 = float(entry_second.get())
    course3 = float(entry_third.get())
    course4 = float(entry_fourth.get())
    course5 = float(entry_fifth.get())
    course6 = float(entry_sixth.get())
    term_gpa = (course1+course2+course3+course4+course5+course6)/6
    lbl_term_gpa.config(text="%.3f"%term_gpa)

# overall gpa method
def overall_gpa():
    pass
    # TODO implement the overall gpa using the global semester_marks

# search method
def search(tag):
    messagebox.showinfo("Search for %s results"%tag,"TODO: Implement search")

# about method
def about():
    messagebox.showinfo("About GPA Calculator","This is still a prototype \nthat needs heavy testing")

# exit method
def exit():
    main_form.quit()


# control definitions
lbl_score = Label(main_form, font=large_font, background="light grey", width=10, anchor="c", text="")
lbl_term_gpa = Label(main_form, font=large_font, background="light green", width=10, anchor="c", text="")
lbl_mark = Label(main_form, font=large_font, background="light blue", width=10, anchor="c", text="")

btn_first = Button(main_form, font=normal_font, text="First", width=10, command=partial(first_set))
btn_second = Button(main_form, font=normal_font, text="Second", width=10, command=partial(second_set))
btn_third = Button(main_form, font=normal_font, text="Third", width=10, command=partial(third_set))
btn_fourth = Button(main_form, font=normal_font, text="Fourth", width=10, command=partial(fourth_set))
btn_fifth = Button(main_form, font=normal_font, text="Fifth", width=10, command=partial(fifth_set))
btn_sixth = Button(main_form, font=normal_font, text="Sixth", width=10, command=partial(sixth_set))
btn_seventh = Button(main_form, font=normal_font, text="Seventh", width=10, command=partial(seventh_set))
btn_eighth = Button(main_form, font=normal_font, text="Eighth", width=10, command=partial(eighth_set))
btn_term = Button(main_form, font=normal_font, text="Term GPA", width=10, command=partial(term_gpa))
btn_all = Button(main_form, font=normal_font, text="Overall GPA", width=10, command=partial(overall_gpa))

lbl_semester = Label(main_form, font=large_font, width=22, anchor="w", text="First Semester")
lbl_empty1 = Label(main_form, font=normal_font, width=5, anchor="w", text="")
lbl_course1 = Label(main_form, font=normal_font, width=30, anchor="w", text="LH135 : ESP I")
lbl_course2 = Label(main_form, font=normal_font, width=30, anchor="w", text="BA113 : Physics I")
lbl_course3 = Label(main_form, font=normal_font, width=30, anchor="w", text="BA103 : Calculus I")
lbl_course4 = Label(main_form, font=normal_font, width=30, anchor="w", text="AR115 : Visual Studies")
lbl_course5 = Label(main_form, font=normal_font, width=30, anchor="w", text="CS111 : Int. to Computers")
lbl_course6 = Label(main_form, font=normal_font, width=30, anchor="w", text="IS171 : Int. to Information Systems")

entry_first = Entry(main_form, textvariable=textvar1, font=normal_font, justify="center", width=5)
entry_first.bind("<Tab>",lambda x: update_marks_entry1(lbl_semester["text"]))
entry_second = Entry(main_form, textvariable=textvar2, font=normal_font, justify="center", width=5)
entry_second.bind("<Tab>",lambda x: update_marks_entry2(lbl_semester["text"]))
entry_third = Entry(main_form, textvariable=textvar3, font=normal_font, justify="center", width=5)
entry_third.bind("<Tab>",lambda x: update_marks_entry3(lbl_semester["text"]))
entry_fourth = Entry(main_form, textvariable=textvar4, font=normal_font, justify="center", width=5)
entry_fourth.bind("<Tab>",lambda x: update_marks_entry4(lbl_semester["text"]))
entry_fifth = Entry(main_form, textvariable=textvar5, font=normal_font, justify="center", width=5)
entry_fifth.bind("<Tab>",lambda x: update_marks_entry5(lbl_semester["text"]))
entry_sixth = Entry(main_form, textvariable=textvar6, font=normal_font, justify="center", width=5)
entry_sixth.bind("<Tab>",lambda x: update_marks_entry6(lbl_semester["text"]))

entry_search = Entry(main_form, font=small_font, justify="center", width=15)
btn_search = Button(main_form, font=normal_font, text="Search", width=10, command=lambda:search(entry_search.get()))
btn_about = Button(main_form, font=normal_font, text="About", width=10, command=partial(about))
btn_exit = Button(main_form, font=normal_font, text="Exit", width=10, command=partial(exit))

# grid layout
btn_first.grid(row=0,column=0)
btn_second.grid(row=0,column=1)
btn_third.grid(row=0,column=2)
btn_fourth.grid(row=0,column=3)
btn_fifth.grid(row=1,column=0)
btn_sixth.grid(row=1,column=1)
btn_seventh.grid(row=1,column=2)
btn_eighth.grid(row=1,column=3)
btn_term.grid(row=0,column=5)
btn_all.grid(row=1,column=5)

lbl_score.grid(row=3,column=5)
lbl_term_gpa.grid(row=4,column=5)
lbl_mark.grid(row=5,column=5)

lbl_empty1.grid(row=2,column=0,columnspan=4)
lbl_semester.grid(row=3,column=0, columnspan=3)
lbl_course1.grid(row=5,column=0, columnspan=3)
lbl_course2.grid(row=6,column=0, columnspan=3)
lbl_course3.grid(row=7,column=0, columnspan=3)
lbl_course4.grid(row=8,column=0, columnspan=3)
lbl_course5.grid(row=9,column=0, columnspan=3)
lbl_course6.grid(row=10,column=0, columnspan=3)

entry_first.grid(row=5,column=3)
entry_second.grid(row=6,column=3)
entry_third.grid(row=7,column=3)
entry_fourth.grid(row=8,column=3)
entry_fifth.grid(row=9,column=3)
entry_sixth.grid(row=10,column=3)

entry_search.grid(row=6,column=5)
btn_search.grid(row=7,column=5)
btn_about.grid(row=8,column=5)
btn_exit.grid(row=9,column=5)


main_form.mainloop()