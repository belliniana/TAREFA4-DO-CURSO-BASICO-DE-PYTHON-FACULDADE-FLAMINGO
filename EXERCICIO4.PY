#Curso Básico de Python
#Nome do desenvolvedor: ANA LUIZA DE MORAIS BELLINI
#Versão 1.0
#Exercício de lógica de programação
#Com a linguagem de programação Python
#Exercício: 4) Faça um algoritmo que leia três notas de um aluno, calcule e escreva 
# a média final deste aluno.Considerar que a média é ponderada e que o peso das
# notas é 2, 3 e 5. Fórmula para o cálculo da média final é: mediafinal =(n1 * 2 + n2 * 3 + n3 * 5)/10

nota1=float(input("Digite a primeira nota: "))
nota2=float(input("Digite a segunda nota: "))
nota3=float(input("Digite a terceira nota: "))
media_final=(nota1*2+nota2*3+nota3*5)/10
print("A média final do aluno é:", media_final)
print("OBRIGADA POR UTILIZAR O PROGRAMA >3")