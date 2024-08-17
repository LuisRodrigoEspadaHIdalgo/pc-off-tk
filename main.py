#Mini app con tkinter para ejecutar shutdown
#y apagar la pc
import tkinter as tk

root = tk.Tk()

message = tk.Label(root, text="Ingrese en cuantos minutos se apagará la pc:")
message.pack()

root.title("Apagar Pc")

window_width = 300
window_height = 200

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.resizable(False, False)
root.attributes('-topmost', 1)
root.iconbitmap('./img/kipi.ico')


root.mainloop()