#!/usr/bin/env python
"""
Conversion Central - Unit Converter
Developed by Caleb Landis
Version: Alpha 1.2

Necessary items to ensure are downloaded:
    python 3
    tkinter
    pip
    pyshortcuts

To do:
    Eventually add settings page to ask for permission to add Conversion Central to desktop and/or startmenu
    Figure out how to have user download all necessary items to run Conversion Central
    Create simple web page where user can download Conversion Central
"""

# import all necessary items from tkinter
from tkinter import *
from tkinter import StringVar
from tkinter import OptionMenu
from tkinter import messagebox
#import pdb
# create desktop shortcut for application
#from pyshortcuts import *
#from pyshortcuts import make_shortcut

"""
# import extra modules to build app?
from com import *
from dbm import *
from asyncio import *
from pkg_resources import *
from win32com import *
"""

# python debugger
# pdb.set_trace()

"""
# locates this python script and other pertaining information in order to create desktop shortcut
make_shortcut('/Applications/Conversion Central/ConversionCentral.py',
              name='Conversion Central',
              description='Unit Converter',
              folder=None,
              icon='/Applications/Conversion Central/Icon.icns',
              terminal=False, desktop=True, startmenu=True,
              executable='/Library/Frameworks/Python.framework/Versions/3.9/bin/python3.9')
"""

# Conversion Central's icon was made by Left Martinez, and downloaded from (https://www.iconfinder.com/iconsets/free-construction-tools)
# This icon is being used purely for learning and experimental purposes. Conversion Central is a free application that serves as a project for me to learn and practice.


# create a class called "App" passing the value (Tk)
class App(Tk):
    # in "App", create an initializer function that initializes "self"
    def __init__(self):
        #initialize Tk
        Tk.__init__(self)

        # identify the initial visual attributes of the window in "App"
        # define headerFont, window title, size of window, and background color
        self.headerFont = ("System", "15", "bold italic")
        self.title("Conversion Central - Unit Converter")
        self.geometry("553x300")
        self["bg"] = "#FFFF99"

        # create a variable called "optionList" with a list of all measurement types
        optionList = ["Length", "Mass", "Volume", "Temperature", "Time"]
        # createa a variable called "variable" and make it global
        global variable
        # make "variable" a string variable
        variable = StringVar(self)
        # in variable, set the current measurement type to the first option to be seen in optionMenu
        variable.set(optionList[0])
        # create a variable called "option" that contains an optionMenu with setting from "variable" and displays everything in "optionList"
        # when a user interacts with "option", execute "measurementType()"
        option = OptionMenu(self, variable, *optionList, command = self.measurementType)
        # insert "option" into grid at the top left corner of the UI, with sticky = "w"
        option.grid(row = 0, column = 0, padx = 8, sticky = "w")

        # create a variable called "Menu" that adds a functional menu bar
        # add menu to program
        menuBar = Menu(self)
        self.config(menu = menuBar)

        # create a variable called "fileMenu" that creates a file menu
        # will be used to add a "File" tab to the menu bar
        fileMenu = Menu(menuBar)
        # add a command to "fileMenu" called "Help: Conversion" that executes "helpConversion()" when selected
        fileMenu.add_command(label = "Help: Conversion", command = self.helpConversion)
        # add a command to "fileMenu" called "Help: Measurement Types" that executes "helpType()" when selected
        fileMenu.add_command(label = "Help: Measurement Types", command = self.helpType)
        # add a command to "fileMenu called "Settings" that executes "settings()" when selected
        fileMenu.add_command(label = "Settings", command = self.openSettings)
        # add a command to "fileMenu" called "Exit" that executes "exitProgram()" when selected
        fileMenu.add_command(label = "Exit", command = self.exitProgram)
        # add "File" menu to the menu bar
        menuBar.add_cascade(label = "File", menu = fileMenu)

        # execute "length()"
        # is the initial measurement type that the user is first welcomed to
        self.length()

    # create a function called "measurementType" passing "self" and "event" as parameters
    # used as event command for optionMenu
    def measurementType(self, event):
        # if the first value in optionMenu gets "Length", clear last grid and execute "length()"
        # executes "forget()" to clear last grid
        if variable.get() == "Length":
            self.forget()
            self.length()
        # if the first value in optionMenu gets "Mass", clear last grid and execute "mass()"
        # executes "forget()" to clear last grid
        elif variable.get() == "Mass":
            self.forget()
            self.mass()
        # if the first value in optionMenu gets "Volume", clear last grid and execute "volume()"
        # executes "forget()" to clear last grid
        elif variable.get() == "Volume":
            self.forget()
            self.volume()
        # if the first value in optionMenu gets "Temperature", clear last grid and execute "temp()"
        # executes "forget()" to clear last grid
        elif variable.get() == "Temperature":
            self.forget()
            self.temp()
        # if the first value in optionMenu gets "Time", clear last grid and execute "time()"
        # executes "forget()" to clear last grid
        else:
            self.forget()
            self.time()

    # create a function called "forget" passing "self" as a parameter
    # used to clear last grid when changing between measurment types with optionMenu
    def forget(self):
        # clear "conversionCentral" label
        self.conversionCentral.grid_forget()
        # clear "txtMeasurement1" entry
        self.txtMeasurement1.grid_forget()
        # clear "arrow" label
        self.arrow.grid_forget()
        # clear "txtMeasurement2" label
        self.txtMeasurement2.grid_forget()
        # clear "units1" Listbox
        self.units1.grid_forget()
        # clear "convert" button
        self.convert.grid_forget()
        # clear "units2" Listbox
        self.units2.grid_forget()

    # create a function called "helpConversion" passing "self" as a parameter
    # displays a pop up window that tells the user how to calculate a conversion
    def helpConversion(self):
        messagebox.showinfo(title = "Help: Conversion", message = "To calculate a conversion, type in the current value of the measurement, select which unit the measurement is currently in and the desired unit after conversion. Click the convert button, and Conversion Central calculates the result instantly!")

    # create a function called "helpType(self)" passing "self" as a parameter
    # displays a pop up window that tells the user how to switch between measurement types
    def helpType(self):
        messagebox.showinfo(title = "Help: Type", message = "Users can choose between multiple different types of measurements to convert: length, mass, volume, temperature, and time. To switch between these, click on the drop down menu at the top left corner of the screen and select desired measurement type.")

    # create a function called "settings(self)" passing "self" as a parameter
    # displays a new window with settings to create a desktop and/or start menu shortcut
    def openSettings(self):
        settings.__init__(self)
        # settings.createWindow(self)

    # create a function called "exitProgram" passing "self" as a paramter and executes "exit()"
    # used to exit program when user selects "Exit" command in menu bar
    def exitProgram(self):
        exit()

    # create a function called "length" passing "self" as a parameter
    # sets up Length UI grid
    def length(self):
        # set window dimensions when selected
        self.geometry("553x300")

        # create a variable called "conversionCentral" and make it a label widget
        self.conversionCentral = Label(self, text = "Conversion Central", font = self.headerFont, bg = "#FFFF99")
        # add "conversionCentral" to top center grid and add y padding
        self.conversionCentral.grid(row = 0, column = 1, pady = 5)

        # create a variable called "txtMeasurement1" and make it an entry widget for user input
        self.txtMeasurement1 = Entry(self)
        # add "txtMeasurement1" to middle left grid and add x and y padding
        self.txtMeasurement1.grid(row = 1, column = 0, padx = 8, pady = 10)

        # create a variable called "arrow" and make it a label widget
        self.arrow = Label(self, text = "----->", font = self.headerFont, bg = "#FFFF99")
        # add "arrow' to center of grid
        self.arrow.grid(row = 1, column = 1)

        # create a variable called "txtMeasurement2" and make it a label with anchor = "w" and a groove relief
        self.txtMeasurement2 = Label(self, bg = "#fff", anchor = "w", relief = "groove")
        # add "txtMeasurement2" to middle right grid with sticky = "we"
        self.txtMeasurement2.grid(row = 1, column = 2, sticky = "we")

        # create a variable called "units1" and make it a Listbox widget
        # exportselection lets the user select from both Listboxes instead of only one selection being made at a time
        self.units1 = Listbox(self, height = 11, exportselection = 0)
        # add "units1" to bottom left grid and add y padding
        self.units1.grid(row = 2, column = 0, pady = 10)
        # insert length measurements into "units1" Listbox
        self.units1.insert(END, "Kilometer", "Hectometer", "Decameter", "Meter", "Decimeter", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch")

        # create a variable called "convert" and make it a button widget
        self.convert = Button(self, text = "Convert to")
        # add "convert" to bottom middle grid
        self.convert.grid(row = 2, column = 1)
        # when "convert" gets clicked on, execute "checkLengthSel()"
        self.convert["command"] = self.checkLengthSel

        # create a variable called "units2" and make it a Listbox widget
        # exportselection lets the user select from both Listboxes instead of only one selection being made at a time
        self.units2 = Listbox(self, height = 11, exportselection = 0)
        # add "units2" to bottom right grid
        self.units2.grid(row = 2, column = 2)
        # insert length measurments into "units2" Listbox
        self.units2.insert(END, "Kilometer", "Hectometer", "Decameter", "Meter", "Decimeter", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch")


        """
        used for matching rows and collumns to window resizing
        probably won't use because it looks ugly

        for g in range(3):
            self.grid_rowconfigure(g, weight=1)
            self.grid_columnconfigure(g, weight=1)
        """

    # create a function called "checkLengthSel" passing "self" as a parameter
    # used to make sure the user selects units to convert from and to
    def checkLengthSel(self):
        # create a variable called "selected1" that goes through all of "units1"
        selected1 = self.units1.curselection()
        # create a variable called "selected2" that goes through all of "units2"
        selected2 = self.units2.curselection()
        # create a variable called "measurement" that gets the value from "txtMeasurement1"
        measurement = self.txtMeasurement1.get()
        # create a variable called "checkInt" that exececutes "checkInt()"
        checkInt = self.checkInt()
        # execute "checkInt()"
        checkInt

        # if "selected1" doesn't find a selection from "units1", execute "noUnit1" to inform the user
        if selected1 == ():
            self.noUnit1()
        # if "selected2" doesn't find a selection from "units2", execute "noUnit2" to inform the user
        elif selected2 == ():
            self.noUnit2()
        # if the user does not input anything into "txtMeasurement1", execute "invalideMeasurement()" to inform the user
        elif measurement == "":
            self.invalidMeasurement()
        # if measurement gets something that is not an integer, execute "invalidMeasurement()" to inform the user
        elif checkInt == False:
            self.invalidMeasurement()
        else:
            # create a variable called "selValue1" that gets the selectied option from "units1"
            selValue1 = self.units1.get(selected1[0])
            # create a variable called "baseUnit" with initial value "lengthConverter1()"
            baseUnit = self.lengthConverter1()
            # execute "lengthConverter1"
            baseUnit
            # execute "lengthConverter2" passing the returned value from "lengthConverter1"
            self.lengthConverter2(baseUnit)

    # create a function called "noUnit1" passing the parameter "self"
    # used to notify user through a messagebox if they did not select an input unit
    def noUnit1(self):
        messagebox.showinfo(title = "No Input Unit Selected", message = "No input unit selected. Please select a unit to convert from.")

    # create a function called "noUnit2" passing the parameter "self"
    # used to notify user through a messagebox if they did not select an output unit
    def noUnit2(self):
        messagebox.showinfo(title = "No Output Unit Selected", message = "No output unit selected. Please select a unit to convert to.")

    # create a function called "checkInt" passing the parameter "self"
    # used to check to see if the user entered a measurement that is an integer
    def checkInt(self):
        # create a variable called "measurement" that gets the value from "txtMeasurement1"
        measurement = self.txtMeasurement1.get()
        # if measurement gets a digit, return "True"
        # if not, return "False"
        if measurement.isdigit():
            return True
        return False

    # create a function called "invalidMeasurement" passing the parameter "self"
    # used to notify user through a messagebox that the measurement they entered is not valid
    def invalidMeasurement(self):
        messagebox.showinfo(title = "Invalid Measurement Entered", message = "Invalid measurement entered. Please enter a measurement in the form of an integer to convert.")

    # create a function called "lengthConverter1" passing self as a parameter and returns a value of "baseUnit"
    # converts measurement from selected unit in "units1" to a base unit
    # makes calculation process much easier
    def lengthConverter1(self):
        # create a variable called "measurement" that gets user input from "txtMeasurement1" and makes it floating point
        measurement = float(self.txtMeasurement1.get())
        # create a variable called "selected1" that goes through all units in "units1"
        selected1 = self.units1.curselection()
        # create a variable called "selValue1" that gets user's selected unit from "units1"
        selValue1 = self.units1.get(selected1[0])

        # meters is base unit
        # if selected, convert kilometers to meters and return its value
        if selValue1 == "Kilometer":
            baseUnit = measurement*1000
            return baseUnit
        # if selected, convert hectometers to meters and return its value
        elif selValue1 == "Hectometer":
            baseUnit = measurement*100
            return baseUnit
        # if selected, convert decameters to meters and return its value
        elif selValue1 == "Decameter":
            baseUnit = measurement*10
            return baseUnit
        # if selected, convert decimeters to meters and return its value
        elif selValue1 == "Decimeter":
            baseUnit = measurement/10
            return baseUnit
        # if selected, convert centimeters to meters and return its value
        elif selValue1 == "Centimeter":
            baseUnit = measurement/100
            return baseUnit
        # if selected, convert millimeters to meters and return its value
        elif selValue1 == "Millimeter":
            baseUnit = measurement/1000
            return baseUnit
        # if selected, convert miles to meters and return its value
        elif selValue1 == "Mile":
            baseUnit = measurement*(1609.34)
            return baseUnit
        # if selected, convert yards to meters and return its value
        elif selValue1 == "Yard":
            baseUnit = measurement*(0.9144)
            return baseUnit
        # if selected, convert feet to meters and return its value
        elif selValue1 == "Foot":
            baseUnit = measurement*(0.3048)
            return baseUnit
        # if selected, convert inches to meters and return its value
        elif selValue1 == "Inch":
            baseUnit = measurement*(0.0254)
            return baseUnit
        else:
            # meters is selected and is already the base unit
            # return "baseUnit"
            baseUnit = measurement
            baseUnit = float(baseUnit)
            return baseUnit

    # create a function called "lengthConverter2" passing "self" and "baseUnit" as parameters
    # converts measurement from baseUnit to selected unit in "units2"
    def lengthConverter2(self, baseUnit):
        # create a variable called "selected2" that goes through all units in "units2"
        selected2 = self.units2.curselection()
        # create a variable called "selValue1" that gets user's selected unit from "units1"
        selValue2 = self.units2.get(selected2[0])

        # if selected, convert baseUnit to kilometers and display calculation in "txtMeasurement2"
        if selValue2 == "Kilometer":
            result = baseUnit/1000
            self.txtMeasurement2["text"] = "{}".format(result)
        # if selected, convert baseUnit to hectometers and display calculation in "txtMeasurement2"
        elif selValue2 == "Hectometer":
            result = baseUnit/100
            self.txtMeasurement2["text"] = "{}".format(result)
        # if selected, convert baseUnit to decameters and display calculation in "txtMeasurement2"
        elif selValue2 == "Decameter":
            result = baseUnit/10
            self.txtMeasurement2["text"] = "{}".format(result)
        # if selected, convert baseUnit to decimeters and display calculation in "txtMeasurement2"
        elif selValue2 == "Decimeter":
            result = baseUnit*10
            self.txtMeasurement2["text"] = "{}".format(result)
        # if selected, convert baseUnit to centimeters and display calculation in "txtMeasurement2"
        elif selValue2 == "Centimeter":
            result = baseUnit*100
            self.txtMeasurement2["text"] = "{}".format(result)
        # if selected, convert baseUnit to millimeters and display calculation in "txtMeasurement2"
        elif selValue2 == "Millimeter":
            result = baseUnit*1000
            self.txtMeasurement2["text"] = "{}".format(result)
        # if selected, convert baseUnit to miles and display calculation in "txtMeasurement2"
        elif selValue2 == "Mile":
            result = baseUnit*(0.000621371)
            self.txtMeasurement2["text"] = "{}".format(result)
        # if selected, convert baseUnit to yards and display calculation in "txtMeasurement2"
        elif selValue2 == "Yard":
            result = baseUnit*(1.09361)
            self.txtMeasurement2["text"] = "{}".format(result)
        # if selected, convert baseUnit to feet and display calculation in "txtMeasurement2"
        elif selValue2 == "Foot":
            result = baseUnit*(3.28084)
            self.txtMeasurement2["text"] = "{}".format(result)
        # if selected, convert baseUnit to inches and display calculation in "txtMeasurement2"
        elif selValue2 == "Inch":
            result = baseUnit*(39.3701)
            self.txtMeasurement2["text"] = "{}".format(result)
        else:
            # meters is selected and is already the base unit
            # display calculation in "txtMeasurement2"
            result = baseUnit
            result = float(result)
            self.txtMeasurement2["text"] = "{}".format(result)

    # the rest of the "App" object is essentially just the length functions repeated with everything formatted for the different measurement types

    # create a function called "mass" passing "self" as a parameter
    # sets up Mass UI grid
    def mass(self):
        # set window dimensions when selected
        self.geometry("553x300")

        # create a variable called "conversionCentral" and make it a label widget
        self.conversionCentral = Label(self, text = "Conversion Central", font = self.headerFont, bg = "#FFFF99")
        # add "conversionCentral" to top center grid and add y padding
        self.conversionCentral.grid(row = 0, column = 1, pady = 5)

        # create a variable called "txtMeasurement1" and make it an entry widget for user input
        self.txtMeasurement1 = Entry(self)
        # add "txtMeasurement1" to middle left grid and add x and y padding
        self.txtMeasurement1.grid(row = 1, column = 0, padx = 8, pady = 10)

        # create a variable called "arrow" and make it a label widget
        self.arrow = Label(self, text = "----->", font = self.headerFont, bg = "#FFFF99")
        # add "arrow' to center of grid
        self.arrow.grid(row = 1, column = 1)

        # create a variable called "txtMeasurement2" and make it a label with anchor = "w" and a groove relief
        self.txtMeasurement2 = Label(self, bg = "#fff", anchor = "w", relief = "groove")
        # add "txtMeasurement2" to middle right grid with sticky = "we"
        self.txtMeasurement2.grid(row = 1, column = 2, sticky = "we")

        # create a variable called "units1" and make it a Listbox widget
        # exportselection lets the user select from both Listboxes instead of only one selection being made at a time
        self.units1 = Listbox(self, height = 11, exportselection = 0)
        # add "units1" to bottom left grid and add y padding
        self.units1.grid(row = 2, column = 0, pady = 10)
        # insert mass measurements into "units1" Listbox
        self.units1.insert(END, "Kilogram", "Hectogram", "Decagram", "Gram", "Decigram", "Centigram", "Milligram", "Metric Ton", "US Ton", "Pound", "Ounce")

        # create a variable called "convert" and make it a button widget
        self.convert = Button(self, text = "Convert to")
        # add "convert" to bottom middle grid
        self.convert.grid(row = 2, column = 1)
        # when "convert" gets clicked on, execute "checkVolumeSel()"
        self.convert["command"] = self.checkMassSel

        # create a variable called "units2" and make it a Listbox widget
        #exportselection lets the user select from both Listboxes instead of only one selection being made at a time
        self.units2 = Listbox(self, height = 11, exportselection = 0)
        # add "units2" to bottom right grid
        self.units2.grid(row = 2, column = 2)
        # insert mass measurments into "units2" Listbox
        self.units2.insert(END, "Kilogram", "Hectogram", "Decagram", "Gram", "Decigram", "Centigram", "Milligram", "Metric Ton", "US Ton", "Pound", "Ounce")

    # create a function called "checkMassSel" passing "self" as a parameter
    # used to make sure the user selects units to convert from and to
    def checkMassSel(self):
        # create a variable called "selected1" that goes through all of "units1"
        selected1 = self.units1.curselection()
        # create a variable called "selected2" that goes through all of "units2"
        selected2 = self.units2.curselection()
        # create a variable called "measurement" that gets the value from "txtMeasurement1"
        measurement = self.txtMeasurement1.get()
        # create a variable called "checkInt" that exececutes "checkInt()"
        checkInt = self.checkInt()
        # execute "checkInt()"
        checkInt

        # if "selected1" doesn't find a selection from "units1", execute "noUnit1" to inform the user
        if selected1 == ():
            self.noUnit1()
        # if "selected2" doesn't find a selection from "units2", execute "noUnit2" to inform the user
        elif selected2 == ():
            self.noUnit2()
        # if the user does not input anything into "txtMeasurement1", execute "invalideMeasurement()" to inform the user
        elif measurement == "":
            self.invalidMeasurement()
        # if measurement gets something that is not an integer, execute "invalidMeasurement()" to inform the user
        elif checkInt == False:
            self.invalidMeasurement()
        else:
            # create a variable called "selValue1" that gets the selectied option from "units1"
            selValue1 = self.units1.get(selected1[0])
            # create a variable called "baseUnit" with initial value "massConverter1()"
            baseUnit = self.massConverter1()
            # execute "massConverter1"
            baseUnit
            # execute "massConverter2" passing the returned value from "massConverter1"
            self.massConverter2(baseUnit)

    # create a function called "massConverter1" passing self as a parameter and returns a value of "baseUnit"
    # converts measurement from selected unit in "units1" to a base unit
    def massConverter1(self):
        # create a variable called "measurement" that gets user input from "txtMeasurement1" and makes it floating point
        measurement = float(self.txtMeasurement1.get())
        # create a variable called "selected1" that goes through all units in "units1"
        selected1 = self.units1.curselection()
        # create a variable called "selValue1" that gets user's selected unit from "units1"
        selValue1 = self.units1.get(selected1[0])

        # grams is base unit
        # if selected, convert kilograms to grams and return its value
        if selValue1 == "Kilogram":
            baseUnit = measurement*1000
            return baseUnit
        # if selected, convert hectograms to grams and return its value
        elif selValue1 == "Hectogram":
            baseUnit = measurement*100
            return baseUnit
        # if selected, convert decagrams to grams and return its value
        elif selValue1 == "Decagram":
            baseUnit = measurement*10
            return baseUnit
        # if selected, convert decigram to grams and return its value
        elif selValue1 == "Decigram":
            baseUnit = measurement/10
            return baseUnit
        # if selected, convert centigrams to grams and return its value
        elif selValue1 == "Centigram":
            baseUnit = measurement/100
            return baseUnit
        # if selected, convert milligrams to grams and return its value
        elif selValue1 == "Milligram":
            baseUnit = measurement/1000
            return baseUnit
        # if selected, convert metric tons to grams and return its value
        elif selValue1 == "Metric Ton":
            baseUnit = measurement*(1000000)
            return baseUnit
        # if selected, convert US tons to grams and return its value
        elif selValue1 == "US Ton":
            baseUnit = measurement*(907185)
            return baseUnit
        # if selected, convert pounds to grams and return its value
        elif selValue1 == "Pound":
            baseUnit = measurement*(453.592)
            return baseUnit
        # if selected, convert ounces to grams and return its value
        elif selValue1 == "Ounce":
            baseUnit = measurement*(28.3495)
            return baseUnit
        else:
            # grams is selected and is already the base unit
            # return "BaseUnit"
            baseUnit = measurement
            baseUnit = float(baseUnit)
            return baseUnit

    # create a function called "massConverter2" passing "self" and "baseUnit" as parameters
    # converts measurement from baseUnit to selected unit in "units2"
    def massConverter2(self, baseUnit):
        # create a variable called "selected2" that goes through all units in "units2"
        selected2 = self.units2.curselection()
        # create a variable called "selValue1" that gets user's selected unit from "units1"
        selValue2 = self.units2.get(selected2[0])

        # if selected, convert baseUnit to kilograms and display calculation in "txtMeasurement2"
        if selValue2 == "Kilogram":
            result = baseUnit/1000
            self.txtMeasurement2["text"] = "{}".format(result)
        # if selected, convert baseUnit to hectograms and display calculation in "txtMeasurement2"
        elif selValue2 == "Hectogram":
            result = baseUnit/100
            self.txtMeasurement2["text"] = "{}".format(result)
        # if selected, convert baseUnit to decagrams and display calculation in "txtMeasurement2"
        elif selValue2 == "Decagram":
            result = baseUnit/10
            self.txtMeasurement2["text"] = "{}".format(result)
        # if selected, convert baseUnit to decigrams and display calculation in "txtMeasurement2"
        elif selValue2 == "Decigram":
            result = baseUnit*10
            self.txtMeasurement2["text"] = "{}".format(result)
        # if selected, convert baseUnit to centigrams and display calculation in "txtMeasurement2"
        elif selValue2 == "Centigram":
            result = baseUnit*100
            self.txtMeasurement2["text"] = "{}".format(result)
            # if selected, convert baseUnit to milligrams and display calculation in "txtMeasurement2"
        elif selValue2 == "Milligram":
            result = baseUnit*1000
            self.txtMeasurement2["text"] = "{}".format(result)
        # if selected, convert baseUnit to metric tons and display calculation in "txtMeasurement2"
        elif selValue2 == "Metric Ton":
            result = baseUnit/(1000000)
            self.txtMeasurement2["text"] = "{}".format(result)
        # if selected, convert baseUnit to US tons and display calculation in "txtMeasurement2"
        elif selValue2 == "US Ton":
            result = baseUnit*(0.0000011023)
            self.txtMeasurement2["text"] = "{}".format(result)
        # if selected, convert baseUnit to pounds and display calculation in "txtMeasurement2"
        elif selValue2 == "Pound":
            result = baseUnit*(0.00220462)
            self.txtMeasurement2["text"] = "{}".format(result)
        # if selected, convert baseUnit to ounces and display calculation in "txtMeasurement2"
        elif selValue2 == "Ounce":
            result = baseUnit*(0.035274)
            self.txtMeasurement2["text"] = "{}".format(result)
        else:
            # grams is selected and is already the base unit
            # display calculation in "txtMeasurement2"
            result = baseUnit
            result = float(result)
            self.txtMeasurement2["text"] = "{}".format(result)

    # create a function called "volume" passing "self" as a parameter
    # sets up Volume UI grid
    def volume(self):
        # set window dimensions when selected
        self.geometry("553x275")

        # create a variable called "conversionCentral" and make it a label widget
        self.conversionCentral = Label(self, text = "Conversion Central", font = self.headerFont, bg = "#FFFF99")
        # add "conversionCentral" to top center grid and add y padding
        self.conversionCentral.grid(row = 0, column = 1, pady = 5)

        # create a variable called "txtMeasurement1" and make it an entry widget for user input
        self.txtMeasurement1 = Entry(self)
        # add "txtMeasurement1" to middle left grid and add x and y padding
        self.txtMeasurement1.grid(row = 1, column = 0, padx = 8, pady = 10)

        # create a variable called "arrow" and make it a label widget
        self.arrow = Label(self, text = "----->", font = self.headerFont, bg = "#FFFF99")
        # add "arrow' to center of grid
        self.arrow.grid(row = 1, column = 1)

        # create a variable called "txtMeasurement2" and make it a label with anchor = "w" and a groove relief
        self.txtMeasurement2 = Label(self, bg = "#fff", anchor = "w", relief = "groove")
        # add "txtMeasurement2" to middle right grid with sticky = "we"
        self.txtMeasurement2.grid(row = 1, column = 2, sticky = "we")

        # create a variable called "units1" and make it a Listbox widget
        # exportselection lets the user select from both Listboxes instead of only one selection being made at a time
        self.units1 = Listbox(self, height = 9, exportselection = 0)
        # add "units1" to bottom left grid and add y padding
        self.units1.grid(row = 2, column = 0, pady = 10)
        # insert volume measurements into "units1" Listbox
        self.units1.insert(END, "US Liquid Gallon", "US Liquid Quart", "US Liquid Pint", "US Legal Cup", "US Fluid Ounce", "US Tablespoon", "US Teaspoon", "Liter", "Milliliter")

        # create a variable called "convert" and make it a button widget
        self.convert = Button(self, text = "Convert to")
        # add "convert" to bottom middle grid
        self.convert.grid(row = 2, column = 1)
        # when "convert" gets clicked on, execute "checkVolumeSel()"
        self.convert["command"] = self.checkVolumeSel

        # create a variable called "units2" and make it a Listbox widget
        #exportselection lets the user select from both Listboxes instead of only one selection being made at a time
        self.units2 = Listbox(self, height = 9, exportselection = 0)
        # add "units2" to bottom right grid
        self.units2.grid(row = 2, column = 2)
        # insert volume measurments into "units2" Listbox
        self.units2.insert(END, "US Liquid Gallon", "US Liquid Quart", "US Liquid Pint", "US Legal Cup", "US Fluid Ounce", "US Tablespoon", "US Teaspoon", "Liter", "Milliliter")

    # create a function called "checkVolumeSel" passing "self" as a parameter
    # used to make sure the user selects units to convert from and to
    def checkVolumeSel(self):
        # create a variable called "selected1" that goes through all of "units1"
        selected1 = self.units1.curselection()
        # create a variable called "selected2" that goes through all of "units2"
        selected2 = self.units2.curselection()
        # create a variable called "measurement" that gets the value from "txtMeasurement1"
        measurement = self.txtMeasurement1.get()
        # create a variable called "checkInt" that exececutes "checkInt()"
        checkInt = self.checkInt()
        # execute "checkInt()"
        checkInt

        # if "selected1" doesn't find a selection from "units1", execute "noUnit1" to inform the user
        if selected1 == ():
            self.noUnit1()
        # if "selected2" doesn't find a selection from "units2", execute "noUnit2" to inform the user
        elif selected2 == ():
            self.noUnit2()
        # if the user does not input anything into "txtMeasurement1", execute "invalideMeasurement()" to inform the user
        elif measurement == "":
            self.invalidMeasurement()
        # if measurement gets something that is not an integer, execute "invalidMeasurement()" to inform the user
        elif checkInt == False:
            self.invalidMeasurement()
        else:
            # create a variable called "selValue1" that gets the selectied option from "units1"
            selValue1 = self.units1.get(selected1[0])
            # create a variable called "baseUnit" with initial value "volumeConverter1()"
            baseUnit = self.volumeConverter1()
            # execute "volumeConverter1"
            baseUnit
            # execute "volumeConverter2" passing the returned value from "volumeConverter1"
            self.volumeConverter2(baseUnit)

    # create a function called "volumeConverter1" passing self as a parameter and returns a value of "baseUnit"
    # converts measurement from selected unit in "units1" to a base unit
    def volumeConverter1(self):
        # create a variable called "measurement" that gets user input from "txtMeasurement1" and makes it floating point
        measurement = float(self.txtMeasurement1.get())
        # create a variable called "selected1" that goes through all units in "units1"
        selected1 = self.units1.curselection()
        # create a variable called "selValue1" that gets user's selected unit from "units1"
        selValue1 = self.units1.get(selected1[0])

        # liters is base unit
        # if selected, convert US Liquid Gallon to liters and return its value
        if selValue1 == "US Liquid Gallon":
            baseUnit = measurement*(3.785)
            return baseUnit
        # if selected, convert US Liquid Quart to liters and return its value
        elif selValue1 == "US Liquid Quart":
            baseUnit = measurement/(1.057)
            return baseUnit
        # if selected, convert US Liquid Pint to liters and return its value
        elif selValue1 == "US Liquid Pint":
            baseUnit = measurement/(2.113)
            return baseUnit
        # if selected, convert US Legal Cup to liters and return its value
        elif selValue1 == "US Legal Cup":
            baseUnit = measurement/(4.167)
            return baseUnit
        # if selected, convert US Fluid Oz to liters and return its value
        elif selValue1 == "US Fluid Ounce":
            baseUnit = measurement/(33.814)
            return baseUnit
        # if selected, convert US Tablespoon to liters and return its value
        elif selValue1 == "US Tablespoon":
            baseUnit = measurement/(67.628)
            return baseUnit
        # if selected, convert US Teaspoon to liters and return its value
        elif selValue1 == "US Teaspoon":
            baseUnit = measurement/(203)
            return baseUnit
        # if selected, convert Milliliters to liters and return its value
        elif selValue1 == "Milliliter":
            baseUnit = measurement/1000
            return baseUnit
        else:
            # liters is selected and is already the base unit
            # return "BaseUnit"
            baseUnit = measurement
            baseUnit = float(baseUnit)
            return baseUnit

    # create a function called "massConverter2" passing "self" and "baseUnit" as parameters
    # converts measurement from baseUnit to selected unit in "units2"
    def volumeConverter2(self, baseUnit):
        # create a variable called "selected2" that goes through all units in "units2"
        selected2 = self.units2.curselection()
        # create a variable called "selValue1" that gets user's selected unit from "units1"
        selValue2 = self.units2.get(selected2[0])

        # if selected, convert baseUnit to US Liquid Gallon and display calculation in "txtMeasurement2"
        if selValue2 == "US Liquid Gallon":
            result = baseUnit/(3.785)
            self.txtMeasurement2["text"] = "{}".format(result)
        # if selected, convert baseUnit to US Liquid Quart and display calculation in "txtMeasurement2"
        elif selValue2 == "US Liquid Quart":
            result = baseUnit*(1.057)
            self.txtMeasurement2["text"] = "{}".format(result)
        # if selected, convert baseUnit to US Liquid Pint and display calculation in "txtMeasurement2"
        elif selValue2 == "US Liquid Pint":
            result = baseUnit*(2.113)
            self.txtMeasurement2["text"] = "{}".format(result)
        # if selected, convert baseUnit to US Legal Cup and display calculation in "txtMeasurement2"
        elif selValue2 == "US Legal Cup":
            result = baseUnit*(4.167)
            self.txtMeasurement2["text"] = "{}".format(result)
        # if selected, convert baseUnit to US Fluid Oz and display calculation in "txtMeasurement2"
        elif selValue2 == "US Fluid Ounce":
            result = baseUnit*(33.814)
            self.txtMeasurement2["text"] = "{}".format(result)
            # if selected, convert baseUnit to US Tablespoon and display calculation in "txtMeasurement2"
        elif selValue2 == "US Tablespoon":
            result = baseUnit*(67.628)
            self.txtMeasurement2["text"] = "{}".format(result)
        # if selected, convert baseUnit to US Teaspoon and display calculation in "txtMeasurement2"
        elif selValue2 == "US Teaspoon":
            result = baseUnit*(203)
            self.txtMeasurement2["text"] = "{}".format(result)
        # if selected, convert baseUnit to Milliliters and display calculation in "txtMeasurement2"
        elif selValue2 == "Milliliter":
            result = baseUnit*1000
            self.txtMeasurement2["text"] = "{}".format(result)
        else:
            # liters is selected and is already the base unit
            # display calculation in "txtMeasurement2"
            result = baseUnit
            result = float(result)
            self.txtMeasurement2["text"] = "{}".format(result)

    # create a function called "temp" passing "self" as a parameter
    # sets up Temperature UI grid
    def temp(self):
        # set window dimensions when selected
        self.geometry("553x175")

        # create a variable called "conversionCentral" and make it a label widget
        self.conversionCentral = Label(self, text = "Conversion Central", font = self.headerFont, bg = "#FFFF99")
        # add "conversionCentral" to top center grid and add y padding
        self.conversionCentral.grid(row = 0, column = 1, pady = 5)

        # create a variable called "txtMeasurement1" and make it an entry widget for user input
        self.txtMeasurement1 = Entry(self)
        # add "txtMeasurement1" to middle left grid and add x and y padding
        self.txtMeasurement1.grid(row = 1, column = 0, padx = 8, pady = 10)

        # create a variable called "arrow" and make it a label widget
        self.arrow = Label(self, text = "----->", font = self.headerFont, bg = "#FFFF99")
        # add "arrow' to center of grid
        self.arrow.grid(row = 1, column = 1)

        # create a variable called "txtMeasurement2" and make it a label with anchor = "w" and a groove relief
        self.txtMeasurement2 = Label(self, bg = "#fff", anchor = "w", relief = "groove")
        # add "txtMeasurement2" to middle right grid with sticky = "we"
        self.txtMeasurement2.grid(row = 1, column = 2, sticky = "we")

        # create a variable called "units1" and make it a Listbox widget
        # exportselection lets the user select from both Listboxes instead of only one selection being made at a time
        self.units1 = Listbox(self, height = 3, exportselection = 0)
        # add "units1" to bottom left grid and add y padding
        self.units1.grid(row = 2, column = 0, pady = 10)
        # insert temp measurements into "units1" Listbox
        self.units1.insert(END, "Fahrenheit", "Celsius", "Kelvin")

        # create a variable called "convert" and make it a button widget
        self.convert = Button(self, text = "Convert to")
        # add "convert" to bottom middle grid
        self.convert.grid(row = 2, column = 1)
        # when "convert" gets clicked on, execute "checkTempSel()"
        self.convert["command"] = self.checkTempSel

        # create a variable called "units2" and make it a Listbox widget
        # exportselection lets the user select from both Listboxes instead of only one selection being made at a time
        self.units2 = Listbox(self, height = 3, exportselection = 0)
        # add "units2" to bottom right grid
        self.units2.grid(row = 2, column = 2)
        # insert temp measurments into "units2" Listbox
        self.units2.insert(END, "Fahrenheit", "Celsius", "Kelvin")

    # create a function called "checkTempSel" passing "self" as a parameter
    # used to make sure the user selects units to convert from and to
    def checkTempSel(self):
        # create a variable called "selected1" that goes through all of "units1"
        selected1 = self.units1.curselection()
        # create a variable called "selected2" that goes through all of "units2"
        selected2 = self.units2.curselection()
        # create a variable called "measurement" that gets the value from "txtMeasurement1"
        measurement = self.txtMeasurement1.get()
        # create a variable called "checkInt" that exececutes "checkInt()"
        checkInt = self.checkInt()
        # execute "checkInt()"
        checkInt

        # if "selected1" doesn't find a selection from "units1", execute "noUnit1" to inform the user
        if selected1 == ():
            self.noUnit1()
        # if "selected2" doesn't find a selection from "units2", execute "noUnit2" to inform the user
        elif selected2 == ():
            self.noUnit2()
        # if the user does not input anything into "txtMeasurement1", execute "invalideMeasurement()" to inform the user
        elif measurement == "":
            self.invalidMeasurement()
        # if measurement gets something that is not an integer, execute "invalidMeasurement()" to inform the user
        elif checkInt == False:
            self.invalidMeasurement()
        else:
            # create a variable called "selValue1" that gets the selectied option from "units1"
            selValue1 = self.units1.get(selected1[0])
            # create a variable called "baseUnit" with initial value "lengthConverter1()"
            baseUnit = self.tempConverter1()
            # execute "lengthConverter1"
            baseUnit
            # execute "lengthConverter2" passing the returned value from "lengthConverter1"
            self.tempConverter2(baseUnit)

    # create a function called "tempConverter1" passing self as a parameter and returns a value of "baseUnit"
    # converts measurement from selected unit in "units1" to a base unit
    def tempConverter1(self):
        # create a variable called "measurement" that gets user input from "txtMeasurement1" and makes it floating point
        measurement = float(self.txtMeasurement1.get())
        # create a variable called "selected1" that goes through all units in "units1"
        selected1 = self.units1.curselection()
        # create a variable called "selValue1" that gets user's selected unit from "units1"
        selValue1 = self.units1.get(selected1[0])

        # Celsius is base unit
        # if selected, convert Fahrenheit to Celsius and return its value
        if selValue1 == "Fahrenheit":
            baseUnit = (measurement - 32)*(5/9)
            return baseUnit
        # if selected, convert Kelvin to Celsius and return its value
        elif selValue1 == "Kelvin":
            baseUnit = measurement - 273.15
            return baseUnit
        else:
            # Celsius is selected and is already the base unit
            # return "baseUnit"
            baseUnit = measurement
            baseUnit = float(baseUnit)
            return baseUnit

    # create a function called "tempConverter2" passing "self" and "baseUnit" as parameters
    # converts measurement from baseUnit to selected unit in "units2"
    def tempConverter2(self, baseUnit):
        # create a variable called "selected2" that goes through all units in "units2"
        selected2 = self.units2.curselection()
        # create a variable called "selValue1" that gets user's selected unit from "units1"
        selValue2 = self.units2.get(selected2[0])

        # if selected, convert baseUnit to Fahrenheit and display calculation in "txtMeasurement2"
        if selValue2 == "Fahrenheit":
            result = (baseUnit*(9/5)) + 32
            self.txtMeasurement2["text"] = "{}".format(result)
        # if selected, convert baseUnit to Kelvin and display calculation in "txtMeasurement2"
        elif selValue2 == "Kelvin":
            result = baseUnit + 273.15
            self.txtMeasurement2["text"] = "{}".format(result)
        else:
            # Celsius is selected and is already the base unit
            # display calculation in "txtMeasurement2"
            result = baseUnit
            result = float(result)
            self.txtMeasurement2["text"] = "{}".format(result)

    # create a function called "time" passing "self" as a parameter
    # sets up Time UI grid
    def time(self):
        # set window dimensions when selected
        self.geometry("553x275")

        # create a variable called "conversionCentral" and make it a label widget
        self.conversionCentral = Label(self, text = "Conversion Central", font = self.headerFont, bg = "#FFFF99")
        # add "conversionCentral" to top center grid and add y padding
        self.conversionCentral.grid(row = 0, column = 1, pady = 5)

        # create a variable called "txtMeasurement1" and make it an entry widget for user input
        self.txtMeasurement1 = Entry(self)
        # add "txtMeasurement1" to middle left grid and add x and y padding
        self.txtMeasurement1.grid(row = 1, column = 0, padx = 8, pady = 10)

        # create a variable called "arrow" and make it a label widget
        self.arrow = Label(self, text = "----->", font = self.headerFont, bg = "#FFFF99")
        # add "arrow' to center of grid
        self.arrow.grid(row = 1, column = 1)

        #create a variable called "txtMeasurement2" and make it a label with anchor = "w" and a groove relief
        self.txtMeasurement2 = Label(self, bg = "#fff", anchor = "w", relief = "groove")
        # add "txtMeasurement2" to middle right grid with sticky = "we"
        self.txtMeasurement2.grid(row = 1, column = 2, sticky = "we")

        # create a variable called "units1" and make it a Listbox widget
        # exportselection lets the user select from both Listboxes instead of only one selection being made at a time
        self.units1 = Listbox(self, height = 9, exportselection = 0)
        # add "units1" to bottom left grid and add y padding
        self.units1.grid(row = 2, column = 0, pady = 10)
        # insert time measurements into "units1" Listbox
        self.units1.insert(END, "Century", "Decade", "Calendar Year", "Month", "Week", "Day", "Hour", "Minute", "Second")

        # create a variable called "convert" and make it a button widget
        self.convert = Button(self, text = "Convert to")
        # add "convert" to bottom middle grid
        self.convert.grid(row = 2, column = 1)
        # when "convert" gets clicked on, execute "checkTimeSel()"
        self.convert["command"] = self.checkTimeSel

        # create a variable called "units2" and make it a Listbox widget
        # exportselection lets the user select from both Listboxes instead of only one selection being made at a time
        self.units2 = Listbox(self, height = 9, exportselection = 0)
        # add "units2" to bottom right grid
        self.units2.grid(row = 2, column = 2)
        # insert time measurments into "units2" Listbox
        self.units2.insert(END, "Century", "Decade", "Calendar Year", "Month", "Week", "Day", "Hour", "Minute", "Second")

    # create a function called "checkTimeSel" passing "self" as a parameter
    # used to make sure the user selects units to convert from and to
    def checkTimeSel(self):
        # create a variable called "selected1" that goes through all of "units1"
        selected1 = self.units1.curselection()
        # create a variable called "selected2" that goes through all of "units2"
        selected2 = self.units2.curselection()
        # create a variable called "measurement" that gets the value from "txtMeasurement1"
        measurement = self.txtMeasurement1.get()
        # create a variable called "checkInt" that exececutes "checkInt()"
        checkInt = self.checkInt()
        # execute "checkInt()"
        checkInt

        # if "selected1" doesn't find a selection from "units1", execute "noUnit1" to inform the user
        if selected1 == ():
            self.noUnit1()
        # if "selected2" doesn't find a selection from "units2", execute "noUnit2" to inform the user
        elif selected2 == ():
            self.noUnit2()
        # if the user does not input anything into "txtMeasurement1", execute "invalideMeasurement()" to inform the user
        elif measurement == "":
            self.invalidMeasurement()
        # if measurement gets something that is not an integer, execute "invalidMeasurement()" to inform the user
        elif checkInt == False:
            self.invalidMeasurement()
        else:
            # create a variable called "selValue1" that gets the selectied option from "units1"
            selValue1 = self.units1.get(selected1[0])
            # create a variable called "baseUnit" with initial value "lengthConverter1()"
            baseUnit = self.timeConverter1()
            # execute "lengthConverter1"
            baseUnit
            # execute "lengthConverter2" passing the returned value from "lengthConverter1"
            self.timeConverter2(baseUnit)

    # create a function called "timeConverter1" passing self as a parameter and returns a value of "baseUnit"
    # converts measurement from selected unit in "units1" to a base unit
    def timeConverter1(self):
        # create a variable called "measurement" that gets user input from "txtMeasurement1" and makes it floating point
        measurement = float(self.txtMeasurement1.get())
        # create a variable called "selected1" that goes through all units in "units1"
        selected1 = self.units1.curselection()
        # create a variable called "selValue1" that gets user's selected unit from "units1"
        selValue1 = self.units1.get(selected1[0])

        # seconds is base unit
        # if selected, convert centuries to seconds and return its value
        if selValue1 == "Century":
            baseUnit = measurement*(3.154e+9)
            return baseUnit
        # if selected, convert decades to seconds and return its value
        elif selValue1 == "Decade":
            baseUnit = measurement*(3.154e+8)
            return baseUnit
        # if selected, convert calendar years to seconds and return its value
        elif selValue1 == "Calendar Year":
            baseUnit = measurement*(3.154e+7)
            return baseUnit
        # if selected, convert months to seconds and return its value
        elif selValue1 == "Month":
            baseUnit = measurement*(2.628e+6)
            return baseUnit
        # if selected, convert weeks to seconds and return its value
        elif selValue1 == "Week":
            baseUnit = measurement*604800
            return baseUnit
        # if selected, convert days to seconds and return its value
        elif selValue1 == "Day":
            baseUnit = measurement*86400
            return baseUnit
        # if selected, convert hours to seconds and return its value
        elif selValue1 == "Hour":
            baseUnit = measurement*3600
            return baseUnit
        # if selected, convert minutes to seconds and return its value
        elif selValue1 == "Minute":
            baseUnit = measurement*60
            return baseUnit
        else:
            # seconds is selected and is already the base unit
            # return "baseUnit"
            baseUnit = measurement
            baseUnit = float(baseUnit)
            return baseUnit

    # create a function called "timeConverter2" passing "self" and "baseUnit" as parameters
    # converts measurement from baseUnit to selected unit in "units2"
    def timeConverter2(self, baseUnit):
        # create a variable called "selected2" that goes through all units in "units2"
        selected2 = self.units2.curselection()
        # create a variable called "selValue1" that gets user's selected unit from "units1"
        selValue2 = self.units2.get(selected2[0])

        # if selected, convert baseUnit to centuries and display calculation in "txtMeasurement2"
        if selValue2 == "Century":
            result = baseUnit/(3.154e+9)
            self.txtMeasurement2["text"] = "{}".format(result)
        # if selected, convert baseUnit to decades and display calculation in "txtMeasurement2"
        elif selValue2 == "Decade":
            result = baseUnit/(3.154e+8)
            self.txtMeasurement2["text"] = "{}".format(result)
        # if selected, convert baseUnit to calendar years and display calculation in "txtMeasurement2"
        elif selValue2 == "Calendar Year":
            result = baseUnit/(3.154e+7)
            self.txtMeasurement2["text"] = "{}".format(result)
        # if selected, convert baseUnit to months and display calculation in "txtMeasurement2"
        elif selValue2 == "Month":
            result = baseUnit/(2.628e+6)
            self.txtMeasurement2["text"] = "{}".format(result)
        # if selected, convert baseUnit to weeks and display calculation in "txtMeasurement2"
        elif selValue2 == "Week":
            result = baseUnit/604800
            self.txtMeasurement2["text"] = "{}".format(result)
        # if selected, convert baseUnit to days and display calculation in "txtMeasurement2"
        elif selValue2 == "Day":
            result = baseUnit/86400
            self.txtMeasurement2["text"] = "{}".format(result)
        # if selected, convert baseUnit to hours and display calculation in "txtMeasurement2"
        elif selValue2 == "Hour":
            result = baseUnit/3600
            self.txtMeasurement2["text"] = "{}".format(result)
        # if selected, convert baseUnit to minutes and display calculation in "txtMeasurement2"
        elif selValue2 == "Minute":
            result = baseUnit/60
            self.txtMeasurement2["text"] = "{}".format(result)
        else:
            # seconds is selected and is already the base unit
            # display calculation in "txtMeasurement2"
            result = baseUnit
            result = float(result)
            self.txtMeasurement2["text"] = "{}".format(result)


global settings
class settings(Tk):
    # in "settings", create an initializer function that initializes "self"
    def __init__(self):
        #initialize Tk
        Tk.__init__(self)

        # identify the initial visual attributes of the window in "settings"
        # define headerFont, window title, size of window, and background color
        self.headerFont = ("System", "15", "bold italic")
        self.title("Conversion Central - Settings")
        self.geometry("553x300")
        self["bg"] = "#FFFF99"

        self.test = Label(self, text = "This is a test", font = self.headerFont)
        self.test.grid

# settings = settings.settingsMenu(self)

# create a function called "main"
# passes no parameters
# is the main function that runs "App"
def main():
    # create a variable called "app" that contains "App()" object
    app = App()
    # executes the "App()" object
    # essentially tells the program to run
    app.mainloop()

# if namespace gets "main", execute "main"
# therefore runs application
if __name__ == "__main__":
    main()
