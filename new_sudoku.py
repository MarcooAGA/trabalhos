#MARCO ANTONIO GOTTARDI ANESI INFO 302
#AV2 - DEPENDENCIA DESENVOLVIMENTO DE PROJETO I
#JOGO - NEW SUDOKU
#É NECESSÁRIO TER PYGAME INSTALADO PARA RODAR O CÓDIGO
#DEIXEI CADA PARTE DO CÓDIGO COMENTADA PARA MELHOR INTERPRETAÇÃO DO CÓDIGO

#INSTRUÇÕES DO JOGO
#LETRA D RESETA O TABULEIRO
#LETRA R ESVAZIA TODAS AS CÉLULAS
#TECLA ENTER RESOLVE O TABULEIRO INTEIRO SOZINHO


import pygame
 

pygame.font.init()
 
# Tamanho da tela
screen = pygame.display.set_mode((500, 600))
 
# Titúlo do jogo
pygame.display.set_caption("NEW SUDOKU")

x = 0
y = 0
dif = 500 / 9
val = 0
# Tabuleiro padrão de sudoku
grid =[
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]
 
font1 = pygame.font.SysFont("comicsans", 20)
font2 = pygame.font.SysFont("comicsans", 15)
def get_cord(pos):
    global x
    x = pos[0]//dif
    global y
    y = pos[1]//dif
 

# Destaque a célula selecionada
def draw_box():
    for i in range(2):
        pygame.draw.line(screen, (255, 0, 0), (x * dif-3, (y + i)*dif), (x * dif + dif + 3, (y + i)*dif), 7)
        pygame.draw.line(screen, (255, 0, 0), ( (x + i)* dif, y * dif ), ((x + i) * dif, y * dif + dif), 7)  
 
     
def draw():

    # Desenha as linhas
        
    for i in range (9):
        for j in range (9):
            if grid[i][j]!= 0:
 
                # Preencha a cor azul na grade já numerada
                pygame.draw.rect(screen, (0, 153, 153), (i * dif, j * dif, dif + 1, dif + 1))
 
                # Preencher a grade com os números padrão especificados
                text1 = font1.render(str(grid[i][j]), 1, (0, 0, 0))
                screen.blit(text1, (i * dif + 15, j * dif + 15))
    
    # Desenha linhas horizontalmente e verticalmente para formar a grade        
    for i in range(10):
        if i % 3 == 0 :
            thick = 7
        else:
            thick = 1
        pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), thick)
        pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)     
 

# Preencha o valor inserido na célula  
def draw_val(val):
    text1 = font1.render(str(val), 1, (0, 0, 0))
    screen.blit(text1, (x * dif + 15, y * dif + 15))   
 

# Indicar quando um valor incorreto for inserido
def mostra_erro1():
    text1 = font1.render("Errado!", 1, (0, 0, 0))
    screen.blit(text1, (20, 570)) 
def mostra_erro2():
    text1 = font1.render("Errado! Não é uma tecla válida.", 1, (0, 0, 0))
    screen.blit(text1, (20, 570)) 
 

# Verifica se o valor inserido no tabuleiro é válido
def valido(m, i, j, val):
    for it in range(9):
        if m[i][it]== val:
            return False
        if m[it][j]== val:
            return False
    it = i//3
    jt = j//3
    for i in range(it * 3, it * 3 + 3):
        for j in range (jt * 3, jt * 3 + 3):
            if m[i][j]== val:
                return False
    return True
 
# Resolve o tabuleiro do sudoku usando um algorítmo de backtracking
def resolve(grid, i, j):
     
    while grid[i][j]!= 0:
        if i<8:
            i+= 1
        elif i == 8 and j<8:
            i = 0
            j+= 1
        elif i == 8 and j == 8:
            return True
    pygame.event.pump()   
    for it in range(1, 10):
        if valido(grid, i, j, it)== True:
            grid[i][j]= it
            global x, y
            x = i
            y = j
           
# fundo de cor branca \
            screen.fill((255, 255, 255))
            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(20)
            if resolve(grid, i, j)== 1:
                return True
            else:
                grid[i][j]= 0
           
# fundo de cor branca \
            screen.fill((255, 255, 255))
         
            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(50)   
    return False 
 

# Exibir instruções para o jogo
def instrucoes():
    text1 = font2.render("PRESSIONE D P/ RESETAR OU R P/ ESVAZIAR TUDO", 1, (0, 0, 0))
    text2 = font2.render("PRESSIONE ENTER PARA RESOLVER AUTOMATICAMENTE", 1, (0, 0, 0))
    screen.blit(text1, (20, 520))       
    screen.blit(text2, (20, 540))
 

# Exibir opções quando resolvido
def resultado():
    text1 = font1.render("FIM! PRESSIONE D OU R", 1, (0, 0, 0))
    screen.blit(text1, (20, 570))   
run = True
flag1 = 0
flag2 = 0
rs = 0
erro = 0

# O loop que mantém a janela em execução
while run:
     
    
# Fundo de cor branca
    screen.fill((255, 255, 255))
    # Percorre os eventos armazenados em event.get ()
    for event in pygame.event.get():

        # Sai da janela do jogo
        if event.type == pygame.QUIT:
            run = False 
        
# Coloque o mouse na posição para inserir o número
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag1 = 1
            pos = pygame.mouse.get_pos()
            get_cord(pos)

        # Obtenha o número a ser inserido se a tecla for pressionada
           
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x-= 1
                flag1 = 1
            if event.key == pygame.K_RIGHT:
                x+= 1
                flag1 = 1
            if event.key == pygame.K_UP:
                y-= 1
                flag1 = 1
            if event.key == pygame.K_DOWN:
                y+= 1
                flag1 = 1   
            if event.key == pygame.K_1:
                val = 1
            if event.key == pygame.K_2:
                val = 2   
            if event.key == pygame.K_3:
                val = 3
            if event.key == pygame.K_4:
                val = 4
            if event.key == pygame.K_5:
                val = 5
            if event.key == pygame.K_6:
                val = 6
            if event.key == pygame.K_7:
                val = 7
            if event.key == pygame.K_8:
                val = 8
            if event.key == pygame.K_9:
                val = 9 
            if event.key == pygame.K_RETURN:
                flag2 = 1  

            # SE PRESSIONAR R, TODAS AS CELULAS SE ESVAZIARÃO

            if event.key == pygame.K_r:
                rs = 0
                erro = 0
                flag2 = 0
                grid =[
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]
                ]
            # SE PRESSIONAR D, O TABULEIRO VOLTA AO "NORMAL""
            if event.key == pygame.K_d:
                rs = 0
                erro = 0
                flag2 = 0
                grid =[
                    [7, 8, 0, 4, 0, 0, 1, 2, 0],
                    [6, 0, 0, 0, 7, 5, 0, 0, 9],
                    [0, 0, 0, 6, 0, 1, 0, 7, 8],
                    [0, 0, 7, 0, 4, 0, 2, 6, 0],
                    [0, 0, 1, 0, 5, 0, 9, 3, 0],
                    [9, 0, 4, 0, 6, 0, 0, 0, 5],
                    [0, 7, 0, 3, 0, 0, 0, 1, 2],
                    [1, 2, 0, 0, 0, 7, 4, 0, 0],
                    [0, 4, 9, 2, 0, 6, 0, 0, 7]
                ]
    if flag2 == 1:
        if resolve(grid, 0, 0)== False:
            erro = 1
        else:
            rs = 1
        flag2 = 0   
    if val != 0:           
        draw_val(val)
        # print(x)
        # print(y)
        if valido(grid, int(x), int(y), val)== True:
            grid[int(x)][int(y)]= val
            flag1 = 0
        else:
            grid[int(x)][int(y)]= 0
            mostra_erro2()  
        val = 0   
       
    if erro == 1:
        mostra_erro1() 
    if rs == 1:
        resultado()       
    draw() 
    if flag1 == 1:
        draw_box()      
    instrucoes()   
 
    pygame.display.update() 
 
# Sair do jogo.
pygame.quit()    
