from __future__ import division
from tkinter import *



Raiz=Tk()
Raiz.resizable(width=False, height=False)
Raiz.title("Calculadora - Tkinter Python")
Raiz.iconbitmap(r"C:\Users\Roni\Documents\Ezequiel\Python\Calculadora\03 - Operaciones Matematicas\icons8-calculadora-48.ico")
miFrame=Frame(Raiz)
miFrame.config(bg="#eef2ed")
miFrame2= Frame(Raiz)
miFrame2.config(bg="#eef2ed")
miFrame3= Frame(Raiz)
miFrame3.config(bg="#eef2ed")

miFrame.pack(fill="both", expand=0)
miFrame2.pack(fill="both", expand=0)
miFrame3.pack(fill="x", expand=0)

#------PANTALLA---------------------------------------------------
escrituraEnPantalla = StringVar()
escrituraEnPantalla.set("0")
inputCalculadora = Entry(miFrame, width=14, textvariable=escrituraEnPantalla)
inputCalculadora.grid(row=0, column=0, padx=1, pady=2, sticky="nsew")
inputCalculadora.config(bg="#A2CADF", fg="#454546", justify="right", font=("Calibri", 16, "bold"),borderwidth=1, relief=SOLID)

#------Escritura en pantalla----------------------------------------- 
resultado = "0"
datosIngresados = []
esResultado = False 
respaldo = "0"


def escribe(num):
    if len(escrituraEnPantalla.get()) < 14 :
        escrituraEnPantalla.set(escrituraEnPantalla.get() + num)

def compruebaSiDebeBorrar():
    try:
        if escrituraEnPantalla.get() == str(datosIngresados[0]) and len(datosIngresados) == 1:
            datosIngresados.clear()
            escrituraEnPantalla.set("0")
        if escrituraEnPantalla.get() == "+" or escrituraEnPantalla.get() == "-" or escrituraEnPantalla.get() == "*" or escrituraEnPantalla.get() == "/":
            escrituraEnPantalla.set("0")
    except:
        pass

def compruebaSiHayResultado():
    if esResultado == True:
        borraTodo()


def escribeNumero(num):
    global resultado
    try:
        compruebaSiDebeBorrar()
    except:
        pass
    compruebaSiHayResultado()
    if resultado == "0":
        if num != "0" and num != "." and (len(escrituraEnPantalla.get()) == 1) and escrituraEnPantalla.get().find("0") == 0:   
            escrituraEnPantalla.set(escrituraEnPantalla.get()[:-2])
            escribe(num)

        elif num == "0" and escrituraEnPantalla.get() != "0" :
            escribe(num)   

        elif num != "0" and num != ".": #and len(escrituraEnPantalla.get()) > 1:
            escribe(num)

        elif len(escrituraEnPantalla.get()) == 2 and escrituraEnPantalla.get() == "00":
            borrarNumero()   #si el primer numero ingresado es 0, lo borro             
        
        elif num == "." :
            escribe(num)
            if escrituraEnPantalla.get().count(".")>1:
                borrarNumero()
    else:
        resultado = ""
        escribeNumero(num)

def borrarNumero():
    if len(escrituraEnPantalla.get()) > 1 :
        escrituraEnPantalla.set(escrituraEnPantalla.get()[:-1])
    elif len(escrituraEnPantalla.get()) == 1 :
        escrituraEnPantalla.set("0") 
    elif len(escrituraEnPantalla.get()) == 1 and escrituraEnPantalla.get() == "0":
        borraTodo()

def borraTodo():
    escrituraEnPantalla.set("0")
    datosIngresados.clear()
    global esResultado
    esResultado = False
#------Seteando Teclado---------------------------------------------------
#numeros
for n in range(0, 10):
    Raiz.bind(str(n), lambda event: escribeNumero(event.char)) # Para que se acepten las entradas también desde el NumPad es necesario "duplicar" algunis bindings
    Raiz.bind(f"<KP_{n}>", lambda event: escribeNumero(event.char)) # por eso duplicamos los "n" y "<KP_{n}>"

#punto
Raiz.bind(".", lambda event: escribeNumero(event.char))
Raiz.bind("<KP_Decimal>", lambda event: escribeNumero(event.char))


#operaciones
Raiz.bind("+", lambda event: operacionMatematica(event.char))
Raiz.bind("-", lambda event: operacionMatematica(event.char))
Raiz.bind("*", lambda event: operacionMatematica(event.char))
Raiz.bind("/", lambda event: operacionMatematica(event.char))
Raiz.bind("<Return>", lambda _: igual())
Raiz.bind("<KP_Enter>", lambda _: igual())



#botones de borrado
Raiz.bind("<BackSpace>", lambda _: borrarNumero())
Raiz.bind("<Delete>", lambda _: borraTodo())

#-----Operaciones Matematicas---------------------------------------------------
datosIngresados = []

def operacionMatematica(operacion):
    if datosIngresados == []:
        datosIngresados.append(escrituraEnPantalla.get())
        datosIngresados.append(operacion)
        escrituraEnPantalla.set(operacion)
    elif len(datosIngresados) == 1 and datosIngresados[0] == respaldo: #en teoria esto se da cuando hay un resultado
            datosIngresados.append(operacion)
            escrituraEnPantalla.set(operacion)

    elif len(datosIngresados) == 3:
        if datosIngresados[1] == "+":
            suma()
            
        elif datosIngresados[1] == "-":
            resta()
            
        elif datosIngresados[1] == "*":
            multi()
            
        elif datosIngresados[1] == "/":
            div()    
        global resultado
        resultado="0"    



#operaciones            

def suma():      
    resultado = str(float(datosIngresados[0]) + float(datosIngresados[2]))
    resultado = borraPuntoDecimal(resultado)
    datosIngresados.clear()
    datosIngresados.append(resultado)
    escrituraEnPantalla.set(resultado)
    global respaldo
    respaldo = resultado
    
def resta(): 
    resultado = str(float(datosIngresados[0]) - float(datosIngresados[2]))
    resultado = borraPuntoDecimal(resultado)
    datosIngresados.clear()
    datosIngresados.append(resultado)
    escrituraEnPantalla.set(resultado)
    global respaldo
    respaldo = resultado

def multi(): 
    resultado = str(float(datosIngresados[0]) * float(datosIngresados[2]))
    resultado = borraPuntoDecimal(resultado)
    datosIngresados.clear()
    datosIngresados.append(resultado)
    escrituraEnPantalla.set(resultado)
    global respaldo
    respaldo = resultado

def div(): 
    resultado = str(float(datosIngresados[0]) / float(datosIngresados[2]))
    resultado = borraPuntoDecimal(resultado)
    datosIngresados.clear()
    datosIngresados.append(resultado)
    escrituraEnPantalla.set(resultado)
    global respaldo
    respaldo = resultado
    
def igual():
    if datosIngresados == []:
        pass
    elif len(datosIngresados)==1 and escrituraEnPantalla.get() == datosIngresados[0]:
        borraTodo()
    elif escrituraEnPantalla.get() != "+" and escrituraEnPantalla.get() != "-" and escrituraEnPantalla.get() != "/" and escrituraEnPantalla.get() != "*":
        datosIngresados.append(escrituraEnPantalla.get())        
        operacionMatematica(datosIngresados[1])    

        
def borraPuntoDecimal(resultado):
    resultado = resultado
    if resultado[-2:] == ".0":  #borrar .0
        resultado = resultado.rstrip(resultado[-1])     
        resultado = resultado.rstrip(resultado[-1])               
        escrituraEnPantalla.set(str(resultado))
        return resultado 
    else:
        return resultado

      
#------FILA 1---------------------------------------------------

labelVacia = Button(miFrame2, text="", width=4, state="disabled")
labelVacia.grid(row=1, column=0)
labelVacia.config(bg="white", fg="#454546", font=("Calibri", 12, "bold"), borderwidth=0, relief="solid",justify="center")

botonBorrar = Button(miFrame2, text= "CE", width=4, command=lambda:borraTodo())
botonBorrar.grid(row=1, column=1)
botonBorrar.config(bg="white", fg="#454546", font=("Calibri", 12, "bold"), borderwidth=1,  relief="solid",justify="center")

botonBack = Button(miFrame2, text="<", width=4, command=lambda:borrarNumero()) 
botonBack.grid(row=1, column=2)
botonBack.config(bg="white", fg="#454546", font=("Calibri", 12, "bold"), borderwidth=1, relief="solid",justify="center")


botonDiv = Button(miFrame2, text="/", width=4, command=lambda:operacionMatematica("/"))
botonDiv.grid(row=1, column=3)
botonDiv.config(bg="white", fg="#454546", font=("Calibri", 12, "bold"), borderwidth=1, relief="solid",justify="center")


#------FILA 2---------------------------------------------------
boton7 = Button(miFrame2, text="7", width=4, command=lambda:escribeNumero("7"))
boton7.grid(row=2, column=0)
boton7.config(bg="white", fg="#454546", font=("Calibri", 12, "bold"), borderwidth=1, relief="solid",justify="center")

boton8 = Button(miFrame2, text="8", width=4, command=lambda:escribeNumero("8"))
boton8.grid(row=2, column=1)
boton8.config(bg="white", fg="#454546", font=("Calibri", 12, "bold"), borderwidth=1, relief="solid",justify="center")

boton9 = Button(miFrame2, text="9", width=4, command=lambda:escribeNumero("9"))
boton9.grid(row=2, column=2)
boton9.config(bg="white", fg="#454546", font=("Calibri", 12, "bold"), borderwidth=1, relief="solid",justify="center")

botonMulti = Button(miFrame2, text="*", width=4, command=lambda:operacionMatematica("*"))
botonMulti.grid(row=2, column=3)
botonMulti.config(bg="white", fg="#454546", font=("Calibri", 12, "bold"), borderwidth=1, relief="solid",justify="center")

#------FILA 3---------------------------------------------------
boton4 = Button(miFrame2, text="4", width=4, command=lambda:escribeNumero("4"))
boton4.grid(row=3, column=0)
boton4.config(bg="white", fg="#454546", font=("Calibri", 12, "bold"), borderwidth=1, relief="solid")

boton5 = Button(miFrame2, text="5", width=4, command=lambda:escribeNumero("5"))
boton5.grid(row=3, column=1)
boton5.config(bg="white", fg="#454546", font=("Calibri", 12, "bold"), borderwidth=1, relief="solid")

boton6 = Button(miFrame2, text="6", width=4, command=lambda:escribeNumero("6"))
boton6.grid(row=3, column=2)
boton6.config(bg="white", fg="#454546", font=("Calibri", 12, "bold"), borderwidth=1, relief="solid")

botonMenos = Button(miFrame2, text="-", width=4, command=lambda:operacionMatematica("-"))
botonMenos.grid(row=3, column=3)
botonMenos.config(bg="white", fg="#454546", font=("Calibri", 12, "bold"), borderwidth=1, relief="solid")
#------FILA 4---------------------------------------------------
boton1 = Button(miFrame2, text="1", width=4, command=lambda:escribeNumero("1"))
boton1.grid(row=4, column=0)
boton1.config(bg="white", fg="#454546", font=("Calibri", 12, "bold"), borderwidth=1, relief="solid")

boton2 = Button(miFrame2, text="2", width=4, command=lambda:escribeNumero("2"))
boton2.grid(row=4, column=1)
boton2.config(bg="white", fg="#454546", font=("Calibri", 12, "bold"), borderwidth=1, relief="solid")

boton3 = Button(miFrame2, text="3", width=4, command=lambda:escribeNumero("3"))
boton3.grid(row=4, column=2)
boton3.config(bg="white", fg="#454546", font=("Calibri", 12, "bold"), borderwidth=1, relief="solid")

botonMas = Button(miFrame2, text="+", width=4, command=lambda:operacionMatematica("+"))
botonMas.grid(row=4, column=3)
botonMas.config(bg="white", fg="#454546", font=("Calibri", 12, "bold"), borderwidth=1, relief="solid")

#------FILA 5---------------------------------------------------


boton0 = Button(miFrame3, text="0", width=9, command=lambda:escribeNumero("0"))
boton0.grid(row=0, column=0, columnspan=2, sticky="nsew")
boton0.config(bg="white", fg="#454546", font=("Calibri", 12, "bold"), borderwidth=1, relief="solid",)

botonComa = Button(miFrame3, text=",", width=4, command=lambda:escribeNumero("."))
botonComa.grid(row=0, column=2)
botonComa.config(bg="white", fg="#454546", font=("Calibri", 12, "bold"), borderwidth=1, relief="solid")

botonIgual = Button(miFrame3, text="=", width=4, command=lambda:igual())
botonIgual.grid(row=0, column=3)
botonIgual.config(bg="#A2CADF", fg="#454546", font=("Calibri", 12, "bold"), borderwidth=1, relief="solid")

Raiz.mainloop()