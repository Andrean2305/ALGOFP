import pandas
import tkinter
import Rooms
import Object1_chair_sofa
import pygame
import random
import sys
from color import *

#Compare greedy dan __ : if you use a greedy algorithm, the results of searching for tile locations can collide with other tiles
#//downloaded from flashjunior.ch//

#COLOR####################################################################

red = (255,0,0)
blue = (240,248,255)
black = (0,0,0)
background = (235,255,255)
white = (255,255,255)
yellow = (255,255,0)
green = (0,255,0)

pastel_yellow = (255,223,186)
pastel_red = (255,179,186)
pastel_blues = (186,225,255)
pastel_green = (186,255,201)
pastel_blue = (149,184,209)
pastel_purple = (177,156,217)
pastel_cream = (254, 252, 243)
pastel_dark_cream = (245, 235, 224)
pastel_pink = (240, 219, 219)
pastel_dark_pink = (219, 163, 154)

######################COLOR#############################################
i = 0
pygame.init()

width = 1400
height = 900
surface = pygame.display.set_mode((width,height))

running = True

size_Y = 25
size_X = 27

total_tiles_x_and_y = 525

if size_X > size_Y :
    tile_size = total_tiles_x_and_y//size_X
else:
    tile_size = total_tiles_x_and_y//size_Y

tool_size = width/20 

x_block = (width/2-(size_Y*tile_size)/2)
y_block = height/4.5

wall_img = [1,1,1,1,1,1,1,1,1,1,1,1,1,1]

wall_img[0] = pygame.image.load('Dinding\L.png')
wall_img[1] = pygame.image.load('Dinding\LD.png')
wall_img[2] = pygame.image.load('Dinding\LU.png')
wall_img[3] = pygame.image.load('Dinding\MD.png')
wall_img[4] = pygame.image.load('Dinding\MU.png')
wall_img[5] = pygame.image.load('Dinding\R.png')
wall_img[6] = pygame.image.load('Dinding\RU.png')
wall_img[7] = pygame.image.load('Dinding\RD.png')
wall_img[8] = pygame.image.load('Dinding\FLOOR.png')
wall_img[9] = pygame.image.load('Dinding\DOOR_UP_1.png')
wall_img[10] = pygame.image.load('Dinding\DOOR_UP_2.png')
wall_img[11] = pygame.image.load('Dinding\DOOR_L.png')
wall_img[12] = pygame.image.load('Dinding\DOOR_R.png')
wall_img[13] = pygame.image.load('Dinding\DOOR_D.png')

clock = pygame.image.load('Dinding\CLOCK.png')
clock = pygame.transform.scale(clock, (tile_size,tile_size))

tool_box = pygame.image.load('Tools_Asset\Tools_box.png')
logo = pygame.image.load('Tools_Asset\LOGO.png')

choose = pygame.image.load('Tools_Asset\CHOOSE.png')
choose = pygame.transform.scale(choose, (tool_size,tool_size))


random_box = pygame.image.load('Tools_Asset\RANDOM_NOTIF.png')
random_now = False

for i in range (0,14):
    wall_img[i] = pygame.transform.scale(wall_img[i], (tile_size,tile_size))
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

def clear_map(size_X,size_Y):
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

def randomnize(draw_max,count_bed,count_chair,count_table,count_lemari,size_X,size_Y):
    clear_map(size_X,size_Y)
    room_1.maps = room_1.give_random_door(size_X,size_Y,room_1.maps)

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

count_bed,count_lemari,count_chair,count_table = randomnize(draw_max,count_bed,count_chair,count_table,count_lemari,size_X,size_Y)

i = 0
tool_map = [
    [1,2],
    [3,4],
    [5,6],
    [7,8],
    [9,10],
    [11,12]
]

selected_tool = [
    [0,0],
    [0,0],
    [0,0],
    [0,0],
    [0,0],
    [0,0]
]

def clear_select():
    for i in range (len(tool_map)):
        for j in range (2):
            selected_tool[i][j] = 0

bed_button_w = 50
bed_button_y = 50  

chair_button_w = 100
chair_button_y = 50

desk_button_w = 50
desk_button_y = 100

lemari_button_w = 100 
lemari_button_y = 100

def draw_tools():
    pygame.draw.rect(surface, pastel_red, pygame.Rect(0,0, width/7, height)) # TOOLS SIDE
    surface.blit(tool_box, (0 , 0))
    surface.blit(logo, (0 , 600))

    for i in range (len(tool_map)):
        for j in range (2):
            if tool_map[i][j] == 1 :
                bed_button_w = tool_size/2.4 + j*tool_size
                bed_button_y = 180 + i*tool_size
                pygame.draw.rect(surface, pastel_purple, pygame.Rect(bed_button_w ,bed_button_y, tool_size, tool_size))
            elif tool_map[i][j] == 2 :
                chair_button_w = tool_size/2.4 + j*tool_size
                chair_button_y = 180 + i*tool_size
                pygame.draw.rect(surface, pastel_green, pygame.Rect(chair_button_w ,chair_button_y, tool_size, tool_size))
            elif tool_map[i][j] == 3 :
                desk_button_w = tool_size/2.4 + j*tool_size
                desk_button_y = 180 + i*tool_size
                pygame.draw.rect(surface, pastel_blue, pygame.Rect(desk_button_w ,desk_button_y, tool_size, tool_size)) 
            elif tool_map[i][j] == 4 :
                lemari_button_w = tool_size/2.4 + j*tool_size
                lemari_button_y = 180 + i*tool_size
                pygame.draw.rect(surface, pastel_blues, pygame.Rect(lemari_button_w ,lemari_button_y, tool_size, tool_size))
            elif tool_map[i][j] == 5 :
                object5_w = tool_size/2.4 + j*tool_size
                object5_y = 180 + i*tool_size
                pygame.draw.rect(surface, pastel_purple, pygame.Rect(object5_w ,object5_y, tool_size, tool_size))
            elif tool_map[i][j] == 6 :
                object6_w = tool_size/2.4 + j*tool_size
                object6_y = 180 + i*tool_size
                pygame.draw.rect(surface, pastel_green, pygame.Rect(object6_w ,object6_y, tool_size, tool_size))
            elif tool_map[i][j] == 7 :
                object7_w = tool_size/2.4 + j*tool_size
                object7_y = 180 + i*tool_size
                pygame.draw.rect(surface, pastel_blue, pygame.Rect(object7_w ,object7_y, tool_size, tool_size)) 
            elif tool_map[i][j] == 8 :
                object8_w = tool_size/2.4 + j*tool_size
                object8_y = 180 + i*tool_size
                pygame.draw.rect(surface, pastel_blues, pygame.Rect(object8_w ,object8_y, tool_size, tool_size))
            elif tool_map[i][j] == 9 :
                object9_w = tool_size/2.4 + j*tool_size
                object9_y = 180 + i*tool_size
                pygame.draw.rect(surface, pastel_purple, pygame.Rect(object9_w ,object9_y, tool_size, tool_size))
            elif tool_map[i][j] == 10 :
                object10_w = tool_size/2.4 + j*tool_size
                object10_y = 180 + i*tool_size
                pygame.draw.rect(surface, pastel_green, pygame.Rect(object10_w ,object10_y, tool_size, tool_size))
            elif tool_map[i][j] == 11 :
                object11_w = tool_size/2.4 + j*tool_size
                object11_y = 180 + i*tool_size
                pygame.draw.rect(surface, pastel_blue, pygame.Rect(object11_w ,object11_y, tool_size, tool_size)) 
            elif tool_map[i][j] == 12 :
                object12_w = tool_size/2.4 + j*tool_size
                object12_y = 180 + i*tool_size
                pygame.draw.rect(surface, pastel_blues, pygame.Rect(object12_w ,object12_y, tool_size, tool_size))

            if selected_tool[i][j] == 1 :
                choosen_w = tool_size/2.4 + j*tool_size
                choosen_y = 180 + i*tool_size

                overlays = pygame.Surface((tool_size,tool_size))                  
                overlays.set_alpha(150)                
                overlays.fill((0,0,0))              
                surface.blit(overlays, (choosen_w , choosen_y))  
            ##DOWN FOR LINE/BOX
            
            pygame.draw.rect(surface, black, pygame.Rect(tool_size/2.4 + j*tool_size, 180 + tool_size*i,tool_size,tool_size),2) # TOOLS SIDE
    pygame.draw.rect(surface, black, pygame.Rect(tool_size/2.4,180,len(tool_map[0]) * tool_size,len(tool_map)* tool_size),4) # TOOLS SIDE

    return bed_button_w,bed_button_y,chair_button_w,chair_button_y,desk_button_w,desk_button_y,lemari_button_w,lemari_button_y

def find_clock():
    clock_now = random.randint(1,size_Y - 2)

    while map[0][clock_now] == 1:
        clock_now = random.randint(1,size_Y - 2)
    return clock_now

clock_now = find_clock()
def drawgame():
    door = 0
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

            if map[z][h] == 0 :
                surface.blit(wall_img[8], (x_block + h*tile_size , y_block + z*tile_size ))
            if map[z][h] == 2 :
                pygame.draw.rect(surface, red, pygame.Rect(x_block + h*tile_size, y_block + z*tile_size,tile_size,tile_size))
            if map[z][h] == 3 :
                pygame.draw.rect(surface, white, pygame.Rect(x_block + h*tile_size, y_block + z*tile_size,tile_size,tile_size))
            if map[z][h] == 4 :
                pygame.draw.rect(surface, blue, pygame.Rect(x_block + h*tile_size, y_block + z*tile_size,tile_size,tile_size))
            if map[z][h] == 5 :
                pygame.draw.rect(surface, yellow, pygame.Rect(x_block + h*tile_size, y_block + z*tile_size, tile_size, tile_size))
            
            if map[z][h] == 1 and z == 0:
                surface.blit(wall_img[9+door], (x_block + h*tile_size , y_block + z*tile_size ))
                door+=1 
            elif map[z][h] == 1 and h == 0:
                surface.blit(wall_img[11], (x_block + h*tile_size , y_block + z*tile_size ))
            elif map[z][h] == 1 and h == size_Y - 1:
                surface.blit(wall_img[12], (x_block + h*tile_size , y_block + z*tile_size ))
            elif map[z][h] == 1 and z == size_X-1:
                surface.blit(wall_img[13], (x_block + h*tile_size , y_block + z*tile_size ))

    if ((Mouse_y - y_block)//tile_size) > 0 and (Mouse_y - y_block)//tile_size < size_X - 1 and ((Mouse_x - x_block)//tile_size > 0) and ((Mouse_x - x_block)//tile_size < size_Y - 1):
        overlays = pygame.Surface((tile_size,tile_size))                  
        overlays.set_alpha(50)                
        overlays.fill((0,0,0))              
        surface.blit(overlays, (x_block + (Mouse_x - x_block)//tile_size*tile_size,y_block + (Mouse_y-y_block)//tile_size*tile_size))  

    surface.blit(clock, (x_block + clock_now*tile_size , y_block + 3))
width = surface.get_width()
height = surface.get_height()

color = (255,255,255)
  
color_light = (170,170,170)
color_dark = (100,100,100)

tools_clicked = "a"

randomnizer_width = width/7
randomnizer_height = randomnizer_width/3.5

button_width = width/2 - randomnizer_width/2
button_height = height/9  

smallfont = pygame.font.Font('Text\pixelFJ8pt1__.TTF',int(randomnizer_width/8.5))
text = smallfont.render('Randomnizer' , True , black)

t_block = x_block
random_close_x,random_close_y,random_close_length,random_close_height = 437.5 + 60, y_block - 110, 63,55
random_plusW_x,random_plusW_y,random_plusW_length,random_plusW_height = 437.5 + 140,y_block - 15,32,32
random_minW_x,random_minW_y,random_minW_length,random_minW_height = 437.5 + 140,y_block + 20,32,32
random_plusL_x,random_plusL_y,random_plusL_length,random_plusL_height = 437.5 + 270,y_block - 15,32,32
random_minL_x,random_minL_y,random_minL_length,random_minL_height = 437.5 + 270,y_block + 20,32,32
random_confirm_x,random_confirm_y,random_confirm_length,random_confirm_height = 437.5 + 185,y_block + 75,135,40

print(x_block)
take_width = 20
take_length = 20

while running:
    click_now = True
    
    #TOOLS

    surface.fill(pastel_yellow)

    bed_button_w,bed_button_y,chair_button_w,chair_button_y,desk_button_w,desk_button_y,lemari_button_w,lemari_button_y = draw_tools()
    Mouse_x, Mouse_y = pygame.mouse.get_pos()
    #TOOLS
    # print(Mouse_x - (1400-(15*35))/2, Mouse_y - 200)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            #Random_tool
            if button_width <= mouse[0] <= button_width + randomnizer_width and button_height <= mouse[1] <= button_height + randomnizer_height and random_now == False:
                random_now = True

            if random_now:
                if random_close_x <= mouse[0] <= random_close_x + random_close_length and random_close_y <= mouse[1] <= random_close_y + random_close_height:
                    random_now = False
                if random_plusW_x <= mouse[0] <= random_plusW_x + random_plusW_length and random_plusW_y <= mouse[1] <= random_plusW_y + random_plusW_height:
                    take_width += 1
                if random_minW_x <= mouse[0] <= random_minW_x + random_minW_length and random_minW_y <= mouse[1] <= random_minW_y + random_minW_height and take_width - 1 > 14:
                    take_width -= 1
                if random_plusL_x <= mouse[0] <= random_plusL_x + random_plusL_length and random_plusL_y <= mouse[1] <= random_plusL_y + random_plusL_height:
                    take_length += 1
                if random_minL_x <= mouse[0] <= random_minL_x + random_minL_length and random_minL_y <= mouse[1] <= random_minL_y + random_minL_height and take_length - 1 > 14 :
                    take_length -= 1
                if random_confirm_x <= mouse[0] <= random_confirm_x + random_confirm_length and random_confirm_y <= mouse[1] <= random_confirm_y + random_confirm_height:
                    size_X = take_width
                    size_Y = take_length

                    room_1.size_X = take_width
                    room_1.size_Y = take_length

                    room_1.maps = room_1.make_map(room_1.size_X,room_1.size_Y)
                    map = room_1.maps
                    if size_X > size_Y :
                        tile_size = total_tiles_x_and_y//size_X
                    else:
                        tile_size = total_tiles_x_and_y//size_Y

                    x_block = (width/2-(size_Y*tile_size)/2)

                    wall_img[0] = pygame.image.load('Dinding\L.png')
                    wall_img[1] = pygame.image.load('Dinding\LD.png')
                    wall_img[2] = pygame.image.load('Dinding\LU.png')
                    wall_img[3] = pygame.image.load('Dinding\MD.png')
                    wall_img[4] = pygame.image.load('Dinding\MU.png')
                    wall_img[5] = pygame.image.load('Dinding\R.png')
                    wall_img[6] = pygame.image.load('Dinding\RU.png')
                    wall_img[7] = pygame.image.load('Dinding\RD.png')
                    wall_img[8] = pygame.image.load('Dinding\FLOOR.png')
                    wall_img[9] = pygame.image.load('Dinding\DOOR_UP_1.png')
                    wall_img[10] = pygame.image.load('Dinding\DOOR_UP_2.png')
                    wall_img[11] = pygame.image.load('Dinding\DOOR_L.png')
                    wall_img[12] = pygame.image.load('Dinding\DOOR_R.png')
                    wall_img[13] = pygame.image.load('Dinding\DOOR_D.png')

                    clock = pygame.image.load('Dinding\CLOCK.png')
                    clock = pygame.transform.scale(clock, (tile_size,tile_size))

                    tool_box = pygame.image.load('Tools_Asset\Tools_box.png')
                    logo = pygame.image.load('Tools_Asset\LOGO.png')

                    choose = pygame.image.load('Tools_Asset\CHOOSE.png')
                    choose = pygame.transform.scale(choose, (tool_size,tool_size))


                    random_box = pygame.image.load('Tools_Asset\RANDOM_NOTIF.png')
                    
                    for i in range (0,14):
                        wall_img[i] = pygame.transform.scale(wall_img[i], (tile_size,tile_size))
                    randomnize(draw_max,count_bed,count_chair,count_table,count_lemari,size_X,size_Y)
                    random_now = False
                    clock_now = find_clock()

            #Bed_Tools
            if bed_button_w <= mouse[0] <= bed_button_w + tool_size and bed_button_y <= mouse[1] <= bed_button_y + tool_size and tools_clicked != "BED":
                clear_select()
                selected_tool[0][0] = 1
                tools_clicked = "BED"
                click_now = False
            
            if bed_button_w <= mouse[0] <= bed_button_w + tool_size and bed_button_y <= mouse[1] <= bed_button_y + tool_size and tools_clicked == "BED" and click_now:
                tools_clicked = "a"
                clear_select()

            #Chair tool
            if chair_button_w <= mouse[0] <= chair_button_w + tool_size and chair_button_y <= mouse[1] <= chair_button_y + tool_size and tools_clicked != "CHAIR":
                clear_select()
                tools_clicked = "CHAIR"
                selected_tool[0][1] = 1
                click_now = False

            if chair_button_w <= mouse[0] <= chair_button_w + tool_size and chair_button_y <= mouse[1] <= chair_button_y + tool_size and tools_clicked == "CHAIR" and click_now:
                tools_clicked = "a"
                clear_select()

            #Desk tool
            if desk_button_w <= mouse[0] <= desk_button_w + tool_size and desk_button_y <= mouse[1] <= desk_button_y + tool_size and tools_clicked != "DESK":
                clear_select()
                tools_clicked = "DESK"
                selected_tool[1][0] = 1
                click_now = False

            if desk_button_w <= mouse[0] <= desk_button_w + tool_size and desk_button_y <= mouse[1] <= desk_button_y + tool_size and tools_clicked == "DESK" and click_now:
                tools_clicked = "a"
                clear_select()

            #lemari tool
            if lemari_button_w <= mouse[0] <= lemari_button_w + tool_size and lemari_button_y <= mouse[1] <= lemari_button_y + tool_size and tools_clicked != "LEMARI":
                clear_select()
                selected_tool[1][1] = 1
                tools_clicked = "LEMARI"
                click_now = False

            if lemari_button_w <= mouse[0] <= lemari_button_w + tool_size and lemari_button_y <= mouse[1] <= lemari_button_y + tool_size and tools_clicked == "LEMARI" and click_now:
                tools_clicked = "a"
                clear_select()

            #drawing tools to the map
            if random_now == False:
                if ((Mouse_y - y_block)//tile_size) > 0 and (Mouse_y - y_block)//tile_size < size_X - 1 and ((Mouse_x - x_block)//tile_size > 0) and ((Mouse_x - x_block)//tile_size < size_Y - 1):

                    if x_block <= mouse[0] <= x_block + tile_size*size_Y and y_block <= mouse[1] <= y_block + tile_size*size_X and tools_clicked == "BED":
                        map[int((Mouse_y - y_block)//tile_size)][int((Mouse_x - x_block)//tile_size)] = 3
                    elif x_block <= mouse[0] <= x_block + tile_size*size_Y and y_block <= mouse[1] <= y_block + tile_size*size_X and tools_clicked == "CHAIR":
                        map[int((Mouse_y - y_block)//tile_size)][int((Mouse_x - x_block)//tile_size)] = 2
                    elif x_block <= mouse[0] <= x_block + tile_size*size_Y and y_block <= mouse[1] <= y_block + tile_size*size_X and tools_clicked == "DESK":      #
                        map[int((Mouse_y - y_block)//tile_size)][int((Mouse_x - x_block)//tile_size)] = 4                                                      #
                    elif x_block <= mouse[0] <= x_block + tile_size*size_Y and y_block <= mouse[1] <= y_block + tile_size*size_X and tools_clicked == "LEMARI":    #
                        map[int((Mouse_y - y_block)//tile_size)][int((Mouse_x - x_block)//tile_size)] = 5                                                      #
            ##############################################################################################################################

    mouse = pygame.mouse.get_pos()

    if button_width <= mouse[0] <= button_width + randomnizer_width and button_height <= mouse[1] <= button_height + randomnizer_height:  #hover
        pygame.draw.rect(surface,pastel_dark_pink,[button_width,button_height,randomnizer_width,randomnizer_height],0,3)
        pygame.draw.rect(surface,pastel_dark_cream,[button_width,button_height,randomnizer_width,randomnizer_height],5,3)
    else:
        pygame.draw.rect(surface,pastel_pink,[button_width,button_height,randomnizer_width,randomnizer_height],0,3)
        pygame.draw.rect(surface,pastel_cream,[button_width,button_height,randomnizer_width,randomnizer_height],5,3)
      
    # superimposing the text onto our button
    surface.blit(text , (button_width + button_width//80,button_height + button_width // 35))
      
    # updates the frames of the game
    drawgame()

    if random_now :
        overlay = pygame.Surface((width - 200,height))  
        overlay.set_alpha(128)                
        overlay.fill((0,0,0))           
        surface.blit(overlay, (200,0))   

        surface.blit(random_box, (437.5 + 13  , y_block - 120 ))

        smallfont1 = pygame.font.Font('Text\pixelFJ8pt1__.TTF',int(randomnizer_width/4.5))
        text_width = smallfont1.render(str(take_width) , True , white)    
        text_length = smallfont1.render(str(take_length) , True , white)   

        surface.blit(text_width , (437.5 + 58 , y_block ))
        surface.blit(text_length , (437.5 + 188  , y_block))
    pygame.display.flip()


pygame.quit()


#enter lenght menjadi size y 
#enter height menjadi size x
#total work_hours = 7+3+8+2+1+4+8 :D