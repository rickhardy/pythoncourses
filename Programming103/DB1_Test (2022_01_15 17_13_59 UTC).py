

import sqlite3

def create(name, cores, cpu, ram, cost):
    insert_sql = "INSERT INTO computer(name, cores, cpu_speed, ram, cost) VALUES ('{}', {},  {},  {},  '{}' )".format(name, cores, cpu, ram, cost)

    conn.execute(insert_sql)

    conn.commit()
    
def read(name):
    select_sql = "SELECT * FROM computer WHERE name = '{}'".format(name)

    result = conn.execute(select_sql)

    return result.fetchone()



conn = sqlite3.connect("computer_cards.db")
result = conn.execute("SELECT * FROM Computer")
computers = result.fetchall()
print (computers)
print (type (computers))
print (type(computers[0]))




for computer in computers:
    name, cores, cpu, ram, cost = computer[0],computer[1],computer[2],computer[3],computer[4]
    
    
    print(name, cores, cpu, ram, cost)


create ("MacbookAir", 3, 34, 34,45 )

name = input("Name >")

card = read(name)

print(card)
