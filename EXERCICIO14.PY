#Curso Básico de Python
#Nome do desenvolvedor: ANA LUIZA DE MORAIS BELLINI
#Versão 1.0
#Exercício de lógica de programação
#Com a linguagem de programação Python
#Exercício: 14) Ler 3 valores (considere que não serão informados valores iguais)
# e escrever o maior deles.

numero1=float(input("Digite o primeiro número: "))
numero2=float(input("Digite o segundo número: "))
numero3=float(input("Digite o terceiro número: "))
maior_numero=numero1
if numero2>maior_numero:
    maior_numero=numero2
if numero3>maior_numero:
    maior_numero=numero3
print("O maior número é:", maior_numero)
print("OBRIGADA POR UTILIZAR O PROGRAMA >3")