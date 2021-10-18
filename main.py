from tkinter import *

root = Tk()
root.title('Resister calculator')
root.geometry('500x400+500+200')
root.resizable(False, False)

dict = {
    'Black': {
        'digit': 0,
        'multiplier': 1,
        'tolerance': None,
        'temperature': 250
    },
    'Brown': {
        'digit': 1,
        'multiplier': 10,
        'tolerance': 1,
        'temperature': 100
    },
    'Red': {
        'digit': 2,
        'multiplier': 100,
        'tolerance': 2,
        'temperature': 50
    },
    'Orange': {
        'digit': 3,
        'multiplier': 1000,
        'tolerance': None,
        'temperature': 15
    },
    'Yellow': {
        'digit': 4,
        'multiplier': 10000,
        'tolerance': None,
        'temperature': 25
    },
    'Green': {
        'digit': 5,
        'multiplier': 100000,
        'tolerance': 0.5,
        'temperature': 20
    },
    'Blue': {
        'digit': 6,
        'multiplier': 1000000,
        'tolerance': 0.25,
        'temperature': 10
    },
    'Violet': {
        'digit': 7,
        'multiplier': None,
        'tolerance': 0.1,
        'temperature': 5
    },
    'Grey': {
        'digit': 8,
        'multiplier': None,
        'tolerance': None,
        'temperature': 1
    },
    'White': {
        'digit': None,
        'multiplier': None,
        'tolerance': None,
        'temperature': None
    },
    'Gold': {
        'digit': None,
        'multiplier': 0.1,
        'tolerance': 5,
        'temperature': None
    },
    'Silver': {
        'digit': None,
        'multiplier': 0.01,
        'tolerance': 10,
        'temperature': None
    },
}

FONT = ("Helvetica", 14)
PHOTO = 'resistor.png'

sub_menu = Menu()
sub_menu.add_command(label='Resistor color')
sub_menu.add_command(label='Calculator')
sub_menu.add_command(label='About')

main_menu = Menu()
root.config(menu=main_menu)
main_menu.add_cascade(label='Research')
main_menu.add_cascade(label='Documentation', menu=sub_menu)


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
OptionMenu(root, multiplier, 'Black', 'Brown', 'Red', 'Orange', 'Yellow', 'Green', 'Blue').place(x=260, y=100)

tolerance = StringVar()
tolerance.set('Tolerance')
OptionMenu(root, tolerance, 'Brown', 'Red', 'Green', 'Blue', 'Violet', 'Gold', 'Silver').place(x=360, y=100)

temp1 = 1
temp2 = 1
temp3 = 1
temp4 = 1
temp5 = 1

def number():

    global temp1, temp2, temp3, temp4, temp5

    for x, y in dict.items():
        if first_digit.get() == x:
            temp1 = y['digit']
        if first_digit.get() != x:
            temp1 = 0

        if second_digit.get() == x:
            temp2 = y['digit']
        if second_digit.get() != x:
            temp2 = 0

        if third_digit.get() == x:
            temp3 = y['digit']

        if multiplier.get() == x:
            temp4 = y['multiplier']

        if tolerance.get() == x:
            temp5 = y['tolerance']

    num = [temp1, temp2, temp3]
    return int(' '.join(str(num).split(',')).removeprefix('[').removesuffix(']').replace(' ', ''))

def ans():
    return str([round(((number() * int(temp4)) + float(temp5 / 100)), 2),
                round(((number() * int(temp4)) - float(temp5 / 100)), 2)]).replace(',', '-')


def made():
    Label(root, text=f'{number()} * {temp4} ± {temp5} = {ans()} Ω', font=FONT).place(x=100, y=70)
    return None


Button(root, text='Enter', command=made).place(x=220, y=150)

root.mainloop()