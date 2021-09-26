print('''
 .-----------------..----------------. .----------------. .----------------. .----------------.   
| .--------------. | .--------------. | .--------------. | .--------------. | .--------------. |  
| | ____  _____  | | |     ____     | | |  _________   | | |      __      | | |    _______   | |  
| ||_   \|_   _| | | |   .'    `.   | | | |  _   _  |  | | |     /  \     | | |   /  ___  |  | |  
| |  |   \ | |   | | |  /  .--.  \  | | | |_/ | | \_|  | | |    / /\ \    | | |  |  (__ \_|  | |  
| |  | |\ \| |   | | |  | |    | |  | | |     | |      | | |   / ____ \   | | |   '.___`-.   | |  
| | _| |_\   |_  | | |  \  `--'  /  | | |    _| |_     | | | _/ /    \ \_ | | |  |`\____) |  | |  
| ||_____|\____| | | |   `.____.'   | | |   |_____|    | | ||____|  |____|| | |  |_______.'  | |  
| |              | | |              | | |              | | |              | | |              | |  
| '--------------' | '--------------' | '--------------' | '--------------' | '--------------' |  
 '----------------' '----------------' '----------------' '----------------' '----------------'   
''')
print("Insturções: digite as notas sem ponto ou virgula EX: 9.7 -> 97 ")

quer_continuar = True

while quer_continuar:
    nome_aluno = input("\nDigite o no nome do aluno: ")
    aluno = {

        "Matemática": int(input("Digite a nota de Matematica: ")),
        "Português": int(input("Digite a nota de Portugues: ")),
        "Física": int(input("Digite a nota de Física: ")),
        "Inglês": int(input("Digite a nota de Inglês: ")),
     }
    aluno_1 = []
    for i in aluno:
        aluno_1.append(aluno[i])

    media_aluno = sum(aluno_1) / len(aluno)
    media_aluno_ponderada = (aluno_1[0] * 0.4) + (aluno_1[1] * 0.1) + (aluno_1[2] * 0.3) + (aluno_1[3] * 0.2)

    print(f"\nNome do(a) aluno(a): {nome_aluno}\n"
          f"Média aritimética: {media_aluno.__round__()}\n"
          f"Média ponderada {media_aluno_ponderada.__round__()}\n")
    opicao = input("Quer fazer outra operação? sim / não  -  ").lower()
    if opicao == "sim":
        quer_continuar = True
    else:
        quer_continuar = False