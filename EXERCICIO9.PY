#Curso Básico de Python
#Nome do desenvolvedor: ANA LUIZA DE MORAIS BELLINI
#Versão 1.0
#Exercício de lógica de programação
#Com a linguagem de programação Python
#Exercício: 9) Ler o ano atual e o ano de nascimento de uma pessoa. 
# Escrever uma mensagem que diga se ela poderá ou não votar este ano 
# (não é necessário considerar o mês em que a pessoa nasceu).

ano_atual=int(input("Digite o ano atual: "))
ano_nascimento=int(input("Digite o ano de nascimento: "))
idade=ano_atual-ano_nascimento
if idade >= 16:
    print("Você poderá votar este ano!")
else:
    print("Você não poderá votar este ano.")
print("OBRIGADA POR UTILIZAR O PROGRAMA >3")