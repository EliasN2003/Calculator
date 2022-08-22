from tkinter import *
from tkinter import messagebox


# GUI Calculator

root = Tk()
root.title("Simple calculator")

# The entry bar
Entry_bar = Entry(root, width=35, borderwidth=5)
Entry_bar.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


# Function for a number clicked
def button_click(number):
    current = Entry_bar.get()       # Saves the typed number
    Entry_bar.delete(0, END)        # Clears entry bar
    Entry_bar.insert(0, str(current) + str(number))   # Prints the saved number and then the new number on the entry bar


# Clear button
def button_clear():
    Entry_bar.delete(0, END)        # Clears the entry bar


# Add button
def button_plus():
    global calculation
    calculation = "Addition"
    global f_num
    f_num = float(Entry_bar.get())
    Entry_bar.delete(0, END)


# Equals button
def button_equal():
    sec_num = float(Entry_bar.get())      # Saves the second number typed
    Entry_bar.delete(0, END)

    try:
        if calculation == "Addition":       # Checks what calculation we are doing
            Entry_bar.insert(0, str(f_num + sec_num))

        elif calculation == "Multiplication":
            Entry_bar.insert(0, str(f_num * sec_num))

        elif calculation == "Division":
            Entry_bar.insert(0, str(f_num / sec_num))

        elif calculation == "Subtraction":
            Entry_bar.insert(0, str(f_num - sec_num))

    except ZeroDivisionError:       # Prints a popup error if you divide by zero
        messagebox.showerror("Division by zero", "Unable to divide by zero")


# Multiplication button
def button_mul():
    global calculation
    calculation = "Multiplication"
    global f_num
    f_num = float(Entry_bar.get())
    Entry_bar.delete(0, END)


# Division button
def button_div():
    global calculation
    calculation = "Division"
    global f_num
    f_num = float(Entry_bar.get())
    Entry_bar.delete(0, END)


# Subtraction button
def button_sub():
    global calculation
    calculation = "Subtraction"
    global f_num
    f_num = float(Entry_bar.get())
    Entry_bar.delete(0, END)


# Creation of buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_plus = Button(root, text="+", padx=39, pady=20, command=button_plus)
button_equal = Button(root, text="=", padx=88, pady=20, command=button_equal)
button_clear = Button(root, text="Clear", padx=78, pady=20, command=button_clear)
button_mul = Button(root, text="*", padx=41, pady=20, command=button_mul)
button_div = Button(root, text="/", padx=41, pady=20, command=button_div)
button_sub = Button(root, text="-", padx=41, pady=20, command=button_sub)


# Placement of buttons
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_plus.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)
button_mul.grid(row=6, column=0)
button_div.grid(row=6, column=1)
button_sub.grid(row=6, column=2)


root.mainloop()
