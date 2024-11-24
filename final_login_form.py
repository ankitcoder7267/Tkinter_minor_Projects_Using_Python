from tkinter import *
from tkinter import messagebox

def login():
    username = entry1.get()
    password = entry2.get()
    if username == "" and password == "":
        messagebox.showinfo("", "Blank Not Allowed")
    elif username == "Ankit Madhesiya" and password == "madhesiyaankit@123":
        messagebox.showinfo("", "Login Successfully 😉😉😉")
    else:
        messagebox.showinfo("", "Incorrect username and password 😒😒😒")

def reset_fields():
    """Clear the username and password fields."""
    entry1.delete(0, END)
    entry2.delete(0, END)

def close_app():
    """Close the application."""
    root.destroy()

def draw_gradient(canvas, color1, color2):
    for i in range(300):  # Height of the window
        ratio = i / 300
        r = int((1 - ratio) * int(color1[1:3], 16) + ratio * int(color2[1:3], 16))
        g = int((1 - ratio) * int(color1[3:5], 16) + ratio * int(color2[3:5], 16))
        b = int((1 - ratio) * int(color1[5:7], 16) + ratio * int(color2[5:7], 16))
        color = f'#{r:02x}{g:02x}{b:02x}'
        canvas.create_line(0, i, 400, i, fill=color)

root = Tk()
root.title("ANKIT LOGIN FORM")

# Set the size of the window and make it non-resizable
root.geometry("400x300")
root.resizable(False, False)

# Create a canvas for the gradient
canvas = Canvas(root, width=400, height=300)
canvas.pack()

# Draw the gradient from light pink to light blue
draw_gradient(canvas, "#FFB6C1", "#ADD8E6")

# Create a frame for the form
frame = Frame(canvas, bg="#ffffff", padx=20, pady=20)
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

Label(frame, text="Username", bg="#ffffff", font=("Arial", 12)).grid(row=0, column=0, pady=10)
Label(frame, text="Password", bg="#ffffff", font=("Arial", 12)).grid(row=1, column=0, pady=10)

entry1 = Entry(frame, bd=2, font=("Arial", 12))
entry1.grid(row=0, column=1)

entry2 = Entry(frame, bd=2, show="*", font=("Arial", 12))
entry2.grid(row=1, column=1)

# Medium-sized buttons
Button(frame, text="Login", command=login, height=1, width=12, bd=3, bg="#FF69B4", fg="#ffffff", font=("Arial", 12)).grid(row=2, column=0, pady=10)
Button(frame, text="Reset", command=reset_fields, height=1, width=12, bd=3, bg="#FF69B4", fg="#ffffff", font=("Arial", 12)).grid(row=2, column=1, pady=10)
Button(frame, text="Close", command=close_app, height=1, width=26, bd=3, bg="#FF69B4", fg="#ffffff", font=("Arial", 12)).grid(row=3, columnspan=2, pady=10)

root.mainloop()
