import datetime

print('''
██████╗ ██╗ █████╗ ███████╗    ██╗   ██╗██╗██╗   ██╗██╗██████╗  ██████╗ ███████╗
██╔══██╗██║██╔══██╗██╔════╝    ██║   ██║██║██║   ██║██║██╔══██╗██╔═══██╗██╔════╝
██║  ██║██║███████║███████╗    ██║   ██║██║██║   ██║██║██║  ██║██║   ██║███████╗
██║  ██║██║██╔══██║╚════██║    ╚██╗ ██╔╝██║╚██╗ ██╔╝██║██║  ██║██║   ██║╚════██║
██████╔╝██║██║  ██║███████║     ╚████╔╝ ██║ ╚████╔╝ ██║██████╔╝╚██████╔╝███████║
╚═════╝ ╚═╝╚═╝  ╚═╝╚══════╝      ╚═══╝  ╚═╝  ╚═══╝  ╚═╝╚═════╝  ╚═════╝ ╚══════╝
                                                                                
''')
quer_continuar = True

while quer_continuar:
    ano = int(input("Qual o ano que você nasceu? : "))
    mes = int(input("Qual o mês que você nasceu? : "))
    dia = int(input("Qual o dia que você nasceu? : "))
    data_1 = datetime.datetime(ano, mes, dia)
    data_2 = datetime.datetime.now()

    diff = data_2 - data_1

    dias = diff.days
    anos, dias = dias // 365, dias % 365
    meses, dias = dias // 30, dias % 30

    d = str(data_1.strftime("%d-%m-%Y")).split(" ")

    print(f"Desde {d[0]} se passaram {anos} anos, {meses} meses, {dias} dias, um total de {diff.days} dias corridos\n")

    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f"Você sabia? {ano} Foi um ano Bisexto!!!\n")
    else:
        print(f"{ano} Não foi um ano Bisexto\n")
    opicao = input("\nQuer fazer outra operação? sim / não  -  ").lower()
    if opicao == "sim":
        quer_continuar = True
    else:
        quer_continuar = False