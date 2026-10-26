# inheritance


# single level 


# class person1:
#     def __init__(self):
#         pass
#     def read(self):
#         print("prson can read")
#     def run(self):
#         print("person can run")

# class person2(person1):

#     def __init__(self):
#         pass
#     def jump(self):
#         print("person can jump")
#     def write(self):
#         print("person can write")

# p2.person2()
# p2.read() 


# multi level



# class person1:
#     def __init__(self):
#         pass
#     def read(self):
#         print("prson can read")
#     def run(self):
#         print("person can run")


# class person2(person1):

#     def __init__(self):
#         pass
#     def jump(self):
#         print("person can jump")
#     def write(self):
#         print("person can write")

# class person3(person2):

#     def __init__(self):
#         pass
#     def walk(self):
#         print("person can walk")
#     def swim(self):
#         print("person can swim")  

# class person4(person3):

#     def __init__(self):
#         pass
#     def sleep(self):
#         print("person can sleep")
#     def eat(self):
#         print("person can eat")              

# p4 = person4()
# p4.read()
# p4.swim()                




# encapsulation





# abstractions






# polymorphism




# class person1:
#     def __init__(self):
#         pass
#     def read(self):
#         print("prson can read")
#     def run(self):
#         print("person can run")
#     def speak(self):
#         print("person can speak")


# class person2(person1):

#     def __init__(self):
#         pass
#     def jump(self):
#         print("person can jump")
#     def write(self):
#         print("person can write")
#     def speak(self):
#             print("person2 can speak")    

# class person3(person2):

#     def __init__(self):
#         pass
#     def walk(self):
#         print("person can walk")
#     def swim(self):
#         print("person can swim") 
#     def speak(self):
#             print("person3 can speak")     

# class person4(person3):

#     def __init__(self):
#         pass
#     def sleep(self):
#         print("person can sleep")
#     def eat(self):
#         print("person can eat") 
#     def speak(self):
#         print("person4 can speak") 
#         super().speak()

# p4 = person4()
# p4.speak()
 



# multi

# class person1:
#     def __init__(self):
#         pass
#     def read(self):
#         print("prson can read")
#     def run(self):
#         print("person can run")
#     def speak(self):
#         print("person can speak")


# class person2():

#     def __init__(self):
#         pass
#     def jump(self):
#         print("person can jump")
#     def write(self):
#         print("person can write")
#     def speak(self):
#             print("person2 can speak")    

# class person3():

#     def __init__(self):
#         pass
#     def walk(self):
#         print("person can walk")
#     def swim(self):
#         print("person can swim") 
#     def speak(self):
#             print("person3 can speak")     

# class person4(person1,person2,person3):

#     def __init__(self):
#         pass
#     def sleep(self):
#         print("person can sleep")
#     def eat(self):
#         print("person can eat") 
   
        

# p4 = person4()
# p4.speak()
 


#  polymorphism


# operator overloading


# class student:
#     def __init__(self,m1,m2):
#         self.m1 = m1
#         self.m2 = m2
#     def __add__(self,othr):
#         t1 = self.m1 + othr.m1
#         t2 = self.m2 + othr.m2
#         return(t1,t2)
#     def __sub__(self,othr):
#         print("no difference allowed")

# s1 = student(7,8)
# s2 = student(5,10)
# print(s1+s2)
# s1-s2        



# class student:
#     def __init__(self,m1,m2):
#         self.m1 = m1
#         self.m2 = m2
#     def __mul__(self,othr):
#         t1 = self.m1 * othr.m1
#         t2 = self.m2 * othr.m2
#         return(t1,t2)
#     def __truediv__(self,othr):
#         t1 = self.m1 / othr.m1
#         t2 = self.m2 / othr.m2
#         return(t1,t2)

# s1 = student(7,8)
# s2 = student(5,10)
# print(s1*s2)
# print(s1/s2)  





# method overloading 

# class mydata:
#     def __init__(self):
#         pass
#     def display(self,a,b):
#         print(a,b)
#     def display(self,a,b,c):
#         print(a,b,c)

# d1 = mydata()
# d1.display(3,4)
# d1.display(5,6,7)





# method overriting 


# class A:
#     def __init__(self):
#         pass

#     def hello(self):
#         print("A hello")
# class B(A):
#     def __init__(self):
#         pass

#     def hello(self):
#         print("B hello")

# b = B()
# b.hello()       



# day24




# from abc import ABC,abstractmethod



# class Animal(ABC):
#     def __init__(self):
#         pass
#     @abstractmethod
#     def make_sound(self):
#         print("animal make sound")

# class Dog(Animal):
#     def __init__(self):
#         pass

#     def make_sound(self):
#         print("makes sound")
# d = Dog()                







from abc import ABC,abstractmethod

class payment(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def pay(self,amount):
        pass
class upipayment(payment):
    def __init__(self):
        pass
    def pay(self,amount):
        print(f"payed {amount} with upi")

class cardpayment(payment):
    def __init__(self):
        pass
    def pay(self,amount):
        print(f"payed {amount} with cards")

upi = upipayment()
card = cardpayment()
upi.pay(2000)
card.pay(2000)