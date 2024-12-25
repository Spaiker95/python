class My_class:
    def __init__(self, x = 1, y = 1):
        self.x = x
        self.y = y

    def summ(self):
        return self.x + self.y
    
    
tom = My_class(4, 3)

print(tom.summ())
    

        
