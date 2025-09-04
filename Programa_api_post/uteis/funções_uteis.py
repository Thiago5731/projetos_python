#funções_uteis.

def validação():
    """loop de validação (pergunta [s/n])"""
    while True:
            confirma = str(input('Você deseja rodar outra API? [S/N]: ')).upper().strip()
            if confirma == 'N':
                print ('Até a proxima! Qualquer sugestão de melhoria, pode nós encaminhar! ')
                loop += 1
                break
            if confirma != 'S' and confirma != 'N':
                print ('Por favor escolha uma opção valida! ')
            if confirma == 'S':
                break


def titulo():
     """marcação do titulo cmd"""
     print('-'*50)