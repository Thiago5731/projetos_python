#hosts_win.py

import subprocess
sair = 0
while sair == 0:
    print('-' * 32)
    print('Bem vindo(a) ao programa de DNS!')
    print('-' * 32)
    dominio = input('Digite o domínio em questão: ').strip().lower()

    print('-' * 32)
    print(f'O domínio selecionado foi: {dominio}')
    print('-' * 32)

    # Consulta geral
    print('+' * 64)
    tipo = "A"
    result = subprocess.run(["nslookup", "-type=" + tipo, dominio, "8.8.8.8"], capture_output=True, text=True)
    print("\nConsulta geral:")
    print(result.stdout if result.returncode == 0 else f"Erro ao consultar {tipo} do domínio {dominio}")
    print('+' * 64)

    # Consulta tipo NS
    print('+' * 64)
    tipo = "NS"
    result = subprocess.run(["nslookup", "-type=" + tipo, dominio, "8.8.8.8"], capture_output=True, text=True)
    print("\nTipo NS:")
    print(result.stdout if result.returncode == 0 else f"Erro ao consultar {tipo} do domínio {dominio}")
    print('+' * 64)

    # Consulta tipo MX
    print('+' * 64)
    tipo = "MX"
    result = subprocess.run(["nslookup", "-type=" + tipo, dominio, "8.8.8.8"], capture_output=True, text=True)
    print("\nTipo MX:")
    print(result.stdout if result.returncode == 0 else f"Erro ao consultar {tipo} do domínio {dominio}")
    print('+' * 64)

    # Consulta tipo TXT
    print('+' * 64)
    tipo = "TXT"
    result = subprocess.run(["nslookup", "-type=" + tipo, dominio, "8.8.8.8"], capture_output=True, text=True)
    print("\nTipo TXT:")
    print(result.stdout if result.returncode == 0 else f"Erro ao consultar {tipo} do domínio {dominio}")
    print('+' * 64)

    exit = str(input('Você deseja sair? [S/N]')).strip().upper()
    if exit == 'S':
        sair += 1
