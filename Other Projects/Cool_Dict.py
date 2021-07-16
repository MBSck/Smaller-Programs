# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 16:05:05 2020

@author: LocalAdmin
"""

"""
w = Label(root, text = "Cool Dictionary")   #labels the window
w.pack()    #makes window fit to text size
"""
# -*- coding: utf-8 -*-

# Implement github repo in order to update the code
# Find way to run the python code as a program

# use traitsui as a way to build UIs

import tkinter as tk #K leingeschrieben in python 3.X
import tkinter.messagebox as mbox
import sqlite3 as sq    # Use for database construction
from sys import platform

# Centers the windows in the middle of the screen


class Center(tk.Frame):
    def __init__(self, master):
        self.master = master
    def center(self):
        #Gets the dimensions from the screen
        self.window_width = self.master.winfo_reqwidth()
        self.window_height = self.master.winfo_reqheight()
        #Gets the half of the both dimensions
        self.position_right = int(self.master.winfo_screenwidth()/2 - self.window_width/2)
        self.position_down = int(self.master.winfo_screenheight()/2 - self.window_height/2)
        #Positions the window in the center of the page
        self.master.geometry("+{}+{}".format(self.position_right, self.position_down))

# Makes a Popup Window appear
class PopupWindow(tk.Frame):
    def __init__(self, master):
        self.master = master
        self.top = tk.Toplevel(self.master)
        # sets the size of the program and checks for the os
        if platform == "linux" or "linux2":
            self.top.geometry("170x120")
        elif platform == "win32":
            self.top.geometry("130x115")
        self.create_widgets()
        # Center the Window
        self.mid = Center(self.top)
        self.mid.center()

    def create_widgets(self):
        # Create the Name of the Window
        self.top_label_w = tk.Label(self.top, text="Input your Word!")
        self.top_label_w.grid(row=0, column=1, columnspan=2)
        # Create both the Entry fields for the Program
        self.top_entry_w = tk.Entry(self.top, width=20)
        self.top_entry_w.grid(row=1, column=1, columnspan=2)
        self.top_entry_w.focus()
        # Create the second Entry field
        self.top_label_cw = tk.Label(self.top, text="Input your Cool Word!")
        self.top_label_cw.grid(row=2, column=1, columnspan=2)
        self.top_entry_cw = tk.Entry(self.top, width=20)
        self.top_entry_cw.grid(row=3, column=1, columnspan=2)
        # Create the Enter and cancle buttons
        self.top_confirm = tk.Button(self.top, text="Confirm", command=self.confirm)
        self.top_confirm.grid(row=4, column=2)
        self.top_cancle = tk.Button(self.top, text="Cancle", command=self.cancel)
        self.top_cancle.grid(row=4, column=1)

    def confirm(self):
        self.value_w = self.top_entry_w.get()
        self.value_cw = self.top_entry_cw.get()
        if (self.value_w == ""
            or self.value_cw == ""):
            mbox.showerror("Input required!", "There has to be a value in both fields!")
            self.top.destroy()
            self.w_pop = PopupWindow(self.master) 
        else:
            # Call the sql_lib
            self.sql = Sql_lib()
            self.sql.new_entry(self.value_w, self.value_cw)
            # self.sql.get_all_entries() #only for test reasons here DELETE LATER!!!
            self.top.destroy()
    def cancel(self):
        self.top.destroy()
        
class TextPopup(tk.Frame):
    def __init__(self, master, geometry, windowname):
        self.master = master
        self.geo = geometry
        self.wn = windowname
        self.top_t = tk.Toplevel(self.master)
        self.top_t.geometry(self.geo)
        self.create_widgets()
        # Center the Windows
        self.cent = Center(self.top_t)
        self.cent.center()
        # Initalize Library
        self.sql = Sql_lib()
    def create_widgets(self):
        # Create the Name of the window
        self.top_t_label = tk.Label(self.top_t, text=self.wn)
        self.top_t_label.grid(row=0, column=1, columnspan=2)
        # Create the widgets
        if self.top_t.label["text"] == "About":
            pass
        elif self.top_t_label["text"] == "Vocabulary List":
            pass
            # self.all_entries = self.sql.get_all_entries()
            # for entry in all_entries:
                #print()
        
        
        
# The Main Window
class MainWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        # Create a Titel
        self.master.title("The Cool Dictionary")
        # Sets the size of the box and checks what os you have
        if platform == "linux" or platform == "linux2":
            self.master.geometry("290x125")
        elif platform == "win32":
            self.master.geometry("235x115")
        self.create_widgets()
        self.create_menu()
        self.center = Center(self.master)
        self.center.center()

    def create_widgets(self):
        # Add Text Message to Input
        self.instructions = tk.Label(self.master, text="Write a Word and Search for its Translation!")
        self.instructions.grid(column=1, row=0, columnspan=1)
        # Add Input Windows for the Normal Words
        self.word_slot= tk.Entry(self.master, width=30)
        self.word_slot.grid(column=1, row=1, columnspan=1)
        self.word_slot.focus()
        # Create Search Button
        self.search = tk.Button(self.master)
        self.search["text"] = "Search"
        self.search["command"] = self.search_translation #self.search_for_entry
        self.search.grid(column=1, row=5, columnspan=1)
        # Create Add New Entry register
        # Create Text Message to Output
        self.output = tk.Label(self.master, text="The Cool Word is: ")
        self.output.grid(column=1, row=3, columnspan=1)
        # Create Output field for cool word
        self.word_field_text = tk.StringVar()
        self.word_field_slot = tk.Entry(self.master, textvariable=self.word_field_text, width=30, state="disabled")
        self.word_field_slot.grid(column=1, row=4, columnspan=1)

    def create_menu(self):
        # Create File Slot
        self.menu = tk.Menu(self.master)
        self.file_item = tk.Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.file_item)
        self.file_item.add_command(label="Add new translation", command=self.popup)
        self.file_item.add_command(label="View all entries", command=self.entry_window)
        # Create About
        self.about_item = tk.Menu(self.menu)
        self.about_item.add_command(label="About", command=self.about)
        self.menu.add_cascade(label="About", menu=self.about_item)
        # Configurates the Menu
        self.master.config(menu=self.menu)
        # def list_of_entries(self):

    def popup(self):
        self.w_pop = PopupWindow(self.master)

    def entry_window(self):
        if platform == "linux" or "linux2":
            self.geo_e = "130x115"
        elif platform == "win32":
            self.geo_e = "130x115"
        self.w_text = TextPopup(self.master, self.geo_e,  "Vocabulary List")

    def about(self):
        if platform == "linux" or "linux2":
            self.geo_a = "130x115"
        elif platform == "win32":
            self.geo_a = "130x115"
        self.w_about = TextPopup(self.master, self.geo_a , "About")

    # def show_all_entries(self):
    def search_translation(self):
        # Get the input words
        self.word = self.word_slot.get()
        self.word = self.word.lower()
        self.word = self.word.split()
        # Initialize and use the function from the sql_library
        self.sql = Sql_lib()
        self.sql.search_for_entry(self.word)
        self.out = self.sql.row_word
        if self.out != "":
            self.word_field_text.set(self.out)

# The Database with the words in it


class Sql_lib:
        def __init__(self):
            # Initialize the github repo and the repo on the Pc
            # Create the Database in SQL
            self.con = sq.connect("./Words_and_Translations.db")
            self.pointer = self.con.cursor()
            self.sql_order = """
                CREATE TABLE IF NOT EXISTS translation (
                word VARCHAR(20),
                coolword VARCHAR(20)
                );"""
            self.pointer.execute(self.sql_order)
            # Check if Database already exists and has already content in it, if not create it
            self.pointer.execute("""SELECT word FROM translation""")
            if not self.pointer.fetchone():  #fetchone returns first row only  
                self.word_list = [("ok","Oak nuggins"), ("yes", "Yank train"), ("no", "Nuns on ripple"),
                                  ("think", "I put a boogie dollar down"), ("golf", " Do you slap the dimpled balls?"),
                                  ("sick", "Mama's got the nasty jam"), ("idea", "That's a gold hat, cool cat!"),
                                  ("job", "This gig is gonna slash me hips"), ("lunch", "Dip me in ya Monday milk")]
                self.pointer.executemany("""
                                         INSERT INTO translation VALUES (?,?)
                                         """, self.word_list)
            self.con.commit()

        def get_all_entries(self):
            self.con = sq.connect("./Words_and_Translations.db")
            self.pointer = self.con.cursor()
            self.pointer.execute("SELECT word, coolword FROM translation")
            self.content = self.pointer.fetchall()
            #print(self.content) #only for test reasons here DELETE LATER!!!

        def new_entry(self, word, coolword):
            self.w = word
            self.w = self.w.lower()
            self.cw = coolword
            self.cw = self.cw.lower()
            self.con = sq.connect("./Words_and_Translations.db")
            self.pointer = self.con.cursor()
            self.pointer.execute("""
                INSERT INTO translation VALUES(?,?)
                """, (self.w, self.cw))
            self.con.commit()

        def search_for_entry(self, searchword):
            self.sw = searchword
            self.fw = ""
            self.get_all_entries()
            # This trys to find the word and then gets the second entry of the word pair
            try:
                self.row = self.pointer.execute("""SELECT word, coolword FROM translation WHERE word = ?
                                                """,(self.sw))
                self.row_word = self.row.fetchall()
                self.row_word = self.row_word[0]
                self.row_word = self.row_word[1]
            except:
                mbox.showerror("Not Included", "There is no translation for this word (yet)!")
        # def update(self):


if __name__ == "__main__":
    root = tk.Tk()
    MainWindow(root)
    root.mainloop()