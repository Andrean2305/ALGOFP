import random

class chair :
    _length_x = 0
    _length_y = 0

    min_x = 1
    min_y = 1

    max_x = 4
    max_y = 2

    code = 2

    def random_length(self,batas_x,batas_y):
        self._length_x = random.randint(self.min_x, batas_y)
        self._length_y = random.randint(self.min_y, batas_x)

        if (self._length_x > 4):
            self._length_x = random.randint(self.min_x, self.max_x)

        if (self._length_y > 2):
            self._length_y = random.randint(self.min_y, self.max_y)
        
        # self._length_x = 2 #tester
        # self._length_y = 2 #tester

    def give_chair(self):
        print(self._length_x,"aaaa", self._length_y)
        return self._length_x,self._length_y
