import tkinter as tk
from tkinter import Label, Button

import re
#fazer ajustes finais com o columnspan
#printar na tela os resultados
#testar
#renomear as variáveis e funções

expressao=""

def calculadora_binario():
    print("Binário para Decimal")
    frame_inicio.pack_forget()
    frame_binario.pack(fill="both", expand=True) 
    #Definindo novo frame
    pass

def calculadora_decimal():
    print("Decimal para Binário")
    frame_inicio.pack_forget()
    frame_decimal.pack(fill="both", expand=True) 
    

def retornar_menu():
    frame_binario.pack_forget()
    frame_decimal.pack_forget()
    frame_inicio.pack(fill="both", expand=True)




#Parte do código destinado a parte da calculadora de decimal para binário

expressao_decimal = ""

def clicar_decimal(t):
    global expressao_decimal

   
    if t== "=":
        mostrar_resultado_decimal()
    elif t== "C":
        limpar_decimal()
    elif t== "⌫":
        remover_decimal()
    else:
        editar_decimal(t)

def editar_decimal(t):
    global expressao_decimal
    expressao_decimal += t
    label_expressao_decimal.config(text=f"Operação: {expressao_decimal}")

def limpar_decimal():
    global expressao_decimal
    expressao_decimal = ""
    label_expressao_decimal.config(text=f"Operação: {expressao_decimal}")

def remover_decimal():
    global expressao_decimal
    expressao_listada = list(expressao_decimal)
    if expressao_listada:  # Evita erro se estiver vazio
        expressao_listada.pop()
        expressao_decimal = "".join(expressao_listada)
    label_expressao_decimal.config(text=f"Operação: {expressao_decimal}")

def mostrar_resultado_decimal():
    global expressao_decimal
    try:
        resultado = eval(expressao_decimal)
        resultado_binario = bin(int(resultado))[2:]
        label_expressao_decimal.config(text=f"Resultado bin:{resultado_binario}(Resultado inteiro:{resultado})")
                                       
        expressao_decimal = str(resultado)
    except Exception:
        label_expressao_decimal.config(text="Erro: Expressão inválida")
        expressao_decimal = ""
        



#Funções destinadas a calculadora de binário para decimal
# Funções destinadas à calculadora de binário para decimal
expressao_binario = ""

def clicar_binario(t):
    global expressao_binario

    if t == "=":
        mostrar_resultado_binario()
    elif t == "C":
        limpar_tudo_binario()
    elif t == "⌫":
        remover_ultimo_binario()
    else:
        editar_operacao_binario(t)

def limpar_tudo_binario():
    global expressao_binario
    expressao_binario = ""
    label_expressao_binario.config(text=f"Operação: {expressao_binario}")

def remover_ultimo_binario():
    global expressao_binario
    expressao_listada = list(expressao_binario)
    if expressao_listada:
        expressao_listada.pop(-1)
        expressao_binario = "".join(expressao_listada)
    label_expressao_binario.config(text=f"Operação: {expressao_binario}")

def mostrar_resultado_binario():
    global expressao_binario
    try:
        #separará todos os elementos da expressão.ex=["10","+","10"]
        tokens = re.findall(r'[01]+|[^\s01]', expressao_binario)

        #adicionará os valores já convertidos para decimal nessa lista
        nova_expressao = []
        for token in tokens:
            if re.fullmatch(r'[01]+', token):
                # É um número binário: converte
                decimal = str(int(token, 2))
                nova_expressao.append(decimal)
            else:
                # É operador: mantém como está
                nova_expressao.append(token)

        # Junta os tokens convertidos em uma string
        expressao_decimal = ''.join(nova_expressao)
       
        
   
        # Avalia a expressão decimal
        resultado = eval(expressao_decimal)
        resultado_binario=bin(resultado)
    
       
        label_expressao_binario.config(text=f"Resultado em decimal: {resultado}(Resultado binário:{resultado_binario})")
        expressao_binario = str(resultado)
    except Exception:
        label_expressao_binario.config(text="Erro: Expressão inválida")
        expressao_binario = ""

def editar_operacao_binario(t):
    global expressao_binario
    expressao_binario += t
    label_expressao_binario.config(text=f"Operação: {expressao_binario}")





# Criação da janela principal
janela = tk.Tk()
janela.title("B1tMath") #definindo título
janela.geometry("600x600+500+200")#definindo tamanho e onde ficará a  janela
janela.config(bg="black")
janela.resizable(False, False)

#  Criação do Frame de início
frame_inicio = tk.Frame(janela, bg="black")


#Widgets é qualquer coisa visual que aparecerá dentro do código
texto_orientacao = Label(frame_inicio, text="Bem vindo ao B1tMath", fg="green", bg="black", font=("Courier", 16))
texto_orientacao.grid(column=0, row=0, pady=(0, 40))

texto_opcao1 = Button(frame_inicio, text="OPÇÃO 1 (B1NÁR10 → DECIMAL)", fg="green", bg="black",font=("Courier", 16), command=calculadora_binario)
texto_opcao1.grid(column=0, row=5, pady=10)

texto_opcao2 = Button(frame_inicio, text="OPÇÃO 2 (DECIMAL → B1NÁRI0)", fg="green", bg="black",font=("Courier",16), command=calculadora_decimal)
texto_opcao2.grid(column=0, row=6, pady=10)

#  Mostra o frame na janela principal
frame_inicio.pack(fill="both", expand=True)




#Criando frame da calculadora
frame_decimal=tk.Frame(janela,bg="black")

#botões começarão a partir da linha 1 para que 
botoes_decimal = [
    ("C", 1, 0), ("⌫", 1, 1), ("(", 1, 2), (")", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("/", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("*", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("-", 4, 3),
    ("0", 5, 0), (".", 5, 1), ("=", 5, 2), ("+", 5, 3),
]



#for utilizado para a criação dos botões
for texto, linha, coluna in botoes_decimal:
    botao = tk.Button(frame_decimal, text=texto, font=("Courier", 20),bg="black", fg="green",command=lambda t=texto: clicar_decimal(t))
    botao.grid(row=linha, column=coluna, sticky="nsew", padx=2, pady=2)



# criando um label para mostrar os resultados
label_expressao_decimal = tk.Label(frame_decimal, text="Operação: ",font=("Courier,30"),width=60)
label_expressao_decimal.grid(row=0, column=0, columnspan=4)
label_expressao_decimal.config(bg="black",fg="green")

#botão voltar menu
voltar_menu_decimal=tk.Button(frame_decimal,text="Voltar menu",command=retornar_menu,bg="black",fg="green")
voltar_menu_decimal.grid(row=7,column=0, columnspan=3)















#Criando frame de binário para decimal
frame_binario=tk.Frame(janela,bg="black")
#expand true faz com que o espaço seja totalmente preenchido
#fill=both faz o espaço crescer horizontalmente e verticalmente

#criando os botões responsivos para a calculadora
#sticky="nsew"--->faz o botão crescer para que preencha todo a parte do grid
#necessita usar lamba para executar apenas quando o usuário clicar no botão

#Tupla em relação ao texto que será mostrado,linha,coluna
botoes = [
    ("0", 3, 0), ("1", 3, 1),
    ("+", 1, 0), ("-", 1, 1),
    ("*", 2, 0), ("/", 2, 1),
    ("C", 1, 2), ("⌫", 2, 2),
    ("=", 3, 2)
]

#usando um for para criar esses botões de forma automática,sem a necessidade de criar manualmente
for texto, linha, coluna in botoes:
    botao = tk.Button(frame_binario, text=texto,font=("Arial", 20),bg="black", fg="green",command=lambda t=texto: clicar_binario(t))
    botao.grid(row=linha, column=coluna, sticky="nsew", padx=2, pady=2)

# criando um label para mostrar os resultados
label_expressao_binario = tk.Label(frame_binario, text="Operação: ",font=("Courier,30"),width=60)
label_expressao_binario.grid(row=0, column=0, columnspan=3)
label_expressao_binario.config(bg="black",fg="green")

#botão voltar menu
voltar_menu_binario=tk.Button(frame_binario,text="Voltar menu",command=retornar_menu,bg="black",fg="green")
voltar_menu_binario.grid(row=5,column=0, columnspan=3)







#validando para não rodar um comando perigoso







# Loop principal da aplicação
janela.mainloop()
