import sqlite3
import shutil
import hashlib



class ScreenManager:
    def __init__(self, initial_screen=None):
        # Initialize with an initial screen if provided
        self._current_screen = initial_screen

    def get_current_screen(self):
        # Getter method for current_screen
        return self._current_screen

    def set_current_screen(self, target_screen):
        # Setter method to update the screen
        if self._current_screen != target_screen:
            self._current_screen = target_screen
            return True  # Indicate that a change occurred
        return False  # No change needed

class User:
    def __init__(
        self, empID, fname, lname, salary, nationalID, password, isAdmin
    ) -> None:
        # some fields not in table
        self.empID = empID
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.nationalID = nationalID
        self.password = password
        self.isAdmin = False
        self.conn = sqlite3.connect("./databases/users.db")
        self.curr = self.conn.cursor()
        with self.conn:
            self.curr.execute(
                """ CREATE TABLE IF NOT EXISTS users(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            empID INTEGER UNIQUE,
                            fname TEXT,
                            lname TEXT,
                            salary INTEGER,
                            nationalID NUMERIC
                            password TEXT,
                            isAdmin BLOB
                            )"""
            )
        self.conn.close()

    def create_user(self):
        conn = sqlite3.connect("./databases/users.db")
        curr = conn.cursor()
        with conn:
            curr.execute(
                "INSERT INTO users(empID,fname,lname,salary,nationalID,isAdmin) VALUES(:empID,:fname,:lname,:salary,:nationalID,:isAdmin)",
                {
                    "empID": self.empID,
                    "fname": self.fname,
                    "lname": self.lname,
                    "salary": self.salary,
                    "nationalID": self.nationalID,
                    "isAdmin": self.isAdmin,
                },
            )

    def show_user(loggedInUserID=None):
        conn = sqlite3.connect("./databases/users.db")
        curr = conn.cursor()
        if loggedInUserID:
            return curr.execute(f"SELECT * FROM users WHERE empID = {loggedInUserID}").fetchone()[2]
        else:
            with conn:
                return curr.execute("SELECT * FROM users").fetchall()
            
    def show_user_as_dict(loggedInUserID=None):
        conn = sqlite3.connect("./databases/users.db")
        conn.row_factory = sqlite3.Row
        curr = conn.cursor()
        with conn:
            curr.execute(f"SELECT * FROM users WHERE empID = {loggedInUserID}")
            rows = curr.fetchall()
        
            # Convert rows to a list of dictionaries
            return [dict(row) for row in rows]

            
    def get_total_users():
        conn = sqlite3.connect("./databases/users.db")
        curr = conn.cursor()
        with conn:
            curr.execute("SELECT  COUNT(*) FROM users")
            return curr.fetchone()[0]



    def update_user(id, empID, fname, lname, salary, nationalID):
        conn = sqlite3.connect("./databases/users.db")
        curr = conn.cursor()
        with conn:
            # curr.execute("UPDATE users SET empID=669 WHERE id=:id", {"id": id})
            curr.execute(
                "UPDATE users SET empID=:empID,fname=:fname,lname=:lname,salary=:salary,nationalID=:nationalID WHERE id=:id",
                {
                    "id": id,
                    "empID": empID,
                    "fname": fname,
                    "lname": lname,
                    "salary": salary,
                    "nationalID": nationalID,
                },
            )

    def delete_user(id):
        conn = sqlite3.connect("./databases/users.db")
        curr = conn.cursor()
        with conn:
            curr.execute("DELETE FROM users WHERE id=:id", {"id": id})

class Product:
    # ?inventory?
    # "INSERT INTO products VALUES(:prodID,:name,:descripton,:quantity,:price,:image)",
    def __init__(self, prodID, name, descripton, quantity, price, image) -> None:
        self.prodID = prodID
        self.name = name
        self.descripton = descripton
        self.quantity = quantity
        self.price = price
        self.image = image
        self.conn = sqlite3.connect("./databases/products.db")
        self.curr = self.conn.cursor()
        with self.conn:
            self.curr.execute(
                """ CREATE TABLE IF NOT EXISTS products(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    prodID INTEGER UNIQUE,
                    name TEXT,
                    descripton TEXT,
                    quantity INTEGER,
                    price INTEGER,
                    image TEXT
                    )"""
            )
        self.conn.close()

    def create_product(self):
        conn = sqlite3.connect("./databases/products.db")
        curr = conn.cursor()
        hash_value = hashlib.sha256(b"GrOuP 9").hexdigest()
        ext = self.image.split(".")[-1]

        with conn:  # add self. and delete above variables
            curr.execute(
                "INSERT INTO products (prodID,name,descripton,quantity,price,image) VALUES(:prodID,:name,:descripton,:quantity,:price,:image)",
                {
                    "prodID": self.prodID,
                    "name": self.name,
                    "descripton": self.descripton,
                    "quantity": self.quantity,
                    "price": self.price,
                    "image": hash_value + "." + ext,
                },
            )
            shutil.copy(self.image, "./images/products/" + hash_value + "." + ext)

    def show_product():
        conn = sqlite3.connect("./databases/products.db")
        curr = conn.cursor()
        with conn:
            curr.execute("SELECT * FROM products")
            return curr.fetchall()
        
    def get_products_as_Dict():
        conn = sqlite3.connect("./databases/products.db")
        conn.row_factory = sqlite3.Row
        curr = conn.cursor()
        with conn:
            curr.execute("SELECT * FROM products")
            rows = curr.fetchall()
        
            # Convert rows to a list of dictionaries
            return [dict(row) for row in rows]


    def update_product(id, prodID, name, descripton, quantity, price, image="PATCH"):
        conn = sqlite3.connect("./databases/products.db")
        curr = conn.cursor()
        with conn:
            curr.execute(
                "UPDATE products SET prodID=:prodID,name=:name,descripton=:descripton,quantity=:quantity,price=:price WHERE id=:id",
                {
                    "id": id,
                    "prodID": prodID,
                    "name": name,
                    "descripton": descripton,
                    "quantity": quantity,
                    "price": price,
                    # "image": image, PATCH nilisahau kuchukua edited picture
                },
            )

    def delete_product(id):
        conn = sqlite3.connect("./databases/products.db")
        curr = conn.cursor()
        with conn:
            curr.execute("DELETE FROM products WHERE id = :id", {"id": id})

class Transaction:
    # ?receipt? - show transcations made by a person at a time
    # ?total cost? of receipt
    # the price is already there or else there are discounts
    def __init__(self, madeByEmpID, prodID, quantity, price, time) -> None:
        self.empID = madeByEmpID
        self.prodID = prodID
        self.quantity = quantity
        self.price = price
        self.time = time
        self.receiptID = 77  # edit records from tbl
        self.discount = 0
        self.conn = sqlite3.connect("./databases/transactions.db")
        self.curr = self.conn.cursor()
        with self.conn:
            self.curr.execute("ATTACH DATABASE 'products.db' AS products")
            self.curr.execute("ATTACH DATABASE 'users.db' AS users")
            self.curr.execute(
                """ CREATE TABLE IF NOT EXISTS transactions (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        receiptID INTEGER,
                        empID INTEGER,
                        prodID INTEGER,
                        quantity INTEGER,
                        discount INTEGER,
                        time NUMERIC,
                        FOREIGN KEY (prodID) REFERENCES products(id),
                        FOREIGN KEY (empID) REFERENCES users(id)
                        )"""
            )
        self.conn.close()

    def create_transaction(self):
        # receipt id ndio itahold all transactions made at the same time na ita act ka receipt
        conn = sqlite3.connect("./databases/transactions.db")
        curr = conn.cursor()
        idHotfix = 0
        with conn:
            curr.execute("SELECT * FROM transactions")
            idHotfix = len(curr.fetchall())
        idHotfix += 1
        with conn:
            curr.execute(
                "INSERT INTO transactions(receiptID,empID,prodID,quantity,discount,time) VALUES(:receiptID,:empID,:prodID,:quantity,:discount,:time)",
                {
                    "receiptID": self.receiptID,
                    "empID": self.empID,
                    "prodID": self.prodID,
                    "quantity": self.quantity,
                    "discount": self.discount,
                    "time": self.time,
                },
            )

    def show_transaction():
        conn = sqlite3.connect("./databases/transactions.db")
        curr = conn.cursor()
        with conn:
            return curr.execute("SELECT * FROM transactions").fetchall()
        
    def get_transcations_as_Dict():
        conn = sqlite3.connect("./databases/transactions.db")
        conn.row_factory = sqlite3.Row
        curr = conn.cursor()
        with conn:
            curr.execute("SELECT * FROM transactions")
            rows = curr.fetchall()
        
            # Convert rows to a list of dictionaries
            return [dict(row) for row in rows]

    def update_transaction(
        id, receiptID, empID, prodID, quantity, discount, time
    ) -> None:
        conn = sqlite3.connect("./databases/transactions.db")
        curr = conn.cursor()
        with conn:
            curr.execute(
                " UPDATE transactions  SET receiptID=:receiptID,empID=:empID,prodID=:prodID,quantity=:quantity,discount=:discount,time=:time WHERE id = :id",
                {
                    "id": id,
                    "receiptID": receiptID,
                    "empID": empID,
                    "prodID": prodID,
                    "quantity": quantity,
                    "discount": discount,
                    "time": time,
                },
            )

    def delete_transaction(id):
        conn = sqlite3.connect("./databases/transactions.db")
        curr = conn.cursor()
        with conn:
            curr.execute(
                "DELETE FROM transactions WHERE id = :id",
                {"id": id},
            )
            # print(curr.fetchall())

class Receipt:  # hii tuta angalia
    pass