from tkinter import *

root = Tk()
root.title("Calculator")

gui_width = 350
gui_height = 500
root.geometry(f"{gui_width}x{gui_height}")
root.minsize(gui_width, gui_height)

scvalue = StringVar()
scvalue.set("")

screen = Entry(root, textvar=scvalue, font="lucida 40")
screen.pack(fill=X, padx=10, pady=10)

f1 = Frame(root, bg="grey")

def click(event):
    global scvalue
    text = event.widget.cget("text")

    if text == "=":
        if scvalue.get().isdigit():
            theValue = int(scvalue.get())
        else:
            try:
                theValue = eval(screen.get())
            except Exception as e:
                theValue = "Invalid!"

        scvalue.set(theValue)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()

    elif text == "←":
        backspace_it = scvalue.get()[:-1]
        scvalue.set(backspace_it)
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


for i in range(6, 9):
    b = Button(f1, text=f"{i+1}", font="lucida 40")
    b.grid(row=1, column=i-6+1, padx=1, pady=1, sticky="NSEW")
    b.bind(f"<Button-1>", click)
    i += 1

for i in range(3, 6):
    b = Button(f1, text=f"{i+1}", font="lucida 40")
    b.grid(row=2, column=i-3+1, padx=1, pady=1, sticky="NSEW")
    b.bind(f"<Button-1>", click)
    i += 1

for i in range(0, 3):
    b = Button(f1, text=f"{i+1}", font="lucida 40")
    b.grid(row=3, column=i+1, padx=1, pady=1, sticky="NSEW")
    b.bind(f"<Button-1>", click)
    i += 1

clear = Button(f1, text="C", font="lucida 35")
clear.grid(row=0, column=1, padx=1, pady=1, sticky="NSEW")
clear.bind(f"<Button-1>", click)

percent = Button(f1, text="%", font="lucida 35")
percent.grid(row=0, column=2, padx=1, pady=1, sticky="NSEW")
percent.bind(f"<Button-1>", click)

backspace = Button(f1, text="←", font="lucida 32")
backspace.grid(row=0, column=3, padx=1, pady=1, sticky="NSEW")
backspace.bind(f"<Button-1>", click)

divide = Button(f1, text="/", font="lucida 32")
divide.grid(row=0, column=4, padx=1, pady=1, sticky="NSEW")
divide.bind(f"<Button-1>", click)

multiply = Button(f1, text="*", font="lucida 32")
multiply.grid(row=1, column=4, padx=1, pady=1, sticky="NSEW")
multiply.bind(f"<Button-1>", click)

minus = Button(f1, text="-", font="lucida 32")
minus.grid(row=2, column=4, padx=1, pady=1, sticky="NSEW")
minus.bind(f"<Button-1>", click)

add = Button(f1, text="+", font="lucida 32")
add.grid(row=3, column=4, padx=1, pady=1, sticky="NSEW")
add.bind(f"<Button-1>", click)

result = Button(f1, text="=", font="lucida 32")
result.grid(row=4, column=4, padx=1, pady=1, sticky="NSEW")
result.bind(f"<Button-1>", click)

zero = Button(f1, text="0", font="lucida 32")
zero.grid(row=4, column=2, padx=1, pady=1, sticky="NSEW")
zero.bind(f"<Button-1>", click)

doubleZero = Button(f1, text="00", font="lucida 32")
doubleZero.grid(row=4, column=1, padx=1, pady=1, sticky="NSEW")
doubleZero.bind(f"<Button-1>", click)

decimal = Button(f1, text=".", font="lucida 32")
decimal.grid(row=4, column=3, padx=1, pady=1, sticky="NSEW")
decimal.bind(f"<Button-1>", click)


f1.pack()

root.mainloop()