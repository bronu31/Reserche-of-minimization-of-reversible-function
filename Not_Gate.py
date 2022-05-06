class Not_Gate:


    def __init__(self, lain):
        self.lain=lain

    def use_Not(self,num):
        return num ^ (1 << self.lain)

    def __str__(self): return "Not gate at lain: {}".format(self.lain)