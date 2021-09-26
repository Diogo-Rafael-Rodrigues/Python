print('''
 ▄▄▄▄▄▄▄▄▄▄▄ ▄▄       ▄▄ ▄▄▄▄▄▄▄▄▄▄▄
▐░░░░░░░░░░░▐░░▌     ▐░░▐░░░░░░░░░░░▌
 ▀▀▀▀█░█▀▀▀▀▐░▌░▌   ▐░▐░▐░█▀▀▀▀▀▀▀▀▀
     ▐░▌    ▐░▌▐░▌ ▐░▌▐░▐░▌
     ▐░▌    ▐░▌ ▐░▐░▌ ▐░▐░▌
     ▐░▌    ▐░▌  ▐░▌  ▐░▐░▌
     ▐░▌    ▐░▌   ▀   ▐░▐░▌
     ▐░▌    ▐░▌       ▐░▐░▌
 ▄▄▄▄█░█▄▄▄▄▐░▌       ▐░▐░█▄▄▄▄▄▄▄▄▄
▐░░░░░░░░░░░▐░▌       ▐░▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀▀ ▀         ▀ ▀▀▀▀▀▀▀▀▀▀▀

''')
print("Instruções: use ponto em vez de virgula na sua altura. Ex 1.70 ")


altura = float(input("Qual sua altura? "))
peso = float(input("Qual seu peso em kg: "))

imc_resultado = round(peso / altura ** 2)

if imc_resultado < 18.5:
    print(f"Seu IMC é {imc_resultado}, Você está abaixo do peso ideal.")
elif imc_resultado < 25:
    print(f"Seu IMC é {imc_resultado}, Você está no peso ideal.")
elif imc_resultado < 30:
    print(f"Seu IMC é {imc_resultado}, Você está um pouco acima do peso ideal.")
elif imc_resultado < 35:
    print(f"Seu IMC é maior {imc_resultado}, Você está obeso.")
else:
    print(f"Seu IMC é {imc_resultado}, Você deveria ir ao médico.")

input("Clique pra fechar ")