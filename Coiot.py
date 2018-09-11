from tkinter import filedialog
from Arquivo import isolarMensagens


TIPO, TIME_STAMP, LONGITUDE, LATITUDE, ALTITUDE, BPM, N_PASSOS = list(range(7))

with open(filedialog.askopenfilename(filetypes = [("Text files", "*.txt")])) as arquivo:
	mensagem = isolarMensagens(arquivo)

# imprime tabela formatada
#for i in mensagem:
#	for x in i:
#		print("{:24}".format(x), end='')
#	print()