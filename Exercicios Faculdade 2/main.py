import math
import datetime
#-----------------------------------------------------------------------------------------------------#
# 1:A partir de um valor de temperatura em graus Farenheit informado pelo usuário, faça a
# conversão para a respectiva temperatura em graus Celsius.


temp_f = float(input("Digite o a temperatura em Farenheit "))

temp_c = (temp_f - 32)/1.800
print("A temperatura em Celsius é : {:.2f}".format(temp_c))

# ----------------------------------------------------------------------------------------------------#

# 2. Faça a conversão de uma determinada quantidade de polegadas para centímetros.

polegadas = float(input("Digite a quantidade de polegadas: "))
centimetros = polegadas * 2.54
print("A converção de polegadas em centímentros é : {:.2f}".format(centimetros))

#----------------------------------------------------------------------------------------------------#

# 3. Dada uma determinada quantidade em km/h (quilômetros por hora), faça a conversão para mph (milhas por hora)

kilomentros = float(input("Digite a quantidade de Km/h voce quer converter para milhas por hora: "))
milhas = kilomentros * 1.60934
print("A converção de kilmetros em milhas é : {:.2f}".format(milhas))

#---------------------------------------------------------------------------------------------------#
# 4. Crie um programa que, se lhe for informado um valor de horas, minutos e segundos, ele
# exibirá a quantidade de segundos totais que os valores informados representam.
horas = 0
minutos = 0
segundos = 0
opcao = input("escolha a conversão que você deseja: \nPara converter horas para segundos digite -> 1\n"
              "Para converter segundos em  em horas digite -> 2 ")
if opcao == "1":
    horas = int(input("Digite uma quantidade de horas : "))
    minutos = int(input("Digite uma quantidade de minutos : "))
    segundos = int(input("Digite uma quantidade de segundos : "))
    total_segundos = (horas * 3600) + (minutos * 60) + segundos
    print(F"O total digitado equivale a : {total_segundos} segundos")

#5. Faça o caminho inverso da questão 4, ou seja, a partir de uma certa quantidade de segundos,
#você deve calcular quantas horas, minutos e segundos o valor informado representa.
elif opcao == "2":
    segundos = int(input("Digite uma quantidade de segundos : "))
    total = str(datetime.timedelta(seconds=segundos))

    print(F"O total digitado equivale a : {total} ")
else:
    print("Opção inválida.")
#--------------------------------------------------------------------------------------------------#

# 6. Fórmula de Bhaskara.

a = float(input("Entre com o valor de A: "))
b = float(input("Entre com o valor de B: "))
c = float(input("Entre com o valor de C: "))

delta = (b ** 2) - 4 * a * c

if a == 0:
    print("O valor de a, tem que ser diferente de 0")
elif delta < 0:
    print("A equação de 2º grau não possui raízes reais!")
else:
    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    x2 = (-b - delta ** (1 / 2)) / (2 * a)
    print("S = {:.2f},{:.2f}".format(x1, x2))

#------------------------------------------------------------------------------------------------#
#
# 7. Monte um programa que quando executado seja possível, após obter o valor de raio (em
# centímetros) da base do canecão e a altura do canecão, exibir qual a capacidade máxima de
# água possível de ser fervida para sua bebida. Sua resposta estará em ml (mililitros).


PI = 3.14

base = float(input("Digite o valor da base da caneca : ")) / 2
altura = float(input("Digite a altura da caneca: "))

area_base = PI * (base * base)
volume_de_agua = area_base * altura
print("O volume de em militros é de : {:.1f}".format(volume_de_agua))

# ----------------------------------------------------------------------------------------------#
#8. Um atleta treina em uma pista de corrida circular de 400 metros. Ao final do treino, com
# base na quantidade de voltas dadas e no tempo total do treino (em segundos), ele quer saber:
# • O percurso total do treino (em quilômetros);
# • O tempo médio por quilômetro (em segundos).
PISTA = 400
voltas = int(input("Digite o total de voltas dadas na pista: "))
tempo = int(input("Digite o seu tempo final: "))

total_km = PISTA * voltas
tempo_medio_km = tempo / (total_km /1000)
total = str(datetime.timedelta(seconds=tempo_medio_km))
print(f"Correu um total de {total_km / 1000}KM em um tempo medio de {total} por km")

#-----------------------------------------------------------------------------------------------#
# 9. Leia o código-fonte e explique o que ele faz ou pretende fazer.
# 10. Nele, de propósito, introduzi 2 erros. Aponte que erros são esses e arrume-os.

var1 = chr(99)
var2 = chr(102)
var3 = chr(65)
var4 = chr(69)
print("O professor disse que programadores necessitam treinar codigos.")
print("Mas o que os programadores necessitam de verdade é", var1, var3, var2, var4)
print("Concorda?")

print("Deixando isso de lado, digite 4 letras:")
var1 = input()
var2 = input()
var3 = input()
var4 = input()
numvar1 = ord(var1)
numvar2 = ord(var2)
numvar3 = ord(var3)
numvar4 = ord(var4)
print("sequencia original: ", var1, var2, var3, var4)
print("Sequencia invertida: ", var4, var3, var2, var1)
media = ((numvar1 + numvar2 + numvar3 + numvar4) / 4.0)
print("Media:", media)
print("Sequencia criptografada:", chr(numvar1+13),
chr(numvar2+13), chr(numvar3+13), chr(numvar4+13))