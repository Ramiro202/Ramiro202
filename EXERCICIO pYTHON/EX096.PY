
from os import system


def somar(larg, compr):
    area = larg * compr
    return area

def main():
    largura = float(input("LARGURA (m): "))
    comprimento = float(input("COMPRIMENTO (m): "))
    resultado = somar(largura, comprimento)

    print(f"A área de um terreno de {largura}x{comprimento} é de {resultado:.2f}m")

system("clear")
print(" Controle de Terreno")
print("__"*20)
main()
