import random
import string
import os
import time

letrasMaiusculas = string.ascii_uppercase
letrasMinusculas = string.ascii_lowercase
numerosDecimais = string.digits
todosEspeciais = string.punctuation
maiusculas = False
minusculas = False
numeros = False
especiais = False
todosCaracteres = ""
tiposCaracteres = ['Letras maiúsculas','Letras minúsculas','Números','Caracteres especiais']
armazenarTipos = []


comprimentoSenha = input("Digite o comprimento de senha desejado: ")
comprimentoSenha = comprimentoSenha.strip()
comprimentoSenha = int(comprimentoSenha)


while len(armazenarTipos) < 4:
    
    print("\nTodos os tipos:\n")
    
    print(f"-{tiposCaracteres[0]}(1)")
    print(f"-{tiposCaracteres[1]}(2)")
    print(f"-{tiposCaracteres[2]}(3)")
    print(f"-{tiposCaracteres[3]}(4)")
        
    print("-Proxima Etapa(5)")
    
    print(f'\nTipos escolhidos: {armazenarTipos}')
    escolhaCaracteres = input("Digite o número de quais tipos de caracteres devem ser incluidos (uma por vez): ")
    escolhaCaracteres = escolhaCaracteres.strip()
    
    if escolhaCaracteres == '1':
        if 'Letras maiúsculas' in armazenarTipos:
            print('\nCaracter já incluso')
            time.sleep(4)
        else:
            armazenarTipos.append(tiposCaracteres[0])
        os.system('cls')
    elif escolhaCaracteres == '2':
        if 'Letras minúsculas' in armazenarTipos:
            print('\nCaracter já incluso')
            time.sleep(4)
        else:
            armazenarTipos.append(tiposCaracteres[1])
        os.system('cls')
    elif escolhaCaracteres == '3':
        if 'Números' in armazenarTipos:
            print('\nCaracter já incluso')
            time.sleep(4)
        else:
            armazenarTipos.append(tiposCaracteres[2])
        os.system('cls')
    elif escolhaCaracteres == '4':
        if 'Caracteres especiais' in armazenarTipos:
            print('\nCaracter já incluso')
            time.sleep(4)
        else:
            armazenarTipos.append(tiposCaracteres[3])
        os.system('cls')
    elif escolhaCaracteres == '5':
        print(f'\nTipos escolhidos: {armazenarTipos}')
        break
    else:
        print("\nSomente números inteiros de 1 a 5")
        time.sleep(4)
        os.system('cls')

os.system('cls')
print(f'\nTipos escolhidos: {armazenarTipos}\n')

for lerLista in armazenarTipos:
    
    if lerLista == (tiposCaracteres[0]):
        todosCaracteres += letrasMaiusculas
    elif lerLista == (tiposCaracteres[1]):
        todosCaracteres += letrasMinusculas
    elif lerLista == (tiposCaracteres[2]):
        todosCaracteres += numerosDecimais
    elif lerLista == (tiposCaracteres[3]):
        todosCaracteres += todosEspeciais


senhaBoa = False
verificaMaiscula = False
verificaMinuscula = False
verificaNumero = False
verificaEspecial = False

while(True):
    
    senha = "".join(random.choice(todosCaracteres) for _ in range(comprimentoSenha))
    print(senha)
    
    alterar = input("Deseja mudar a senha?\n")
    
    if alterar.lower() in ('sim','s'):
        print("")
        continue
    elif alterar.lower() in ('não','nao','n'):
        break
    else:
        break
    
    
        
    
