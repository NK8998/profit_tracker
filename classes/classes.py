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
        self, empID, email, fname, lname, salary, nationalID, password, isAdmin
    ) -> None:
        # some fields not in table
        self.empID = empID
        self.email = email
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.nationalID = nationalID
        self.password = password
        self.isAdmin = isAdmin
        self.conn = sqlite3.connect("./databases/users.db")
        self.curr = self.conn.cursor()
        with self.conn:
            self.curr.execute(
                """ CREATE TABLE IF NOT EXISTS users(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            empID TEXT UNIQUE,
                            email TEXT UNIQUE,
                            fname TEXT,
                            lname TEXT,
                            salary INTEGER,
                            nationalID NUMERIC
                            password TEXT,
                            isAdmin INTEGER
                            )"""
            )
        self.conn.close()

    def create_user(self):
        conn = sqlite3.connect("./databases/users.db")
        curr = conn.cursor()
        with conn:
            curr.execute(
                "INSERT INTO users(empID, email,fname,lname,salary,nationalID,password,isAdmin) VALUES(:empID,:email,:fname,:lname,:salary,:nationalID,:password,:isAdmin)",
                {
                    "empID": self.empID,
                    "email": self.email,
                    "fname": self.fname,
                    "lname": self.lname,
                    "salary": self.salary,
                    "nationalID": self.nationalID,
                    "password": self.password,
                    "isAdmin": self.isAdmin,
                },
            )

    def show_user(loggedInUserID=None):
        conn = sqlite3.connect("./databases/users.db")
        curr = conn.cursor()
        
        # Show specific user if ID provided
        if loggedInUserID:
            curr.execute("SELECT * FROM users WHERE empID = ?", (loggedInUserID,))
            user_data = curr.fetchone()
            
            # Return the third column if user exists, else return None
            if user_data:
                return user_data[3]  # Replace [2] with the specific column index/name if necessary
            else:
                return None
        else:
            # Show all users if no ID is provided
            with conn:
                return curr.execute("SELECT * FROM users").fetchall()
    
    def verify_user(email, password):
        conn = sqlite3.connect("./databases/users.db")
        conn.row_factory = sqlite3.Row  # This makes rows return as dictionaries
        curr = conn.cursor()
        
        with conn:
            result = curr.execute(
                "SELECT * FROM users WHERE email = ? AND password = ?", (email, password)
            ).fetchone()
            
            if result:
                # Convert the Row to a dictionary
                return dict(result)
            else:
                return False

            
    def show_user_as_dict(loggedInUserID=None):
        conn = sqlite3.connect("./databases/users.db")
        conn.row_factory = sqlite3.Row
        curr = conn.cursor()
        with conn:
            curr.execute("SELECT * FROM users WHERE empID = ?", (loggedInUserID,))
            rows = curr.fetchall()
        
            # Convert rows to a list of dictionaries
            return [dict(row) for row in rows]

            
    def get_total_users():
        conn = sqlite3.connect("./databases/users.db")
        curr = conn.cursor()
        with conn:
            curr.execute("SELECT  COUNT(*) FROM users")
            return curr.fetchone()[0]



    def update_user(empID, email, fname, lname, salary, nationalID, password):
        conn = sqlite3.connect("./databases/users.db")
        curr = conn.cursor()
        with conn:
            # curr.execute("UPDATE users SET empID=669 WHERE id=:id", {"id": id})
            curr.execute(
                "UPDATE users SET email=:email,fname=:fname,lname=:lname,salary=:salary,nationalID=:nationalID,password=:password WHERE empID=:empID",
                {
                    "email": email,
                    "fname": fname,
                    "lname": lname,
                    "salary": salary,
                    "nationalID": nationalID,
                    "password": password,
                    "empID": empID
                },
            )

    def delete_user(empID):
        conn = sqlite3.connect("./databases/users.db")
        curr = conn.cursor()
        with conn:
            curr.execute("DELETE FROM users WHERE empID=:empID", {"empID": empID})

class Product:
    # ?inventory?
    # "INSERT INTO products VALUES(:prodID,:name,:descripton,:quantity,:price,:image)",
    def __init__(self, prodID, name, descripton, quantity, buying_price, selling_price) -> None:
        self.prodID = prodID
        self.name = name
        self.descripton = descripton
        self.quantity = quantity
        self.buying_price = buying_price
        self.selling_price = selling_price
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
                    buying_price INTEGER,
                    selling_price INTEGER
                    )"""
            )
        self.conn.close()

    def create_product(self):
        conn = sqlite3.connect("./databases/products.db")
        curr = conn.cursor()
        # hash_value = hashlib.sha256(b"GrOuP 9").hexdigest()
        # ext = self.image.split(".")[-1]

        with conn:  # add self. and delete above variables
            curr.execute(
                "INSERT INTO products (prodID,name,descripton,quantity,buying_price, selling_price) VALUES(:prodID,:name,:descripton,:quantity,:buying_price,:selling_price)",
                {
                    "prodID": self.prodID,
                    "name": self.name,
                    "descripton": self.descripton,
                    "quantity": self.quantity,
                    "buying_price": self.buying_price,
                    "selling_price": self.selling_price,
                },
            )
            # shutil.copy(self.image, "./images/products/" + hash_value + "." + ext)

    def show_product():
        conn = sqlite3.connect("./databases/products.db")
        curr = conn.cursor()
        with conn:
            curr.execute("SELECT * FROM products")
            return curr.fetchall()
        
    def get_specific_product(podID):
        conn = sqlite3.connect("./databases/products.db")
        conn.row_factory = sqlite3.Row
        curr = conn.cursor()
        with conn:
            curr.execute("SELECT * FROM products WHERE prodID = ?", (podID,))
            row = curr.fetchone()  # Use fetchone to get a single row
            return dict(row) if row else None  # Convert to dict and handle if no row is found
  
    def get_products_as_Dict():
        conn = sqlite3.connect("./databases/products.db")
        conn.row_factory = sqlite3.Row
        curr = conn.cursor()
        with conn:
            curr.execute("SELECT * FROM products")
            rows = curr.fetchall()
        
            # Convert rows to a list of dictionaries
            return [dict(row) for row in rows]
    
    def filter_products_as_Dict(query):
        conn = sqlite3.connect("./databases/products.db")
        conn.row_factory = sqlite3.Row
        curr = conn.cursor()
        with conn:
            curr.execute("SELECT * FROM products WHERE name LIKE ?", ('%' + query + '%',))
            rows = curr.fetchall()

            # Convert rows to a list of dictionaries
            return [dict(row) for row in rows]



    def update_product(prodID, name=None, description=None, quantity=None, buying_price=None, selling_price=None):
        conn = sqlite3.connect("./databases/products.db")
        curr = conn.cursor()
        
        # Start building the dynamic query
        query = "UPDATE products SET prodID=:prodID, "
        updates = []
        params = {}

        # Ensure prodID is always part of the WHERE clause
        params["prodID"] = prodID
        # Add fields to update only if they are not None
        if name is not None:
            updates.append("name=:name")
            params["name"] = name
        if description is not None:
            updates.append("descripton=:descripton")
            params["descripton"] = description
        if quantity is not None:
            updates.append("quantity=:quantity")
            params["quantity"] = quantity
        if buying_price is not None:
            updates.append("buying_price=:buying_price")
            params["buying_price"] = buying_price
        if selling_price is not None:
            updates.append("selling_price=:selling_price")
            params["selling_price"] = selling_price

        # Join the updates into the query
        query += ", ".join(updates) + " WHERE prodID=:prodID"

        # Execute the query
        with conn:
            curr.execute(query, params)

    def delete_product(prodID):
        conn = sqlite3.connect("./databases/products.db")
        curr = conn.cursor()
        with conn:
            curr.execute("DELETE FROM products WHERE prodID = :prodID", {"prodID": prodID})

class Transaction:
    # ?receipt? - show transcations made by a person at a time
    # ?total cost? of receipt
    # the price is already there or else there are discounts
    def __init__(self, transactionID, madeByEmpID, empName, prodName, prodID, quantity, buying_price, selling_price, discount, time) -> None:
        self.transactionID = transactionID  # edit records from tbl
        self.empID = madeByEmpID
        self.empName = empName
        self.prodID = prodID
        self.prodName = prodName
        self.quantity = quantity
        self.buying_price = buying_price
        self.selling_price = selling_price
        self.discount = discount
        self.time = time
        self.conn = sqlite3.connect("./databases/transactions.db")
        self.curr = self.conn.cursor()
        with self.conn:
            self.curr.execute(
                """ CREATE TABLE IF NOT EXISTS transactions (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        transactionID INTEGER,
                        empID INTEGER,
                        empName TEXT,
                        prodID INTEGER,
                        prodName TEXT,
                        quantity INTEGER,
                        price INTEGER,
                        discount INTEGER,
                        time NUMERIC
                        )"""
            )
        self.conn.close()

    def create_transaction(self):
        # receipt id ndio itahold all transactions made at the same time na ita act ka receipt
        conn = sqlite3.connect("./databases/transactions.db")
        curr = conn.cursor()
        with conn:
            curr.execute(
                "INSERT INTO transactions(transactionID,empID,empName,prodID,prodName,quantity,buying_price,selling_price,discount,time) VALUES(:transactionID,:empID,:empName,:prodID,:prodName,:quantity,:buying_price,:selling_price,:discount,:time)",
                {
                    "transactionID" : self.transactionID,
                    "empID": self.empID,
                    "empName": self.empName,
                    "prodID": self.prodID,
                    "prodName": self.prodName,
                    "quantity": self.quantity,
                    "buying_price": self.buying_price,
                    "selling_price": self.selling_price,
                    "discount": self.discount,
                    "time": self.time,
                },
            )

    def show_transaction():
        conn = sqlite3.connect("./databases/transactions.db")
        curr = conn.cursor()
        with conn:
            return curr.execute("SELECT transactionID, empName, prodName, quantity, buying_price, selling_price, discount, time FROM transactions").fetchall()
        
    def get_transcations_as_Dict():
        conn = sqlite3.connect("./databases/transactions.db")
        conn.row_factory = sqlite3.Row
        curr = conn.cursor()
        with conn:
            curr.execute("SELECT * FROM transactions")
            rows = curr.fetchall()
        
            # Convert rows to a list of dictionaries
            return [dict(row) for row in rows]

    def update_transaction(transactionID, quantity, discount
    ) -> None:
        conn = sqlite3.connect("./databases/transactions.db")
        curr = conn.cursor()
        with conn:
            curr.execute(
                " UPDATE transactions  SET quantity=:quantity,discount=:discount WHERE transactionID = :transactionID",
                {
                    "transactionID":transactionID,
                    "quantity": quantity,
                    "discount": discount
                },
            )
    def get_top_5_products_based_on_transactions():
        conn = sqlite3.connect("./databases/transactions.db")
        curr = conn.cursor()

        with conn:
            # SQL query to calculate profit grouped by prodID
            curr.execute("""
                SELECT 
                    prodName, 
                    SUM((selling_price - buying_price) * quantity) AS total_profit
                FROM transactions
                GROUP BY prodName
                ORDER BY total_profit DESC
                LIMIT 5
            """)

            # Fetch the results
            top_products = curr.fetchall()

        # Close the connection
        conn.close()

        # Return the top 5 products as a dictionary
        return {row[0]: row[1] for row in top_products}



    def delete_transaction(transactionID):
        conn = sqlite3.connect("./databases/transactions.db")
        curr = conn.cursor()
        with conn:
            curr.execute(
                "DELETE FROM transactions WHERE transactionID = :transactionID",
                {"transactionID": transactionID},
            )
            # print(curr.fetchall())

class Receipt:  # hii tuta angalia
    pass

class PanelManager:
    def __init__(self, initial_panel=None):
        # Initialize with an initial screen if provided
        self._current_panel = initial_panel

    def get_current_panel(self):
        # Getter method for current_screen
        return self._current_panel

    def set_current_panel(self, target_panel):
        # Setter method to update the screen
        if self._current_panel != target_panel:
            self._current_panel = target_panel
            return True  # Indicate that a change occurred
        return False  # No change needed
    