#gerador de senhas
#importa a biblioteca para randomizar e importa os alfabetos
import random
import string
#variaveis
loop = 0

#mensagem inicial
print ('-'*30)
print ('Bem vindo ao gerador de senhas! ')
print ('-'*30)
#função que gera senha 
def geradorSenha():
    #faz uma lista coma variavel senha
    senha = list()
    #variavel vazia. Nem sei para que to usando isso mais
    senhapronta = ''
    #importa os alfabetos e junta eles
    alfabeto_Mai = string.ascii_lowercase
    alfabeto_min = string.ascii_uppercase
    alfabeto_comp = alfabeto_min + alfabeto_Mai
    #faz uma seleção para o usuario (tamanho da senha)
    selecao = int(input('Qual o tamanho da sua senha? '))
    #faz um loop com o tamnhao selecionado
    for c in range(0, selecao):
        numeros = random.randrange(0, 9)
        letras = random.choice(alfabeto_comp)
        senha.append(letras)
        senha.append(str(numeros))
        senha[:]
    #mostra a senha 
    senhapronta = ''.join(senha[:selecao])
    print('Sua senha é:')
    print(senhapronta)
    #senhapronta.join(senha)
    #print (senhapronta)


#programa principal
while loop == 0:
    menu = int(input('Digite um valor valido: \n [1] Gerar senha \n [2] Sair \nValor: '))
    if menu == 1:
        geradorSenha()
        pergunta = str(input('Deseja gerar outra senha? [S/N]: ')).upper().strip()
        if pergunta == 'S':
            geradorSenha()
        elif pergunta != 'S' or 'N':
            print('Bye!! ')
            loop += 1
    if menu == 2:
        print ('Bye !!!')
        loop += 1
    elif menu != 1 or 2:
        print ('Escolha uma opção valida! ')
    else: 
        print('Bye! ')
        loop += 1