from tkinter import *
from tkinter import messagebox
BG = "#B0C4DE"


def calcular():
    altura = float(entry_altura.get())
    peso = int(entry_peso.get())

    imc_resultado = round(peso / altura ** 2)

    if imc_resultado < 18.5:
        messagebox.showinfo(title="Resultado", message=f"Seu IMC é {imc_resultado}, Você está abaixo do peso ideal.")
    elif imc_resultado < 25:
        messagebox.showinfo(title="Resultado", message=f"Seu IMC é {imc_resultado}, Você está no peso ideal.")
    elif imc_resultado < 30:
        messagebox.showinfo(title="Resultado", message=f"Seu IMC é {imc_resultado},"
                                                       f" Você está um pouco acima do peso ideal.")
    elif imc_resultado < 35:
        messagebox.showinfo(title="Resultado", message=f"Seu IMC é maior {imc_resultado}, Você está obeso.")
    else:
        messagebox.showinfo(title="Resultado", message=f"Seu IMC é {imc_resultado}, Você deveria ir ao médico.")
    entry_altura.delete(0, END)
    entry_peso.delete(0, END)


# ---------------------------- UI SETUP ------------------------------------ #

window = Tk()
window.title("IMC")
window.config(padx=10, pady=10, bg=BG)

# ------------- CANVAS -------------- #
canvas = Canvas(width=850, height=280, highlightthickness=10)
logo_img = PhotoImage(file="imc.png")
canvas.create_image(450, 150, image=logo_img)
canvas.grid(column=0, row=0, columnspan=2)

# ------------- LABELS -------------- #
altura_label = Label(text="ALTURA: ", bg=BG, font=("arial", 15, "bold"))
altura_label.grid(column=0, row=1)

peso_label = Label(text="PESO: ", bg=BG, font=("arial", 15, "bold"))
peso_label.grid(column=0, row=2)

# ------------- ENTRIES ------------- #

entry_altura = Entry(width=20, font=('calibre', 14, 'normal'))
entry_altura.focus()
entry_altura.grid(column=1, row=1, padx=4, pady=4)

entry_peso = Entry(width=20, font=('calibre', 14, 'normal'))
entry_peso.grid(column=1, row=2, columnspan=2, padx=4, pady=4)

# ------------- BUTTONS ------------- #

button_calc = Button(text="CALCULAR!", command=calcular, width=20, relief=GROOVE)
button_calc.grid(column=1, row=4, columnspan=2, padx=4, pady=4)

window.mainloop()
