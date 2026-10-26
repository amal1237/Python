import sqlite3
conn = sqlite3.connect("task.db") 
cursor = conn.cursor()
cursor.execute('''
            CREATE TABLE IF NOT EXISTS task(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tname VARCHAR(20),
            tdes TEXT
            )        
        ''')
def addtask():
    conn = sqlite3.connect("task.db") 
    cursor = conn.cursor()
    name=input("enter task name :--")
    des=input("enter task des:--")

    cursor.execute('''
        INSERT into task(tname,tdes)
        VALUES(?,?)
''',(name,des))
    
    conn.commit()
    print(" task added 👍🏻 ")

def viewtask():
    conn = sqlite3.connect("task.db") 
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM task
''')
    data=cursor.fetchall()
    if data:
        print("data found")
        for i in data:
            print(f"{i[0]}--{i[1]}--{i[2]}")
    else:
        print("no task found")

def searchtask():
    conn = sqlite3.connect("task.db") 
    cursor = conn.cursor()
    t_id = int(input("enter task id :--"))
    cursor.execute('''
        SELECT * FROM task WHERE ID = ?
        ''',(t_id,))
    data = cursor.fetchone()
    if data:
        print("data found")
        print(data[1])

def edittask():
    conn = sqlite3.connect("task.db") 
    cursor = conn.cursor() 
    t_id = int(input("enter task id : "))
    name = input("enter new task name:-")
    des = input("enter new task des:-")
    cursor.execute('''
        UPDATE task SET tname = ?,tdes = ? WHERE id = ?
        ''',(name,des,t_id)) 
    conn.commit()
    print("Task updated")

def deletetask():
    conn = sqlite3.connect("task.db") 
    cursor = conn.cursor() 
    t_id = int(input("enter task id : ")) 
    cursor.execute('''
        DELETE FROM task WHERE id = ?
        ''',(t_id,))  
    ch = input("Are you sure you want to delete this task --- y/n ? --")
    if ch == "y":
        conn.commit()
        print("task deleted")
    else:
        print("cancelled")    


def main():
    print("Welcome to task management system")
    while True:
        ch=int(input("enter your choice \n1. addtask \n2.viewtask \n3.searchtask \n4.edittask \n5.deletetask \n6.exit \n------"))
        if ch==1:
            addtask()
            pass
        elif ch==2:
            viewtask()
            pass
        elif ch==3:
            searchtask()

        elif ch==4:
            edittask() 

        elif ch==5:
            deletetask()       
            

        elif ch==6:
            break
main()



