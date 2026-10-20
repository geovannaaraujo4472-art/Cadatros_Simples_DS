#Variaveis para cadastro
nome = ""
idade = ""
usuario = ""
senha = ""

#Variaveís para login
login_usuario = ""
login_senha = ""
#Apenas a tela de visualização
while True:
    print ("====================")
    print (" Sistema de Cadastro")
    print ("====================")]





    print ("1 - Cadastrar")
    print ("2- Fazer login")
    print ("3 - Sair " )
    opcao = input ("Escolha uma opção:")
#Funcionalidades
    #Se o usuario digitar o valor 1, vai ser exibido
    # a ação abaixo:
    if (opcao == "1"): 
         print("======================")
         print("===Tela de Cadastro===")     
         print("======================")
         nome =  input ("Digite o seu nome: ")
         idade = input ("Digite a sua idade: ")
         usuario = input ("Digite o seu usuario: ")
         senha = input ("Digite sua senha: ")
         print ("\n Cadastro realizado!\n")
    #se digitar 2, abre a tela de login
    elif(opcao == "2"):
         print("======================")
         print("====Tela de Login ====")
         print("======================")
         login_usuario = input ("Digite o usuário:   ")
         login_senha = input("Digite a senha :")

         #Processamento de ususario e senha
         if login_usuario == usuario and login_senha == senha :
            print("\nLogin realizado com sucesso!\n")
            print("Bem vindo,", nome)
         #Se não estiver correta entra no caso abaixo
         else:
             print("Usuário ou senha incorretos")
             
    #se digitar 3, sai da execução
    elif(opcao == "3"):
        print("Vocé está saindo do cadastro, até mais!")
        break 
 #Se não for nem 1, 2 ou 3, mostrar erro e repetir código
 else:
     print ("Valor digitado, inválido, use apenas números inteiros do menu")
