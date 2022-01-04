import tkinter as tk
from tkinter import Button, Frame, Label, LabelFrame, Tk, ttk, messagebox, Text
import json


class App:
    def __init__(self, master):
        self.master = master
        master.title('Resister Calculator')
        master.geometry('500x500')
        master.resizable(True, True)

        # VALIABLE
        self.color = ['None', 'Black', 'Brown', 'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Violet', 'Grey', 'White', 'Gold', 'Silver']
        self.tab = ttk.Notebook(root)
        self.Home = ttk.Frame(self.tab)
        self.Search = ttk.Frame(self.tab)
        self.Docs = ttk.Frame(self.tab)

        self.tab.add(self.Home, text='Home')
        self.tab.add(self.Search, text='Search')
        self.tab.add(self.Docs, text='Docs')

        self.tab.pack(expand=1, fill='both')

        # -- Main Page --

        self.select = ttk.Labelframe(self.Home, text='Select Color')
        self.select.place(x=10, y=10)

        self.ans = ttk.Labelframe(self.Home, text='Answer :')
        self.ans.place(x=30, y=280)

        self.firstDigitLabel = Label(self.select, text='First Digit')
        self.firstDigitLabel.pack()

        self.firstDigitValue = tk.StringVar()
        self.firstDigit = ttk.Combobox(self.select, textvariable=self.firstDigitValue)
        self.firstDigit['values'] = self.color[:10]
        self.firstDigit['state'] = self.color[0]

        self.firstDigit.pack(padx=5, pady=5)

        self.secondDigitLabel = Label(self.select, text='Second Digit')
        self.secondDigitLabel.pack()

        self.secondDigitValue = tk.StringVar()
        self.secondDigit = ttk.Combobox(self.select, textvariable=self.secondDigitValue)
        self.secondDigit['values'] = self.color[:10]
        self.secondDigit['state'] = self.color[0]

        self.secondDigit.pack(padx=5, pady=5)

        self.multiplierDigitLabel = Label(self.select, text='Multiplier')
        self.multiplierDigitLabel.pack()

        self.multiplierDigitValue = tk.StringVar()
        self.multiplierDigit = ttk.Combobox(self.select, textvariable=self.multiplierDigitValue)
        self.multiplierDigit['values'] = self.color[1:]
        self.multiplierDigit['state'] = self.color[0]

        self.multiplierDigit.pack(padx=5, pady=5)

        self.toleranceDigitLabel = Label(self.select, text='Tolerance')
        self.toleranceDigitLabel.pack()

        self.toleranceDigitValue = tk.StringVar()
        self.toleranceDigit = ttk.Combobox(self.select, textvariable=self.toleranceDigitValue)
        self.toleranceDigit['values'] = self.color[2:10]
        self.toleranceDigit['state'] = self.color[0]

        self.toleranceDigit.pack(padx=5, pady=5)

        self.enter = Button(self.select,text='Enter', command=self.showOutput)
        self.enter.pack()

        self.answerLab = Label(self.ans)
        self.answerLab.pack()

        self.colorFrame = LabelFrame(self.Home, text='Color :')
        self.colorFrame.place(x=200, y=10)

        self.colorFirstDigit = Label(self.colorFrame, height=2, width=4)
        self.colorFirstDigit.pack()

        self.colorSecondDigit = Label(self.colorFrame, height=2, width=4)
        self.colorSecondDigit.pack()
        
        self.colorMultiplierDigit = Label(self.colorFrame, height=2, width=4)
        self.colorMultiplierDigit.pack()

        self.colorToleranceDigit = Label(self.colorFrame, height=2, width=4)
        self.colorToleranceDigit.pack()

        # --- Documant Page ---

        self.documentFrame = LabelFrame(self.Docs)
        self.documentFrame.pack()
        self.documentText = Text(self.documentFrame)

        with open('Docs/Document.txt') as f:
            line = f.readlines()

        x = 4
        for i in reversed(range(len(line))):
            self.documentText.insert('1.0', line[i])
            x -= 1

        self.documentText.pack()

    def findingValue(self):
        with open("digitValue.json", "r") as f:
            data = json.load(f)
        
        number = []
        formula = []

        if self.firstDigitValue.get() != '' and self.firstDigitValue.get() != 'None':
            for x, y in data.items():
                if self.firstDigitValue.get() == x:
                    number.append(y['digit'])
        else:
            number.append(0)
        
        if self.secondDigitValue.get() != '' and self.secondDigitValue.get() != 'None':
            for x, y in data.items():
                if self.secondDigitValue.get() == x:
                    number.append(y['digit'])
        else:
            number.append(0)

        formula.append(int(''.join(str(x) for x in number)))
        
        if self.multiplierDigitValue.get() != '' and self.toleranceDigitValue.get() != '':
            
            for x, y in data.items():
                if self.multiplierDigitValue.get() == x:
                    formula.append(y['multiplier'])

            for x, y in data.items():
                if self.toleranceDigitValue.get() == x:
                    formula.append(y['tolerance'])
        else:
            messagebox.showwarning("Warning", "Are you sure that noting Multiplier, Tolerance ?")

        return formula

    def calculator(self):
        lists = self.findingValue()
        return [((lists[0] * lists[1]) - ((lists[0] * lists[1])* lists[2])), ((lists[0] * lists[1]) + ((lists[0] * lists[1])* lists[2]))]

    def showOutput(self):
        ans = self.calculator()
        minimumValue = ans[0]
        maximumValue = ans[1]

        self.answerLab['text'] = f'{minimumValue} --> {maximumValue}'
        self.showColor()

        return f'{minimumValue} --> {maximumValue}'

    def showColor(self):
        with open("digitValue.json", "r") as f:
            data = json.load(f)

        formula = []

        if self.firstDigitValue.get() != '' and self.firstDigitValue.get() != 'None':
            for x, y in data.items():
                if self.firstDigitValue.get() == x:
                    self.colorFirstDigit['bg'] = str(x).lower()
                    
        if self.secondDigitValue.get() != '' and self.secondDigitValue.get() != 'None':
            for x, y in data.items():
                if self.secondDigitValue.get() == x:
                    self.colorSecondDigit.config(bg = str(x).lower())
                    
        if self.multiplierDigitValue.get() != '' and self.toleranceDigitValue.get() != '':
            for x, y in data.items():
                if self.multiplierDigitValue.get() == x:    
                    self.colorMultiplierDigit.config(bg = str(x).lower())

            for x, y in data.items():
                if self.toleranceDigitValue.get() == x:    
                    self.colorToleranceDigit.config(bg = str(x).lower())

        return formula


    
if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()