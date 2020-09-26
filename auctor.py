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
        image_path_list.append(filename + '/' + f)
    print(image_list[0])
    print(filename)


# Tkinter Basic Setup ########################################
root = Tk()
root.title('Auctor')
root.iconbitmap('logo.ico')
root.geometry("1280x720")
###############################################################

# Frames ######################################################
setting_up_frame = LabelFrame(root, text='Start here!', padx=5, pady=5)
setting_up_frame.pack(anchor=W, fill=Y, expand=False, side=LEFT, padx=10, pady=10)

picture_frame = LabelFrame(root, text='Pictures', padx=50, pady=50)
picture_frame.pack(anchor=N, fill=BOTH, expand=True, side=LEFT, padx=10, pady=10)
###############################################################

# folder_path_picture_directory
folder_path_picture_directory = StringVar()
picture_directory_label = Label(setting_up_frame, textvariable=folder_path_picture_directory)
picture_directory_label.pack()
picture_directory_button = Button(setting_up_frame, text="Browse picture directory",
                                  command=get_pictures)
picture_directory_button.pack()

# directory_right browser
directory_right = StringVar()
directory_right_label = Label(setting_up_frame, textvariable=directory_right)
directory_right_label.pack()
directory_right_button = Button(setting_up_frame, text="Browse directory_right", command=get_directory_right)
directory_right_button.pack()

# directory_left browser
directory_left = StringVar()
directory_left_label = Label(setting_up_frame, textvariable=directory_left)
directory_left_label.pack()
directory_left_button = Button(setting_up_frame, text="Browse directory_left", command=get_directory_left)
directory_left_button.pack()


# show images
def forward():
    global my_label
    my_label.pack_forget()
    im = Image.open(image_path_list[0])
    ph = ImageTk.PhotoImage(im)
    my_label = Label(picture_frame, image=ph)
    my_label.image = ph
    my_label.pack()


image_path_list = []
image_list = []
my_label = Label(picture_frame)

start_button = Button(picture_frame, text="start Button", command=forward)
start_button.pack()


# listen for button presses
def leftKey(event):
    file_to_move = image_path_list[0]
    shutil.move(file_to_move, directory_left.get())
    image_path_list.pop(0)
    forward()
    print("Left key pressed")


def rightKey(event):
    file_to_move = image_path_list[0]
    shutil.move(file_to_move, directory_right.get())
    image_path_list.pop(0)
    forward()
    print("Right key pressed")


def skipKey(event):
    image_path_list.pop(0)
    forward()
    print("skip key pressed")


def deleteKey(event):
    file_to_delete = image_path_list[0]
    os.remove(file_to_delete)
    image_path_list.pop(0)
    forward()
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
