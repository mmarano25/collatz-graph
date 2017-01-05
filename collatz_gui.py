import tkinter as tk

title_text = """Enter a number.
The histogram will display the stopping points for the Collatz theorem up until that number."""


class CollatzGui(tk.Frame):
    def __init__(self, root=None):
        tk.Frame.__init__(self, root)
        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self, text=title_text, anchor="c")
        entry_stringvar = tk.StringVar()
        entry_box = tk.Entry(self, textvariable=entry_stringvar, justify=tk.CENTER)
        self.enter_button = tk.Button(self, text="Go!")

        title_label.pack(side="top", fill="both", expand=True)
        entry_box.pack(side="top", fill="both", expand=True)
        self.enter_button.pack(side="top", fill="both", expand=True)


if __name__ == "__main__":
    root = tk.Tk()
    view = CollatzGui(root)
    view.pack(side="top", fill="both", expand=True)
    root.mainloop()
