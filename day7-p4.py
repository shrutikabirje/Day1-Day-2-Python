Write a program to count how many reference variables in a program. 



import sys
class count():
    def __init__(self,name):
        self.name=name
s=count('shruu')
print(s.name)
print(sys.getrefcount(s))

