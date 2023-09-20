from os import system
from random import randint 

def numeroAleatorio():
    return randint(1,100)

def verificaChute(chute,numeroRandom):
    
    if chute > numeroRandom:
        system('cls')
        print("\nChute maior que o número aleatório")
        return True
    elif chute < numeroRandom:
        system('cls')
        print("\nChute menor que o número aleatório")
        return True
    else:
        system('cls')
        print("\nPARABÉNS!!! Você acertou o número aleatório")
        return False
    
def interfaceJogo():
    
    numeroRandom = numeroAleatorio()
    print("Jogo da adivinhação!\n\n-Adivinhe um número entre 1 e 100\n-Você tem 5 vidas\n\n")
    
    while True:

        chute = int(input("Digite o seu chute: "))
        sair = verificaChute(chute,numeroRandom) 
        if sair is False:
            system('cls')
            jogarNovamente = input("Deseja jogar novamente? (S/n)\n")
            
            if jogarNovamente.lower() in ('s','sim'):
                numeroRandom = numeroAleatorio()
                continue
            else:
                break

interfaceJogo()
        
        

    
    