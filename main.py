import tkinter as tk
from tkinter import Button, Checkbutton, Entry, Frame, Label, LabelFrame, StringVar, Tk, ttk, messagebox, Text
from PIL import ImageTk, Image
from colorama import Fore
import json


class App:
    def __init__(self, master):
        self.master = master
        master.title('Resister Calculator')
        master.geometry('500x500')
        master.resizable(True, True)

        # -- VALIABLE --

        self.color = ['None', 'Black', 'Brown', 'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Violet', 'Grey', 'White', 'Gold', 'Silver']

        # -- Tab --

        self.tab = ttk.Notebook(root)
        self.Home = ttk.Frame(self.tab)  # Main tab
        self.Search = ttk.Frame(self.tab) # Seaching tab --In process--
        self.Docs = ttk.Frame(self.tab)

        self.tab.add(self.Home, text='Home')
        self.tab.add(self.Search, text='Search')
        self.tab.add(self.Docs, text='Docs')

        self.tab.pack(expand=1, fill='both')

        # -- Main Page --

        self.select = ttk.Labelframe(self.Home, text='Select Color')
        self.select.place(x=10, y=10)

        self.ans = ttk.Labelframe(self.Home, text='Result :')
        self.ans.place(x=30, y=300)

        # -- Selection Frame --

        self.firstDigitLabel = Label(self.select, text='First Digit')
        self.firstDigitLabel.pack()

        self.firstDigitValue = tk.StringVar()
        self.firstDigit = ttk.Combobox(self.select, textvariable=self.firstDigitValue)  # First Digti Value 
        self.firstDigit['values'] = self.color[:10] # Set array to 0-10 ('None', 'Black', 'Brown', 'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Violet', 'Grey', 'White')
        self.firstDigit['state'] = self.color[0] # Set Start at None

        self.firstDigit.pack(padx=5, pady=5)

        self.secondDigitLabel = Label(self.select, text='Second Digit')
        self.secondDigitLabel.pack()

        self.secondDigitValue = tk.StringVar()
        self.secondDigit = ttk.Combobox(self.select, textvariable=self.secondDigitValue)
        self.secondDigit['values'] = self.color[:10] # Set array to 0-10 ('None', 'Black', 'Brown', 'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Violet', 'Grey', 'White')
        self.secondDigit['state'] = self.color[0] # Set Start at None

        self.secondDigit.pack(padx=5, pady=5)

        self.multiplierDigitLabel = Label(self.select, text='Multiplier')
        self.multiplierDigitLabel.pack()

        self.multiplierDigitValue = tk.StringVar()
        self.multiplierDigit = ttk.Combobox(self.select, textvariable=self.multiplierDigitValue)
        self.multiplierDigit['values'] = self.color[1:] # Didn't has None choice
        self.multiplierDigit['state'] = self.color[0]

        self.multiplierDigit.pack(padx=5, pady=5)

        self.toleranceDigitLabel = Label(self.select, text='Tolerance')
        self.toleranceDigitLabel.pack()

        self.toleranceDigitValue = tk.StringVar()
        self.toleranceDigit = ttk.Combobox(self.select, textvariable=self.toleranceDigitValue)
        self.toleranceDigit['values'] = self.color[2:10] # By ('Brown', 'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Violet', 'Grey')
        self.toleranceDigit['state'] = self.color[0]

        self.toleranceDigit.pack(padx=5, pady=5)

        # Check if Enter Button was pressed then do ShowOutPut Functions

        self.enter = Button(self.select,text='Enter', command=self.showOutput)
        self.enter.pack()

        # Show How many range of Resister in ohm

        self.MintoMaxLab = Label(self.ans)
        self.MintoMaxLab.pack()

        # Show Static Value of Resister in ohm

        self.MediumLab = Label(self.ans)
        self.MediumLab.pack()

        # Show Watt Value in J/s

        self.WattLab = Label(self.ans)
        self.WattLab.pack()

        '''self.WIDTHS = 50
        self.HEIGHTS = 230
        self.resisterImage = Image.open('docs/image/blankResister.png')
        self.imageResize = self.resisterImage.resize((self.WIDTHS, self.HEIGHTS))

        self.img = ImageTk.PhotoImage(self.imageResize)
        self.imgLab = Label(image=self.img)
        self.imgLab.image = self.img

        self.imgLab.place(x=200, y=10)
        '''

        # Setting Color Frame
        
        self.colorFrame = LabelFrame(self.Home, text='Color :')
        self.colorFrame.place(x=200, y=10)

        # First digit color on resister 

        self.colorFirstDigit = Label(self.colorFrame, height=2, width=4)
        self.colorFirstDigit.pack()

        # Second digit color on resister 

        self.colorSecondDigit = Label(self.colorFrame, height=2, width=4)
        self.colorSecondDigit.pack()

        # Multiplier color on resister 
        
        self.colorMultiplierDigit = Label(self.colorFrame, height=2, width=4)
        self.colorMultiplierDigit.pack()

        # Tolerance color on resister

        self.colorToleranceDigit = Label(self.colorFrame, height=2, width=4)
        self.colorToleranceDigit.pack()

        # --- Search Tab --

        self.processLab = Label(self.Search, text='🔧 On Working 🔨')
        self.processLab.pack()

        self.process = ttk.Progressbar(self.Search, orient='horizontal', mode='determinate', length=200)
        self.process.pack()
        self.process.start()

        # --- Documant Page ---

        self.documentFrame = LabelFrame(self.Docs)
        self.documentFrame.pack()
        self.documentText = Text(self.documentFrame)

        with open('Docs/Document.txt') as f: # Get text(Documentation) to <path>
            line = f.readlines()

        x = 4
        for i in reversed(range(len(line))): # Place Text by revese under to above
            self.documentText.insert('1.0', line[i])
            x -= 1

        self.documentText.pack()

    def findingValue(self):
        with open("digitValue.json", "r") as f:  # Read Dictionary data
            data = json.load(f)
        
        number = []
        formula = []

        if self.firstDigitValue.get() != '' and self.firstDigitValue.get() != 'None': # if key name equal color tag
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

    def calculateResister(self):
        lists = self.findingValue()
        self.minimumValue = (lists[0] * lists[1]) - ((lists[0] * lists[1])* lists[2]) # Find minimum range
        self.maximumValue = (lists[0] * lists[1]) + ((lists[0] * lists[1])* lists[2]) # Find maximum range
        self.resistanceValue = self.minimumValue + self.maximumValue / 2

        return [self.minimumValue, self.maximumValue, self.resistanceValue]
            
    def calculateWatt(self):
        lists = self.findingValue()
        return 230 ** 2 / (lists[0] + lists[1])

    def showOutput(self):
        resistance = self.calculateResister()

        self.MintoMaxLab['text'] = f'{resistance[0]} ohm --> {resistance[1]} ohm'
        self.MediumLab['text'] = f'≈ {(resistance[0] + resistance[1]) / 2} ohm'
        self.WattLab['text'] = f'{round(self.calculateWatt(), 2)} Watt'
        
        self.showColor()
    
    def showColor(self):
        with open("digitValue.json", "r") as f: # Read json data file for read color tag
            data = json.load(f)

        formula = []

        if self.firstDigitValue.get() != '' and self.firstDigitValue.get() != 'None':
            for x, y in data.items():
                if self.firstDigitValue.get() == x:
                    self.colorFirstDigit['bg'] = str(x).lower() # Setting configuration on that label so you can't change at all
                    
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


    # -- Frame Search --

        # In process
    


            
if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()