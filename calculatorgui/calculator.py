import math
import tkinter as tk

class Calculator:

    def __init__(self,root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("350x400")

        self.root.grid_rowconfigure(0, weight=0)
        self.root.grid_rowconfigure(1, weight=0)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)

        self.entry = tk.Entry(self.root, font=("Arial",20),justify="center")
        self.entry.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=2, pady=2)

        clear_btn = tk.Button(self.root,text="C",font=("Arial",18),command=self.clear)
        clear_btn.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)

        squareroot_btn = tk.Button(self.root,text="√",font=("Arial",18),command=self.squareroot)
        squareroot_btn.grid(row=1, column=1,sticky="nsew",padx=2,pady=2)

        powerto2 = tk.Button(self.root,text="x²",font=("Arial",18),command=self.powerto2)
        powerto2.grid(row=1, column=2,sticky="nsew",padx=2,pady=2)


        self.buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]

        self.create_buttons()


    def create_buttons(self):
        button_frame = tk.Frame(self.root)
        button_frame.grid(row=2, column=0, columnspan=3, sticky="nsew",padx=2, pady=2)

        for i in range(4):
            button_frame.grid_rowconfigure(i,weight=1)
            button_frame.grid_columnconfigure(i,weight=1)

        for i, row in enumerate(self.buttons):
            for j, btn in enumerate(row):
                if btn == "=":
                    action = self.calculate
                else:
                    action = lambda x=btn: self.button_click(x)

                button = tk.Button(
                    button_frame,
                    text=btn,
                    font=("Arial", 18),
                    command=action
                )

                button.grid(row=i, column=j, sticky="nsew",padx=1,pady=1)
                
    def button_click(self,value):
        current = self.entry.get()
        self.entry.delete(0,tk.END)
        self.entry.insert(0,current + str(value))

    def calculate(self):
        try:
            result = eval(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))
        except Exception:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Fehler")

    def squareroot(self):
        try:
            value = float(self.entry.get())
            result = math.sqrt(value)

            self.entry.delete(0,tk.END)
            self.entry.insert(0,str(result))
        except:
            self.entry.delete(0,tk.END)
            self.entry.insert(0,"Fehler")

    def powerto2(self):
        try:
            value = float(self.entry.get())
            y = 2
            result = math.pow(value,y)

            self.entry.delete(0,tk.END)
            self.entry.insert(0,str(result))
        except:
            self.entry.delete(0,tk.END)
            self.entry.insert(0,"Fehler")


    def clear(self):
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()