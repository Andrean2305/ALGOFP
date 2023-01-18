import random

class lemari :
    _length_x = 0
    _length_y = 0
    
    pojok = False
    max_x = 4
    max_y = 2

    min_x = 1
    min_y = 1

    code = 5

    def random_length(self,batas_x,batas_y):
        self._length_x = random.randint(self.min_x, batas_y)
        self._length_y = random.randint(self.min_y, batas_x)

        if (self._length_x > 4):
            self._length_x = random.randint(self.min_x, self.max_x)

        if (self._length_y > 2):
            self._length_y = random.randint(self.min_y, self.max_y)

    def give_table(self):
        print(self._length_x,"aaaa", self._length_y)
        return self._length_x,self._length_y
