import datetime

nome = []
idade = []
data = []
email = []
cpf = []
velho = []
vezes = 0
a = 0
b = 0

while True:

    nomeCompleto = input("Nome completo: ")
    novoEmail = input("Email: ")
    novoCPF = input("CPF: ")

    dia, mes, ano = input("Data de Nascimento (DD/MM/AAAA): ").split('/')
    dataNasc = datetime.date(int(ano), int(mes), int(dia))
    hoje = datetime.date.today()
    idadeCont = hoje.year - dataNasc.year - \
        ((hoje.month, hoje.day) < (dataNasc.month, dataNasc.day))

    nome.append(nomeCompleto[:40])
    data.append(dataNasc)
    idade.append(idadeCont)
    email.append(novoEmail[:40])
    cpf.append(novoCPF[:11])
    vezes += 1

    parar = input("Deseja adicionar mais algum paciente? ")
    parar = parar.lower()
    if parar in ('sim, s, ss'):
        continue
    else:
        break

for i in range(vezes):
    if idade[i] > 65:
        a = a + 1
        with open("./PYTHON2/Exerc6/PastaExtra/PacienteGrupoRisco.txt", "a") as normal:
            normal.write(
                f'Paciente {a}: \n Nome: {nome[i]} \n Email: {email[i]} \n \
                    CPF: {cpf[i]} \n Data de Nascimento: {data[i]} \n')
    else:
        b = b + 1
        with open("./PYTHON2/Exerc6/PastaExtra/PacienteNormal.txt", "a") as diff:
            diff.write(
                f'Paciente {b}: \n Nome: {nome[i]} \n Email: {email[i]} \n \
                    CPF: {cpf[i]} \n Data de Nascimento: {data[i]} \n')

if __name__ == '__main__':
    print('Esse código é uma simulação de banco de dados')
