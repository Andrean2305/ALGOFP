import random
import Object1_chair_sofa
import Object2_Bed
import Object3_desk
import Object4_lemari

class Room :
    size_X = 0
    size_Y = 0
    sofas = Object1_chair_sofa.chair()
    beds = Object2_Bed.bed()
    table = Object3_desk.table()
    lemari = Object4_lemari.lemari()

    maps = []

    def __init__(self, size_x = 5, size_y = 5):
        self.size_X = size_x
        self.size_Y = size_y
        self.sofas.random_length((size_x//2),(size_y//2)) 
        self.beds.random_length((size_x//2),(size_y//2))
        self.table.random_length((size_x//2),(size_y//2))
        self.lemari.random_length((size_x//2),(size_y//2))
        

    def sofa(self,anak_sofa):
        self.sofas = anak_sofa
    
    def print_map(self,map) :
        for z in range (len(map)) :
            print(map[z])
        print()

    def make_map(self, size_of_map_y,size_of_map_x):
        map_now = []
        map_now = [[0 for i in range(size_of_map_x)] for j in range(size_of_map_y)]
        
        for z in range (size_of_map_x) :
            for h in range (size_of_map_y):
                if (z == 0 or z == size_of_map_x -1 or h == 0 or h == size_of_map_y - 1):
                    map_now[h][z] = 8

        self.print_map(map_now)

        return map_now

    def give_random_door(self, size_of_map_y,size_of_map_x,map) :
        map_now = map
        x_Pos = random.randint(0,size_of_map_x - 1)

        if x_Pos == 0 or x_Pos == size_of_map_x - 1:
            y_Pos = random.randint(1,size_of_map_y - 2)
        else :
            y_Pos = random.choice([0,size_of_map_y - 1])

        map_now[y_Pos][x_Pos] = 1
        
        if (0 < x_Pos < size_of_map_x - 1):
            i = random.randint(0,1)
            if i == 0 :
                if x_Pos > 1 :
                    map_now[y_Pos][x_Pos - 1] = 1
                else :
                    map_now[y_Pos][x_Pos + 1] = 1
            else :
                if x_Pos < size_of_map_x - 2 :
                    map_now[y_Pos][x_Pos + 1] = 1
                else :
                    map_now[y_Pos][x_Pos - 1] = 1
        
        elif (x_Pos == 0 or x_Pos == size_of_map_x - 1):
            i = random.randint(0,1)
            if i == 0 :
                if y_Pos > 1 :
                    map_now[y_Pos - 1][x_Pos] = 1
                else :
                    map_now[y_Pos + 1][x_Pos] = 1
            else :
                if y_Pos < size_of_map_y - 2 :
                    map_now[y_Pos + 1][x_Pos] = 1
                else :
                    map_now[y_Pos - 1][x_Pos] = 1

        self.print_map(map_now)
        return map_now

    def give_furniture(self,panjang,lebar,kode):

        babi = True
        ea = 1
        while (babi):

            print("MENGOCOK TEMPAT",ea)
            j,i = random.randint(1,self.size_X - 2),random.randint(1,self.size_Y - 2)
            anjing = True
            
            # if self.maps[j][i] == 0 and self.maps[j + 1][i] != 1 and self.maps[j-1][i] != 1 and self.maps[j][i+1] != 1 and self.maps[j][i-1] != 1:
            if (self.maps[j][i] == 0 
                and (self.maps[j + 1][i] == 0 or self.maps[j + 1][i] == 8) 
                and (self.maps[j - 1][i] == 0 or self.maps[j - 1][i] == 8)
                and (self.maps[j][i + 1] == 0 or self.maps[j][i + 1] == 8)
                and (self.maps[j][i - 1] == 0 or self.maps[j][i - 1] == 8)):

                self.maps[j][i] = kode

                babi = False
                test_kanan = True
                
                while(anjing):
                    if (panjang > 1 or lebar > 1):

                        kiri_kanan = random.choice([1,-1])
                        if ((0 < i + (panjang*kiri_kanan) < self.size_Y - 1)):
                            kiri_kanan = kiri_kanan
                        else : 
                            kiri_kanan = kiri_kanan * (-1)

                        atas_bawah = random.choice([1,-1])         
                        if ((0 < j + (lebar*atas_bawah) < self.size_X - 1)):
                            atas_bawah = atas_bawah
                        else : 
                            atas_bawah = atas_bawah * (-1)

                        # print("Kanan ", j,i)
                        if (0 < i + (panjang)*kiri_kanan < self.size_Y - 1 and 0 < j + (lebar)*atas_bawah < self.size_X - 1): 

                            # print ("PlusMinus", atas_bawah,kiri_kanan)
                            # print ("Panjang = ",panjang, "Lebar = ",lebar)

            
                            for a in range (0, lebar):
                                # print("this is the counted = ",j + a*atas_bawah)
                                for z in range (0,panjang) :

                                    if ((self.maps[j + a*atas_bawah][i + z*kiri_kanan] != 0 and self.maps[j + a*atas_bawah][i + z*kiri_kanan] != kode) 
                                        # or self.maps[j + a * atas_bawah][i + (z + 1) * kiri_kanan] == 1 
                                        # or self.maps[j + (a + 1) *atas_bawah][i + z * kiri_kanan] == 1
                                        # or (self.maps[j - 1][i + z * kiri_kanan] == 1)
                                        # or self.maps[j + 1][i + z * kiri_kanan] == 1 
                                        # or self.maps[j + a * atas_bawah][i + 1] == 1
                                        # or self.maps[j + a * atas_bawah][i - 1] == 1 ):

                                        or self.maps[j + a * atas_bawah][i + (z + 1) * kiri_kanan] != 0 and self.maps[j + a * atas_bawah][i + (z + 1) * kiri_kanan] != 8 
                                        or self.maps[j + (a + 1) *atas_bawah][i + z * kiri_kanan] != 0 and self.maps[j + (a + 1) *atas_bawah][i + z * kiri_kanan] != 8
                                        or (self.maps[j - 1][i + z * kiri_kanan] != 0) and (self.maps[j - 1][i + z * kiri_kanan] != 8)
                                        or self.maps[j + 1][i + z * kiri_kanan] != 0 and self.maps[j + 1][i + z * kiri_kanan] != 8 
                                        or self.maps[j + a * atas_bawah][i + 1] != 0 and self.maps[j + a * atas_bawah][i + 1] != 8
                                        or self.maps[j + a * atas_bawah][i - 1] != 0 and self.maps[j + a * atas_bawah][i - 1] != 8):
                                        test_kanan = False
                                        break
                                        
                                if (a == lebar - 1 and test_kanan == True):
                                    for a in range (0, lebar):
                                        for z in range (0,panjang):
                                                # print("Location= ",j+a*atas_bawah, i+z*kiri_kanan)
                                                # print ("Before=",self.maps[j+a*atas_bawah][i+z*kiri_kanan])
                                                self.maps[j + a*atas_bawah][i + z*kiri_kanan] = kode
                                                # print()
                                                # print ("After=",self.maps[j+a*atas_bawah][i+z*kiri_kanan])
                                    anjing = False
                        else :
                            test_kanan = False
                                
                        if (test_kanan == False):
                            if (kode == 3):
                                self.beds.random_length((self.size_X//2),(self.size_Y//2))
                                panjang = self.beds._length_x
                                lebar = self.beds._length_y
                                # print("AISHAAAAAAAAAAAAAAAAAAAAAAAAAAAAS")
                            elif (kode == 2):
                                self.sofas.random_length((self.size_X//2),(self.size_Y//2)) 
                                panjang = self.sofas._length_x
                                lebar = self.sofas._length_y
                                # print("AISHAAASSSSSSSSSSSSSSSSSSSSSSSZZZZZZZZZ")
                            elif (kode == 4):
                                self.table.random_length((self.size_X//2),(self.size_Y//2)) 
                                panjang = self.table._length_x
                                lebar = self.table._length_y
                                # print("AISHAAASSSSSSSSSSSSSSSSSSSSSSSZZZZZZZZZ")   
                            elif (kode == 5):
                                self.lemari.random_length((self.size_X//2),(self.size_Y//2)) 
                                panjang = self.lemari._length_x
                                lebar = self.lemari._length_y
                                # print("AISHAAASSSSSSSSSSSSSSSSSSSSSSSZZZZZZZZZ")     

                            ea +=1
                            anjing = False

                            babi = True
                            test_kanan = True

                            self.maps[j][i] = 0
                        
                            if (ea > 5000):
                                anjing = False
                                babi = False
                                
                    elif(panjang == 1 and lebar == 1) :
                        self.maps[j][i] = kode
                        anjing = False
                                    
        self.print_map(self.maps)
    
    def check_space(self,map_x,map_y,min_x,min_y):
        checking = 0
        for z in range (1, map_y - 1) :
            for h in range (1 , map_x - 1):
                if self.maps[z][h] == 0 :
                    
                    if ((z + min_y < map_y - 1) and (h + min_x < map_x - 1)):
                        for i in range (0, min_y): #2
                            for j in range(0,min_x): #3
                                if (self.maps[z + i][h + j] != 0 
                                    # or self.maps[z + i][h + j + 1] == 1
                                    # or self.maps[z + i][h + j - 1] == 1
                                    # or self.maps[z + i + 1][h + j] == 1
                                    # or self.maps[z + i - 1][h + j] == 1):

                                    or self.maps[z + i][h + j + 1] != 0 and self.maps[z + i][h + j + 1] != 8
                                    or self.maps[z + i][h - 1] != 0 and self.maps[z + i][h - 1] != 8 
                                    or self.maps[z + i + 1][h + j] != 0 and self.maps[z + i + 1][h + j] != 8
                                    or self.maps[z - 1][h + j] != 0 and self.maps[z - 1][h + j] != 8):
                                    break
                                
                                else:
                                    checking +=1

                                if checking == min_x+min_y :
                                    print("yes")
                                    return True
                    else :
                        break
        return False

            
                
                
            






#input 4 and 3 resulted in 3 row and 4 column