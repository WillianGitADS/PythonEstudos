from random import randrange
import time

def display_board(a,b,c,d,e,f,g,h,i):
    print("**********************************************\n")
    print("+-------+-------+-------+")
    print("\n|       |       |       |")
    print("\n|  ",a,"  |  ",b,"  |  ",c,"  |")
    print("\n|       |       |       |")
    print("\n+-------+-------+-------+")
    print("\n|       |       |       |")
    print("\n|  ",d,"  |  ",e,"  |  ",f,"  |")
    print("\n|       |       |       |")
    print("\n+-------+-------+-------+")
    print("\n|       |       |       |")
    print("\n|  ",g,"  |  ",h,"  |  ",i,"  |")
    print("\n|       |       |       |")
    print("\n+-------+-------+-------+\n")
    print("**********************************************")
    
    return

def enter_move():
    while True:
        posicao_play = int(input("Player: "))
        if posicao_play > 0 and posicao_play < 10:
            if posicao_play not in list_escolha:
                list_escolha.append(posicao_play)
                list_atualiza[posicao_play - 1] = '0'
                return "Jogador"
            else:
                print("Valor já foi escolhido!!!")
        else:
            print("Valor dever ser entre 1 e 9!!!")

def draw_move():
    for elem in list_possibilidade:
        z = 1 + randrange(len(list_possibilidade))
        #print("Posicao Escolhida pelo PC: ", z)
        if z not in list_escolha:
            list_atualiza[z - 1] = 'X'
            list_escolha.append(z)
            print("Computador:", z)
            return "Computador" 

def vitoria(play):
    print("************** Vitória do", play, "***********")
    return False

def victory_for(a,b,c,d,e,f,g,h,i,play):
    if play == "Jogador":
        k = "0"
    else:
        k = "X"
    if (a == k  and b == k and c == k ):
        return vitoria(play)
    if (d == k and e == k and f == k):
        return vitoria(play)
    if (g == k and h == k and i == k):
       return vitoria(play)
    if (a == k and d == k and g == k):
        return vitoria(play)
    if (b == k and e == k and h == k):
       return vitoria(play)
    if (c == k and f == k and i == k):
        return vitoria(play)
    if (a == k and e == k and i == k):
        return vitoria(play)
    if (c == k and e == k and g == k):
        return vitoria(play)
    else:
        return True

def atualiza_quadro():
    a = list_atualiza[0]
    b = list_atualiza[1]
    c = list_atualiza[2]
    d = list_atualiza[3]
    e = list_atualiza[4]
    f = list_atualiza[5]
    g = list_atualiza[6]
    h = list_atualiza[7]
    i = list_atualiza[8]
    
    display_board(a,b,c,d,e,f,g,h,i)
    status = victory_for(a,b,c,d,e,f,g,h,i, play)
    return status
    
list_escolha = []
list_possibilidade = [ 1, 2, 3, 4, 6, 7, 8, 9, 0]
list_atualiza = [ 1, 2, 3, 4, 5, 6, 7, 8, 9]
status = True

a = list_atualiza[0]
b = list_atualiza[1]
c = list_atualiza[2]
d = list_atualiza[3]
e = list_atualiza[4]
f = list_atualiza[5]
g = list_atualiza[6]
h = list_atualiza[7]
i = list_atualiza[8]

display_board(1,2,3,4,5,6,7,8,9)
while (len(list_escolha) < 9 and status == True):
    
    if status:
        play = enter_move()

        status = atualiza_quadro()

       #print(list_atualiza)
       #
       # if status == False:
       #    atualiza_quadro()
       #    break
       #     
    if status:
        play = draw_move()
        '''
        #print(list_atualiza)
        status = victory_for(a,b,c,d,e,f,g,h,i, play)
'''
        status = atualiza_quadro()
        if status == False:
            break
    else:
        break
if status == True:
    print("****************Empate!!!*********************")
    print("***************Fim de Jogo********************")
else:
    print("***************Fim de Jogo********************")

    

