class Queue:
    def __init__(self):
        self.q = []
    def enque(self,data):
        self.q.append(data)
    def denque(self):
        popEle = -1
        if len(self.q) >0:
            popEle = self.q.pop(0)
        return popEle
    def print(self):
        for i in self.q:
            print(i,end=" ")
        print()
q= Queue()
q.enque(1)
q.enque(2)
q.enque(3)
q.enque(4)
q.enque(5)
q.print()
q.denque()
q.denque()
q.denque()
q.print()