from tkinter import *
import pycep_correios

def printar():
    cep1 = cep.get()
    endereco = pycep_correios.get_address_from_cep(cep1)
    resultado1 = Label(window, text='Logradouro: ' + endereco['logradouro']).grid(row=5, column=0, columnspan=3)
    resultado2 = Label(window, text='Bairro: ' + endereco['bairro']).grid(row=6, column=0, columnspan=3)
    resultado3 = Label(window, text='Cidade: ' + endereco['cidade']).grid(row=7, column=0, columnspan=3)
    resultado4 = Label(window, text='Complemento: ' + endereco['complemento']).grid(row=8, column=0, columnspan=3)
    resultado5 = Label(window, text='UF: ' + endereco['uf']).grid(row=9, column=0, columnspan=3)
    resultado6 = Label(window, text='CEP: ' + endereco['cep']).grid(row=10, column=0, columnspan=3)

window = Tk()
window.title('Consulta de CEP')
window.geometry('450x380')
window.resizable(False, False)
filename = PhotoImage(file = r"C:\Users\Ana\Desktop\busca.jpg")
filename = filename.subsample(3,3)
img = Label(image=filename)
img.place(x=0, y=0, relheight=1.6, relwidth=1.6)

Label(window, text='Digite o CEP (apenas os números) ', padx=10, pady=30).grid(row=3, column=0)
cep = Entry(window)
cep.grid(row=3, column=1)
Button(window, text='Consultar', command= printar, height=2, width=10).grid(row=3, column=2, padx=20)

window.mainloop()

