import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("手机计算器")
        self.geometry("400x500")  # 增加窗口大小
        self.resizable(False, False)

        self.result_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        # 显示框
        entry = tk.Entry(self, textvariable=self.result_var, font=("Arial", 24), justify='right')
        entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # 按钮布局
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+']
        ]

        for row_index, row in enumerate(buttons):
            for col_index, button in enumerate(row):
                action = lambda x=button: self.on_button_click(x)
                tk.Button(self, text=button, command=action, font=("Arial", 18), width=5, height=2).grid(row=row_index + 1, column=col_index, padx=5, pady=5)

    def on_button_click(self, char):
        if char == 'C':
            self.result_var.set('')  # 清空输入框
        elif char == '=':
            try:
                expression = self.result_var.get()
                result = eval(expression)  # 计算表达式
                self.result_var.set(result)
            except Exception:
                self.result_var.set('错误')  # 显示错误信息
        else:
            current_text = self.result_var.get()
            self.result_var.set(current_text + char)  # 添加输入到显示框

if __name__ == "__main__":
    calculator = Calculator()
    calculator.mainloop()