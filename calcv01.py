#Calculadora simples utilizando a linguagem python.
#____________________________________________________#
#importanto tkinter
from tkinter import *
from tkinter import ttk

#cores
cor1 = "#080808" #preta
cor2= "#d4c600" #amarela
cor3= "#f4f5f0" #branca
cor4= "#0d2f6e" # azul
cor5= "#969696" #cinza

janela = Tk()
janela.title("Calculadora v0.1")
janela.geometry("269x315")
janela.config(bg=cor1)

#Criando Frame
frame_tela = Frame(janela, width= 270, height= 50, bg= cor4)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width= 270, height= 268)
frame_corpo.grid(row=1, column=0)

# variavel todos valores em uma estring
todos_valores =''
valor_texto = StringVar()

#criando Fução
def entrar_valores(event):

    global todos_valores
    todos_valores = todos_valores + str(event)

    #passando valor para tela
    valor_texto.set(todos_valores)

#função para calcular
def calcular():
    global todos_valores
    resultado= eval(todos_valores)

    valor_texto.set(str(resultado))

#função limpa tela
def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")
app_label= Label(frame_tela, textvariable=valor_texto, width=18, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18 '), bg= cor4, fg= cor3) #anchor="e" mostra resultado na tela no lado direito
app_label.place(x=0,y=0)

#Criando Botões
b1= Button(frame_corpo, command=limpar_tela,text='C', width=11, height=2,bg=cor5, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b1.place(x=1, y=0)
b2= Button(frame_corpo,command= lambda : entrar_valores('%'), text='%', width=5, height=2, bg=cor5, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b2.place(x=123, y=0)
b3= Button(frame_corpo, command= lambda : entrar_valores('/'),text='/', width=7, height=2, bg=cor2, fg=cor3, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b3.place(x=188, y=0)

b4= Button(frame_corpo, command= lambda : entrar_valores('7'),text='7', width=5, height=2,bg=cor5, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b4.place(x=1, y=53)
b5= Button(frame_corpo, command= lambda : entrar_valores('8'),text='8', width=5, height=2, bg=cor5, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b5.place(x=62, y=53)
b6= Button(frame_corpo, command= lambda : entrar_valores('9'),text='9', width=5, height=2, bg=cor5, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b6.place(x=123, y=53)
b7= Button(frame_corpo,command= lambda : entrar_valores('*'), text='*', width=7, height=2, bg=cor2, fg=cor3, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b7.place(x=188, y=53)

b8= Button(frame_corpo, command= lambda : entrar_valores('4'),text='4', width=5, height=2,bg=cor5, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b8.place(x=1, y=105)
b9= Button(frame_corpo,command= lambda : entrar_valores('5'), text='5', width=5, height=2, bg=cor5, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b9.place(x=62, y=105)
b10= Button(frame_corpo, command= lambda : entrar_valores('6'),text='6', width=5, height=2, bg=cor5, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b10.place(x=123, y=105)
b11= Button(frame_corpo, command= lambda : entrar_valores('-'),text='-', width=7, height=2, bg=cor2, fg=cor3, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b11.place(x=188, y=105)

b12= Button(frame_corpo, command= lambda : entrar_valores('1'),text='1', width=5, height=2,bg=cor5, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b12.place(x=1, y=159)
b13= Button(frame_corpo, command= lambda : entrar_valores('2'),text='2', width=5, height=2, bg=cor5, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b13.place(x=62, y=159)
b14= Button(frame_corpo, command= lambda : entrar_valores('3'),text='3', width=5, height=2, bg=cor5, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b14.place(x=123, y=159)
b15= Button(frame_corpo, command= lambda : entrar_valores('+'),text='+', width=7, height=2, bg=cor2, fg=cor3, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b15.place(x=188, y=159)

b16= Button(frame_corpo,command= lambda : entrar_valores('0'), text='0', width=11, height=2,bg=cor5, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b16.place(x=1, y=213)
b17= Button(frame_corpo, command= lambda : entrar_valores('.'),text=',', width=5, height=2, bg=cor5, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b17.place(x=123, y=213)
b18= Button(frame_corpo, command= calcular, text='=', width=7, height=2, bg=cor2, fg=cor3, font=('Ivy 13 bold'), relief= RAISED, overrelief=RIDGE)
b18.place(x=188, y=213)

janela.mainloop()
