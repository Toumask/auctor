import glob
import os
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import shutil
from tkinter.filedialog import askopenfile


def get_directory_right():
    global directory_right
    filename = filedialog.askdirectory()
    directory_right.set(filename)
    print(filename)


def get_directory_left():
    global directory_left
    filename = filedialog.askdirectory()
    directory_left.set(filename)
    print(filename)


def get_pictures():
    global folder_path_picture_directory
    global image_list
    global image_path_list
    filename = filedialog.askdirectory()
    folder_path_picture_directory.set(filename)
    valid_images = [".jpg", ".png"]
    for f in os.listdir(filename):
        ext = os.path.splitext(f)[1]
        if ext.lower() not in valid_images:
            continue
        image_list.append(Image.open(os.path.join(filename, f)))
        image_path_list.append(filename + '/' + f)
    print(image_list[0])
    print(filename)


# Tkinter Basic Setup
root = Tk()
root.title('Auctor')
root.geometry("1280x720")

# folder_path_picture_directory
folder_path_picture_directory = StringVar()
picture_directory_label = Label(root, textvariable=folder_path_picture_directory)
picture_directory_label.grid(row=0, column=1)
picture_directory_button = Button(text="Browse picture directory",
                                  command=get_pictures)
picture_directory_button.grid(row=0, column=3)

# directory_right browser
directory_right = StringVar()
directory_right_label = Label(root, textvariable=directory_right)
directory_right_label.grid(row=1, column=1)
directory_right_button = Button(text="Browse directory_right", command=get_directory_right)
directory_right_button.grid(row=1, column=3)

# directory_left browser
directory_left = StringVar()
directory_left_label = Label(root, textvariable=directory_left)
directory_left_label.grid(row=2, column=1)
directory_left_button = Button(text="Browse directory_left", command=get_directory_left)
directory_left_button.grid(row=2, column=3)

image_number = 1


# show images
def forward(number):
    global my_label
    global image_number
    number = image_number
    my_label.grid_forget()
    ph = ImageTk.PhotoImage(image_list[number - 1])
    my_label = Label(image=ph)
    my_label.image = ph
    my_label.grid()
    image_number = image_number + 1


image_path_list = []
image_list = []
my_label = Label()
my_label.grid()

start_button = Button(text="start Button", command=lambda: forward(image_number))
start_button.grid(row=3, column=1)


# listen for button presses
def leftKey(event):
    global image_number
    file_to_move = image_path_list[0]
    shutil.move(file_to_move, directory_left.get())
    image_path_list.pop(0)
    forward(image_number)
    print("Left key pressed")


def rightKey(event):
    global image_number
    file_to_move = image_path_list[0]
    shutil.move(file_to_move, directory_right.get())
    image_path_list.pop(0)
    forward(image_number)
    print("Right key pressed")


def skipKey(event):
    global image_number
    forward(image_number)
    print("skip key pressed")


def deleteKey(event):
    global image_number
    file_to_delete = image_list[0]
    os.remove(file_to_delete)
    image_list.pop(0)
    forward(image_number)
    print("delete key pressed")


root.bind('<Up>', deleteKey)
root.bind('<Down>', skipKey)
root.bind('<Left>', leftKey)
root.bind('<Right>', rightKey)

root.bind('<w>', deleteKey)
root.bind('<s>', skipKey)
root.bind('<a>', leftKey)
root.bind('<d>', rightKey)

# main loop
root.mainloop()
