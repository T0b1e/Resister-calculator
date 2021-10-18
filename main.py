from tkinter import *
import math

root = Tk()
root.title('Resister calculator')
root.geometry('500x400+500+200')
root.resizable(False, False)

dict = {
    'Black': 0,
    'Brown': 1,
    'Red': 2,
    'Orange': 3,
    'Yellow': 4,
    'Green': 5,
    'Blue': 6,
    'Violet': 7,
    'Grey': 8,
    'White': 9,
}

FONT = ("Helvetica", 14)
PHOTO = 'resister.png'

Label(root, text='Resister calculator', font=FONT).pack()

first_digit = StringVar()
first_digit.set('1 Digit')
OptionMenu(root, first_digit,
           'None', 'Black', 'Brown', 'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Violet', 'Grey', 'White')\
    .place(x=20, y=100)

second_digit = StringVar()
second_digit.set('2 Digit')
OptionMenu(root, second_digit,
           'None', 'Black', 'Brown', 'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Violet', 'Grey', 'White')\
    .place(x=100, y=100)

third_digit = StringVar()
third_digit.set('3 Digit')
OptionMenu(root, third_digit, 'Black', 'Brown', 'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Violet', 'Grey', 'White')\
    .place(x=180, y=100)

multiplier = StringVar()
multiplier.set('Multiplier')
OptionMenu(root, multiplier, '1', '10', '100', '1000', '10,000', '100,000', '1,000,000', '0.1', '0.01').place(x=260, y=100)

tolerance = StringVar()
tolerance.set('Tolerance')
OptionMenu(root, tolerance, '1%', '2%', '0.5%', '0.25%', '0.1%', '5%', '10%').place(x=360, y=100)


def number():
    for x, y in dict.items():
        if first_digit.get() == x:
            temp1 = y
        if first_digit.get() != x:
            temp1 = 0

        if second_digit.get() == x:
            temp2 = y
        if first_digit.get() != x:
            temp2 = 0

        if third_digit.get() == x:
            temp3 = y

    num = [temp1, temp2, temp3]
    return int(' '.join(str(num).split(',')).removeprefix('[').removesuffix(']').replace(' ', ''))


def ans():
    return math.floor(number() * int(multiplier.get()) + float(((tolerance.get()).split('%'))[0]) / 100)


def made():
    Label(root, text=f'{number()} * {multiplier.get()} ± {tolerance.get()} = {ans()}', font=FONT).place(x=150, y=70)
    return None


Button(root, text='Enter', command=made).place(x=220, y=150)

root.mainloop()