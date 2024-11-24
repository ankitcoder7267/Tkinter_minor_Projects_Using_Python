#====>>>>>>> Here is the basic code of the dicerolling game .

# from tkinter import *
# import random as r 

# root = Tk()
# # root.geometry("700*450")
# root.title("Roll Dice Game")

# label = Label(root,text="",font=("times",260))
# def roll():
#     dice = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685',]
#     label.config(text=f"{r.choice(dice)}{r.choice(dice)}")
#     label.pack()
# button=Button(root,text="Lets roll......",width=40,height=1,font=10,bg="red",bd=1,command=roll)
# button.pack(padx=5,pady=5)
# root.mainloop()


#====>>>>>>> Here is the code after apply somes designing on them . 

from tkinter import *
import random as r

def roll():
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    die1 = r.choice(dice)
    die2 = r.choice(dice)
    label.config(text=f"{die1} {die2}")  # Update the dice display
    
    if die1  ==  die2:
        result_label.config(text="Congratulations! You win the game!", fg="green")
    else:
        result_label.config(text="Keep trying!", fg="black")

root = Tk()
root.geometry("700x450")  # Fixed dimensions
root.title("Roll Dice Game")

# Set background color
root.config(bg="lightblue")

label = Label(root, text="", font=("Times", 160), bg="lightblue")
label.pack(pady=20)  # Spacing above the label

result_label = Label(root, text="", font=("Arial", 14), bg="lightblue")
result_label.pack(pady=20)  # Now placed between the dice and button

button = Button(root, text="Let's Roll...", width=40, height=1, font=("Arial", 14), bg="blue", command=roll)
button.pack(pady=20)  # Spacing below the button

root.mainloop()
