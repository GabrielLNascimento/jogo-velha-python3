import os
import random # cpu joga

jogarnovamente = 's'
jogadas = 0
quemJoga = 2 # 1 = CPU / 2 = jogador
maxjogada = 9
win = 'n'
velha = [
    [' ',' ',' '],  # 00, 01, 02
    [' ',' ',' '],  # 10, 11, 12
    [' ',' ',' ']   # 20, 21, 22
]

def tela(): # imprimir o layout da tela
    global velha
    global jogadas

    os.system('cls') or None

    print('    0   1   2')
    print('0:  ' + velha[0][0] + ' | ' + velha[0][1] + ' | ' + velha[0][2])   
    print('   -----------') 
    print('1:  ' + velha[1][0] + ' | ' + velha[1][1] + ' | ' + velha[1][2])  
    print('   -----------')
    print('2:  ' + velha[2][0] + ' | ' + velha[2][1] + ' | ' + velha[2][2]) 
    print('\n')
    print('Jogadas: ' + str(jogadas))

def jogadorJoga():
    global jogadas
    global quemJoga
    global win
    global maxjogada

    if(quemJoga == 2 and jogadas<maxjogada):    # verifica se é a vez do jogador
        try:
            l = int(input('Linha...: '))  # pede para escolher a linha  
            c = int(input('Coluna..: '))  # pede para escolher a coluna
            while velha[l][c] != ' ':   
            # enquanto as posição for diferente de espaço vazio (ou seja, se tem Letra)
                l = int(input('Linha...: '))    
                c = int(input('Coluna..: '))
            velha[l][c] = 'X' 
            # caso não tenha letra, adiciona o 'X'  

            # pega os valores da variavel 'l' e 'c' e coloca la nos seus lugares
            #exemplo => l = 0 / c = 1 => vai ser na linha 0 e coluna 1

            quemJoga = 1
            jogadas = jogadas + 1
        except:
            print('Linha ou coluna inválida')
            os.system('pause')
        
def CPUganha():
    global velha

    if velha[0][0] == velha[0][1] == 'O' and velha[0][2] == ' ':
        velha[0][2] = 'O'
        return True
    elif velha[0][1] == 'O' and velha[0][2] == 'O' and velha[0][0] == ' ':
        velha[0][0] = 'O'
        return True
    elif velha[0][0] == 'O' and velha[0][2] == 'O' and velha[0][1] == ' ':
        velha[0][1] = 'O'
        return True
    elif velha[1][0] == velha[1][1] == 'O' and velha[1][2] == ' ':
        velha[1][2] = 'O'
        return True
    elif velha[1][1] == 'O' and velha[1][2] == 'O' and velha[1][0] == ' ':
        velha[1][0] = 'O'
        return True
    elif velha[1][0] == 'O' and velha[1][2] == 'O' and velha[1][1] == ' ':
        velha[1][1] = 'O'
        return True
    elif velha[2][0] == velha[2][1] == 'O' and velha[2][2] == ' ':
        velha[2][2] = 'O'
        return True
    elif velha[2][1] == 'O' and velha[2][2] == 'O' and velha[2][0] == ' ':
        velha[2][0] = 'O'
        return True
    elif velha[2][0] == 'O' and velha[2][2] == 'O' and velha[2][1] == ' ':
        velha[2][1] = 'O'
        return True
    elif velha[0][0] == velha[1][0] == 'O' and velha[2][0] == ' ':
        velha[2][0] = 'O'
        return True
    elif velha[2][0] == velha[1][0] == 'O' and velha[0][0] == ' ':
        velha[0][0] = 'O'
        return True
    elif velha[2][0] == velha[0][0] == 'O' and velha[1][0] == ' ':
        velha[1][0] = 'O'
        return True
    elif velha[0][1] == velha[1][1] == 'O' and velha[2][1] == ' ':
        velha[2][1] = 'O'
        return True
    elif velha[2][1] == velha[1][1] == 'O' and velha[0][1] == ' ':
        velha[0][1] = 'O'
        return True
    elif velha[2][1] == velha[0][1] == 'O' and velha[1][1] == ' ':
        velha[1][1] = 'O'
        return True
    elif velha[0][2] == velha[1][2] == 'O' and velha[2][2] == ' ':
        velha[2][2] = 'O'
        return True
    elif velha[2][2] == velha[1][2] == 'O' and velha[0][2] == ' ':
        velha[0][2] = 'O'
        return True
    elif velha[2][2] == velha[0][2] == 'O' and velha[1][2] == ' ':
        velha[1][2] = 'O'
        return True
    elif velha[0][0] == velha[1][1] == 'O' and velha[2][2] == ' ':
        velha[2][2] = 'O'
        return True
    elif velha[0][0] == velha[2][2] == 'O' and velha[1][1] == ' ':
        velha[1][1] = 'O'
        return True
    elif velha[1][1] == velha[2][2] == 'O' and velha[0][0] == ' ':
        velha[0][0] = 'O'
        return True
    elif velha[0][2] == velha[1][1] == 'O' and velha[2][0] == ' ':
        velha[2][0] = 'O'
        return True
    elif velha[0][2] == velha[2][0] == 'O' and velha[1][1] == ' ':
        velha[1][1] = 'O'
        return True
    elif velha[1][1] == velha[2][0] == 'O' and velha[0][2] == ' ':
        velha[0][2] = 'O'
        return True
    
def verificaCPU():
    global velha

    if velha[0][0] == velha[0][1] == 'X' and velha[0][2] == ' ':
        velha[0][2] = 'O'
        return
    elif velha[0][1] == 'X' and velha[0][2] == 'X' and velha[0][0] == ' ':
        velha[0][0] = 'O'
        return
    elif velha[0][0] == 'X' and velha[0][2] == 'X' and velha[0][1] == ' ':
        velha[0][1] = 'O'
        return
    elif velha[1][0] == velha[1][1] == 'X' and velha[1][2] == ' ':
        velha[1][2] = 'O'
        return
    elif velha[1][1] == 'X' and velha[1][2] == 'X' and velha[1][0] == ' ':
        velha[1][0] = 'O'
        return
    elif velha[1][0] == 'X' and velha[1][2] == 'X' and velha[1][1] == ' ':
        velha[1][1] = 'O'
        return
    elif velha[2][0] == velha[2][1] == 'X' and velha[2][2] == ' ':
        velha[2][2] = 'O'
        return
    elif velha[2][1] == 'X' and velha[2][2] == 'X' and velha[2][0] == ' ':
        velha[2][0] = 'O'
        return
    elif velha[2][0] == 'X' and velha[2][2] == 'X' and velha[2][1] == ' ':
        velha[2][1] = 'O'
        return
    elif velha[0][0] == velha[1][0] == 'X' and velha[2][0] == ' ':
        velha[2][0] = 'O'
    elif velha[2][0] == velha[1][0] == 'X' and velha[0][0] == ' ':
        velha[0][0] = 'O'
    elif velha[2][0] == velha[0][0] == 'X' and velha[1][0] == ' ':
        velha[1][0] = 'O'
    elif velha[0][1] == velha[1][1] == 'X' and velha[2][1] == ' ':
        velha[2][1] = 'O'
    elif velha[2][1] == velha[1][1] == 'X' and velha[0][1] == ' ':
        velha[0][1] = 'O'
    elif velha[2][1] == velha[0][1] == 'X' and velha[1][1] == ' ':
        velha[1][1] = 'O'
    elif velha[0][2] == velha[1][2] == 'X' and velha[2][2] == ' ':
        velha[2][2] = 'O'
    elif velha[2][2] == velha[1][2] == 'X' and velha[0][2] == ' ':
        velha[0][2] = 'O'
    elif velha[2][2] == velha[0][2] == 'X' and velha[1][2] == ' ':
        velha[1][2] = 'O'
    elif velha[0][0] == velha[1][1] == 'X' and velha[2][2] == ' ':
        velha[2][2] = 'O'
        return
    elif velha[0][0] == velha[2][2] == 'X' and velha[1][1] == ' ':
        velha[1][1] = 'O'
        return
    elif velha[1][1] == velha[2][2] == 'X' and velha[0][0] == ' ':
        velha[0][0] = 'O'
        return
    elif velha[0][2] == velha[1][1] == 'X' and velha[2][0] == ' ':
        velha[2][0] = 'O'
        return
    elif velha[0][2] == velha[2][0] == 'X' and velha[1][1] == ' ':
        velha[1][1] = 'O'
        return
    elif velha[1][1] == velha[2][0] == 'X' and velha[0][2] == ' ':
        velha[0][2] = 'O'
        return

    # Se não houver oportunidade de bloquear ou ganhar, escolha uma posição aleatória
    else:
        l = random.randrange(0, 3)
        c = random.randrange(0, 3)
        while velha[l][c] != ' ':
            l = random.randrange(0, 3)
            c = random.randrange(0, 3)
        velha[l][c] = 'O'
        

def CPUjoga():
    global jogadas
    global quemJoga
    global win
    global maxjogada 
       
    if jogadas == 1:
        l = random.randrange(0, 3)
        c = random.randrange(0, 3)
        while velha[l][c] != ' ':
            l = random.randrange(0, 3)
            c = random.randrange(0, 3)
        velha[l][c] = 'O'
        quemJoga = 2
        jogadas += 1
    elif quemJoga == 1 and jogadas == 3:  # Adicionamos essa condição para garantir que a CPU jogue apenas uma vez após a jogada do jogador
        if CPUganha():
            quemJoga = 2
            jogadas += 1
            return
        verificaCPU()

        quemJoga = 2
        jogadas += 1
    elif quemJoga == 1 and jogadas == 5:  
        if CPUganha():
            quemJoga = 2
            jogadas += 1
            return
        verificaCPU()

        quemJoga = 2
        jogadas += 1
    elif quemJoga == 1 and jogadas == 7:  
        if CPUganha():
            quemJoga = 2
            jogadas += 1
            return
        verificaCPU()

        quemJoga = 2
        jogadas += 1
    elif quemJoga == 1 and jogadas == 9:  
        if CPUganha():
            quemJoga = 2
            jogadas += 1
            return
        verificaCPU()

        quemJoga = 2
        jogadas += 1
    

    # Verifica se há duas casas ocupadas por 'X' e coloca 'O' na casa restante na linha il

def verificarVitoria():
    global velha
    vitoria = 'n'
    simbolos = ['X','O']
    for s in simbolos:
        vitoria = 'n'


        #verificar em linhas
        il = ic = 0 # indice da linha e da coluna
        while il < 3: # enquanto indice da linha for menor do que 3
            soma = 0  
            ic = 0
            while ic < 3:   # enquanto indice da coluna menor do que 3
                if(velha[il][ic] == s): # se na posição il e ic tiver um simbolo
                    soma = soma + 1 # add 1 na soma
                ic+=1 #adiciona 1 indice de coluna a mais
            il+=1 # dps de passar por todos os indices de coluna, ele incrementa +1 na linha
            if (soma == 3): # a soma da 3 quando as letras 'x' ou 'o' estão nas 3 posições
                vitoria = s # vitoria vai ser igual a 'X' ou 'O'
                break
        if(vitoria !='n'):
            break   # para o loop inteiro


        #verificar colunas
        il = ic = 0
        while ic < 3: # enquanto indice da coluna for menor do que 3
            soma = 0
            il = 0 
            while il < 3: # enquanto indice da linha menor do que 3
                if(velha[il][ic] == s): # se na posição il e ic tiver um simbolo
                    soma = soma + 1 # add 1 na soma
                il+=1 #adiciona 1 indice de linha a mais
            if (soma == 3): # a soma da 3 quando as letras 'x' ou 'o' estão nas 3 posições
                vitoria = s # vitoria vai ser igual a 'X' ou 'O'
                break
            ic+=1 # add +1 no indice da coluna, enquanto ser menor do que 3
        if(vitoria !='n'): 
            break # para o loop inteiro
        

        # verificar diagonal 1
        soma = 0
        idiag = 0   ##indice é o mesmo para ambos os lados
        while idiag < 3: # enquanto meu indice for menor do que 3
            if(velha[idiag][idiag] == s): # se tiver letra na posição do valor do indice
                soma += 1   #adiciona +1 na soma
            idiag += 1 # dando true ou falso acima, add +1 no indice
        if (soma == 3):
                vitoria = s
                break
        
        #verificar diagonal 2
        soma = 0
        idiagl = 0
        idiagc = 2

        while idiagl < 3:  # Corrigido o critério de parada do loop
            if 0 <= idiagc < 3:  # Verificar se o índice da coluna está dentro dos limites
                if (velha[idiagl][idiagc] == s): #0 e #2 => tiver uma letra
                    soma += 1   # add +1 na soma
            idiagl += 1 # aumentando o inidice da linha
            idiagc -= 1 # diminuindo o indice da coluna
        if(soma==3):
            vitoria = s
            break
    return vitoria

def redefenir():
    global velha
    global jogadas
    global quemJoga
    global maxjogada
    global win
    jogadas = 0 
    quemJoga = 2 # 1 = CPU / 2 = jogador
    maxjogada = 9
    win = 'n'
    velha = [
        [' ',' ',' '],
        [' ',' ',' '],
        [' ',' ',' ']
    ]



while(jogarnovamente == 's'):
    while True:
        tela()
        jogadorJoga()
        CPUjoga()
        tela()
        vit = verificarVitoria()
        if(vit != 'n' or jogadas == maxjogada or jogadas == 8):
            break

    print('FIM de jogo!')
    if (vit == 'X' or vit == 'O'):
        print('Resultado: Jogador ' + vit + ' venceu!')
    else:
        print('RESULTADO: Empate!')
    jogarnovamente = input('Quer jogar novamente? [s/n]: ')
    redefenir()
