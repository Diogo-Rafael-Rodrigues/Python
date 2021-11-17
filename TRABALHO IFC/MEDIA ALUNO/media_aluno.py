from tkinter import *
from tkinter import messagebox


# ---------------- Constantes ------------------------------#

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"



def calcular():

    # Dicionário para aquisições de dados
    aluno = {

        "Matemática": entry_matematica.get(),
        "Português": entry_portugues.get(),
        "Física": entry_fisica.get(),
        "Inglês": entry_ingles.get(),
    }
    media_ponderada = {

        "Matemática": entry_peso_matematica.get(),
        "Português": entry_peso_portugues.get(),
        "Física": entry_peso_fisica.get(),
        "Inglês": entry_peso_ingles.get(),
    }
    # conversão dos dados do dicionario em listas
    aluno_1 = []
    media_ponderada_1 = []
    for i in aluno:

        aluno_1.append(int(aluno[i]))
        media_ponderada_1.append(int(media_ponderada[i]) / 10)

    # feito a conta de media e de aplicação de peso sobre as notas.
    media_aluno = sum(aluno_1) / len(aluno)
    media_aluno_ponderada = (aluno_1[0] * media_ponderada_1[0]) \
                            + (aluno_1[1] * media_ponderada_1[1]) \
                            + (aluno_1[2] * media_ponderada_1[2]) \
                            + (aluno_1[3] * media_ponderada_1[3])



    # mostra para o usuario o resultado processado

    nome_aluno = str(entry_aluno.get())
    dado = f"\nNome do(a) aluno(a): {nome_aluno} \nMédia aritimética: {media_aluno.__round__()}\nMédia ponderada: {media_aluno_ponderada.__round__()}\n"

    # condicionaiS e condicionais aninhadas:

    if media_aluno >= 70 or media_aluno_ponderada >= 70:
        if media_aluno >= 70 and media_aluno_ponderada >= 70:

            messagebox.showinfo(title="PARABÉNS",
                                message=f"{dado}Passou de ano por média aritimética e ponderada")
        if media_aluno >= 70 and media_aluno_ponderada <= 70:
            messagebox.showinfo(title="PARABÉNS",
                                message=f"{dado}Passou de ano por média aritimética")
        if media_aluno <= 70 and media_aluno_ponderada >= 70:
            messagebox.showinfo(title="PARABÉNS",
                                message=f"{dado}Passou de ano por média ponderada")
    elif media_aluno <= 70 and media_aluno >= 40 or media_aluno_ponderada <= 70 and media_aluno_ponderada >= 40:

        messagebox.showinfo(title="NÃO FOI DESSA VEZ",
                            message=f"{dado}Não desanime, ainda tem recuperação!")
    elif media_aluno <= 40 and media_aluno >= 00 or media_aluno_ponderada <= 40 and media_aluno_ponderada >= 00:

        messagebox.showinfo(title="NÃO FOI DESSA VEZ",
                            message=f"{dado}Você deveria ouvir seus pais e estudado mais! Você foi reprovado.")
    else:
        messagebox.showinfo(title="X",
                            message=f"{dado}Ops, Algo deu errado!")

    entry_aluno.delete(0, END)
    entry_matematica.delete(0, END)
    entry_portugues.delete(0, END)
    entry_fisica.delete(0, END)
    entry_ingles.delete(0, END)
    entry_peso_matematica.delete(0, END)
    entry_peso_portugues.delete(0, END)
    entry_peso_fisica.delete(0, END)
    entry_peso_ingles.delete(0, END)


# ---------------------------- UI SETUP ------------------------------------ #
window = Tk()
window.title("Notas dos Alunos")
window.config(padx=10, pady=10, bg=GREEN)

# ------------- CANVAS -------------- #
canvas = Canvas(width=200, height=320, highlightthickness=0)
logo_img = PhotoImage(file="notas.png")
canvas.create_image(100, 160, image=logo_img)
canvas.grid(column=0, row=0, columnspan=4)

# ------------- LABELS -------------- #
title_label = Label()
title_label.config(text="NOTAS", fg=RED, bg=GREEN, font=(FONT_NAME, 35, "bold"))
title_label.grid(column=0, row=1, columnspan=4, padx=10, pady=10)

matematica_label = Label(text="Aluno: ", bg=GREEN)
matematica_label.grid(column=0, row=2)

matematica_label = Label(text="Matemática: ", bg=GREEN)
matematica_label.grid(column=0, row=3)

portugues_label = Label(text="Português: ", bg=GREEN)
portugues_label.grid(column=0, row=4)

fisica_label = Label(text="Física: ", bg=GREEN)
fisica_label.grid(column=0, row=5)

ingles_label = Label(text="Inglês: ", bg=GREEN)
ingles_label.grid(column=0, row=6)

peso_1_label = Label(text="Peso: ", bg=GREEN)
peso_1_label.grid(column=2, row=3)

peso_2_label = Label(text="Peso: ", bg=GREEN)
peso_2_label.grid(column=2, row=4)

peso_3_label = Label(text="Peso: ", bg=GREEN)
peso_3_label.grid(column=2, row=5)

peso_4_label = Label(text="Peso: ", bg=GREEN)
peso_4_label.grid(column=2, row=6)
# ------------- ENTRIES ------------- #

entry_aluno = Entry(width=16, font=('calibre', 14, 'normal'))
entry_aluno.focus()
entry_aluno.grid(column=1, row=2,columnspan=3, padx=3, pady=3)

entry_matematica = Entry(width=6, font=('calibre', 14, 'normal'))
entry_matematica.grid(column=1, row=3, padx=3, pady=3)

entry_portugues = Entry(width=6, font=('calibre', 14, 'normal'))
entry_portugues.grid(column=1, row=4, padx=3, pady=3)

entry_fisica = Entry(width=6, font=('calibre', 14, 'normal'))
entry_fisica.grid(column=1, row=5, padx=3, pady=3)

entry_ingles = Entry(width=6, font=('calibre', 14, 'normal'))
entry_ingles.grid(column=1, row=6, padx=3, pady=3)

entry_peso_matematica = Entry(width=5, font=('calibre', 14, 'normal'))
entry_peso_matematica.grid(column=3, row=3, padx=3, pady=3)

entry_peso_portugues = Entry(width=5, font=('calibre', 14, 'normal'))
entry_peso_portugues.grid(column=3, row=4, padx=3, pady=3)

entry_peso_fisica = Entry(width=5, font=('calibre', 14, 'normal'))
entry_peso_fisica.grid(column=3, row=5, padx=3, pady=3)

entry_peso_ingles = Entry(width=5, font=('calibre', 14, 'normal'))
entry_peso_ingles.grid(column=3, row=6, padx=3, pady=3)

# ------------- BUTTONS ------------- #

button_calc = Button(text="CALCULAR!", command=calcular, width=10,highlightthickness=10, relief=GROOVE)#
button_calc.grid(column=1, row=7, columnspan=4, padx=10, pady=10)

window.mainloop()
