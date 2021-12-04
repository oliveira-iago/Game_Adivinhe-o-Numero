'''
29.04.2020 - Primeira versão
03.12.2021 - Update 2.0
Autor: Iago Leonardo Alves de Oliveira
----------------------------------------
Este programa escolhe um número aleatório
Pede para o usuário adivinhá-lo, dizendo se o palpite está próximo (sendo maior ou menor)
ele conta uma tentativa a cada palpite do usuário
----------------------------------------
Há três níveis diferentes:
Fácil   - Número entre 1 e 10
Normal  - Número entre 1 e 20
Difícil - Número entre 1 e 50
Insano  - Número entre 1 e 100
----------------------------------------
'''

#OS usada para ações no sistema operacional - TIME, aguardar
import os, time
#RANDOM faz o sistema escolher ou ordenar valores de forma aleatoria
import random
#COLORAMA usada para dar cores às strings // pip install colorama
import colorama
colorama.init()

#Cores
azul = '\033[1;94m'
vermelho = '\033[31m'
verde = '\033[1;92m'
amarelo = '\033[1;93m'
limpa = '\033[0;0m'


#Nome do bot em verde
bot = '\t' + verde + 'Robot: ' + limpa

#Limpa o terminal
os.system('cls')

print('\n\n\n' + bot + 'Olá! Qual é o seu nome?')
time.sleep(0.5)
#Recebe o nome do usuario
usuario = str(input('\tEu me chamo ' + azul))
#Formata o nome
usuario = '\t' + azul + usuario + ': ' + limpa


#Função principal do game
def jogo():
    #Animação de Carregando...
    time.sleep(0.2)
    os.system('cls')
    print(limpa + 'Carregando')
    time.sleep(0.10)
    os.system('cls')
    print('Carregando.')
    time.sleep(0.10)
    os.system('cls')
    print('Carregando..')
    time.sleep(0.10)
    os.system('cls')
    print('Carregando...')

    time.sleep(0.3)
    os.system('cls')
    
    #Seleção de nível
    print('\n\n\n' + bot + 'Beleza, {}! Em qual nível você quer jogar?'.format(usuario.replace(': ', '').replace('\t', '').replace(azul, '')))
    time.sleep(0.5)
    print('\n\t[{}1{}] Fácil   - Número entre {}1{} e {}10{}'.format(azul, limpa, amarelo, limpa, amarelo, limpa))
    time.sleep(0.5)
    print('\t[{}2{}] Normal  - Número entre {}1{} e {}20{}'.format(azul, limpa, amarelo, limpa, amarelo, limpa))
    time.sleep(0.5)
    print('\t[{}3{}] Difícil - Número entre {}1{} e {}50{}'.format(azul, limpa, amarelo, limpa, amarelo, limpa))
    time.sleep(0.5)
    print('\t[{}4{}] Insano  - Número entre {}1{} e {}100{}'.format(azul, limpa, amarelo, limpa, amarelo, limpa))

    time.sleep(0.5)
    #Recebe o nivel que o usuário deseja jogar
    nivel = str(input('\n\tDigite o número do nível desejado: ' + azul))

    #Enquanto o nivel for diferente das opções
    while nivel != '1' and nivel != '2' and nivel != '3' and nivel != '4':
        #Exibe o aviso
        print(vermelho + '\n\tINSIRA UM VALOR VÁLIDO!' + limpa)
        time.sleep(0.5)
        #Recebe o nivel que o usuário deseja jogar
        nivel = str(input('\n\tDigite o número do nível desejado: ' + azul))

    print('\n')
    #Se o nivel for Fácil
    if nivel == '1':
        time.sleep(0.5)
        print(bot + 'Ahhh, então você quer moleza?')
        time.sleep(0.5)
        print(bot + 'Hahaha!')

        #Define o valor maximo do numero
        max = 10

    #Se o nivel for Normal
    elif nivel == '2':
        time.sleep(0.5)
        print(bot + 'Nem muito difícil, mas também nem muito fácil!')
        time.sleep(0.5)
        print(bot + 'Vamos nessa!')

        #Define o valor maximo do numero
        max = 20

    #Se o nivel for Difícil
    elif nivel == '3':
        time.sleep(0.5)
        print(bot + 'Então você gosta de um desafio?')
        time.sleep(0.5)
        print(bot + 'Quero ver se você manda bem no chute!')

        #Define o valor maximo do numero
        max = 50

    #Senão, é Insano
    else:
        time.sleep(0.5)
        print(bot + 'Quase impossível de você ganhar')
        time.sleep(0.5)
        print(bot + 'Você tem 5% de chance de acertar!')

        #Define o valor maximo do numero
        max = 100

    time.sleep(2)
    os.system('cls')
    print('\n\n\n' + bot + 'Consegue adivinhar o número que estou pensando?')
    time.sleep(0.5)
    print(bot + 'Ele está entre 1 e {}. Dê um chute!'.format(max))

    #Numero que o bot escolheu com base no nivel
    num_bot = int(random.randint(1, max))

    #Aqui armazenará o numero do usuario
    num_user = int()
    #Aqui armazenará o numero de tentativas
    tentativas = int()

    #Enquanto o numero do usuario for diferente do bot e as tentativas menores que 5
    while num_bot != num_user and tentativas < 5:

        #Recebe o número do usuario
        num_user = int(input(usuario))
        print('\n')

        #Usa uma das tentativas
        tentativas = tentativas + 1
        #Calcula as tentativas restantes    
        restantes = 5 - tentativas
        
        #Se o usuario inserir um numero menor que 1 ou maior que o maximo
        if num_user < 1 or num_user > max:
            os.system('cls')
            #Exibe um alerta
            print(amarelo + '\n\t\t\tVocê escolheu um número inválido' + limpa)
            time.sleep(0.5)
            print(bot + 'O número que estou pensando está entre 1 e {}'.format(max))
            time.sleep(0.5)
            #Exibe as tentativas restantes
            print(bot + 'Você tem {} tentativas restantes'.format(restantes))

        #Senão, se o numero do usuario for maior que o numero do bot
        elif num_user > num_bot:
            os.system('cls')
            #Exibe a dica
            print('\n\n\n' + bot + 'O número que eu estou pensando é menor que {}'.format(num_user))
            time.sleep(0.5)
            print(bot + 'Você tem {} tentativas restantes'.format(restantes))

        #Senão, se o número do usuario for menor que o do bot
        elif num_user < num_bot:
            os.system('cls')
            #Exibe a dica
            print('\n\n\n' + bot + 'O número que eu estou pensando é maior que {}'.format(num_user))
            time.sleep(0.5)
            print(bot + 'Você tem {} tentativas restantes'.format(restantes))


    #Aqui saiu do loop
    #Se o usuario acertou com 0 tentativas
    if num_user == num_bot and tentativas == 0:
        time.sleep(0.5)
        #Exibe a mensagem
        print(bot + 'De primeira. Leu minha mente!')

    #Senão, se o usuario apenas acertou
    elif num_user == num_bot:
        time.sleep(0.5)
        #Exibe a mensagem
        print(bot + 'Isso aí! Você acertou!')
        
    #Senão, se o usuario esgotou as tentativas
    elif tentativas >= 5:
        time.sleep(0.5)
        #Exibe a mensagem
        print('\n' + bot + 'Você esgotou o número de tentativas. Boa sorte na próxima!')
        time.sleep(0.5)
        print(bot + 'O número que eu estava pensando era o {}'.format(num_bot))

    time.sleep(1)
    #Bot agradece
    print('\n' + bot + 'Valeu por jogar comigo!')
    time.sleep(0.5)
    print(bot + 'O que quer fazer agora?')

    time.sleep(0.5)
    #Opções
    print('\n\t[{}1{}] Jogar novamente'.format(azul, limpa))
    print('\t[{}2{}] Sair'.format(vermelho, limpa))

    time.sleep(0.5)
    #Recebe a escolha do usuário
    escolha = str(input('\n\tDigite o número da opção desejada: ' + amarelo))

    #Enquanto a escolha for menor que 1 e maior que 2
    while escolha != '1' and escolha != '2':
        #Exibe o aviso
        print(vermelho + '\n\tINSIRA UM VALOR VÁLIDO!' + limpa)

        #Recebe a escolha do usuário
        escolha = str(input('\n\tDigite o número da opção desejada: ' + amarelo))


    #Se for jogar novamente
    if escolha == '1':
        #Chama a mesma função
        jogo()
    
    #Senão, se a escolha for sair
    elif escolha == '2':
        #Se despede e sai
        time.sleep(0.5)
        print('\n' + bot + 'Que pena que precisa sair')
        time.sleep(0.5)
        print(bot + 'Até mais {}!'.format(usuario.replace(': ', '').replace('\t', '').replace(azul, '')))
        time.sleep(3)
        os._exit(0)

#Inicia o jogo
jogo()