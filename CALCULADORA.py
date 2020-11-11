from tkinter import ttk
from tkinter import *
import tkinter as tk


def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb


def calculadora(num1, num2, operador):
    if operador == "+":
        resultado = num1 + num2
    elif operador == "-":
        resultado = num1 - num2
    elif operador == "*":
        resultado = num1 * num2
    elif operador == "/":
        resultado = round(num1 / num2, 2)
    else:
        resultado = num1 ** num2

    return resultado


def click_calcular(historial, label, num1, num2, operador):

    valor1 = float(num1)
    valor2 = float(num2)

    res = calculadora(valor1, valor2, operador)

    historial.insert(END, res)

    label.configure(text="Resultado: "+str(res))


def init_window():

    window = tk.Tk()  # Crea pantalla
    window.title("Mi primera aplicacion: Calculadora")
    window.geometry('450x450')

    label = tk.Label(window, text='Calculadora', font=('Arial bold', 16))
    label.grid(column=0, row=0)

    entrada1 = tk.Entry(window, width=10)
    entrada2 = tk.Entry(window, width=10)

    entrada1.grid(column=1, row=1)
    entrada2.grid(column=1, row=2)

    label_entrada1 = tk.Label(window, text='Ingrese primer numero:', font=('Arial bold', 10))
    label_entrada1.grid(column=0, row=1)

    label_entrada2 = tk.Label(window, text='Ingrese segundo numero:', font=('Arial bold', 10))
    label_entrada2.grid(column=0, row=2)

    label_operador = tk.Label(window, text="Escoja un operador", font=('Arial bold', 10))
    label_operador.grid(column=0, row=3)

    combo_operadores = ttk.Combobox(window)
    combo_operadores['values'] = ('+', '-', '*', '/', 'pow')
    combo_operadores.current(0)
    combo_operadores.grid(column=1, row=3)

    label_resultado = tk.Label(window, text="Resultado:", font=("Arial bold", 15))
    label_resultado.grid(column=0, row=5)

    historial = tk.Listbox(window, bg="LightSkyBlue1")
    historial.grid(column=1, row=18)

    def delete():
        historial.delete(ANCHOR)

    labelcol = tk.Label(window, text='Controles RGB:', font=('Arial bold', 12))
    labelcol.grid(column=1, row=6)

    labelh = tk.Label(window, text='Historial:', font=('Arial bold', 12))
    labelh.grid(column=1, row=17)
    boton_borrar = tk.Button(window, text="Borrar", command=delete)
    boton_borrar.grid(column=1, row=19)

    boton = tk.Button(window,
                      command=lambda: click_calcular(
                          historial,
                          label_resultado,
                          entrada1.get(),
                          entrada2.get(),
                          combo_operadores.get()),
                      text="Calcular",
                      bg="purple",
                      fg="white")

    boton.grid(column=1, row=4)

    def cambio():
        window.configure(bg=_from_rgb((w.get(), w1.get(), w2.get())))
        label.configure(bg=_from_rgb((w.get(), w1.get(), w2.get())))
        label_operador.configure(bg=_from_rgb((w.get(), w1.get(), w2.get())))
        label_entrada1.configure(bg=_from_rgb((w.get(), w1.get(), w2.get())))
        label_entrada2.configure(bg=_from_rgb((w.get(), w1.get(), w2.get())))
        label_resultado.configure(bg=_from_rgb((w.get(), w1.get(), w2.get())))
        labelh.configure(bg=_from_rgb((w.get(), w1.get(), w2.get())))
        labelcol.configure(bg=_from_rgb((w.get(), w1.get(), w2.get())))
        if w.get() <= 75 and w1.get() <= 75 and w2.get() <= 75:
            label.configure(fg="white")
            label_operador.configure(fg="white")
            label_entrada1.configure(fg="white")
            label_entrada2.configure(fg="white")
            label_resultado.configure(fg="white")
            labelh.configure(fg="white")
            labelcol.configure(fg="white")
        else:
            label.configure(fg="black")
            label_operador.configure(fg="black")
            label_entrada1.configure(fg="black")
            label_entrada2.configure(fg="black")
            label_resultado.configure(fg="black")
            labelh.configure(fg="black")
            labelcol.configure(fg="black")

    w = tk.Scale(window, from_=0, to=255, orient=HORIZONTAL, resolution=1)
    w.grid(column=0, row=7)

    w1 = tk.Scale(window, from_=0, to=255, orient=HORIZONTAL, resolution=1)
    w1.grid(column=1, row=7)

    w2 = tk.Scale(window, from_=0, to=255, orient=HORIZONTAL, resolution=1)
    w2.grid(column=2, row=7)

    botonz = tk.Button(window, text="Cambiar color de fondo", command=cambio)
    botonz.grid(column=1, row=10)

    window.mainloop()
    

def main():
    init_window()


main()
