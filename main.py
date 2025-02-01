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

# este script debe crear una ventana que permita programar el tiempo de apagado en minutos o cancelar alguna
# programación ya realizada
from subprocess import run


#ans = run("shutdown /s /t 3600",  shell = True, capture_output = True)

ans = run("shutdown /a",  shell = True, capture_output = True)

print("retorno de run ", ans)
print("tipo del retorno de run ", type(ans))
print("return code:",ans.returncode)
print("return stderr:",ans.stderr)

#el codigo de exito en cualquier caso es 0. los mensajes de exito son vacíos ''

## error cuando queres programar el apagado pero ya programaste uno anterior
## codigo de error: 1190
## mesaje de error: b'Ya se program\xa2 un cierre del sistema.(1190)\n'

## error cuando queres cancelar el tiempo de apagado pero no hay ningun tiempo programado
## codigo de error: 1116
## mesaje de error: b'No se puede anular el apagado del sistema porque no se estaba apagando.(1116)\n'
root.mainloop()