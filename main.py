# import os
#
# path = "E:\\old"
#
# if os.path.exists(path):
#     print("That location exists!")
#     if os.path.isfile(path):
#         print("That is a file")
#     elif os.path.isdir(path):
#         print("That is a directory!")
# else:
#     print ("That location doesn't exist!")

# try:
#     with open('test.txt') as file:
#         print(file.read())
# except FileNotFoundError:
#     print ("That file was not found :(")

# text = "hello ladies and gents \n my name is omar hesham"
# with open('test.txt', 'w') as file:
#     print(file.write(text))
# text2 = '\nI am 30 years old'
# with open('test.txt', 'a') as file:
#     print(file.write(text2))

# import shutil
#
# shutil.copy('test.txt','E:\\old\\copy.txt')
# shutil.rmtree() removes folder and all files and folders inside
# import os
#
# source = 'test.txt'
# destination = 'E:\\old\\test.txt'
# os.remove() for files
# os.rmdir() for folders
# try:
#     if os.path.exists(destination):
#         print('file already exists')
#     else:
#         os.replace(source, destination)
#         print(source, "was moved")
# except FileNotFoundError as e:
#     print(source, "was not found")
#
# import random
#
# options = ("rock", "paper", "scissors")
# running = True
#
# while running:
#
#     player = None
#     computer = random.choice(options)
#
#     while player not in options:
#         player = input("Enter a choice (rock, paper, scissors): ")
#
#     print(f"Player: {player}")
#     print(f"Computer: {computer}")
#
#     if player == computer:
#         print("It's a tie!")
#     elif player == "rock" and computer == "scissors":
#         print("You win!")
#     elif player == "paper" and computer == "rock":
#         print("You win!")
#     elif player == "scissors" and computer == "paper":
#         print("You win!")
#     else:
#         print("You lose!")
#
#     if not input("Play again? (y/n): ").lower() == "y":
#         running = False
#
# print("Thanks for playing!")

# class Animal:
#     alive = True
#
#     def eat(self):
#         print("This animal is eating")
#
#     def sleep(self):
#         print("This animal is sleeping")
#
#
# class Rabbit(Animal):
#
#     def run(self):
#         print("This rabbit is running")
#
#
# class Fish(Animal):
#
#     def swim(self):
#         print("This fish is swimming")
#
#
# class Hawk(Animal):
#
#     def fly(self):
#         print("This hawk is flying")
#
#
# rabbit = Rabbit()
# fish = Fish()
# hawk = Hawk()
#
# print(rabbit.alive)
# fish.eat()
# hawk.sleep()
#
# rabbit.run()
# fish.swim()
# hawk.fly()

# multiple inheritance = when a child class is derived from more than one parent class

# class Prey:
#
#     def flee(self):
#         print("This animal flees")
#
#
# class Predator:
#
#     def hunt(self):
#         print("This animal is hunting")
#
#
# class Rabbit(Prey):
#     pass
#
#
# class Hawk(Predator):
#     pass
#
#
# class Fish(Prey, Predator):
#     pass
#
#
# rabbit = Rabbit()
# hawk = Hawk()
# fish = Fish()
#
# # rabbit.flee()
# # hawk.hunt()
# fish.flee()
# fish.hunt()
# class Animal:
#
#     def eat(self):
#         print("This animal is eating")
#
#
# class Rabbit(Animal):
#     def eat(self):
#         print("This rabbit is eating a carrot")
#
#
# rabbit = Rabbit()
# rabbit.eat()
# class Car:
#
#     def turn_on(self):
#         print("You start the engine")
#         return self
#
#     def drive(self):
#         print("You drive the car")
#         return self
#
#     def brake(self):
#         print("You step on the brakes")
#         return self
#
#     def turn_off(self):
#         print("You turn off the engine")
#         return self
#
#
# car = Car()
#
# car.turn_on() \
#     .drive() \
#     .brake() \
#     .turn_off()

# class Rectangle:
#     def __init__(self, width, length):
#         self.width = width
#         self.length = length
#
#
# class Square(Rectangle):
#     def __init__(self, width, length):
#         super().__init__(width, length)
#
#     def area(self):
#         return self.length * self.width
#
#
# class Cube(Rectangle):
#     def __init__(self, width, length, height):
#         super().__init__(width, length)
#         self.height = height
#
#     def volume(self):
#         return self.length * self.width * self.height
#
#
# square = Square(3, 3)
# print(square.area())
# cube = Cube(3, 3, 3)
# print(cube.volume())

# from abc import ABC, abstractmethod
#
#
# class Vehicle(ABC):
#     @abstractmethod
#     def drive(self):
#         pass
# class Duck:
#
#     def walk(self):
#         print("This duck is walking")
#
#     def talk(self):
#         print("This duck is quacking")
#
#
# class Chicken:
#
#     def walk(self):
#         print("This chicken is walking")
#
#     def talk(self):
#         print("This chicken is clucking")
#
#
# class Person():
#
#     def catch(self, duck):
#         duck.walk()
#         duck.talk()
#         print("You caught the critter!")
#
#
# duck = Duck()
# chicken = Chicken()
# person = Person()

# person.catch(chicken)

# foods = list()
#
# while True:
#     food = input ("what is your preferred food")
#     if food == "quit":
#         break
#     foods.append(food)

# foods = list()
#
# while food := input("what is your preferred food") != "quit":
#     foods.append(food)

# def loud(text):
#     return text.upper()
#
#
# def quiet(text):
#     return text.upper()
#
#
# def hello(func):
#     text = func("hello")
#     print(text)
#
# hello(quiet)

# def divisor(x):
#     def dividend(y):
#         return y/x
#     return dividend()

# addition = lambda x, y, z: x + y + z
# print(addition(2, 2, 2))
#
# age_checker = lambda age: True if age >= 18 else False
# print(addition(2, 2, 2))
#
# print(age_checker(19))

# names = ("Omar", "Hesham", "Mohamed", "Hassan")
# print(sorted(names))

# students = [("Squidward", "F", 60),
#             ("Sandy", "A", 33),
#             ("Patrick", "D", 36),
#             ("Spongebob", "B", 20),
#             ("Mr.Grabs", "C", 78)]
#
# age = lambda ages: ages[2]
# students.sort(key=age)

# students = (("Squidward", "F", 60),
#             ("Sandy", "A", 33),
#             ("Patrick", "D", 36),
#             ("Spongebob", "B", 20),
#             ("Mr.Grabs", "C", 78))
#
# age = lambda ages: ages[2]
# sorted_tuple = sorted(students, key=age)
# for i in students:
#     print(i)

# store = [("shirt", 20.00),
#          ("pants", 25.00),
#          ("jacket", 50.00),
#          ("socks", 10.00)]
# to_EGP = lambda data: (data[0], data[1]*31)
#
# store_EGP = map(to_EGP,store)
#
# for i in store_EGP:
#     print(i)

# friends = [("Frank", 18),
#            ("Joey", 19),
#            ("Daniel", 15),
#            ("jack", 21),
#            ("jay", 12),
#            ("Kim", 17)]
# filtered = lambda age_checker: age_checker[1] >= 18
#
# after_filter = filter(filtered, friends)
#
# for i in after_filter:
#     print(i)
#
# import functools
#
# letters = ["H", "E", "L", "L", "O"]
# words = lambda x, y: x + y
# print(functools.reduce(words, letters))


# list comprehension =  a way to create a new list with less syntax
#                       can mimic certain lambda functions, easier to read
#                       list = [expression for item in iterable]
#                       list = [expression for item in iterable if conditional]
#                       list = [expression if/else for item in iterable]
# --------------------------------------------------------------
# squares = []  # create an empty list
# for i in range(1, 11):  # create a for loop
#     squares.append(i * i)  # define what each loop iteration should do
# print(squares)
#
# # create a list AND defines what each loop iteration should do
# squares = [i * i for i in range(1, 11)]
# print(squares)

# lista = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
#
# passing_list = list(filter(lambda x: x >= 60, lista))
# pass_list = [i for i in lista if i >= 60]
# pass_fail = [i if i >= 50 else "fail" for i in lista]
# print(passing_list)
# print(pass_list)
# print(pass_fail)
# -------------------------------------------------------------------------
# dictionary comprehension = create dictionaries using an expression
#                            can replace for loops and certain lambda functions
#
# dictionary = {key: expression for (key,value) in iterable}
# dictionary = {key: expression for (key,value) in iterable if conditional}
# dictionary = {key: (if/else) for (key,value) in iterable}
# dictionary = {key: function(value) for (key,value) in iterable}
# -------------------------------------------------------------------------
# cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
# cities_in_C = {key: round((value - 32) * (5 / 9)) for (key, value) in cities_in_F.items()}
# desc_cities = {key: ("Warm" if value > 40 else "cold") for (key, value) in cities_in_F.items()}
# print(cities_in_C)
# print(desc_cities)
# weather = {'New York': "snowing", 'Boston': "sunny", 'Los Angeles': "sunny", 'Chicago': "cloudy"}
# sunny_weather = {key: value for (key, value) in weather.items() if value == "sunny"}
# print(sunny_weather)

# usernames = ["Dude", "Bro", "Mister"]
# passwords = ("p@ssword", "abc123", "guest")
# login_dates = ["1/1/2021", "1/2/2021", "1/3/2021"]
#
# users = zip(usernames,passwords,login_dates)
#
# for i in users:
#     print (i)

# import time
# ***************************************************************************
# print(time.ctime(0))    # convert a time expressed in seconds since epoch to a readable string
#                                        epoch = when your computer thinks time began (reference point)
# print(time.time())      # return current seconds since epoch
# print(time.ctime(time.time())) # will get current time

# ***************************************************************************
# time.strftime(format, time_object) = formats a time_object to a string
# time_object = time.localtime() # local time
# time_object = time.gmtime()  # UTC time
# local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
# print(local_time)

# ***************************************************************************
# time.strptime(string_string, format) = parses a string representing time/date and returns a struct_time object
# time_string = "20 April, 2020"
# time_object = time.strptime(time_string,"%d %B, %Y")
# print(time_object)

# ***************************************************************************
# time.asctime(time_tuple) = accepts a time_object or a tuple up to 9 elements and returns a string
# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
# time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
# time_string = time.asctime(time_tuple)
# print(time_string)

# ***************************************************************************
# time.asctime(time_tuple) = accepts a time_object or a tuple up to 9 elements and return seconds since epoch
# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
# time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
# time_string = time.mktime(time_tuple)
# print(time_string)
# ******************************************************
# Python threading tutorial
# ******************************************************
# thread =  a flow of execution. Like a separate order of instructions.
#                  However, each thread takes a turn running to achieve concurrency
#                  GIL = (global interpreter lock),
#                  allows only one thread to hold the control of the Python interpreter at any one time

# cpu-bound = program/task spends most of it's time waiting for internal events (CPU intensive)
#             use multiprocessing

# io bound = program/task spends most of it's time waiting for external events (user input, web scraping)
#            uses multithreading

# import threading
# import time
#
#
# def eat_breakfast():
#     time.sleep(3)
#     print("You eat breakfast")
#
#
# def drink_coffee():
#     time.sleep(4)
#     print("You drank coffee")
#
#
# def study():
#     time.sleep(5)
#     print("You finish studying")
#
#
# x = threading.Thread(target=eat_breakfast, args=())
# x.start()
#
# y = threading.Thread(target=drink_coffee, args=())
# y.start()
#
# z = threading.Thread(target=study, args=())
# z.start()
#
# x.join()
# y.join()
# z.join()
#
# print(threading.active_count())
# print(threading.enumerate())
# print(time.perf_counter())

# ******************************************************

# daemon thread = a thread that runs in the background, not important for program to run
#                 your program will not wait for daemon threads to complete before exiting
#                 non-daemon threads cannot normally be killed, stay alive until a task is complete
#
#                 ex. background tasks, garbage collection, waiting for input, long-running processes

# import threading
# import time
#
#
# def timer():
#     print()
#     count = 0
#     while True:
#         time.sleep(1)
#         count += 1
#         print("logged in for: ", count, "seconds")
#
#
# x = threading.Thread(target=timer, daemon=True)
# x.start()
#
# # x.setDaemon(True)
# # print(x.isDaemon())
#
# answer = input("Do you wish to exit?")

# from multiprocessing import Process, cpu_count
# import time
#
#
# def counter(num):
#     count = 0
#     if count < num:
#         count += 1
#
#
# def main():
#     print(cpu_count())
#     a = Process(target=counter, args=(250000,))
#     b = Process(target=counter, args=(250000,))
#     c = Process(target=counter, args=(250000,))
#     d = Process(target=counter, args=(250000,))
#
#     a.start()
#     b.start()
#     c.start()
#     d.start()
#
#     a.join()
#     b.join()
#     c.join()
#     d.join()
#     print("finished in ", time.perf_counter(), "sec")
#
#
# if __name__ == '__main__':
#     main()
# from tkinter import *
#
# window = Tk()  # instantiating instance of a window
# window.geometry("420x420")
# window.title("First GUI Program")
# icon = PhotoImage(file='startup-png-22.png')
# hellow = PhotoImage(file='Hello-Transparent.png')
# window.iconphoto(True, icon)
# window.config(background='#5cfcff')
# label = Label(window,
#               text="Hello World",
#               font=("Arial", 40, 'bold'),
#               fg="#00FF00",  # font color
#               bg="blue",  # background color
#               relief=RAISED,  # for border enable
#               bd=10,  # for border size
#               padx=20,  # padding between words and border in width
#               pady=20,  # padding between words and border in height
#               #image=hellow,
#               compound='bottom')
# label.pack()
#
#
# # label.place(x=0, y=0)
# count = 0
# def click():
#     global count
#     count +=1
#     print(count)
#
#
# button_image = PhotoImage(file="R.png")
# button = Button(window,
#                 text="click me!",
#                 command=click,
#                 font=("Comic Sans", 30),
#                 fg="#00ff00",
#                 bg="black",
#                 activebackground="#00ff00",  # changes color instead of flashing white after clicking
#                 activeforeground="black",
#                 state=ACTIVE,  # enable and disable button
#                 image=button_image,
#                 compound="bottom")
# button.pack()
# window.mainloop()

# from tkinter import *
#
# window = Tk()
#
# entry = Entry(window,
#               font=("Arial", 50),
#               fg='#00ff00',
#               bg='black',
#               show='*')
# entry.pack(side='left')
#
#
# def submit():
#     username = entry.get()
#     print("submit button says: " + username)
#     entry.config(state=DISABLED)
#
# submit_button = Button(window, text='Submit', command=submit)
# submit_button.pack(side='right')
#
#
# def delete():
#     entry.delete(0, END)
#
#
# delete_button = Button(window, text='Delete', command=delete)
# delete_button.pack(side='right')
#
#
# def backspace():
#     entry.delete(len(entry.get()) - 1, END)
#
#
# backspace_button = Button(window, text='Delete', command=backspace)
# backspace_button.pack(side='right')
# window.mainloop()
# from tkinter import *
#
#
# def display():
#     if x.get() == 1:
#         print("you agree")
#     else:
#         print("seems you don't agree")
#
#
# window = Tk()
# x = IntVar()
# python_icon = PhotoImage(file='python.png')
# check_button = Checkbutton(window,
#                            text="I agree to do something",
#                            variable=x,
#                            onvalue=1,
#                            offvalue=2,
#                            command=display,
#                            font=("Arial", 20),
#                            fg="#00ff00",
#                            bg="black",
#                            activeforeground="#00ff00",
#                            activebackground="black",
#                            image=python_icon,
#                            padx='15',
#                            pady='20',
#                            compound='left'
#                            )
# check_button.pack()
# window.mainloop()
#
# from tkinter import *
#
# food = ["hamburger", "pizza", "hotdog"]
#
# window = Tk()
# pizza_image = PhotoImage(file='Pizza.png')
# hamburger_image = PhotoImage(file='Hamburger.png')
# hotdog_image = PhotoImage(file='hotdog.png')
# food_images = [hamburger_image, pizza_image, hotdog_image]
#
#
# def order():
#     if x.get() == 0:
#         print("you ordered hamburger")
#     elif x.get() == 1:
#         print("you ordered pizza")
#     else:
#         print("you ordered hotdog")
#
#
# x = IntVar()
# window.geometry("420x420")
#
# for index in range(len(food)):
#     radiobutton = Radiobutton(window,
#                               text=food[index],
#                               variable=x,
#                               value=index,
#                               padx=25,
#                               font=("impact", 20),
#                               image=food_images[index],
#                               compound="right",
#                               indicatoron=False,
#                               width=375,
#                               command=order)
#     radiobutton.pack(anchor=W)
# window.mainloop()
# from tkinter import *
#
#
# def submit():
#     print("the temperature is " + str(scale.get()) + " degree C")
#
#
# window = Tk()
#
# scale = Scale(window,
#               from_=100,
#               to=0,
#               length=600,
#               orient=VERTICAL,
#               font=('Consolas', 20),
#               tickinterval=10,
#               showvalue=False,  # hide current value
#               troughcolor="#69EAFF",
#               fg="#FF1C00",
#               bg="black"
#               )
# # scale.set(50) #indicates where the bar should start from
# scale.pack()
#
# button = Button(window, text="Submit", command=submit)
# button.pack()
#
# window.mainloop()
# from tkinter import *
#
#
# def submit():
#     food = []
#     for index in list_box.curselection():
#         food.insert(index, list_box.get(index))
#     print("uou have ordered:")
#     for i in food:
#         print(i)
#
# def add():
#     list_box.insert(list_box.size(), entry.get())
#     list_box.config(height=list_box.size())
#
#
# def delete():
#     for index in reversed(list_box.curselection()):
#         list_box.delete(index)
#     list_box.config(height=list_box.size())
#
#
# Window = Tk()
#
# list_box = Listbox(Window,
#                    bg="#f7ffde",
#                    font=("Constantia", 35),
#                    width=12,
#                    selectmode=MULTIPLE
#                    )
# list_box.pack()
# list_box.insert("1", "Pizza")
# list_box.insert("2", "Garlic Bread")
# list_box.insert("3", "hotdog")
# list_box.insert("4", "pasta")
# list_box.insert("5", "Hamburger")
# list_box.config(height=list_box.size())
#
# entry = Entry(Window)
# entry.pack()
# button_submit = Button(Window, text="Submit", command=submit)
# button_submit.pack()
#
# button_add = Button(Window, text="Add", command=add)
# button_add.pack()
#
# button_delete = Button(Window, text="delete", command=delete)
# button_delete.pack()
# Window.mainloop()

# from tkinter import messagebox
# from tkinter import *
#
#
# def click():
#     messagebox.showinfo(title="Info", message="showing information to user")
#     messagebox.showwarning(title="warning", message="showing warning to user")
#     messagebox.showerror(title="error",message="something went wrong", icon ='error')
#     if messagebox.askokcancel(title="do a thing", message="do you want to do a thing"):
#         print("you agreed doing a thing!")
#     else:
#         print("you didn't agree doing a thing!")
#     if messagebox.askretrycancel(title="do a thing", message="do you want to retry a thing"):
#         print("you retried doing a thing!")
#     else:
#         print("you didn't agree retrying a thing!")
#     if messagebox.askyesno(title="hey", message="do you like cake"):
#         print("same do i")
#     else:
#         print("why not")
#
#
# Window = Tk()
#
# button = Button(Window, text="click me", command=click)
# button.pack()
# Window.mainloop()

# from tkinter import *
# from tkinter import colorchooser
#
#
# def click():
#     user_input = text.get("1.0", END)
#     Window.config(bg=colorchooser.askcolor()[1])
#     text.config(bg=colorchooser.askcolor()[1])
#     print(user_input)
#
#
# Window = Tk()
#
# button = Button(Window, text="select requested color", command=click)
# button.pack()
# text = Text(Window)
# text.pack()
# Window.mainloop()

# from tkinter import *
# from tkinter import filedialog
#
#
# def openfile():
#     filepath = filedialog.askopenfilename(initialdir="E:\\CV",
#                                           title="Open file okay?",
#                                           filetypes=(("text files", "*.txt"),
#                                                      ("all files", "*.*")))
#     with open(filepath) as file:
#         print(file.read())
#
#
# def savefile():
#     file = filedialog.asksaveasfile(defaultextension='.txt',
#                                     filetypes=[("Text Files", ".txt"), ("HTML", ".html"), ("All Files", ".*")],
#                                     initialdir="E:\\CV",
#                                     title="Open file okay?",
#                                     )
#     if file is None:
#         return
#     filetext = str(text.get(1.0, END))
#     file.write(filetext)
#     file.close()
#
#
# Window = Tk()
# Window.geometry("420x420", )
# button_open = Button(Window, text="Open file", command=openfile, )
# button_open.pack(side="left")
# button_save = Button(Window, text="Save file", command=savefile)
# button_save.pack(side="left")
# text = Text(Window)
# text.pack(side="right")
# Window.mainloop()

# from tkinter import *
#
#
# def openfile():
#     print("files has been opened")
#
#
# def savefile():
#     print("files has been saved")
#
#
# window = Tk()
# openimage= PhotoImage(file="open.png")
# menubar = Menu(window)
# window.config(menu=menubar)
# fileMenu = Menu(menubar, tearoff=0)  # used to remove annoying line at the beginning
# editMenu = Menu(menubar, tearoff=0)
#
# menubar.add_cascade(label="File", menu=fileMenu)
# menubar.add_cascade(label="Edit", menu=editMenu)
#
# fileMenu.add_command(label="Open", command=openfile,image=openimage,compound="left")
# fileMenu.add_command(label="Save", command=savefile)
# fileMenu.add_separator()
# fileMenu.add_command(label="Exit", command=quit)
#
# editMenu.add_command(label="Copy")
# editMenu.add_command(label="Paste")
# editMenu.add_command(label="Cut")
# window.mainloop()

# from tkinter import *
#
# window = Tk()
# frame = Frame(window)
# frame.pack()
# Button(frame, text="w", font=("Consolas", 25), width=3).pack(side=TOP)
# Button(frame, text="A", font=("Consolas", 25), width=3).pack(side=LEFT)
# Button(frame, text="S", font=("Consolas", 25), width=3).pack(side=LEFT)
# Button(frame, text="D", font=("Consolas", 25), width=3).pack(side=LEFT)
# window.mainloop()

# from tkinter import *
#
#
# def create_window():
#     new_window = Tk()  # Toplevel() = new window 'on top' of other windows, linked to a 'bottom' window
#     # Tk() = new independent window
#     # old_window.destroy()   #close out of old window
#
#
# old_window = Tk()
#
# Button(old_window, text="create new window", command=create_window).pack()
#
# old_window.mainloop()
# from tkinter import *
# from tkinter import ttk
#
# window = Tk()
#
# notebook = ttk.Notebook(window)  # widget that manages a collection of windows/displays
#
# tab1 = Frame(notebook)  # new frame for tab 1
# tab2 = Frame(notebook)  # new frame for tab 2
#
# notebook.add(tab1, text="Tab 1")
# notebook.add(tab2, text="Tab 2")
# notebook.pack(expand=True, fill="both")  # expand = expand to fill any space not otherwise used
# # fill = fill space on x and y-axis
# Label(tab1, text="Hello, this is tab#1", width=50, height=25).pack()
# Label(tab2, text="Goodbye, this is tab#2", width=50, height=25).pack()
#
# window.mainloop()


# from tkinter import *
#
# # grid() = geometry manager that organizes widgets in a table-like structure in a parent widget
#
# window = Tk()
#
# titleLabel = Label(window, text="Enter your info", font=("Arial", 25)).grid(row=0, column=0, columnspan=2)
#
# firstNameLabel = Label(window, text="First name: ", width=20, bg="red").grid(row=1, column=0)
# firstNameEntry = Entry(window).grid(row=1, column=1)
#
# lastNameLabel = Label(window, text="Last name: ", bg="green").grid(row=2, column=0)
# lastNameEntry = Entry(window).grid(row=2, column=1)
#
# emailLabel = Label(window, text="email: ", bg="blue").grid(row=3, column=0)
# emailEntry = Entry(window).grid(row=3, column=1)
#
# submitButton = Button(window, text="Submit").grid(row=4, column=0, columnspan=2)
#
# window.mainloop()
# from tkinter import *
# from tkinter.ttk import *
# import time
#
#
# def start():
#     GB = 100
#     download = 0
#     speed = 1
#     while (download < GB):
#         time.sleep(0.05)
#         bar['value'] += (speed / GB) * 100
#         download += speed
#         percent.set(str(int((download / GB) * 100)) + "%")
#         text.set(str(download) + "/" + str(GB) + " GB completed")
#         window.update_idletasks()
#
#
# window = Tk()
#
# percent = StringVar()
# text = StringVar()
#
# bar = Progressbar(window, orient=HORIZONTAL, length=300)
# bar.pack(pady=10)
#
# percentLabel = Label(window, textvariable=percent).pack()
# taskLabel = Label(window, textvariable=text).pack()
#
# button = Button(window, text="download", command=start).pack()
#
# window.mainloop()

# canvas =  widget that is used to draw graphs, plots, images in a window

# from tkinter import *
#
# window = Tk()
#
# canvas = Canvas(window,height=500,width=500)
# #canvas.create_line(0,0,500,500,fill="blue",width=5)
# #canvas.create_line(0,500,500,0,fill="red",width=5)
# #canvas.create_rectangle(50,50,250,250,fill="purple")
# #points = [250,0,500,500,0,500]
# #canvas.create_polygon(points,fill="yellow",outline="black",width=5)
# #canvas.create_arc(0,0,500,500,style=PIESLICE,start=270,width=5)
# canvas.create_arc(0,0,500,500,fill="red",extent=180,width=10)
# canvas.create_arc(0,0,500,500,fill="white",extent=180,start=180,width=10)
# canvas.create_oval(190,190,310,310,fill="white",width=10)
# canvas.pack()
#
# window.mainloop()

# from tkinter import *
#
#
# def pressedkey(event):
#     label.config(text=event.keysym)
#
#
# window = Tk()
# window.bind("<Key>", pressedkey)
# label = Label(window, font=("Helvetica", 100))
# label.pack()
# window.mainloop()
# from tkinter import *
#
#
# def doSomething(event):
#     print("Mouse coordinates: " + str(event.x) + "," + str(event.y))
#
#
# window = Tk()
#
# window.bind("<Button-1>", doSomething)  # left mouse click
# # window.bind("<Button-2>",doSomething) #scroll wheel
# # window.bind("<Button-3>",doSomething) #right mouse click
# # window.bind("<ButtonRelease>",doSomething)#mousebutton release
# # window.bind("<Enter>",doSomething) #enter the window
# # window.bind("<Leave>",doSomething) #leave the window
# # window.bind("<Motion>",doSomething) #Where the mouse moved
# window.mainloop()
#
# from tkinter import *
#
# def drag_start(event):
#     widget = event.widget
#     widget.startX = event.x
#     widget.startY = event.y
#
# def drag_motion(event):
#     widget = event.widget
#     x = widget.winfo_x() - widget.startX + event.x
#     y = widget.winfo_y() - widget.startY + event.y
#     widget.place(x=x,y=y)
#
# window = Tk()
#
# label = Label(window,bg="red",width=10,height=5)
# label.place(x=0,y=0)
#
# label2 = Label(window,bg="blue",width=10,height=5)
# label2.place(x=100,y=100)
#
# label.bind("<Button-1>",drag_start)
# label.bind("<B1-Motion>",drag_motion)
#
# label2.bind("<Button-1>",drag_start)
# label2.bind("<B1-Motion>",drag_motion)
#
# window.mainloop()

# from tkinter import *
#
#
# def move_up(event):
#     label.place(x=label.winfo_x(), y=label.winfo_y() - 10)
#
#
# def move_down(event):
#     label.place(x=label.winfo_x(), y=label.winfo_y() + 10)
#
#
# def move_right(event):
#     label.place(x=label.winfo_x() + 10, y=label.winfo_y())
#
#
# def move_left(event):
#     label.place(x=label.winfo_x() - 10, y=label.winfo_y())
#
#
# window = Tk()
# window.geometry("500x500")
# window.bind("<w>", move_up)
# window.bind("<s>", move_down)
# window.bind("<d>", move_right)
# window.bind("<a>", move_left)
# car = PhotoImage(file="car.png")
# label = Label(window, image=car)
# label.place(x=0, y=0)
# window.mainloop()

# from tkinter import *
# from time import *

# def update():
#     time_string = strftime("%I:%M:%S %p")
#     time_label.config(text=time_string)
#
#     day_string = strftime("%A")
#     day_label.config(text=day_string)
#
#     date_string = strftime("%B %d, %Y")
#     date_label.config(text=date_string)
#
#     window.after(1000,update)
#
#
# window = Tk()
#
# time_label = Label(window,font=("Arial",50),fg="#00FF00",bg="black")
# time_label.pack()
#
# day_label = Label(window,font=("Ink Free",25,"bold"))
# day_label.pack()
#
# date_label = Label(window,font=("Ink Free",30))
# date_label.pack()
#
# update()
#
# window.mainloop()

# import smtplib
#
# sender = "omar.hesham.shehab@gmail.com"
# receiver = "omar.hesham.shehab@outlook.com"
# password = "Delpiero#25!!92"
# subject = "Python email test"
# body = "I wrote an email! :D"
#
# # header
# message = f"""From: Snoop Dogg{sender}
# To: Nicholas Cage{receiver}
# Subject: {subject}\n
# {body}
# """
# server = smtplib.SMTP("smtp.gmail.com", 587)
# server.starttls()
#
# try:
#     server.login(sender,password)
#     print("Logged in...")
#     server.sendmail(sender, receiver, message)
#     print("Email has been sent!")
#
# except smtplib.SMTPAuthenticationError:
#     print("unable to sign in")
