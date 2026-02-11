from tkinter import *
from tkinter import Tk, ttk
import os
# importando Pillow

from PIL import Image, ImageTk
# importando barra de progresso do Tlinter
from tkinter.ttk import Progressbar

# importando matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure


################# cores ###############
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   
co6 = "#038cfc"   
co7 = "#3fbfb9"  
co8 = "#263238"   
co9 = "#e9edf5"   

colors = ['#5588bb', '#66bbbb','#99bb55', '#ee9944', '#444466', '#bb5555']

#criando janela 

janela = Tk()
janela.title()
janela.geometry('900x650')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")

#criando iframe para divisão da tela

framecima = Frame(janela, width=1043, height=50, bg=co1, relief="flat")
framecima.grid(row=0,column=0)

frameMeio = Frame(janela, width=1043, height=361, bg=co1,pady=20, relief="raised")
frameMeio.grid(row=1,column=0,pady=1,padx=0,sticky=NSEW)

framebaixo = Frame(janela, width=1043, height=300, bg=co1, relief="flat")
framebaixo.grid(row=2,column=0,pady=0,padx=0,sticky=NSEW)

frame_graf_py = Frame(frameMeio, width=580, height=250, bg=co2)
frame_graf_py.place(x=415, y=5)

# Trabalhando no frame Cima

#acessando a imagem
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(BASE_DIR, 'Log.png')

app_img = Image.open(img_path)
app_img = app_img.resize((45, 45))
app_img = ImageTk.PhotoImage(app_img)


app_logo = Label(framecima, image=app_img, text="Orçamento pessoal", width= 900, compound=LEFT, padx =5, relief=RAISED, anchor=NW
,font=('Verdana 20 bold'), bg=co1, fg = co4)
app_logo.place(x=0,y=0)

# porcentagem...........
def porcentagem():
    l_nome = Label(frameMeio, text="Porcentagem da Receita gasta", height=1, anchor=NW,font=('Verdana 12 '), bg=co1, fg = co4)
    l_nome.place(x=7, y=5)

    style = ttk.Style()
    style.theme_use('default')
    style.configure("black.Horizontal.TProgressbar", background= '#daed6b')
    style.configure("TProgressbar", thickness=20)
    bar = Progressbar(frameMeio, length=180, style='black.Horizontal.TProgressbar')
    
    
    bar.place(x=10, y=35)
    bar['value'] = 50

    valor = 50
    l_porcentagem = Label(frameMeio, text="{:,.2f}%".format(valor),  anchor=NW,font=('Verdana 12 '), bg=co1, fg = co4)
    l_porcentagem.place(x=200, y=35)


#função do gráfico barra.............................

def grafico_bar():

    lista_categorias = ['Renda', 'Despesas', 'Saldo']
    lista_valores = [3000, 2000, 6236]

    # Cria figura e atribui objetos de eixo
    figura = plt.Figure(figsize=(4, 3.45), dpi=60)
    ax = figura.add_subplot(111)
    ax.autoscale(enable=True, axis='both', tight=None)

    ax.bar(lista_categorias, lista_valores, color=colors, width=0.9)

    # Adiciona rótulos individuais nas barras
    c = 0
    for i in ax.patches:
        ax.text(i.get_x() + i.get_width()/2.0, i.get_height() + .5,
                str("{:,.0f}".format(lista_valores[c])), fontsize=17, fontstyle='italic',
                verticalalignment='bottom', color='dimgrey', ha='center')
        c += 1

    ax.set_xticklabels(lista_categorias, fontsize=16)

    ax.patch.set_facecolor('#ffffff')
    ax.spines['bottom'].set_color('#CCCCCC')
    ax.spines['bottom'].set_linewidth(1)
    ax.spines['right'].set_linewidth(0)
    ax.spines['top'].set_linewidth(0)
    ax.spines['left'].set_color('#CCCCCC')
    ax.spines['left'].set_linewidth(1)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(bottom=False, left=False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(False, color='#EEEEEE')
    ax.xaxis.grid(False)

    canva = FigureCanvasTkAgg(figura, frameMeio)
    canva.get_tk_widget().place(x=10, y=70)



# função de resumo dos valores.........................

def resumo():
    valor = [500,600,420]

    l_linha = Label(frameMeio, text="", width=215, height=1, anchor=NW, font=('Arial 1 '), bg='#545454')
    l_linha.place(x=309, y=52)
    l_sumario = Label(frameMeio, text="Total Renda Mensal      ".upper(),  anchor=NW,font=('Verdana 12 '), bg=co1, fg = '#83a9e6')
    l_sumario.place(x=309, y=35)
    l_sumario = Label(frameMeio, text="R$ {:,.2f}".format(valor[0]), width=0, height=0, anchor=NW,font=('Arial 17 '),bg = co1,  fg = co4)
    l_sumario.place(x=309, y=70)
 


    l_linha = Label(frameMeio, text="", width=215, height=1, anchor=NW, font=('Arial 1 '), bg='#545454')
    l_linha.place(x=309, y=132)
    l_sumario = Label(frameMeio, text="Total despesas Mensais   ".upper(),  anchor=NW,font=('Verdana 12 '), bg=co1, fg = '#83a9e6')
    l_sumario.place(x=309, y=115)
    l_sumario = Label(frameMeio, text="R$ {:,.2f}".format(valor[1]), width=0, height=1, anchor=NW,font=('Arial 17 '), bg=co1, fg = co4)
    l_sumario.place(x=309, y=150)



    l_linha = Label(frameMeio, text="", width=215, height=1, anchor=NW,font=('Arial 1 '), bg='#545454')
    l_linha.place(x=309, y=207)
    l_sumario = Label(frameMeio, text="Total saldo da caixa     ".upper(),  anchor=NW,font=('Verdana 12 '), bg=co1, fg = '#83a9e6')
    l_sumario.place(x=309, y=190)
    l_sumario = Label(frameMeio, text="R$ {:,.2f}".format(valor[2]), width=0, height=1, anchor=NW,font=('Arial 17 '), bg=co1, fg = co4)
    l_sumario.place(x=309, y=220)

# função grafico_pie():
def grafico_pie():
    figura = plt.Figure(figsize=(5, 3), dpi=90)
    ax = figura.add_subplot(111)
    
    lista_valores = [345,225,534]
    lista_categorias = ['Renda', 'Despesa', 'Saldo']

    explode = []
    for i in lista_categorias:
        explode.append(0.05)

    ax.pie(lista_valores, explode=explode, wedgeprops=dict(width=0.2), autopct='%1.1f%%', colors=colors,shadow=True, startangle=90)

    ax.legend(lista_categorias, loc="center right", bbox_to_anchor=(1.55, 0.50))

    canva_categoria = FigureCanvasTkAgg(figura, frame_graf_py)
    canva_categoria.get_tk_widget().grid(row=0, column=0)
porcentagem()
grafico_bar()
resumo()
grafico_pie()


# Criando frames dentro do Frame baixo 

framerenda = Frame(framebaixo, width=300, height=250, bg=co1)
framerenda.grid(row=0,column=0)

frameoperacoes = Frame(framebaixo, width=220, height=250, bg=co1)
frameoperacoes.grid(row=0,column=1, padx=5)

frameconfiguracoes = Frame(framebaixo, width=220, height=250, bg=co1)
frameconfiguracoes.grid(row=0,column=2,padx=5)

# Tabela Renda Mensal

app_tabela = Label(frameMeio, text="Tabela Receitas e Despesas",anchor=NW, font=('Verdana 12'), bg=co1, fg = co4)
app_tabela.place(x=5,y=309)

# função para mostrar renda
def mostrar_renda():
    tabela_head = ['#Id','Categoria','Data','Quantia']

    lista_itens = [[0,2,3,4],[0,2,3,4],[0,2,3,4],[0,2,3,4]]
    
    global tree

    tree = ttk.Treeview(framerenda, selectmode='extended',columns=tabela_head, show="headings")

    vsb = ttk.Scrollbar(framerenda, orient="vertical", command=tree.yview)

    hsb = ttk.Scrollbar(framerenda, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    hd=["center","center","center", "center"]
    h=[30,100,100,100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
#adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in lista_itens:
        tree.insert('', 'end', values=item)
mostrar_renda()
janela.mainloop()