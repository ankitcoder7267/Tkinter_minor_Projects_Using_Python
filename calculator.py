import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        self.master.geometry("400x600")  
        self.master.configure(bg="lightblue")  

        self.result_var = tk.StringVar()

        # Entry for the result
        self.entry = tk.Entry(master, textvariable=self.result_var, font=("Arial", 24), bd=10, insertwidth=2, width=14, borderwidth=4)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Button layout
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(master, text=button, padx=20, pady=20, font=("Arial", 18), bg="white", command=lambda b=button: self.on_button_click(b)).grid(row=row_val, column=col_val, sticky="nsew", padx=5, pady=5)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Clear button
        tk.Button(master, text='C', padx=20, pady=20, font=("Arial", 18), bg="red", command=self.clear).grid(row=row_val, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

        # Configure grid rows and columns to expand
        for i in range(5):
            master.grid_rowconfigure(i, weight=1)
            master.grid_columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == '=': 
            try:
                expression = self.result_var.get()
                result = eval(expression)  # Evaluate the expression
                self.result_var.set(result)
            except Exception:
                self.result_var.set("Error")
        else:
            current_text = self.result_var.get()
            self.result_var.set(current_text + char)

    def clear(self):
        self.result_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
