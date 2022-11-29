import pandas
import tkinter
import Rooms
import Object1_chair_sofa
import pygame
import random
import sys
from color import *

i = 0
pygame.init()

surface = pygame.display.set_mode((1400,900))

running = True

red = (255,0,0)
blue = (240,248,255)
black = (0,0,0)
background = (235,255,255)
white = (255,255,255)
yellow = (255,255,0)
green = (0,255,0)

wall_img = [1,1,1,1,1,1,1,1]
wall_img[0] = pygame.image.load('Dinding\L.png')
wall_img[1] = pygame.image.load('Dinding\LD.png')
wall_img[2] = pygame.image.load('Dinding\LU.png')
wall_img[3] = pygame.image.load('Dinding\MD.png')
wall_img[4] = pygame.image.load('Dinding\MU.png')
wall_img[5] = pygame.image.load('Dinding\R.png')
wall_img[6] = pygame.image.load('Dinding\RU.png')
wall_img[7] = pygame.image.load('Dinding\RD.png')

# while i < 1 :
#         try:
#             print("1 tile = 50cm")
#             print("Input Lenght: ")
#             size_Y = eval(input())

#             print("Input Height: ")
#             size_X = eval(input())
#             i = 1

#             if (size_X < 10 or size_Y < 10):
#                 print("Enter at least 3")
#                 i = 0

#             if (size_X > 20 or size_Y > 20):
#                 print("Too much bro")
#                 i = 0

#             if (size_X == 999 or size_Y == 999):
#                 running = False
#                 pygame.quit()

#         except:
#             print("Masukkin angka dek")

size_Y = 15
size_X = 15

room_1 = Rooms.Room(size_X,size_Y)

room_1.maps = room_1.make_map(room_1.size_X,room_1.size_Y)

room_1.maps = room_1.give_random_door(room_1.size_X,room_1.size_Y,room_1.maps)

map = room_1.maps

kasur = room_1.beds
chair = room_1.sofas
table = room_1.table
lemari = room_1.lemari

count_bed = 0
count_chair = 0
count_table = 0
count_lemari = 0

draw_max = 0

def clear_map():
        for z in range (size_X) :
            for h in range (size_Y):
                if (map[z][h] != 8 
                and map[z][h] != 1) :
                    map[z][h] = 0
                
                if(map[z][h] == 1):
                    map[z][h] = 8

def give_beds():
    if(room_1.check_space(room_1.size_Y,room_1.size_X,kasur.min_x,kasur.min_y)):
        room_1.give_furniture(kasur._length_x,kasur._length_y,kasur.code)
        kasur.random_length((room_1.size_X//2),(room_1.size_Y//2)) 
        return True

def give_chair():
    if(room_1.check_space(room_1.size_Y,room_1.size_X,chair.min_x,chair.min_y)):
        room_1.give_furniture(chair._length_x,chair._length_y,chair.code)
        chair.random_length((room_1.size_X//2),(room_1.size_Y//2))
        return True

def give_table():
    if(room_1.check_space(room_1.size_Y,room_1.size_X,table.min_x,table.min_y)):
        room_1.give_furniture(table._length_x,table._length_y,table.code)
        table.random_length((room_1.size_X//2),(room_1.size_Y//2))
        return True

def give_lemari():
    if(room_1.check_space(room_1.size_Y,room_1.size_X,lemari.min_x,lemari.min_y)):
        room_1.give_furniture(lemari._length_x,lemari._length_y,lemari.code)
        lemari.random_length((room_1.size_X//2),(room_1.size_Y//2))
        return True

def randomnize(draw_max,count_bed,count_chair,count_table,count_lemari):
    clear_map()
    room_1.maps = room_1.give_random_door(room_1.size_X,room_1.size_Y,room_1.maps)

    random_chair = random.randint(1,3)
    random_table = random.randint(1,2)
    random_lemari = random.randint(1,2)

    while(draw_max < 4):
        if count_bed < 1 :
            if give_beds():
                count_bed += 1

        if count_chair < random_chair :
            give_chair()
            count_chair += 1

        if count_table < random_table:
            give_table()
            count_table +=1

        if count_lemari < random_lemari:
            give_lemari()
            count_lemari +=1
        
        draw_max +=1
    print("(3) =",count_bed,"(2) =",count_chair,"(4) =",count_table,"(5) =",count_lemari )
    count_bed = 0
    count_chair = 0
    count_table = 0
    count_lemari = 0

    draw_max = 0
    return count_bed,count_lemari,count_chair,count_table

count_bed,count_lemari,count_chair,count_table = randomnize(draw_max,count_bed,count_chair,count_table,count_lemari)

i = 0

x_block = (1400/2-(15*35)/2)
y_block = 200
tile_size = 35
def drawgame():
    
    for z in range (0,size_X) :
        for h in range (0,size_Y):
            if map[z][h] == 8 :

                if z == 0 and h == 0 :
                    surface.blit(wall_img[2], (x_block + h*tile_size , y_block  + z*tile_size ))
                elif z == 0 and h == size_Y -1 :
                    surface.blit(wall_img[6], (x_block + h*tile_size , y_block + z*tile_size ))
                elif z == size_X -1 and h == size_Y -1:
                    surface.blit(wall_img[7], (x_block + h*tile_size , y_block + z*tile_size ))
                elif z == size_X -1 and h == 0:
                    surface.blit(wall_img[1], (x_block + h*tile_size , y_block + z*tile_size ))
                elif z == 0 and 0 < h < size_Y - 1:
                    surface.blit(wall_img[4], (x_block + h*tile_size , y_block + z*tile_size ))
                elif z == size_X - 1 and 0 < h < size_Y - 1:
                    surface.blit(wall_img[3], (x_block + h*tile_size , y_block + z*tile_size ))
                elif 0 < z < size_X - 1 and h == 0:
                    surface.blit(wall_img[0], (x_block + h*tile_size , y_block + z*tile_size ))
                elif 0 < z < size_X - 1 and h == size_Y - 1:
                    surface.blit(wall_img[5], (x_block + h*tile_size , y_block + z*tile_size ))

            if map[z][h] == 1 :
                pygame.draw.rect(surface, green, pygame.Rect(x_block + h*tile_size, y_block + z*tile_size,tile_size,tile_size))
            if map[z][h] == 2 :
                pygame.draw.rect(surface, red, pygame.Rect(x_block + h*tile_size, y_block + z*tile_size,tile_size,tile_size))
            if map[z][h] == 3 :
                pygame.draw.rect(surface, white, pygame.Rect(x_block + h*tile_size, y_block + z*tile_size,tile_size,tile_size))
            if map[z][h] == 4 :
                pygame.draw.rect(surface, blue, pygame.Rect(x_block + h*tile_size, y_block + z*tile_size,tile_size,tile_size))
            if map[z][h] == 5 :
                pygame.draw.rect(surface, yellow, pygame.Rect(x_block + h*tile_size, y_block + z*tile_size, tile_size, tile_size))

width = surface.get_width()
height = surface.get_height()

smallfont = pygame.font.SysFont('Corbel',25)
text = smallfont.render('Randomnizer' , True , black)

color = (255,255,255)
  
# light shade of the button
color_light = (170,170,170)
  
# dark shade of the button
color_dark = (100,100,100)

tools_clicked = "a"
while running:
    click_now = True
    button_width = 200
    button_height = 400  
    
    # 1400-(15*35))/2 
    # 200

    #TOOLS
    bed_button_w = 50
    bed_button_y = 50  

    chair_button_w = 100
    chair_button_y = 50

    surface.fill(background)
    pygame.draw.rect(surface, white, pygame.Rect(bed_button_w + 20,bed_button_y, 50, 50))

    Mouse_x, Mouse_y = pygame.mouse.get_pos()
    #TOOLS
    # print(Mouse_x - (1400-(15*35))/2, Mouse_y - 200)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if button_width <= mouse[0] <= button_width+140 and button_height <= mouse[1] <= button_height+40:
                randomnize(draw_max,count_bed,count_chair,count_table,count_lemari)
            
            if bed_button_w <= mouse[0] <= bed_button_w + 50 and bed_button_y <= mouse[1] <= bed_button_y + 50 and tools_clicked != "BED":
                tools_clicked = "BED"
                click_now = False
            
            if bed_button_w <= mouse[0] <= bed_button_w + 50 and bed_button_y <= mouse[1] <= bed_button_y + 50 and tools_clicked == "BED" and click_now:
                tools_clicked = "a"
            
            if x_block <= mouse[0] <= x_block + 35*15 and y_block <= mouse[1] <= y_block + tile_size*15 and tools_clicked == "BED":
                map[int((Mouse_y - y_block)//35)][int((Mouse_x - x_block)//35)] = 3

    if tools_clicked == "BED" :
    
        print("aa")

    mouse = pygame.mouse.get_pos()

    if button_width <= mouse[0] <= button_width+140 and button_height <= mouse[1] <= button_height+40:  #hover
        pygame.draw.rect(surface,color_light,[button_width,button_height,140,40])
    else:
        pygame.draw.rect(surface,color_dark,[button_width,button_height,140,40])
      
    # superimposing the text onto our button
    surface.blit(text , (button_width+3,button_height+7))
      
    # updates the frames of the game
    drawgame()

    pygame.display.flip()
   

pygame.quit()


#enter lenght menjadi size y 
#enter height menjadi size x
#total work_hours = 7+3+8+2+1+4+8 :D