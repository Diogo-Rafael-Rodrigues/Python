print('''
 $$$$$$\          $$\                        $$$$$$$$\$$\          $$\                               $$\                   
$$  __$$\         \__|                       $$  _____$$ |         $$ |                              \__|                  
$$ /  \__|$$$$$$\ $$\$$\   $$\$$$$$$\        $$ |     $$ |$$$$$$\$$$$$$\   $$$$$$\  $$$$$$\ $$$$$$$\ $$\ $$$$$$$\ $$$$$$\  
$$ |      \____$$\$$ \$$\ $$  \____$$\       $$$$$\   $$ $$  __$$\_$$  _| $$  __$$\$$  __$$\$$  __$$\$$ $$  _____$$  __$$\ 
$$ |      $$$$$$$ $$ |\$$$$  /$$$$$$$ |      $$  __|  $$ $$$$$$$$ |$$ |   $$ |  \__$$ /  $$ $$ |  $$ $$ $$ /     $$ /  $$ |
$$ |  $$\$$  __$$ $$ |$$  $$<$$  __$$ |      $$ |     $$ $$   ____|$$ |$$\$$ |     $$ |  $$ $$ |  $$ $$ $$ |     $$ |  $$ |
\$$$$$$  \$$$$$$$ $$ $$  /\$$\$$$$$$$ |      $$$$$$$$\$$ \$$$$$$$\ \$$$$  $$ |     \$$$$$$  $$ |  $$ $$ \$$$$$$$\\$$$$$$  |
 \______/ \_______\__\__/  \__\_______|      \________\__|\_______| \____/\__|      \______/\__|  \__\__|\_______|\______/ 
                                                                                                                           
                                                                                                                           
                                                                                                                           
''')
quer_continuar = True

while quer_continuar:
    valor = int(input("Digite o valor a ser sacado: "))
    notas = [100, 50, 20, 10, 5, 1]
    notas.sort()
    notas.reverse()
    numero_de_notas = []
    total = []
    for i in notas:
        numero_de_notas.append(valor / i)
        valor %= i


    for i in range(len(notas)):
        print ("Notas de %d : %d" % (notas[i], numero_de_notas[i]))
        if numero_de_notas[i] >= 1.0:
            total.append(numero_de_notas[i].__floor__())
            total_somado = sum(total)

    print(f'O total de {total_somado} notas foram sacadas')
    opicao = input("\nQuer fazer outra operação? sim / não  -  ").lower()
    if opicao == "sim":
        quer_continuar = True
    else:
        quer_continuar = False