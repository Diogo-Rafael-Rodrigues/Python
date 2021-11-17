import datetime
from tkinter import *
from tkinter import messagebox

PINK = "#e2979c"
RED = "#e7305b"
BLUE = "#ADD8E6"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"



# #Função que imprime e analisa se foi ano bisexto.
def text_fim():


    ano = int(entry_ano.get())
    mes = int(entry_mes.get())
    dia = int(entry_dia.get())
    data_1 = datetime.datetime(ano, mes, dia)
    data_2 = datetime.datetime.now()

    diff = data_2 - data_1

    dias = diff.days
    anos, dias = dias // 365, dias % 365
    meses, dias = dias // 30, dias % 30

    d = str(data_1.strftime("%d-%m-%Y")).split(" ")
    # condicionais
    if anos >= 65:
        messagebox.showinfo(title="-IDOSO-",
                            message=f"Que lenda! Você é um idoso.\nDesde {d[0]} se passaram {anos} anos, {meses} meses,"
                                    f" {dias} dias, um total de {diff.days} dias corridos\n")
    elif anos >= 25 and anos <= 65:

        messagebox.showinfo(title="-ADULTO-",
                            message=f"Vamos a luta você é um adulto afinal!\nDesde {d[0]} se passaram {anos} anos, "
                                    f"{meses} meses, {dias} dias, um total de {diff.days} dias corridos\n")
    elif anos >= 18 and anos <= 25:

        messagebox.showinfo(title="-JOVEM-",
                            message=f"Aproveite! você ainda é um jovem!\nDesde {d[0]} se passaram {anos} anos,"
                                    f" {meses} meses, {dias} dias, um total de {diff.days} dias corridos\n")
    elif anos >= 12 and anos <= 18:

        messagebox.showinfo(title="-ADOLESCENTE-",
                            message=f"Que bagunça! você é mesmo um adolescente!\nDesde {d[0]} se passaram {anos} anos, "
                                    f"{meses} meses, {dias} dias, um total de {diff.days} dias corridos\n")
    elif anos <= 12 and anos >= 0:

        messagebox.showinfo(title="-CRIANÇA-",
                            message=f"Bola, boneca, video-game e sorvete! sei que você adora,"
                                    f" porque você é uma criança!\nDesde {d[0]} se passaram {anos} anos,"
                                    f" {meses} meses, {dias} dias, um total de {diff.days} dias corridos\n")
    #no caso de ser negativo, não chama a função text_fim() para não escrever a data pro usuario.
    elif 0 > anos:
        messagebox.showinfo(title="-ERRO-",
                            message=f"Calma ai, essa pessoa nem nasceu ainda!!")

# ---------------------------- UI SETUP ------------------------------------ #
window = Tk()
window.title("Decubra sua idade")
window.config(padx=10, pady=10, bg=BLUE)

# ------------- CANVAS -------------- #
canvas = Canvas(width=650, height=300, highlightthickness=0)
logo_img = PhotoImage(file="ed.png")
canvas.create_image(325, 150, image=logo_img)
canvas.grid(column=0, row=0, columnspan=3)

# ------------- LABELS -------------- #
title_label = Label()
title_label.config(text="DIAS VIVIDOS", fg=RED, bg=BLUE, font=("arial", 35, "bold"))
title_label.grid(column=0, row=1, columnspan=4, padx=10, pady=10)

ano_label = Label(text="Digite o ano: ", bg=BLUE, font=("arial", 15, "bold"))
ano_label.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

mes_label = Label(text="Digite o mês: ", bg=BLUE, font=("arial", 15, "bold"))
mes_label.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

dia_label = Label(text="Digite o dia: ", bg=BLUE, font=("arial", 15, "bold"))
dia_label.grid(column=0, row=4, columnspan=2, padx=10, pady=10)


# ------------- ENTRIES ------------- #

entry_ano = Entry(width=16, font=('calibre', 14, 'normal'))
entry_ano.focus()
entry_ano.grid(column=1, row=2, columnspan=3, padx=3, pady=3)

entry_mes = Entry(width=16, font=('calibre', 14, 'normal'))
entry_mes.grid(column=1, row=3, columnspan=3, padx=3, pady=3)

entry_dia = Entry(width=16, font=('calibre', 14, 'normal'))
entry_dia.grid(column=1, row=4, columnspan=3, padx=3, pady=3)


# ------------- BUTTONS ------------- #

button_calc = Button(text="CALCULAR!",command=text_fim,  width=10, highlightthickness=10)#
button_calc.grid(column=1, row=5, columnspan=4, padx=10, pady=10)

window.mainloop()
