# Creado por RUBEN EDWIN HUALLA QUISPE
# Para el Curso de EMPRESAS DE BASE TECNOLOGICA II
# Grupo Listas Escolares
# Junio - 2018

import sqlite3
conn = sqlite3.connect('eListasEscolares.db')

c = conn.cursor()
conn.text_factory = str

c.execute("DROP TABLE IF EXISTS Schools")
c.execute("DROP TABLE IF EXISTS Supplier")
c.execute("DROP TABLE IF EXISTS Customer")
c.execute("DROP TABLE IF EXISTS Lists")
c.execute("DROP TABLE IF EXISTS Product")
c.execute("DROP TABLE IF EXISTS PurchaseOrder")
c.execute("DROP TABLE IF EXISTS Ratings")
c.execute("DROP TABLE IF EXISTS OrderItem")
c.execute("DROP TABLE IF EXISTS Orden")

c.execute("CREATE TABLE Schools\
(\
 SchoolId      INT NOT NULL ,\
 SchoolName    VARCHAR(50) NOT NULL ,\
 SchoolAddress VARCHAR(50) NOT NULL ,\
 SchoolStatus  INT NOT NULL ,\
 PRIMARY KEY (SchoolId ASC)\
);")

c.execute(
"CREATE TABLE Supplier\
(\
 SupplierId  INT IDENTITY (1, 1) NOT NULL ,\
 CompanyName VARCHAR(40) NOT NULL ,\
 Phone       VARCHAR(20) NULL ,\
 Address     VARCHAR(50) NOT NULL ,\
 City        VARCHAR(40) NOT NULL ,\
 Country     VARCHAR(40) NOT NULL ,\
 PostalCode  SMALLINT NOT NULL ,\
\
 PRIMARY KEY (SupplierId ASC),\
 CONSTRAINT AK1_Supplier_CompanyName UNIQUE (CompanyName ASC)\
);")

c.execute(
"CREATE TABLE Customer\
(\
 CustomerId        INT IDENTITY (1, 1) NOT NULL ,\
 CustomerFirstName VARCHAR(40) NOT NULL ,\
 CustomerLastName  VARCHAR(40) NOT NULL ,\
 Phone             VARCHAR(20) NULL ,\
 Address           VARCHAR(50) NOT NULL ,\
 City              VARCHAR(40) NOT NULL ,\
 Country           VARCHAR(40) NOT NULL ,\
 PostalCode        SMALLINT NOT NULL ,\
\
 PRIMARY KEY  (CustomerId ASC),\
 CONSTRAINT AK1_Customer_CustomerName UNIQUE  (CustomerFirstName ASC)\
);")

c.execute(
"CREATE TABLE Lists\
(\
 ListId     INT NOT NULL ,\
 PhotoPath  VARCHAR(50) NOT NULL ,\
 SchoolId   INT NOT NULL ,\
 CustomerId INT NOT NULL ,\
\
 PRIMARY KEY (ListId ASC),\
 FOREIGN KEY (SchoolId)\
  REFERENCES Schools(SchoolId),\
 FOREIGN KEY (CustomerId)\
  REFERENCES Customer(CustomerId)\
);")

c.execute(
"CREATE TABLE Product\
(\
 ProductId      INT IDENTITY (1, 1) NOT NULL ,\
 ProductName    VARCHAR(50) NOT NULL ,\
 SupplierId     INT NOT NULL ,\
 UnitPrice      DECIMAL(12,2) NULL ,\
 IsDiscontinued BIT NOT NULL CONSTRAINT DF_Product_IsDiscontinued DEFAULT ((0)) ,\
\
 PRIMARY KEY (ProductId ASC),\
 CONSTRAINT AK1_Product_SupplierId_ProductName UNIQUE  (SupplierId ASC, ProductName ASC),\
 FOREIGN KEY (SupplierId)\
  REFERENCES Supplier(SupplierId)\
);")

c.execute(
"CREATE TABLE Orden(\
 OrderId     INT IDENTITY (1, 1) NOT NULL ,\
 OrderNumber VARCHAR(10) NULL ,\
 CustomerId  INT NOT NULL ,\
 OrderDate   DATETIME NOT NULL CONSTRAINT DF_Order_OrderDate DEFAULT (getdate()) ,\
 TotalAmount DECIMAL(12,2) NOT NULL ,\
\
 PRIMARY KEY (OrderId ASC),\
 CONSTRAINT AK1_Order_OrderNumber UNIQUE (OrderNumber ASC),\
 FOREIGN KEY (CustomerId)\
  REFERENCES Customer(CustomerId)\
);")

c.execute(
"CREATE TABLE PurchaseOrder\
(\
 OrderId         INT NOT NULL ,\
 CustomerId      INT NOT NULL ,\
 TotalPrice      INT NOT NULL ,\
 Date            DATE NOT NULL ,\
 Payment         TINYINT NOT NULL ,\
 DeliveryAddress VARCHAR(50) NOT NULL ,\
 ExpDate         DATE NOT NULL ,\
 ListId          INT NOT NULL ,\
 SupplierId      INT NOT NULL ,\
\
 PRIMARY KEY (OrderId ASC, CustomerId ASC),\
 FOREIGN KEY (OrderId)\
  REFERENCES Orden(OrderId),\
 FOREIGN KEY (CustomerId)\
  REFERENCES Customer(CustomerId),\
 FOREIGN KEY (ListId)\
  REFERENCES Lists(ListId),\
 FOREIGN KEY (SupplierId)\
  REFERENCES Supplier(SupplierId)\
);")

c.execute(
"CREATE TABLE Ratings\
(\
 CustomerId INT NOT NULL ,\
 ProductId  INT NOT NULL ,\
 Rating     TINYINT NOT NULL ,\
\
 PRIMARY KEY (CustomerId ASC, ProductId ASC),\
 FOREIGN KEY (CustomerId)\
  REFERENCES Customer(CustomerId),\
 FOREIGN KEY (ProductId)\
  REFERENCES Product(ProductId)\
);")

c.execute(
"CREATE TABLE OrderItem\
(\
 OrderId   INT NOT NULL ,\
 ProductId INT NOT NULL ,\
 UnitPrice DECIMAL(12,2) NOT NULL ,\
 Quantity  INT NOT NULL ,\
\
 PRIMARY KEY (OrderId ASC, ProductId ASC),\
 FOREIGN KEY (OrderId)\
  REFERENCES Orden(OrderId),\
 FOREIGN KEY (ProductId)\
  REFERENCES Product(ProductId)\
);")

##### INSERT TEST
c.execute("INSERT INTO Schools VALUES (1,'INDEPENDENCIA AMERICANA','AV. INDEPENDENCIA 100',1)")
c.execute("INSERT INTO Supplier VALUES (1,'Tay Loy','34532435','AV. INDEPENDENCIA 20','Arequipa', 'Peru',054)")

### QUERY TEST
# Do this instead
#t = ('fsa',)
c.execute('SELECT * FROM Schools')
print c.fetchone()
c.execute('SELECT * FROM Supplier')
print c.fetchone()

"""
to_db = list()
for line in open("u.user","rb"):
	dr = line.split('|')
	to_db.append(tuple(dr))
c.executemany("INSERT INTO Users (user_id,age,gender,occupation,zip_code) VALUES (?,?,?,?,?)",to_db)

to_db = list()
for line in open("u.data","rb"):
	dr = line.split()
	to_db.append(tuple(dr))
c.executemany("INSERT INTO Ratings (user_id,movie_id,rating,timestamp) VALUES (?,?,?,?)",to_db)

to_db = list()
for line in open("u.item","rb"):
	dr = line.split("|")
	to_db.append(tuple(dr))
c.executemany("INSERT INTO Movies VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",to_db)
"""

conn.commit()
conn.close()
