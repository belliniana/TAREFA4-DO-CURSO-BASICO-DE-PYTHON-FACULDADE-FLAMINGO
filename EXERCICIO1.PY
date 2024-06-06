#Curso Básico de Python
#Nome do desenvolvedor: ANA LUIZA DE MORAIS BELLINI
#Versão 1.0
#Exercício de lógica de programação
#Com a linguagem de programação Python
#Exercício: 1) Escreva um algoritmo para ler o número total de 
# eleitores de um município, o número de votos brancos, nulos e válidos.
# Calcular e escrever o percentual que cada um representa em relação ao total de eleitores.

total_eleitores=int(input("Digite o número total de eleitores: "))
votos_brancos=int(input("Digite o número de votos brancos: "))
votos_nulos=int(input("Digite o número de votos nulos: "))
votos_validos=int(input("Digite o número de votos válidos: "))
percentual_brancos=(votos_brancos/total_eleitores)*100
percentual_nulos=(votos_nulos/total_eleitores)*100
percentual_validos=(votos_validos/total_eleitores)*100
print("Percentual de votos brancos:", percentual_brancos, "%")
print("Percentual de votos nulos:", percentual_nulos, "%")
print("Percentual de votos válidos:", percentual_validos, "%")
print("OBRIGADA POR UTILIZAR O PROGRAMA >3")