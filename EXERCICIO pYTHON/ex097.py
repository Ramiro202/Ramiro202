
from os import system


def escreva(msg):
	tamanho = len(msg)
	print("~~"*tamanho)
	print(f"{msg.center(tamanho*2)}")
	print("~~"*tamanho)


system("clear")
escreva("Ramiro")
escreva("Ramiro Ngando")
escreva("30")
