
from tkinter import filedialog
from tkinter import simpledialog

files_path = filedialog.askdirectory(mustexist=True)
name = simpledialog.askstring("Nombre de los ficheros",
"Escribe el nuevo nombre para los ficheros incluyendo {} donde vayan los números")

print (files_path)
print (name)
