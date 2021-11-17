from tkinter import *
import pandas as pd

AQUA = "#ee6611"
GREEN = "#228B22"
RED = "#e7305b"
FONT_NAME = "Courier"

valor = []


def show():
    n = "".join([str(_) for _ in valor])
    canvas.itemconfig(numero_de_notas_tela, text=f"{n}")


def calcular():
    n = "".join([str(_) for _ in valor])
    n_int = int(n)
    if n_int <= 950:
        canvas.itemconfig(numero_de_notas_tela, text=f"")
        df = pd.DataFrame()


        notas = [100, 50, 20, 10, 5, 2, 1]  # arrumei a nota de 2, que havia esquecido :D
        notas.sort()
        notas.reverse()
        numero_de_notas = []
        total = []
        for i in notas:
            numero_de_notas.append(n_int / i)
            n_int %= i

        for i in range(len(notas)):
            df = df.round(decimals=0).astype(int)
            df = df.append({'Notas': notas[i], "Quantidade": numero_de_notas[i].__floor__()}, ignore_index=True)


            if numero_de_notas[i] >= 1:
                total.append(numero_de_notas[i].__floor__())
                total_somado = sum(total)

        canvas.itemconfig(numero_de_notas_tela, text=f"{df}\n Total de notas: {total_somado}", font=(FONT_NAME, 20, "bold"))
    else:
        canvas.itemconfig(numero_de_notas_tela, text=" Quantia acima\n do permitido!",
                          font=(FONT_NAME, 35, "bold"))
# ---------------------------- UI SETUP ------------------------------------ #
window = Tk()
window.title("CAIXA ELETRONICO")
window.config(padx=10, pady=10, bg=AQUA)

canvas = Canvas(width=500, height=500, highlightthickness=0)
logo_img = PhotoImage(file="cedulas.png")
canvas.create_image(255, 250, image=logo_img)
canvas.grid(column=0, row=0, columnspan=3)
numero_de_notas_tela = canvas.create_text(250, 180, text=f"", fill="white", font=(FONT_NAME, 50, "bold"))

button_ok = Button(text="OK",command=calcular, width=10, fg=GREEN, font=('calibre', 14, 'bold'))
button_ok.grid(column=2, row=4, padx=10, pady=10)


def limpar():
    canvas.itemconfig(numero_de_notas_tela, text="Novo Valor?", font=(FONT_NAME, 40, "bold"))
    valor.clear()
    return valor


button_limpar = Button(text="LIMPAR", command=limpar, width=10, fg=RED, font=('calibre', 14, 'bold'))
button_limpar.grid(column=0, row=4, padx=10, pady=10)


def button_0():
    valor.append(0)
    show()
    return valor


button_0 = Button(text="0", command=button_0, width=15, font=('calibre', 14, 'bold'))
button_0.grid(column=0, row=4, columnspan=3, padx=10, pady=10)


def button_1():
    valor.append(1)
    show()
    return valor


button_1 = Button(text="1", command=button_1, width=10, font=('calibre', 14, 'bold'))
button_1.grid(column=0, row=3, padx=10, pady=10)


def button_2():
    valor.append(2)
    show()
    return valor


button_2 = Button(text="2", command=button_2, width=10, font=('calibre', 14, 'bold'))
button_2.grid(column=1, row=3, padx=10, pady=10)


def button_3():
    valor.append(3)
    show()
    return valor


button_3 = Button(text="3", command=button_3, width=10, font=('calibre', 14, 'bold'))
button_3.grid(column=2, row=3, padx=10, pady=10)


def button_4():
    valor.append(4)
    show()
    return valor


button_4 = Button(text="4", command=button_4, width=10, font=('calibre', 14, 'bold'))
button_4.grid(column=0, row=2, padx=10, pady=10)


def button_5():
    valor.append(5)
    show()
    return valor


button_5 = Button(text="5", command=button_5, width=10, font=('calibre', 14, 'bold'))
button_5.grid(column=1, row=2, padx=10, pady=10)


def button_6():
    valor.append(6)
    show()
    return valor


button_6 = Button(text="6", command=button_6, width=10, font=('calibre', 14, 'bold'))
button_6.grid(column=2, row=2, padx=10, pady=10)


def button_7():
    valor.append(7)
    show()
    return valor


button_7 = Button(text="7", command=button_7, width=10, font=('calibre', 14, 'bold'))
button_7.grid(column=0, row=1, padx=10, pady=10)


def button_8():
    valor.append(8)
    show()
    return valor


button_8 = Button(text="8",command=button_8, width=10, font=('calibre', 14, 'bold'))
button_8.grid(column=1, row=1, padx=10, pady=10)


def button_9():
    valor.append(9)
    show()
    return valor


button_9 = Button(text="9",command=button_9, width=10, font=('calibre', 14, 'bold'))
button_9.grid(column=2, row=1, padx=10, pady=10)

window.mainloop()

