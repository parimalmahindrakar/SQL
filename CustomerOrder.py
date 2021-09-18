import pymysql
from faker import Faker
import random


fake = Faker()

conn = pymysql.connect(
    host = "localhost", 
    database="practice",
    user= "root",
    password=""    
)

cursor = conn.cursor()

# SET sql_mode = ''; 
## If you are getting the gourpby error !   a


query1 = """create table Customer (
    custid int primary key auto_increment,
    name varchar(50) not null,
    gender varchar(1) not null,
    phone varchar(10) not null,
    address varchar(100) not null default "Pune"
);
"""
query2 = '''create table Orders(
    orderid int primary key auto_increment, 
    ordername varchar(50) not null, 
    quantity int, 
    custid int, 
    foreign key(custid) references Customer(custid)
);
'''


try:
    cursor.execute(query1)
    cursor.execute(query2)
    print("Query executed ! [Table Created]")
except pymysql.err.OperationalError :
    print("Table already exists")


ls = [0,1,2,3,4,5,6,7,8,9]

def makenum():
    s = ""
    for _ in ls:
        s += str(random.choice(ls))
    return s



for i in range(200) :

    name = fake.name()
    gender = random.choice(['M','F'])
    phone = makenum()
    addres = fake.city()
    query = f'insert into Customer(name, gender, phone, address) values ( "{name}", "{gender}", "{phone}",  "{addres}");'
    cursor.execute(query)
    conn.commit()



orderlist = ["Bakery" , "Bread",
"Meat" , "Seafood",
"Pasta" , "Rice",
"Oils", "Sauces", "Salad", "Dressings", "Condiments",
"Cereals" , "Breakfast Foods",
"Soups" , "Canned Goods",
"Frozen Foods",
"Dairy", "Cheese",  "Eggs" ,  "coffee/tea", 
"juice", "soda", "sandwich loaves", "dinner rolls", "tortillas bagels",
"vegetables", "spaghetti sauce", "ketchup",
"cheeses", "eggs", "milk", "yogurt", "butter",
"cereals", "flour", "sugar", "pasta", "mixes",
"waffles", "vegetables", "individual meals", "ice cream",
"lunch meat", "poultry", "beef", "pork",
"paper towels", "toilet paper", "aluminum foil", "sandwich bags",
"baby items", "pet items", "batteries", "greeting cards"
]


for i in range(180) :

    ordername = random.choice(orderlist)
    quantity = random.randint(1,15)
    custid = random.randint(1,160)
    query = f'insert into Orders(Ordername, Quantity, custid) values ( "{ordername}", "{quantity}", "{custid}");'
    cursor.execute(query)
    conn.commit()
    
