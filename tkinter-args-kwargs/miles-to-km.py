from tkinter import *

def miles_to_km():
   miles = float(miles_imput.get())
   km = round(miles * 1.609)
   result_label.config(text=f"{km}")

window = Tk()
window.title("Mile to KM Converter")
window.config(padx=20, pady=20)
miles_imput = Entry(width= 7)
miles_imput.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is qual to")
is_equal_label.grid(column=0, row=1)

result_label = Label(text=f"0")
result_label.grid(column=1, row=1)

km_label = Label(text=f"KM")
km_label.grid(column=2, row=1)

button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)



window.mainloop()