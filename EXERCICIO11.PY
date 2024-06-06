#Curso Básico de Python
#Nome do desenvolvedor: ANA LUIZA DE MORAIS BELLINI
#Versão 1.0
#Exercício de lógica de programação
#Com a linguagem de programação Python
#Exercício:11) Ler dois valores (considere que não serão lidos valores iguais)
# e escrevê-los em ordem crescente

valor1=float(input("Digite o primeiro valor: "))
valor2=float(input("Digite o segundo valor: "))
if valor1<valor2:
    menor_valor=valor1
    maior_valor=valor2
else:
    menor_valor=valor2
    maior_valor=valor1
print("Os valores em ordem crescente são:", menor_valor, ",", maior_valor)
print("OBRIGADA POR UTILIZAR O PROGRAMA >3")