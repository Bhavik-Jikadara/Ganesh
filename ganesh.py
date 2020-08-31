import tkinter as tk
from tkinter import ttk
import time

root = tk.Tk()
root.title("Happy Ganesh Chaturthi")
root.geometry("100x50")

# Button create  


def Ganesh():
    
    print("              HAPPY GANESH CHATURTHI               ")

    print("                   ___________                     ")    
    time.sleep(1)
    print("                  (___________)                    ")
    time.sleep(1)
    print("                (    ______     )                  ")
    time.sleep(1)
    print("              (      ______      )                 ")
    time.sleep(1)
    print("               (    /      \    )                  ")
    time.sleep(1)
    print("           ____ ( /  _    _  \ ) _____             ")
    time.sleep(1)
    print("          |     \|   0    0   | /     |            ")
    time.sleep(1)
    print("          |____ /|    /  \    | \_____|            ")
    time.sleep(1)
    print("                  \   |  |   /                     ")
    time.sleep(1)
    print("                 __ \ |  | /  __                   ")
    time.sleep(1)
    print("               /    / |  \_| |  \                  ")
    time.sleep(1)
    print("             /     /_/ \_____|    \                ")
    time.sleep(1)
    print("    ___     /                      \               ")
    time.sleep(1)
    print("   /   \   /                        \   _          ")
    time.sleep(1)
    print("  |     | |\                        /  (_)         ")
    time.sleep(1)
    print("  |     |/| \                      / \-----/       ")
    time.sleep(1)
    print("   \_____/   \                    /   \___/        ")
    time.sleep(1)
    print("  ( --------  \__       0        /----------       ")
    time.sleep(1)
    print(" (                \__       __/             )      ")
    time.sleep(1)
    print("  (                 \_  __ /                 )     ")
    time.sleep(1)
    print("   (                   \                   )       ")
    time.sleep(1)
    print("     (                   |               )         ")
    time.sleep(1)
    print("       -------\______                  )           ")
    time.sleep(1)
    print("                     |   |    ______ )             ")
    time.sleep(1)
    print("                    /_ _ /_ _/                     ")
time.sleep(1)




ganesh = ttk.Button(root,text="Happy Ganesh Chaturthi",command = Ganesh)
ganesh.grid(row=1,column=0)


root.mainloop()