from tkinter import *
from digit import *

root = Tk()
root.title('Resister calculator')
root.geometry('500x400+500+200')
root.resizable(False, False)

FONT = ("Helvetica", 14)
PHOTO = 'resistor.png'


def about_page():
    root.destroy()
    about = Tk()
    about.title('About Page')
    about.geometry('500x400+500+200')
    about.resizable(False, False)

    Label(about, text='Hi my name is Narongkorn Kitrungrot 17', font=10).pack()
    Label(about, text='and I made this for Educational and Study Tkinter', font=10).pack()

    about.mainloop()


def problem_page():  # TODO
    root.destroy()
    problem = Tk()
    problem.title('About Page')
    problem.geometry('500x400+500+200')
    problem.resizable(False, False)

    Label(problem, text='Sending Bug , Error case in text box', font=10).place(x=100, y=100)

    reported = StringVar()
    Entry(problem, reported).place(x=100, y=150)
    reported.get()

    la = Label(problem, text='We received your message', font=10).place(x=100, y=200)
    Button(problem, text='Sending Report', command=la).place(x=100, y=180)

    problem.mainloop()


sub_menu = Menu()
sub_menu.add_command(label='Resistor color')
sub_menu.add_command(label='Calculator')
sub_menu.add_command(label='Problem', command=problem_page)
sub_menu.add_command(label='About', command=about_page)

main_menu = Menu()
root.config(menu=main_menu)
main_menu.add_cascade(label='Research')
main_menu.add_cascade(label='Documentation', menu=sub_menu)


Label(root, text='Resister calculator', font=FONT).pack()

img = PhotoImage(file='resister.png')
Label(root, image=img).pack()

first_digit = StringVar()
first_digit.set('1 Digit')
OptionMenu(root, first_digit,
           'None', 'Black', 'Brown', 'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Violet', 'Grey', 'White')\
    .place(x=20, y=200)

second_digit = StringVar()
second_digit.set('2 Digit')
OptionMenu(root, second_digit,
           'None', 'Black', 'Brown', 'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Violet', 'Grey', 'White')\
    .place(x=100, y=200)

third_digit = StringVar()
third_digit.set('3 Digit')
OptionMenu(root, third_digit, 'Black', 'Brown', 'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Violet', 'Grey', 'White')\
    .place(x=180, y=200)

multiplier = StringVar()
multiplier.set('Multiplier')
OptionMenu(root, multiplier, 'Black', 'Brown', 'Red', 'Orange', 'Yellow', 'Green', 'Blue').place(x=260, y=200)

tolerance = StringVar()
tolerance.set('Tolerance')
OptionMenu(root, tolerance, 'Brown', 'Red', 'Green', 'Blue', 'Violet', 'Gold', 'Silver').place(x=360, y=200)


def numbers():

    set_digit = None
    set_digit = [first_digit.get(), second_digit.get(), third_digit.get(), multiplier.get(), tolerance.get()]
    print(sorte(set_digit))

    return sorte(set_digit)

def create():
    #Label(root, text=f'{} * {number[3]} ± {number[4]} = {0} Ω', font=FONT).place(x=100, y=170)
    print(numbers())
    return None


Button(root, text='Enter', command=numbers).place(x=220, y=250)

if __name__ == '__main__':
    root.mainloop()