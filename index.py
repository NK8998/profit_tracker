# Core libraries
import sqlite3
import datetime
from tkinter import *
import shutil
import hashlib
from customtkinter import *
import tkinter as tk
from PIL import Image
import datetime

from customtkinter import CTk, CTkLabel, CTkEntry, CTkButton

# helpers
from helpers.image_widget import add_image_widget
# helpers

# classes 
from classes.classes import User, ScreenManager
# classes

# 
from screens.users import user_screen
from screens.dashboard import dashboard_screen
from screens.products import product_screen
from screens.transactions import transaction_screen
# 


def main_screen(user_data):
    print(user_data)
    loggedInUserID = user_data['empID']

    screen_manager = ScreenManager()

    window_obj = CTk()
    window_obj.title("Profit Tracker")
    # window_obj.attributes('-fullscreen', True)
    window_obj.iconbitmap("./images/main/profit.ico")
    # Get the screen width and height
    screen_width = window_obj.winfo_screenwidth()
    screen_height = window_obj.winfo_screenheight()

    # Set the window size to match the screen size
    window_obj.geometry(f"{screen_width - 20}x{screen_height - 20}+0+0")
    window_obj.wm_minsize(1280, 720)

    mainMenuBar = Menu(window_obj, tearoff=0)
    window_obj.config(menu=mainMenuBar)
    optionsMenu = Menu(mainMenuBar)
    mainMenuBar.add_cascade(label="options", menu=optionsMenu)
    mainMenuBar.add_cascade(label=f"logged in as: {User.show_user(loggedInUserID)}")
    optionsMenu.add_command(label="About us")
    optionsMenu.add_command(label="Exit")

    
    # Configure columns for the layout
    window_obj.grid_columnconfigure(0, weight=0, minsize=300)  # Fixed-width column
    window_obj.grid_columnconfigure(1, weight=1)  # Expanding column

    # Configure rows to expand vertically
    window_obj.grid_rowconfigure(0, weight=1)

    # Create the first column with fixed width
    main_column1 = tk.Frame(window_obj, bg="white", width=300)
    main_column1.grid(row=0, column=0, sticky='nsew')

    main_column1.columnconfigure(index=0, weight=1)

    # Create the second column, which will take up the remaining space
    main_column2 = tk.Frame(window_obj, bg="#efefef")
    main_column2.grid(row=0, column=1, sticky='nsew')

    main_column2.columnconfigure(index=0, weight=1)
    main_column2.rowconfigure(index=0, weight=1)

    def reinitialize_main_column2(target_screen):
        if screen_manager.set_current_screen(target_screen)  == True:
            print('I ran')
            for widget in main_column2.winfo_children():
                widget.destroy()
            return True
        return False

    def desturi(title, message):  # hii ina act ka message box
        onTop = CTk()
        onTop.lift()
        onTop.title(title)
        onTop.iconbitmap("./images/main/profit.ico")
        onTop.attributes("-topmost", True)
        onTop.bell()
        if "UI" == "UI":
            lbl = CTkLabel(
                onTop,
                text=message,
                font=("sans-serif", 30, "bold"),
                bg_color="red",
            )
            lbl.pack(padx=10, pady=10)
        onTop.mainloop()

    def show_dashboard():
        dashboard_screen(reinitialize_main_column2, main_column2, user_data)

    def show_user():
        user_screen(reinitialize_main_column2, desturi, main_column2)

    def show_product():
        product_screen(reinitialize_main_column2, desturi, main_column2)

    def show_transaction():
        transaction_screen(reinitialize_main_column2, desturi, main_column2)

    def set_up_main():
        # main_column 1 children
        user_icon = add_image_widget(main_column1, "images/main/man-user-circle-icon.png", height=110, width=110)
        user_icon.grid(row=0, column=0, padx=10,pady=(40, 10), sticky='nsew')

        user = User.show_user_as_dict(loggedInUserID)[0]
        CTkLabel(
            main_column1, 
            text=f"{user['fname']} {user['lname']}", 
            font=("sans-serif", 19, 'bold'),
            text_color="#272727",
        ).grid(row=1, column=0, padx=10, pady=(10, 15), sticky="nsew")

        dashboard_btn = CTkButton(
            master=main_column1,
            text=" Dashboard",
            command=show_dashboard,
            font=("sans-serif", 14, "bold"),
            corner_radius=6,
            hover_color="#bde2ff",
            bg_color='white',
            fg_color="#f2f2f2",
            text_color='grey',
            border_width=1,
            border_color="#f2f2f2", 
            width=200,
            height=40,
            anchor='w',
            image=CTkImage(
                dark_image=Image.open("./images/main/dashboard.png"),
                light_image=Image.open("./images/main/dashboard.png"),
            ),
        )
        dashboard_btn.grid(
            row=2,
            column=0,
            pady=(10, 10),
            padx=10
        )  # Adjust the second value for more or less margin

        # entails show users create users
        if user_data['isAdmin'] == 1:
            users_btn = CTkButton(
                master=main_column1,
                text=" Users",
                command=show_user,
                font=("sans-serif", 14, "bold"),
                corner_radius=6,
                hover_color="#bde2ff",
                bg_color='white',
                fg_color="#f2f2f2",
                text_color='grey',
                border_width=1,
                border_color="#f2f2f2", 
                width=200,
                height=40,
                anchor='w',
                image=CTkImage(
                    dark_image=Image.open("./images/main/all_users.png"),
                    light_image=Image.open("./images/main/all_users.png"),
                ),
            )
            users_btn.grid(
                row=3,
                column=0,
                pady=(10, 10),
                padx=10
            )  # Adjust the second value for more or less margin


        # entails add products and show products
        products_btn = CTkButton(
            master=main_column1,
            text=" Products",
            command=show_product,
            font=("sans-serif", 14, "bold"),
            corner_radius=6,
            hover_color="#bde2ff",
            bg_color='white',
            fg_color="#f2f2f2",
            text_color='grey',
            border_width=1,
            border_color="#f2f2f2", 
            width=200,
            height=40,
            anchor='w',
            image=CTkImage(
                dark_image=Image.open("./images/main/show_products.png"),
                light_image=Image.open("./images/main/show_products.png"),
            ),
        )
        products_btn.grid(
            row=4,
            column=0,
            pady=(10, 10),
            padx=10
        ) 

        transaction_btn = CTkButton(
            master=main_column1,
            text=" Transactions",
            command=show_transaction,
            font=("sans-serif", 14, "bold"),
            corner_radius=6,
            hover_color="#bde2ff",
            bg_color='white',
            fg_color="#f2f2f2",
            text_color='grey',
            border_width=1,
            border_color="#f2f2f2", 
            width=200,
            height=40,
            anchor='w',
            image=CTkImage(
                dark_image=Image.open("./images/main/transactions.png"),
                light_image=Image.open("./images/main/transactions.png"),
            ),
        )
        transaction_btn.grid(
            row=5,
            column=0,
            pady=(10, 10),
            padx=10
        ) 
        logout_btn = CTkButton(
            master=main_column1,
            text=" Exit",
            command=show_transaction,
            font=("sans-serif", 14, "bold"),
            corner_radius=6,
            hover_color="#bde2ff",
            bg_color='white',
            fg_color="#f2f2f2",
            text_color='grey',
            border_width=1,
            border_color="#f2f2f2", 
            width=200,
            height=40,
            anchor='w',
            image=CTkImage(
                dark_image=Image.open("./images/main/logout.png"),
                light_image=Image.open("./images/main/logout.png"),
            ),
        )
        logout_btn.grid(
            row=6,
            column=0,
            pady=(10, 10),
            padx=10
        ) 
        show_dashboard()

    set_up_main()     

    window_obj.mainloop()


def login_screen():  # returns user ID of the logged-in 
    

    login_screen_obj = CTk()
    login_screen_obj.title("Login")
    login_screen_obj.iconbitmap("./images/main/profit.ico")
    global user_obj
    user_obj = None

    def validate_login():
        global user_obj
        email = emailInput.get()
        password = passwordInput.get()
        # print("here",User.show_user())
        user_data = User.verify_user(email, password) 
        print(user_data)
        if user_data == False:
            tempWindow = CTk()
            tempWindow.title("Wrong Password")
            tempWindow.iconbitmap("./images/main/profit.ico")
            tempWindow.bell()
            if "UI" == "UI":
                wp = CTkLabel(
                    tempWindow,
                    text="You have entered the wrong login details!",
                    font=("sans-serif", 30, "bold"),
                    bg_color="red",
                )
                wp.pack(padx=10, pady=10)
            tempWindow.mainloop()
        else:
            user_obj = user_data
            login_screen_obj.destroy()

    if "UI" == "UI":
        passwordInput = None
        emailInput = None
        column1 = None

        window_width = 1300
        window_height = 700

        screen_width = login_screen_obj.winfo_screenwidth()
        screen_height = login_screen_obj.winfo_screenheight()

        x_coordinate = (screen_width // 2) - (window_width // 2)
        y_coordinate = (screen_height // 2) - (window_height // 2)

        login_screen_obj.wm_geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")
        login_screen_obj.wm_maxsize(1400, 700)
        login_screen_obj.wm_minsize(500, 0)
        # Configure grid weights to make columns expand and fill width equally
        login_screen_obj.grid_columnconfigure(0, weight=1, minsize=500)
        login_screen_obj.grid_columnconfigure(1, weight=1, minsize=500)
        login_screen_obj.grid_rowconfigure(0, weight=1)


        def recalculateWidth(event):
            window_width = login_screen_obj.winfo_width()
            new_width = int(max(window_width / 2, 400))
            max_width = 400  # Define a maximum width for the input
            passwordInput.configure(width=int(min(new_width * 0.8, max_width)))
            emailInput.configure(width=int(min(new_width * 0.8, max_width)))

            # Configure column1's width
            if window_width <= 1050:
                 # Collapse column1
                login_screen_obj.grid_columnconfigure(0, minsize=0, weight=0) 
                column1.grid_forget() 
            else:
                 # Expand column1
                login_screen_obj.grid_columnconfigure(0, minsize=500, weight=1) 
                column1.grid(row=0, column=0, columnspan=1, sticky="nsew") 

        
        login_screen_obj.bind("<Configure>", recalculateWidth)
        ##### Column 1 start ####
        # Two side-by-side frames filling window equally
        column1 = tk.Frame(login_screen_obj, bg="#3A7FF6", width=550)
        column1.grid(row=0, column=0, columnspan=1, sticky='nsew')

        top_spacer_col1 = tk.Frame(column1)
        top_spacer_col1.pack(side='top', expand=True)

         # Inner content frame to center contents vertically within column1
        content_frame_col1 = tk.Frame(column1, bg="#3A7FF6")
        content_frame_col1.pack(side='top', expand=True)

        bottom_spacer_col1 = tk.Frame(column1)
        bottom_spacer_col1.pack(side='top', expand=True)

        #column 1 children 
        CTkLabel(
            content_frame_col1, 
            text="Welcome to the Profit Tracker App", 
            font=("sans-serif", 24, 'bold')
        ).grid(row=0, column=0, padx=10, pady=0, sticky="w")

        dash_width = int(550 * 0.2)  # 20% of the window width
        dash = tk.Canvas(
            content_frame_col1, 
            width=dash_width, 
            height=5, 
            bg="white", 
            borderwidth=0)
        dash.grid(row=1, column=0, sticky='w', padx=10, pady=(5, 10))

        CTkLabel(
            content_frame_col1, 
            text="We use state of the Art technologies to help keep your business afloat in the background while you deal with your customers at ease.", 
            font=("sans-serif", 15, 'normal'), 
            justify="left", 
            anchor='w', 
            wraplength=350
        ).grid(row=2, column=0, padx=10, pady=30, sticky="w")

        CTkLabel(
            content_frame_col1, 
            text= "Even the best of the best still rely on a Profit Tracker", 
            font=("sans-serif", 15), 
            wraplength=350, 
            justify="left").grid(row=3, column=0, padx=10, pady=20, sticky="w")
        #column 1 children
        #### Column 1 end ####


        #### Column 2 start ####
        column2 = tk.Frame(login_screen_obj, bg="white", width=550)
        column2.grid(row=0, column=1, columnspan=1, sticky='nsew')

        top_spacer_col2 = tk.Frame(column2)
        top_spacer_col2.pack(side='top', expand=True)

        # Inner content frame to center contents vertically within column1
        content_frame_col2 = tk.Frame(column2, bg="white")
        content_frame_col2.pack(side='top', expand=True)

        bottom_spacer_col2 = tk.Frame(column2)
        bottom_spacer_col2.pack(side='top', expand=True)

        #column 2 children
        CTkLabel(
            content_frame_col2, 
            text="Enter Your Details", 
            font=("sans-serif", 25, 'bold'), 
            text_color='#515486'
        ).grid(row=0, column=0, padx=10, pady=15, sticky='w')
        CTkLabel(
            content_frame_col2, 
            text="Email:", 
            font=("sans-serif", 14), 
            anchor='w', 
            text_color='#515486'
        ).grid(row=1, column=0, padx=10, pady=(10, 5), sticky='w')
        emailInput = CTkEntry(
            content_frame_col2, 
            font=("sans-serif", 14), 
            corner_radius=12, 
            height=55, 
            border_width=0, 
            bg_color='transparent', 
            fg_color='#F1F5FF',
            text_color='black'
            )
        emailInput.grid(row=2, column=0, padx=10, pady=(0, 10), sticky='w')

        CTkLabel(
            content_frame_col2, 
            text="Password: ", 
            font=("sans-serif", 14), 
            anchor='w', 
            text_color='#515486'
        ).grid(row=3, column=0, padx=10, pady=(10, 5), sticky='w')
        passwordInput = CTkEntry(
            content_frame_col2, show="*", 
            font=("sans-serif", 14), 
            corner_radius=12, 
            height=55, 
            border_width=0, 
            bg_color='transparent', 
            fg_color='#F1F5FF',
            text_color='black'
            )
        passwordInput.grid(row=4, column=0, padx=10, pady=(0, 10), sticky='w')

        login_button = CTkButton(
            content_frame_col2,
            text="Login",
            command=validate_login,
            font=("sans-serif", 13, "bold"),
            text_color='white',
            hover_color="#4158D0",
            corner_radius=1000,
            height=45,
            fg_color='#3A7FF6'
        )
        login_button.grid(row=5, column=0, columnspan=2, pady=(50, 0))
        ### Column2 end ###

    login_screen_obj.mainloop()
    return user_obj

def databases_initialisations():
    conn = sqlite3.connect("./databases/users.db")
    curr = conn.cursor()
    with conn:  # creating ADMIN account in the database
        curr.execute(
            """ 
            CREATE TABLE IF NOT EXISTS users(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            empID TEXT UNIQUE,
                            email TEXT UNIQUE,
                            fname TEXT,
                            lname TEXT,
                            salary INTEGER,
                            nationalID NUMERIC,
                            password TEXT,
                            isAdmin INTEGER
                            )
            """
        )
                # Check if the admin user exists, and if not, insert it
        if len(curr.execute("SELECT * FROM users").fetchall()) < 1:
            unique_id = 'IYU2SF7'
            curr.execute(
                "INSERT INTO users(empID, email, fname, lname, salary, nationalID, password, isAdmin) VALUES(?, ?, ?, ?, ?, ?, ?, ?)",
                (unique_id, 'admin@gmail.com', 'admin', 'Overseer', 400000, 987456, '12378956', 1)
            )
    conn = sqlite3.connect("./databases/products.db")
    conn = sqlite3.connect("./databases/transactions.db")
    conn.close()

def _DEBUG_():
    if "users" == "users":
        conn = sqlite3.connect("./databases/users.db")
        curr = conn.cursor()

        def createTable():
            with conn:
                curr.execute(
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

        def insert(empID, fname, lname, salary, nationalID, password, isAdmin):
            with conn:  # add self. and delete above variables
                curr.execute(
                    "INSERT INTO users(empID,fname,lname,salary,nationalID,isAdmin) VALUES(:empID,:fname,:lname,:salary,:nationalID,:isAdmin)",
                    {
                        "empID": empID,
                        "fname": fname,
                        "lname": lname,
                        "salary": salary,
                        "nationalID": nationalID,
                        "password": password,
                        "isAdmin": isAdmin,
                    },
                )

        def read():
            curr.execute("SELECT * FROM users")
            for line in curr.fetchall():
                # print(line)
                pass

        def update(id=-1):
            with conn:
                curr.execute("UPDATE users SET empID=669 WHERE id=:id", {"id": id})

        def delete(id=-1):
            with conn:
                curr.execute("DELETE FROM users WHERE id=:id", {"id": id})

        def misc(option="DELETEALL"):
            if option == "DELETEALL":
                with conn:
                    curr.execute("DELETE FROM users")
            if 0:
                # print(curr.execute("SELECT * FROM users").arraysize)
                pass

            if "0" == "schema":
                curr.execute("SELECT name FROM sqlite_master WHERE type='table';")
                tables = curr.fetchall()

                print("Tables in the database:")
                for table in tables:
                    print(table[0])

                for table in tables:
                    table_name = table[0]
                    print(f"\nData from table '{table_name}':")

                    curr.execute(f"PRAGMA table_info('{table_name}');")
                    columns = curr.fetchall()

                    column_names = []
                    primary_keys = set()

                    for column in columns:
                        (
                            column_id,
                            column_name,
                            column_type,
                            not_null,
                            default_value,
                            primary_key,
                        ) = column
                        column_names.append(column_name)
                        if primary_key:
                            primary_keys.add(column_name)

                    curr.execute(f"SELECT * FROM '{table_name}';")
                    rows = curr.fetchall()

                    header = " | ".join(column_names)
                    print(header)

                    for row in rows:
                        formatted_row = []
                        for column_name, value in zip(column_names, row):
                            if column_name in primary_keys:
                                formatted_row.append(
                                    f" {value}"
                                )  # Indicate primary key values
                            else:
                                formatted_row.append(str(value))
                        print(" | ".join(formatted_row))

        createTable()
        # read()
        # misc()
        # insert(1,"Admin","Istrator",100000,12378956,"pass123", True)
        # insert(23, "Lina", "Khan", 75000, 123456, "mypassword", True)
        # insert(89, "Sam", "Lee", 65000, 987654, "securepass", False)
        # insert(45, "Maya", "Patel", 80000, 654321, "helloWorld!", True)
        # misc("DELETEALL")
        # update(7)
        # delete(7)
        read()

    if "products" == "products":
        conn = sqlite3.connect("./databases/products.db")
        curr = conn.cursor()

        def createTable():
            with conn:
                curr.execute(
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

        def insert(prodID, name, descripton, quantity, price, image):
            hash_value = hashlib.sha256(b"GrOuP 9").hexdigest()
            ext = image.split("/")[5].split(".")[-1]

            with conn:  # add self. and delete above variables
                curr.execute(
                    "INSERT INTO products (prodID,name,descripton,quantity,price,image) VALUES(:prodID,:name,:descripton,:quantity,:price,:image)",
                    {
                        "prodID": prodID,
                        "name": name,
                        "descripton": descripton,
                        "quantity": quantity,
                        "price": price,
                        "image": image,
                    },
                )
                shutil.copy(image, "./images/products/" + hash_value + "." + ext)

        def read():
            print("*****************")
            curr.execute("SELECT * FROM products")
            for line in curr.fetchall():
                print(line)
            print("*****************")

        def delete(id):
            with conn:
                curr.execute("DELETE FROM products WHERE id = :id", {"id": id})

        if 0:
            with conn:
                curr.execute("DELETE FROM products")

        createTable()
        # read()
        # insert(
        #     5522,
        #     "Roba",
        #     "Bato",
        #     50000,
        #     223,
        #     "C:/Users/Roberrrto/Pictures/Screenshots/Screenshot 2024-10-06 143800.png",
        # )
        # insert(
        #     2566,
        #     "jaba",
        #     "babab",
        #     50000,
        #     223,
        #     "C:/Users/Roberrrto/Pictures/Screenshots/Screenshot 2024-10-06 143800.png",
        # )
        # insert(
        #     45853,
        #     "dwdwd",
        #     "BWWFWQFEWFato",
        #     50000,
        #     223,
        #     "C:/Users/Roberrrto/Pictures/Screenshots/Screenshot 2024-10-06 143800.png",
        # )
        # insert(
        #     54823,
        #     "EWEWRGRWT",
        #     "BFEFEGFEWGEato",
        #     50000,
        #     223,
        #     "C:/Users/Roberrrto/Pictures/Screenshots/Screenshot 2024-10-06 143800.png",
        # )

        # read()
        # delete(24)

    if "transactions" == "transactions":
        conn = sqlite3.connect("./databases/transactions.db")
        curr = conn.cursor()
        if 1:
            with conn:
                curr.execute(
                    """ CREATE TABLE IF NOT EXISTS transactions (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        receiptID INTEGER,
                        empID INTEGER,
                        prodID INTEGER,
                        quantity INTEGER,
                        discount INTEGER,
                        time NUMERIC
                        )"""
                )

        if 0:
            idHotfix = 0
            with conn:
                curr.execute("SELECT * FROM transactions")
                idHotfix = len(curr.fetchall())
            idHotfix += 1

            receiptID = 47
            empID = 54
            prodID = 35
            quantity = 69
            discount = 1
            time = datetime.datetime(2019, 1, 3, 14, 53, 38, 596477).isoformat()
            with conn:  # add self. and delete above variables
                curr.execute(
                    "INSERT INTO transactions VALUES(:idHotfix,:receiptID,:empID,:prodID,:quantity,:discount,:time)",
                    {
                        "idHotfix": idHotfix,
                        "receiptID": receiptID,
                        "empID": empID,
                        "prodID": prodID,
                        "quantity": quantity,
                        "discount": discount,
                        "time": time,
                    },
                )

        if 0:
            with conn:
                curr.execute("SELECT * FROM transactions")
                print(curr.fetchall())
        if 0:
            pass
        if 0:
            __pili__ = 35
            with conn:
                curr.execute(
                    "DELETE FROM users WHERE empID = :__pili__", {"__pili__": __pili__}
                )


if __name__ == "__main__":
    databases_initialisations()
    # _DEBUG_()
    # print()  # returns user who logged in

    # user_obj = login_screen()
    #'IYU2SF7'

    user_obj = {'id': 1, 'empID': 'IYU2SF7', 'email': 'admin@gmail.com', 'fname': 'admin', 'lname': 'Overseer', 'salary': 400000, 'nationalID': 987456, 'password': '12378956', 'isAdmin': 1}

    # if user_obj:
    main_screen(user_obj)
    # User.show_user(35)

    # _DEBUG_()
