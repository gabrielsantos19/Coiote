from tkinter import filedialog

TIPO, TIME_STAMP, LONGITUDE, LATITUDE, ALTITUDE, BPM, N_PASSOS = list(range(7))
mensagem = []

with open(filedialog.askopenfilename(title = "Abrir", filetypes = [("Text files", "*.txt")])) as arquivo:
	pass

print(N_PASSOS)