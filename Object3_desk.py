import random

class table :
    _length_x = 0
    _length_y = 0

    max_x = 5
    max_y = 3

    min_x = 1
    min_y = 1

    code = 4

    def random_length(self,batas_x,batas_y):
        self._length_x = random.randint(self.min_x, batas_y)
        self._length_y = random.randint(self.min_y, batas_x)

        if (self._length_x > 5):
            self._length_x = random.randint(self.min_x, self.max_x)

        if (self._length_y > 3):
            self._length_y = random.randint(self.max_y, self.max_y)
        
        # self._length_x = 2 #tester
        # self._length_y = 2 #tester

    def give_table(self):
        print(self._length_x,"aaaa", self._length_y)
        return self._length_x,self._length_y
