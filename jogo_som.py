# Example file showing a circle moving on screen
import pygame
import math as mt
from matplotlib import image
import matplotlib
from PIL import ImageColor

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1200, 650))
clock = pygame.time.Clock()
running = True
dt = 0

direcao = "00"

objetivos = [(268,130),(131,275),(344,382)]

mar = [(128, 255, 255),(245,137,142), (136, 0, 21), (153, 217, 234)]

terreno = 0



data_mapa = image.imread("design/exemplo.png")

velo = 2
raiz_meio = mt.sqrt((velo**2)/2)


y_acelerar = 0
x_acelerar = 0

rotacao = 0

turbo = 1

def convert_rgba4hex(x):
    
    hex = (matplotlib.colors.to_hex(x))
    rgb = ImageColor.getcolor(hex, "RGB")
    return(rgb)

def rotacinar_barco(x,y,rot):
    if x < 0:


        if y > 0:
            return(270+45)
        elif y < 0:
            return(270-45)
        else:
            return(270)
    elif x > 0:
        if y > 0:
            return(45)
        elif y < 0:
            return(90+45)
        else:
            return(90)
    else:
        if y > 0:
            return(0)
        elif y < 0:
            return(180)
        else:
            return(rot)
        
#fundo = pygame.image.load('PLN/mapa_navegavel.png')
fundo = pygame.image.load('design/mapa_navegavel_2.png')
barco = pygame.image.load('design/barco.png')
obj = pygame.image.load('design/tiles/chao.png')
pessoa = pygame.image.load('design/gemeos.png')
barco2 = barco
imagem_original = barco




#player_pos = pygame.Vector2(- 10 - 260 * 10,- 10 - 12 * 10)
player_pos = pygame.Vector2(- 10 - 270 * 20,- 10 - 14 * 20)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False
            
        if (event.type == pygame.KEYDOWN):

            keys = pygame.key.get_pressed()

            if keys[pygame.K_w]:
                if direcao[0] == "0":
                    if direcao[1] == "S":
                        y_acelerar = 0
                        direcao = "00"
                    elif direcao[1] == "0":
                        y_acelerar = velo
                        direcao = "0N"
                    elif direcao[1] == "L":
                        y_acelerar = raiz_meio
                        x_acelerar = -raiz_meio
                        direcao = "NL"
                    elif direcao[1] == "O":
                        y_acelerar = raiz_meio
                        x_acelerar = raiz_meio
                        direcao = "NO"
                    else:
                        y_acelerar = velo


                elif direcao[0] == "S":
                    if direcao[1] == "L":
                        y_acelerar = 0
                        direcao = "0L"
                    elif direcao[1] == "O":
                        y_acelerar = 0
                        direcao = "0O"


                else:
                    y_acelerar = velo
                    x_acelerar = 0
                    direcao = "0N"


            if keys[pygame.K_s]:
                if direcao[0] == "0":
                    if direcao[1] == "N":
                        y_acelerar = 0
                        direcao = "00"
                    elif direcao[1] == "0":
                        y_acelerar = -velo
                        direcao = "0S"
                    elif direcao[1] == "L":
                        y_acelerar = -raiz_meio
                        x_acelerar = -raiz_meio
                        direcao = "SL"
                    elif direcao[1] == "O":
                        y_acelerar = -raiz_meio
                        x_acelerar = raiz_meio
                        direcao = "SO"
                    else:
                        y_acelerar = -velo


                elif direcao[0] == "N":
                    if direcao[1] == "L":
                        y_acelerar = 0
                        direcao = "0L"
                    elif direcao[1] == "O":
                        y_acelerar = 0
                        direcao = "0O"


                else:
                    y_acelerar = -velo
                    x_acelerar = 0
                    direcao = "0S"

            if keys[pygame.K_a]:
                if direcao[0] == "0":
                    if direcao[1] == "L":
                        x_acelerar = 0
                        direcao = "00"
                    elif direcao[1] == "0":
                        x_acelerar = velo
                        direcao = "0O"
                    elif direcao[1] == "S":
                        x_acelerar = raiz_meio
                        y_acelerar = -raiz_meio
                        direcao = "SO"
                    elif direcao[1] == "N":
                        x_acelerar = raiz_meio
                        y_acelerar = raiz_meio
                        direcao = "NO"
                    else:
                        x_acelerar = velo


                elif direcao[1] == "L":
                    if direcao[0] == "N":
                        x_acelerar = 0
                        direcao = "0N"
                    elif direcao[0] == "S":
                        x_acelerar = 0
                        direcao = "0S"


                else:
                    x_acelerar = velo
                    y_acelerar = 0
                    direcao = "0O"

                

            if keys[pygame.K_d]:
                if direcao[0] == "0":
                    if direcao[1] == "O":
                        x_acelerar = 0
                        direcao = "00"
                    elif direcao[1] == "0":
                        x_acelerar = -velo
                        direcao = "0L"
                    elif direcao[1] == "S":
                        x_acelerar = -raiz_meio
                        y_acelerar = -raiz_meio
                        direcao = "SL"
                    elif direcao[1] == "N":
                        x_acelerar = -raiz_meio
                        y_acelerar = raiz_meio
                        direcao = "NL"
                    else:
                        x_acelerar = -velo


                elif direcao[1] == "O":
                    if direcao[0] == "N":
                        x_acelerar = 0
                        direcao = "0N"
                    elif direcao[0] == "S":
                        x_acelerar = 0
                        direcao = "0S"

                        
                else:
                    x_acelerar = -velo
                    y_acelerar = 0
                    direcao = "0L"

            if keys[pygame.K_t]:
                turbo = 2
            if keys[pygame.K_p]:
                x_acelerar = 0
                y_acelerar = 0
                turbo = 1

            rotacao = rotacinar_barco(x_acelerar,y_acelerar,rotacao)
            barco2 = pygame.transform.rotate(imagem_original,rotacao)
            


    # fill the screen with a color to wipe away anything from last frame
    screen.fill("blue")

    #print(y_acelerar,x_acelerar)
    #print(int(((player_pos.y+5)//-20)),int((player_pos.x//-20)))

    if terreno == 0:

        if convert_rgba4hex(data_mapa[int(((player_pos.y+5)//-20)),int((player_pos.x//-20))]) not in mar:
            #print("norte")
            if y_acelerar > 0:
                y_acelerar = 0
                turbo = 1
        
        if convert_rgba4hex(data_mapa[int(((player_pos.y-20)//-20)),int((player_pos.x//-20))]) not in mar:
            #print("sul")
            if y_acelerar < 0:
                y_acelerar = 0
                turbo = 1

        if convert_rgba4hex(data_mapa[int((player_pos.y//-20)),int(((player_pos.x+5)//-20))]) not in mar:
            #print("oeste")
            if x_acelerar > 0:
                x_acelerar = 0
                turbo = 1
        
        if convert_rgba4hex(data_mapa[int((player_pos.y//-20)),int(((player_pos.x-20)//-20))]) not in mar:
            #print("leste")
            if x_acelerar < 0:
                x_acelerar = 0
                turbo = 1


    else:
        if convert_rgba4hex(data_mapa[int(((player_pos.y+5)//-20)),int((player_pos.x//-20))])  in mar:
            #print("norte")
            if y_acelerar > 0:
                y_acelerar = 0
                turbo = 1
        
        if convert_rgba4hex(data_mapa[int(((player_pos.y-20)//-20)),int((player_pos.x//-20))])  in mar:
            #print("sul")
            if y_acelerar < 0:
                y_acelerar = 0
                turbo = 1

        if convert_rgba4hex(data_mapa[int((player_pos.y//-20)),int(((player_pos.x+5)//-20))])  in mar:
            #print("oeste")
            if x_acelerar > 0:
                x_acelerar = 0
                turbo = 1
        
        if convert_rgba4hex(data_mapa[int((player_pos.y//-20)),int(((player_pos.x-20)//-20))])  in mar:
            #print("leste")
            if x_acelerar < 0:
                x_acelerar = 0
                turbo = 1




    """if convert_rgba4hex(data_mapa[int(((player_pos.y+5)//40)+1)*-4,int((player_pos.x//40)+1)*-4]) not in mar:
        #print("norte")
        if y_acelerar > 0:
            y_acelerar = 0
    
    if convert_rgba4hex(data_mapa[int(((player_pos.y-20)//40)+1)*-4,int((player_pos.x//40)+1)*-4]) not in mar:
        #print("sul")
        if y_acelerar < 0:
            y_acelerar = 0

    if convert_rgba4hex(data_mapa[int((player_pos.y//40)+1)*-4,int(((player_pos.x+5)//40)+1)*-4]) not in mar:
        #print("oeste")
        if x_acelerar > 0:
            x_acelerar = 0
    
    if convert_rgba4hex(data_mapa[int((player_pos.y//40)+1)*-4,int(((player_pos.x-20)//40)+1)*-4]) not in mar:
        #print("leste")
        if x_acelerar < 0:
            x_acelerar = 0"""

    
    screen.blit(fundo,(screen.get_width() / 2 + player_pos.x, screen.get_height() / 2 +player_pos.y))


    #print(int(((player_pos.y)//-20)),int((player_pos.x//-20)))

    if len(objetivos) > 0:

        objetivo_pos_x = screen.get_width() / 2 + player_pos.x+objetivos[0][0]*20 +10
        objetivo_pos_y = screen.get_height() / 2 + player_pos.y+objetivos[0][1]*20+10


        if (objetivo_pos_x > screen.get_width()):
            objetivo_pos_x = screen.get_width()
        elif (objetivo_pos_x < 0):
            objetivo_pos_x = 0
        
        
        if (objetivo_pos_y > screen.get_height()):
            objetivo_pos_y =screen.get_height()
        elif (objetivo_pos_y < 0):
            objetivo_pos_y = 0

        pygame.draw.circle(screen,"green",(objetivo_pos_x, objetivo_pos_y),10)

        pygame.draw.circle(screen,"white",(objetivo_pos_x, objetivo_pos_y),7,5)

        pygame.draw.circle(screen,"green",(objetivo_pos_x, objetivo_pos_y),5)

        if int(((player_pos.x)//-20))== objetivos[0][0]   and   int((player_pos.y//-20)) == objetivos[0][1]:
            print("entrou")
            objetivos.pop(0)
    else:
        terreno = 1
        player_pos.x -= 20
        objetivos = [(362,361),(362,421),(346,382)]
        x_acelerar = 0
        y_acelerar = 0
        imagem_original = pessoa





    
    

        
        


    player_pos.y += 80 * dt * y_acelerar * turbo

    player_pos.x += 80 * dt * x_acelerar  * turbo

    screen.blit(barco2,(screen.get_width() / 2 - 10, screen.get_height() / 2 - 10))






    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()






