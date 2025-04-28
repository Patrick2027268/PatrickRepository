class myClass:
    def __init__(self,name,color,age): # Parameters for the class instance
        self.name= name
        self.age = age
        self.color = color
    def __str__(self):
        return f"{self.name}"  
    def myFunc(self): 
            print("I'm " + self.name + ". My favorite color is " + self.color + " and I am " + str(self.age) + " years  old.")
p1 = myClass("Joseph","blue",24) # Class instance
print(p1) # return self.name from __str__()
p1.myFunc()

print(type(p1.age))
del p1 # deleters p1 from memory