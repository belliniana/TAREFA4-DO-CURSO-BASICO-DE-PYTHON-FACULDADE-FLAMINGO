#Curso Básico de Python
#Nome do desenvolvedor: ANA LUIZA DE MORAIS BELLINI
#Versão 1.0
#Exercício de lógica de programação
#Com a linguagem de programação Python
#Exercício: 12) Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. 
# Após, calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito). 
# Também testar se saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo', 
# senão escrever a mensagem 'Saldo Negativo'.

numero_conta=input("Digite o número da conta do cliente: ")
saldo=float(input("Digite o saldo atual: "))
debito=float(input("Digite o débito: "))
credito=float(input("Digite o crédito: "))
saldo_atual = saldo - debito + credito
if saldo_atual>=0:
    mensagem="Saldo Positivo"
else:
    mensagem="Saldo Negativo"
print("O saldo atual da conta", numero_conta, "é:", saldo_atual)
print("Mensagem:", mensagem)
print("OBRIGADA POR UTILIZAR O PROGRAMA >3")