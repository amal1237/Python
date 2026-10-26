# oops

# introduction to oops

# object oriented programming

# object


        # attributes -- variables
        # behaviours/methods -- function

# class

        # template/blueprints


# class car:
#     def start():
#         print("car starts")
#     def stops():
#         print("car has stopped")

# car1 = car

# print(car1)
# car1.start()
# car1.stops()





# 
# class car:
#     def __init__(self,n,c):
#         self.name = n
#         self.color = c
#     def start(self):
#         print(f"{self.name} start")
#     def stops(self):
#         print(f"{self.name}has stops")



# car1 = car("maruthi 800","red")
# print(car1.color,car1.name)
# car2 = car("amaze","blue")
# print(car2.color,car2.name)
# car1.start()


# 

# class pen:
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price
#     def compare(self,othr):
#         print(self.name)
# p1 = pen("gripper",20)
# p2 = pen("lexi",10)
# p2.compare(p1)    
# 
#     


# create a class student
# 5
# with 6 attributes name m1 m2 m3 m4 m5
# 3 methods
# sum_of_mark()
# average of mark ()
# display_details()


class student:
    def __init__(self,name,m1,m2,m3,m4,m5):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = m4
        self.m5 = m5
        
    def sum_of_mark(self):
        return self.m1 + self.m2 + self.m3 + self.m4 + self.m5

    def average_of_marks(s1):
        return s1.sum_of_mark()/5

    def display_details(self):
        return self.name,s1.sum_of_mark,s1.average_of_marks
           
s1 = student("mubasheer",42,41,44,45,46)


print(s1.display_details())

