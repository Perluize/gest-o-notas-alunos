
#Tela de boas vindas
print("Bem vindos ao gestão de notas do aluno\n>------------------------------------------<")

#Inserir o nome do aluno
name_aluno = input("insira o nome do aluno ==>")

#Inserir nota de Geografia
nota_geo = float(input("Insira aqui a nota de Geografia ==>"))
while nota_geo not in range(11):
    print("Número invalido")
    nota_geo = float(input("Insira aqui a nota de Geografia ==>"))

#Inserir nota de Historia
nota_his = float(input("Insira aqui a nota de Historia ==>"))
while nota_his not in range(11):
    print("Número invalido")
    nota_his = float(input("Insira aqui a nota de Historia ==>"))

#Inserir nota de Matematica
nota_mat = float(input("Insira aqui a nota de Matematica ==>"))
while nota_mat not in range(11):
    print("Número invalido")
    nota_mat = float(input("Insira aqui a nota de Matematica ==>"))

#Inserir nota de Português
nota_port = float(input("Insira aqui a nota de Português ==>"))
while nota_port not in range(11):
    print("Número invalido")    

#Calcular a media de notas
media = (nota_geo + nota_port + nota_his + nota_mat) / 4

#Determinar a situação do aluno(aprovado ou reprovado)
def status_aprov(media):
    return "Aprovado" if media >= 7 else "Reprovado"

#Exibir um relatorio final
print("\n Segue abaixo o relatorio geral do aluno\n------------------------------------")
print("Nome:",name_aluno)
print("\nNotas:\n","Geografia:", nota_geo,"\n","Historia:", nota_his,"\n","Matematica:", nota_mat,"\n","Português:",nota_port)
print("Media:", media)
print("Status de aprovação:" ,status_aprov(media))
