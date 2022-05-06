import Toffoli_Gate
import Not_Gate


class library_bulder:
    gates=[]
    def __init__(self,qubit):
        self.qubit=qubit


    def __str__(self):
        return "{}:  {}".format("Number of lanes", self.qubit)

    def place_Not(self,lain):
        self.gates.append( Not_Gate.Not_Gate(lain))
    def place_Toffoli(self,lains):
        self.gates.append(Toffoli_Gate.Toffoli_Gate(lains))
    def calculate(self,num):
        for i in range(0,len(self.gates)):
            try: num=self.gates[i].use_Not(num)
            except AttributeError: num=self.gates[i].use_Toffoli(num)
        return num

    def clear(self):
        self.gates=[]


