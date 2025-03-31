import customtkinter as tk
from tkinter import font

janela = tk.CTk()
janela.title("Janela")
janela.geometry('600x380')
janela.minsize(600, 380)
janela.maxsize(600, 380)
janela.iconbitmap('icon.ico')
tk.set_appearance_mode('Dark')
tk.FontManager.load_font('fun.otf')
usuarios = {}


#   Função que valida se login é existente no Banco de Dados

validado = False
lblinvalido = tk.CTkLabel(janela, text="", text_color='red', font=('Tahoma', 10))
lbluserinexistente = tk.CTkLabel(janela, text="", text_color='red', font=('Tahoma', 10))

def validar_login(user, senha):

    global validado
    user_act = user
    if user not in usuarios:
        lblinvalido.configure(janela, text="Usuário inexistente no Sistema!", text_color='red', font=('Tahoma', 10))
        lblinvalido.place(x=200, y=215)
        return False
    if usuarios[user] != senha:
        lblinvalido.configure(janela, text="Senha inválidos!", text_color='red', font=('Tahoma', 10))
        lblinvalido.place(x=200, y=215)
        return False
        


    # Janela de Bem vindo após validação de Login

    painel = tk.CTk()
    painel.geometry('700x400')
    painel.title('Bem Vindo!')

    lblpn = tk.CTkLabel(painel, text='Seja Bem-Vindo!', font=('Comic Sans MS', 34), text_color='green')
    lblpn.pack()

    lblpnuser = tk.CTkLabel(painel, text=f'Usuário: {user_act}', font=('Comic Sans MS', 16))
    lblpnuser.pack()

    painel.mainloop()

    return validado



  #   Função para adicionar os dados no dicionário


#   Função da janela de cadastro

def cadastro():
    global usuarios
    cadastro = tk.CTk()
    cadastro.title('Cadastro de Usuário')
    cadastro.geometry('700x400')
    lblcdmsg = tk.CTkLabel(cadastro, text='', font=('Sans Serif Collection', 24), text_color='#87CEFA')
    
    lblcd = tk.CTkLabel(cadastro, text='Cadastro de Usuário', font=('Georgia', 32), text_color='gray', pady=20)
    lblcd.pack()


    # Elementos da criação do Usuário (Label e entry)

    lblcduser = tk.CTkLabel(cadastro, text='Criar Novo nome de Usuário:', font=('Sylfaen', 16), pady=10)
    lblcduser.place(x=10, y=100)

    txtcduser = tk.CTkEntry(cadastro, placeholder_text='Insira um novo nome de usuário', width=200)
    txtcduser.place(x=10, y=140)


    #   Elementos da criação da Nova senha (Label e Entry)

    lblcdpass = tk.CTkLabel(cadastro, text="Criar uma nova Senha:", font=('Sylfaen', 16), pady=10)
    lblcdpass.place(x=10, y=180)
    
    txtcdpass = tk.CTkEntry(cadastro, placeholder_text='Insira uma nova senha', width=200)
    txtcdpass.place(x=10, y=220)



    def add_dict(u,p):
        if u in usuarios:
            lblcdmsg.configure(cadastro, text='Usuário Já existe.', font=('Sans Serif Collection', 24), text_color='#FF0000')
            lblcdmsg.place(x=10, y=340)
            return False
        usuarios[u] = p
        lblcdmsg.configure(cadastro, text='Usuário Cadastrado com Sucesso', font=('Sans Serif Collection', 24), text_color='#87CEFA')
        lblcdmsg.place(x=10, y=340)


    btncd = tk.CTkButton(cadastro, text='Cadastrar Usuário', text_color='black', command=lambda: add_dict(txtcduser.get(), txtcdpass.get()))
    btncd.place(x=10, y=280)

    cadastro.mainloop()





    # Label Principal:



#   Label inicial: Login de usuário
lbllogin = tk.CTkLabel(janela, text=f"Login de Usuário", font=('Georgia', 22), text_color='gray', pady=30)
lbllogin.pack()


#   Label e entrada referente ao input do User
lbluser = tk.CTkLabel(janela, text="Usuário:", font=('Tahoma', 12), text_color='cyan')
lbluser.place(x=200, y=90)

txtuser = tk.CTkEntry(janela, height=17, width=190)
txtuser.place(y=120, x=200)


#   Label e entrada referente ao input de pass
lblpass = tk.CTkLabel(janela, text=f'Senha:', font=('Tahoma', 12), text_color='cyan')
lblpass.place(x=200, y=160)
txtpass = tk.CTkEntry(janela, height=17, width=190)
txtpass.place(x=200, y=190)


#   Botão de acesso
btnacessar = tk.CTkButton(janela, text='Acessar', text_color='black', command=lambda: validar_login(txtuser.get(), txtpass.get()))
btnacessar.place(x=220, y=280)


#   Botão de cadastro de usuários

btncadastro = tk.CTkButton(janela, text='Cadastrar', text_color='black', command=lambda: cadastro())
btncadastro.place(x=220, y=320)




janela.mainloop()