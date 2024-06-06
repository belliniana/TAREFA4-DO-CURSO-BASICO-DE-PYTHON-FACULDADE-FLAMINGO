#Curso Básico de Python
#Nome do desenvolvedor: ANA LUIZA DE MORAIS BELLINI
#Versão 1.0
#Exercício de lógica de programação
#Com a linguagem de programação Python
#Exercício: 2) Escreva um algoritmo para ler o salário 
# mensal atual de um funcionário e o percentual de reajuste.
# Calcular e escrever o valor do novo salário.

salario_atual=float(input("Digite o salário mensal atual do funcionário: R$"))
percentual_reajuste=float(input("Digite o percentual de reajuste: "))
valor_reajuste=salario_atual*(percentual_reajuste/100)
novo_salario=salario_atual+valor_reajuste
print("O novo salário do funcionário será: R$", novo_salario)
print("OBRIGADA POR UTILIZAR O PROGRAMA >3")