#Curso Básico de Python
#Nome do desenvolvedor: ANA LUIZA DE MORAIS BELLINI
#Versão 1.0
#Exercício de lógica de programação
#Com a linguagem de programação Python
#Exercício: 8) Ler as notas da 1a. e 2a. avaliações de um aluno.
#Calcular a média aritmética simples e escrever uma mensagem que diga se o aluno foi ou não aprovado 
# (considerar que nota igual ou maior que 6 o aluno é aprovado). Escrever também a média calculada.

nota1=float(input("Digite a nota da 1ª avaliação: "))
nota2=float(input("Digite a nota da 2ª avaliação: "))
media=(nota1+nota2)/2
if media>=6:
    situacao="aprovado"
else:
    situacao="reprovado"
print("A média do aluno é:", media)
print("O aluno está", situacao)
print("OBRIGADA POR UTILIZAR O PROGRAMA >3")