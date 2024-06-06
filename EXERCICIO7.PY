#Curso Básico de Python
#Nome do desenvolvedor: ANA LUIZA DE MORAIS BELLINI
#Versão 1.0
#Exercício de lógica de programação
#Com a linguagem de programação Python
#Exercício: 7) As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia,
# e R$ 1,00 se forem compradas pelo menos 12. 
# Escreva um programa que leia o número de maçãs compradas, 
# calcule e escreva o custo total da compra.

quantidade_maca=int(input("Digite o número de maçãs compradas: "))
if quantidade_maca<12:
    custo_total=quantidade_maca*1.30
else:
    custo_total=quantidade_maca*1.00
print("O custo total da compra é R$", custo_total)
print("OBRIGADA POR UTILIZAR O PROGRAMA >3")