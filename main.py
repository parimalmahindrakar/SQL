import pymysql
from faker import Faker
import random


fake = Faker()

conn = pymysql.connect(
    host = "localhost", 
    database="db",
    user= "root",
    password=""    
)

cursor = conn.cursor()

# SET sql_mode = ''; 
## If you are getting the gourpby error !


query = """create table Employee (
    empid int primary key auto_increment,
    name varchar(50) not null,
    gender varchar(1) not null,
    phone varchar(10) not null,
    class varchar(1) not null,
    salary int(10) check(salary >= 20000) not null,
    address varchar(100) not null default "Pune",
    department varchar(50)
);
"""

try:
    cursor.execute(query)
    print("Query executed ! [Table Created]")
except pymysql.err.OperationalError :
    print("Table already exists")


ls = [0,1,2,3,4,5,6,7,8,9]

def makenum():
    s = ""
    for _ in ls:
        s += str(random.choice(ls))
    return s


records = []

for i in range(200) :

    name = fake.name()
    gender = random.choice(['M','F'])
    phone = makenum()
    class_ = random.choice(['A','B','C'])
    salary = random.randint(20000,1000000)
    addres = fake.city()
    department = random.choice(["IT", "IOT", "CSE","ENTC", "MECH"])
    query = f'insert into Employee(name, gender, phone, class, salary, address, department) values ( "{name}", "{gender}", "{phone}", "{class_}", {salary}, "{addres}", "{department}");'
    records.append((name, gender, phone, class_, salary, addres, department))
    cursor.execute(query)
    conn.commit()

