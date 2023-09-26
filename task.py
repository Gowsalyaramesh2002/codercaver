import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    
    if text == "=":
        try:
            result = eval(screen.get())
            screen.set(result)
        except Exception as e:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)

root = tk.Tk()
root.geometry("400x600")
root.title("Calculator")

screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font="lucida 40 bold", bd=20, insertwidth=4, width=14, justify="right")
entry.pack(fill="x")

frame = tk.Frame(root)
frame.pack()

buttons = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "C", "0", "=", "/"
]

row, col = 1, 0
for button_text in buttons:
    button = tk.Button(frame, text=button_text, padx=20, pady=20, font="lucida 20 bold")
    button.grid(row=row, column=col, padx=5, pady=5)
    button.bind("<Button-1>", click)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()

