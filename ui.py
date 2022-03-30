from tkinter import *

from data import get_new_numbers
from merge_sort_function import merge_sort

RED = "#FF6B6B"
BLUE = "#4D96FF"
GREEN = "#6BCB77"


class UserInterface:
    def __init__(self):

        self.window = Tk()
        self.window.title("MERGE SORT MACHINE")
        self.window.config(padx=10, pady=25, bg=RED)
        self.random_numbers = []
        self.title_label = Label(text="MERGE SORT MACHINE", font=("Arial", 30, "italic"), bg=RED, fg="white")
        self.title_label.grid(column=0, row=0, columnspan=2)

        self.canvas = Canvas(width=400, height=200, bg=BLUE)
        self.new_numbers_list = self.canvas.create_text(
            200,
            100,
            width=380,
            text="Fetch Random Numbers Here!",
            font=("Arial", 18, "italic"),
            fil="white")
        self.canvas.grid(column=0, row=1, padx=25)

        self.canvas2 = Canvas(width=400, height=200, bg=GREEN)
        self.canvas2.grid(column=1, row=1, padx=25)
        self.merge_sorted_list = self.canvas2.create_text(
            200,
            100,
            width=380,
            text="Convert To Sorted List Here!",
            font=("Arial", 18, "italic"),
            fil="white")

        self.new_number_button = Button(
            text="MORE NUMBERS!",
            font=("Arial", 20, "italic"),

            width=20,
            borderwidth=3,
            relief="raised",
            bg="white",
            padx=5,
            pady=10,
            command=self.new_list)
        self.new_number_button.grid(column=0, row=3, pady=10)

        self.merge_sort_button = Button(
            text="MERGE SORT NOW!",
            font=("Arial", 20, "italic"),
            width=20,
            borderwidth=3,
            relief="raised",
            bg="white",
            padx=5,
            pady=10,
            command=self.merge)
        self.merge_sort_button.grid(column=1, row=3, pady=10)
        self.window.mainloop()

    def new_list(self):
        new_random_numbers = get_new_numbers()
        self.canvas.itemconfig(self.new_numbers_list, text=new_random_numbers)
        self.random_numbers = new_random_numbers
        print(self.random_numbers)

    def merge(self):
        self.canvas2.itemconfig(self.merge_sorted_list, text=merge_sort(self.random_numbers))
        print(self.merge_sorted_list)








