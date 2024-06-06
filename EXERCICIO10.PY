#Curso Básico de Python
#Nome do desenvolvedor: ANA LUIZA DE MORAIS BELLINI
#Versão 1.0
#Exercício de lógica de programação
#Com a linguagem de programação Python
#Exercício: 10) Ler dois valores (considere que não serão lidos valores iguais) 
# e escrever o maior deles.

valor1=float(input("Digite o primeiro valor: "))
valor2=float(input("Digite o segundo valor: "))
if valor1 > valor2:
    maior_valor=valor1
else:
    maior_valor=valor2
print("O maior valor é:", maior_valor)
print("OBRIGADA POR UTILIZAR O PROGRAMA >3")