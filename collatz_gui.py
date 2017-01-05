import tkinter as tk
import plotting

title_text = """Enter a number.
The histogram will display the stopping points for the Collatz theorem up until that number."""


class CollatzGui(tk.Frame):
    def __init__(self, root=None):
        tk.Frame.__init__(self, root)
        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self, text=title_text, anchor="c")
        self.entry_stringvar = tk.StringVar()
        entry_box = tk.Entry(self, textvariable=self.entry_stringvar, justify=tk.CENTER)
        enter_button = tk.Button(self, text="Go!", command=self._on_button_clicked)

        title_label.pack(side="top", fill="both", expand=True)
        entry_box.pack(side="top", fill="both", expand=True)
        enter_button.pack(side="top", fill="both", expand=True)

    def _on_button_clicked(self):
        print("clicked button!")
        # need to freeze button clicking here
        num = self.entry_stringvar.get()
        plotting.plot_collatz_to_file(int(num))
        self._display_image("temp_file.png")

    def _display_image(self, filename:str):
        # use PIL
        pass

if __name__ == "__main__":
    root = tk.Tk()
    view = CollatzGui(root)
    view.pack(side="top", fill="both", expand=True)
    root.mainloop()
