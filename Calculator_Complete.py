import tkinter as tk

class CalculatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # 创建显示屏
        self.display = tk.Entry(master, font=("Arial", 24), justify="right", width=18, borderwidth=0)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # 创建按钮
        buttons = [
            "AC", "+/-", "%", "÷",
            "7", "8", "9", "×",
            "4", "5", "6", "-",
            "1", "2", "3", "+",
            "0", ".", "="
        ]

        row = 1
        col = 0
        for button in buttons:
            button_width = 5
            button_height = 2

            if button == "0":
                # 将0按钮的宽度调长
                tk.Button(master, text=button, font=("Arial", 16), width=10, height=button_height, command=lambda x=button: self.click(x)).grid(row=5, column=0, columnspan=2, padx=5, pady=5)
            elif button == ".":
                tk.Button(master, text=button, font=("Arial", 16), width=button_width, height=button_height, command=lambda x=button: self.click(x)).grid(row=5, column=2, padx=5, pady=5)
            elif button == "=":
                tk.Button(master, text=button, font=("Arial", 16), width=button_width, height=button_height, command=self.calculate).grid(row=5, column=3, padx=5, pady=5)
            else:
                tk.Button(master, text=button, font=("Arial", 16), width=button_width, height=button_height, command=lambda x=button: self.click(x)).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def click(self, value):
        if value == "AC":
            self.display.delete(0, tk.END)
        elif value == "+/-":
            current = float(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(0, str(-current))
        elif value == "%":
            current = float(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(0, str(current / 100))
        elif value == "=":
            self.calculate()
        elif value == "÷":
            self.display.insert(tk.END, "/")
        elif value == "×":
            self.display.insert(tk.END, "*")
        else:
            self.display.insert(tk.END, value)

    def calculate(self):
        try:
            expression = self.display.get()
            expression = expression.replace("÷", "/")
            expression = expression.replace("×", "*")
            result = eval(expression)
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
        except:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")

root = tk.Tk()
calculator = CalculatorGUI(root)
root.mainloop()