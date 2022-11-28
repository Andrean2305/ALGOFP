import random

class bed :
    _length_x = 0
    _length_y = 0
    code = 3

    max_x = 9
    max_y = 8

    min_x = 3
    min_y = 2

    def random_length(self,batas_x,batas_y):
        self._length_x = random.randint(self.min_x, batas_y)
        self._length_y = random.randint(self.min_y, batas_x)

        if (self._length_x > 10):
            self._length_x = random.randint(self.min_x, self.max_x)

        if (self._length_y > 9):
            self._length_y = random.randint(self.min_y, self.max_y)
        
        # self._length_x = 2 #tester
        # self._length_y = 2 #tester
