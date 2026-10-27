#Variaveis para cadastro
nome = ""
idade = ""
usuario = ""
senha = ""

#Variaveís para login
login_usuario = ""
login_senha = ""

#Variaveis de controle
controle_cadastro = ""

#Apenas a tela de visualização
while True:
    #Alterando controle_cadastro para poder cadastrar quantas vezes eu quiser
    controle_cadastro = "2"
    print ("====================")
    print (" Sistema de Cadastro")
    print ("====================")
   
    print ("1 - Cadastrar")
    print ("2- Fazer login")
    print ("3 - Sair " )

    opcao = input ("Escolha uma opção:")
#Funcionalidades
    #Se o usuario digitar o valor 1, vai ser exibido
    # a ação abaixo:
    if (opcao == "1"): 
        while controle_cadastro != "1":
            print("======================")
            print("===Tela de Cadastro===")     
            print("======================")
            nome =  input ("Digite o seu nome: ")
            idade = input ("Digite a sua idade: ")
            usuario = input ("Digite o seu usuario: ")
            senha = input ("Digite sua senha: ") 

            controle_cadastro = input("\n Você deseja voltar para a tela anterior ?\n 1)-Voltar para o menu anterior;\n Digite qualquer tecla para refazer o cadastro;\n")
           
            if(controle_cadastro == "1"):   
                print ("\n Cadastro realizado!\n")
            else:
                print("Valor digitado inválido, faça o cadastro novamente")
    #se digitar 2, abre a tela de login
    elif(opcao == "2"):
         print("======================")
         print("====Tela de Login ====")
         print("======================")
         login_usuario = input ("Digite o usuário:   ")
         login_senha = input("Digite a senha :")

         #Processamento de ususario e senha
         if login_usuario == usuario and login_senha == senha :
            while True:  
                print ("\nLogin realizado com sucesso!\n")
                print("Bem-vindo,", nome)
                print ("\n=====Àrea do Usuàrio=====\n")
                print ("1 - Ver os dados cadastrados")
                print ("2- Voltar para o menu anterior")
                print ("3- Alterar senha")


                usuario_opcao = input("\nEscolha uma das opções do menu acima:\n ")

                if (usuario_opcao == "1"):
                    print("\n=====================")
                    print("===Dados Cadastrados===")
                    print ("====================\n")
                    #Mostrar dados  de usuário:
                    print("=== Cadastro ===")
                    print ("Nome do cadastro:", nome )
                elif(usuario_opcao == "2"): 
                    print("Idade do usuário:", idade)
                    print("Usuário:", usuario)
                    print ("Senha do usuário:", senha) 
                elif(usuario_opcao == "2"):
                    print("\n Você está voltando para o menu anterior")
                    break 
                elif (usuario_opcao == "3"):
                     senha = input ("\nDigite a nova senha:  ")

                else:
                    print("\nOpção digitado inválida, use os númetros do Menu!")
            #Se não estiver correta entra no caso abaixo
            else:
                print("\nUsuário ou senha incorretos\n")
                
    #se digitar 3, sai da execução
    elif(opcao == "3"):
        print("\nVocé está saindo do cadastro, até mais!\n")
        break  
 #Se não for nem 1, 2 ou 3, mostrar erro e repetir código
    else:
     print ("Valor digitado, inválido, use apenas números inteiros do menu")
