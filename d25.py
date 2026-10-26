# multithreading

# import threading
# import time
# lock = threading.Lock()
# x = 0


# def work(name):
#     global x
#     for i in range(1,4):
#         with lock:
#             x = x + i
#             print(name,x)
#             time.sleep(1)
#     print(x)        
#     # print(f"{name} am working")

# t1 = threading.Thread(target = work,args=["A"])
# t2 = threading.Thread(target= work,args=["B"])

# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print("main", x)




# MULTIPROCESSING


from multiprocessing import process
import os
x = 0
def work(name):
    global x
    print(name,"working")
    print(os.getpid())
    for i in range(1,4):
    
        x = x + i
    print(name,x)
            
        
    

p1 = process(target = work,args=["A"])
p2 = process(target= work,args=["B"])
if __name__ == '__main__':
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("main", x)

    print(os.getpid())

    