def rotation(s1,s2):
    if len(s1) !=len(s2):
        return False
    temp  = s1+s2
    if s2 in temp:
        return True
    else:
        return False
s1 = "abcd"
s2 = "efgs"
#flag = rotation(s1,s2)
#print(flag)
print()
class Queue:
    def __init__(self):
        self.q = []
    
    def enque(self,data):
        self.q.append(data)

    def deque(self):
        popEle = -1
        if len(self.q)>0:
            popEle = self.q.pop(0)
        return popEle

def rotationCheck1(str1,str2):
    if len(str1)!=len(str2):
        return False 
    q1 = Queue()
    q2 = Queue()
    for i in str1:
        q1.enque(i)
    for i in str2:
        q2.enque(i)
    for i in range(len(q1.q)):
        alpha = q2.deque()
        q2.enque(alpha)
        if q1.q == q2.q:
            return True 
    return False



str1 = 'abcd'
str2 = 'efgh'
flag = rotationCheck1(str1,str2)
print(flag)

