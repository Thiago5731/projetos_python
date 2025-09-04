#programa_api
#comentario para esse programa. 
#Vou ter que fazer um biblioteca com outra funções 
#pq só a importação do modulo vai ficar d+ 
# estou pensando em um somente para funções uteis no codigo 
# tipo chegachem: quer continuar? s ou n 
#ou algumas como ('-'*50)
from suporte import funções_suporte
from uteis import funções_uteis
loop = 0 
loop2 = 0

funções_uteis.titulo()
print('Bem vindo ao programa de APIs'.center(50))
funções_uteis.titulo()
usuario = str(input('Para começar, digite seu usuario: '))
funções_uteis.titulo()
senha = str(input('Agora digite sua senha: '))
funções_uteis.titulo()
while loop == 0:
    funções_uteis.titulo()
    print('Segue tabela de todas APIs disponiveis'.center(50))
    funções_uteis.titulo()
    print('API 1: Nome_da_api\n' \
    'API 2: Nome_da_api\n' \
    'API 3: Nome_da_api\n' \
    'API 4: Nome_da_api\n' \
    'API 5: Nome_da_api\n' \
    'API 6: Nome_da_api\n' \
    'API 7: Nome_da_api\n' \
    'API 8: Nome_da_api\n' \
    'API 9: Nome_da_api\n' \
    'API 10: Nome_da_api\n' \
    'API 11: Nome_da_api\n' \
    'API 111: Nome_da_api\n' \
    'API 12: Nome_da_api\n' \
    'API 13: Nome_da_api\n' \
    'API 14: Nome_da_api\n' \
    'API 15: Nome_da_api\n' \
    'API 16: Nome_da_api\n' \
    'API 17: Nome_da_api\n' \
    'API 18: Nome_da_api\n' \
    'API 20: Nome_da_api\n' \
    'API 21: Nome_da_api\n' \
    'API 22: Nome_da_api\n')
    funções_uteis.titulo()
    select = int(input('Digite o numero da API que você quer rodar: '))
    funções_uteis.titulo()
    if select == 1:
        email = str(input('Digite o e-mail em questão: '))
        funções_suporte.api1(usuario, senha, email)
        funções_uteis.validação()
    elif select == 2: 
        email = str(input('Digite o e-mail em questão: '))
        quantidade = str(input('Digite a quantidade nova: '))
        funções_suporte.api2(usuario, senha, email, quantidade)
        funções_uteis.validação()
    elif select == 3:
        email = str(input('Digite o e-mail em questão: '))
        funções_suporte.api3(usuario, senha, email)
        funções_uteis.validação()
    elif select == 4: 
        email = str(input('Digite o email em questão: '))
        funções_suporte.api4(usuario, senha, email)
        funções_uteis.validação()
    elif select == 5: 
        email = str(input('Digite o e-mail em questão: '))
        print('Quotas disponiveis: 2GB 10GB 25GB 50GB 100GB 150GB 200GB')
        quota = int(input('Digite a quota em questão(escreva somente o valor): '))
        funções_suporte.api5(usuario, senha, email, quota)
        funções_uteis.validação()
    elif select == 6: 
        dominio = str(input('Digite o dominio em questão: '))
        funções_suporte.api6(usuario, senha, dominio)
        funções_uteis.validação()
    elif select == 7: 
        dominio = str(input('Digite o dominio em questão: '))
        tipo = str(input('Qual plesk? WINDOWS ou LINUX sempre com caixa alta: '))
        funções_suporte.api7(usuario, senha, dominio, tipo)
        funções_uteis.validação()
    elif select == 8:
        dominio = str(input('Digite o dominio em questão: '))
        host = str(input('Coloque o host do plesk em questão: '))
        funções_suporte.api8(usuario, senha, dominio, host)
        funções_uteis.validação()
    elif select == 9: 
        dominio = str(input('Digite o dominio em questão: '))
        funções_suporte.api9(usuario, senha, dominio)
        funções_uteis.validação()
    elif select == 10:
        ID_revenda = int(input('Adicione o Id da revenda: '))
        funções_suporte.api10(usuario, senha, ID_revenda)
        funções_uteis.validação()
    elif select == 11:
        print('Favor ter atenção ao utilizar essa API!')
        print('A primeiro momento utilize apenas para periodo curto!')
        email_usuario = str(input('Digite o e-mail do usuario: '))
        tem_ini = str(input('Digite o tempo de inicio: Exemplo: dia/mês/ano: '))
        tem_fin = str(input('Digite o tempo de terminio: Exemplo: dia/mês/ano: '))
        funções_suporte.api11(usuario, senha, email_usuario, tem_ini, tem_fin)
        funções_uteis.validação()
    elif select == 111: 
        print('Essa API ainda não está disponivel para uso por esse programa')
        funções_uteis.validação()
    elif select == 12:
        print('Favor ter atenção ao utilizar essa API!')
        print('A primeiro momento utilize apenas para periodo curto!')
        email_usuario = str(input('Digite o e-mail do usuario: '))
        tem_ini = str(input('Digite o tempo de inicio: Exemplo: dia/mês/ano: '))
        tem_fin = str(input('Digite o tempo de terminio: Exemplo: dia/mês/ano: '))
        funções_suporte.api12
        funções_uteis.validação()
    elif select == 13:
        print('Favor ter atenção ao utilizar essa API!')
        print('A primeiro momento utilize apenas para periodos curtos')
        email_usuario = str(input('Digite o email do usuario: '))
        email_remetente = str(input('Digite o e-mail do remetente: '))
        temp_ini = str(input('Digite a data de inicio: dia/mês/ano: '))
        temp_fin = str(input('Digite a data final: dia/mês/ano:'))
        funções_suporte.api13(usuario, senha, email_usuario, email_remetente, temp_ini, temp_fin)
        funções_uteis.validação()
    elif select == 14:
        print('Precisa de testes para saber se o relatorio será gerado corretamente! ')
        dominio = str(input('Digite o dominio em questão: '))
        funções_suporte.api14(dominio, usuario, senha)
        funções_uteis.validação()
    elif select == 15:
        print('Essa Função não foi Habilitada a primeiro momento!')
        funções_uteis.validação()
    elif select == 16:
        dominio = str(input('Digite o dominio em questão: '))
        funções_suporte.api16(usuario, senha, dominio)
        funções_uteis.validação()
    elif select == 17:
        dominio = str(input('Digite o dominio em questão: '))
        funções_suporte.api17(usuario, senha, dominio)
        funções_uteis.validação()
    elif select == 18: 
        print('Essa opção não está disponivel!')
        funções_uteis.validação()
    elif select == 19: 
        print('Essa opção não está disponivel! (caso precise favor entrar em contato solicitando uma atualização!) ')
        funções_uteis.validação()
    elif select == 20: 
        print('Essa opção não está disponivel! (caso precise favor entrar em contato solicitando uma atualização!) ')
        funções_uteis.validação()
    elif select == 21: 
        print('Essa opção não está disponivel! (caso precise favor entrar em contato solicitando uma atualização!) ')
        funções_uteis.validação()
    elif select == 22: 
        print('Essa opção não está disponivel! (caso precise favor entrar em contato solicitando uma atualização!) ')
        funções_uteis.validação()
