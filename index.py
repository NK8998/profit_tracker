# Core libraries
import sqlite3
import datetime
from tkinter import *
from tkinter import filedialog, messagebox, ttk
import shutil
import hashlib
import customtkinter as ctk
from customtkinter import *
import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import datetime
from tkinter import Toplevel, Label, Entry, Button, messagebox, StringVar, ttk

from customtkinter import CTk, CTkLabel, CTkEntry, CTkButton
from tkinter import PhotoImage

# matplotlib
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#matplotlib

# nanoid
from nanoid import generate
# nanoid

# helpers
from helpers.image_widget import add_image_widget
from helpers.panel_generator import generate_panel
# helpers

# classes 
from classes.classes import User, Product, Transaction, ScreenManager, Receipt, PanelManager
# classes


# 
from mock_data import profits_per_week, profit_per_user
# 
def main_screen(loggedInUserID):

    print(loggedInUserID)

    screen_manager = ScreenManager()

    window_obj = CTk()
    window_obj.title("Profit Tracker")
    window_obj.iconbitmap("./images/main/profit.ico")
    # Get the screen width and height
    screen_width = window_obj.winfo_screenwidth()
    screen_height = window_obj.winfo_screenheight()

    # Set the window size to match the screen size
    window_obj.geometry(f"{screen_width}x{screen_height}+0+0")
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


    def show_dashboard():
        should_refresh = reinitialize_main_column2('dashboard')
        if not should_refresh:
            return
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
         # main_column 1 children
        #  main_column 2 children

        # Setup scrollable frame

        main_page_frame = CTkScrollableFrame(master=main_column2, fg_color="#efefef", corner_radius=0)
        main_page_frame.grid(row=0, column=0, sticky=NSEW)

        main_page_frame.columnconfigure(index=0, weight=1)

        CTkLabel(
            main_page_frame, 
            text="Dashboard", 
            font=("sans-serif", 16, 'bold'),
            text_color="grey",
        ).grid(row=0, column=0, padx=10, pady=(10, 15), sticky="W")

        chart_row_frame = CTkScrollableFrame(master=main_page_frame, fg_color='white', bg_color='white', height=350, orientation='horizontal')
        chart_row_frame.grid(row=1, column=0, padx=10, pady=20, sticky=NSEW)

        chart_row_frame.rowconfigure(index=0, weight=1)  
        # chart_row_frame.grid_columnconfigure(0, weight=1)  # For the bar chart
        chart_row_frame.columnconfigure(0, weight=1)  # For the pie chart 
        chart_row_frame.columnconfigure(1, weight=1)  # For the pie chart 
        chart_row_frame.columnconfigure(2, weight=1)  # For the pie chart 


        # chart_row_frame.grid_propagate(False)

        plt.rcParams["axes.prop_cycle"] = plt.cycler(
            color=["#44BEE3", "#4E63E5", "#679EE0", "#3DB5E0", "#2274E6"])
        
        # BAR_CHART
        # Create the bar chart figure
        fig = Figure(figsize=(6, 3), dpi=100)
        ax = fig.add_subplot(111)
        ax.bar(profits_per_week.keys(), profits_per_week.values())
        ax.set_title("Profit per Week")
        ax.set_xlabel("Week")
        ax.set_ylabel("Profits")

        # Embed the figure into the Tkinter frame
        canvas = FigureCanvasTkAgg(fig, master=chart_row_frame)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0, padx=10, pady=10, sticky='nse')


        # Create the pie chart figure
        fig2 = Figure(figsize=(5, 3), dpi=100)
        ax2 = fig2.add_subplot(111)
        ax2.pie(profit_per_user.values(), labels=profit_per_user.keys(), autopct='%1.1f%%', startangle=140)
        ax2.set_title("Profit per User")

        # Embed the pie chart in column 1 of chart_row_frame
        canvas2 = FigureCanvasTkAgg(fig2, master=chart_row_frame)
        canvas2.draw()
        canvas2.get_tk_widget().grid(row=0, column=2, padx=10, pady=10, sticky="nsw")

        CTkLabel(
            master=main_page_frame,
            text="Some Stats:",
            font=("sans-serif", 22, 'bold'), 
            anchor='nw',
            text_color="grey",
        ).grid(row=2, column=0, pady=(20, 5), padx=20, sticky='w')

        stats_row_frame = tk.Frame(main_page_frame, height= 350)
        stats_row_frame.grid(row=3, column=0, padx=20, pady=(10, 20), sticky=NSEW)   

        stats_row_frame.rowconfigure(0, weight=1)
        # stats_row_frame.columnconfigure(1, weight=1)
        stats_row_frame.grid_propagate(False)


        def calculate_profit():
            transactions = Transaction.get_transcations_as_Dict()
            products = {product['prodID']: product['price'] for product in Product.get_products_as_Dict()} 
            
            
            transaction_info = [
                {'quantity': transaction['quantity'], 'price': products[transaction['prodID']]}
                for transaction in transactions
                if transaction['prodID'] in products 
            ]
            
            total_profit = sum(info['quantity'] * info['price'] for info in transaction_info)

            return total_profit

        
        total_profit = calculate_profit()

        box_1 =CTkFrame(stats_row_frame, bg_color='transparent', fg_color="#77d2ff", width=350, height=350)
        box_1.grid(row=0, column=0)

        box_1.grid_propagate(False)
        box_1.columnconfigure(0, weight=1)


        CTkLabel(
            master=box_1,
            text="Monthly Profit:",
            font=("sans-serif", 20, 'bold'), 
            anchor='nw',
            text_color="white",
        ).grid(row=0, column=0, pady=(20, 40), padx=20, sticky='w')

        box_1_image = add_image_widget(box_1, './images/main/profits.png', width=60, height=60, background='#77d2ff')
        box_1_image.grid(row=0, column=1, sticky='ne', padx=20)

        CTkLabel(
            master=box_1,
            text=f"Ksh. {total_profit}",
            font=("sans-serif", 30, 'bold'), 
            anchor='center',
            text_color="black"
        ).grid(row=1, column=0, pady=(40, 40), columnspan=2)
        
            
        
        box_2 = CTkFrame(stats_row_frame, bg_color='transparent', fg_color="#77d2ff", width=350, height=350)
        box_2.grid(row=0, column=2, padx=(50, 0), sticky='e')

        box_2.grid_propagate(False)
        box_2.columnconfigure(0, weight=1)

        total_users = User.get_total_users() - 1

        CTkLabel(
            master=box_2,
            text="Total employees:",
            font=("sans-serif", 20, 'bold'), 
            anchor='w',
        ).grid(row=0, column=0, pady=(10, 40), padx=20, sticky='w')

        box_2_image = add_image_widget(box_2, './images/main/user-group.png', width=60, height=60, background='#77d2ff')
        box_2_image.grid(row=0, column=1, sticky='ne', padx=(20, 20), pady=10)

        CTkLabel(
            master=box_2,
            text=f"{total_users}",
            font=("sans-serif", 30, 'bold'), 
            anchor='center',
            text_color="black"
        ).grid(row=1, column=0, pady=(40, 40), columnspan=2)

        





        
        #  main_column 2 childrens





        window_obj.mainloop()

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

    def create_user():
        def db_query():
            empID = empIDInput.get()
            fname = fnameInput.get()
            lname = lnameInput.get()
            salary = salaryInput.get()
            natID = natIDInput.get()
            password = passwordInput.get()
            confirmPassword = confirmPasswordInput.get()
            if (
                not empID
                and not fname
                and not lname
                and not salary
                and not natID
                and not password
                and not confirmPassword
            ):
                desturi("Missing fields", "Please fill in all the fields")
                return

            if password != confirmPassword:

                desturi("Passwords not matching", "The passwords do not match!")

                return
            isAdmin = False
            # print(empID, fname, lname, salary, natID, password, isAdmin)
            user_obj = User(empID, fname, lname, salary, natID, password, isAdmin)
            user_obj.create_user()

            desturi("User Created", "User Created Successfully")

        temp_window = CTkToplevel(window_obj)
        temp_window.title("Create a user")
        temp_window.minsize(600, 600)
        temp_window.attributes("-topmost", True)
        if "UI" == "UI":
            CTkLabel(
                temp_window,
                text="Enter the deatils of the user",
                font=(
                    "sans-serif",
                    40,
                    "bold",
                ),
                padx=100,
                pady=50,
            ).grid(row=0, column=0, columnspan=2)

            CTkLabel(
                temp_window,
                text="Employee ID: ",
                pady=10,
                font=(
                    "sans-serif",
                    20,
                ),
            ).grid(row=1, column=0)
            empIDInput = CTkEntry(temp_window)
            empIDInput.grid(row=1, column=1)
            CTkLabel(
                temp_window,
                text="First name: ",
                pady=10,
                font=(
                    "sans-serif",
                    20,
                ),
            ).grid(row=2, column=0)
            fnameInput = CTkEntry(temp_window)
            fnameInput.grid(row=2, column=1)
            CTkLabel(
                temp_window,
                text="Last name: ",
                pady=10,
                font=(
                    "sans-serif",
                    20,
                ),
            ).grid(row=3, column=0)
            lnameInput = CTkEntry(temp_window)
            lnameInput.grid(row=3, column=1)
            CTkLabel(
                temp_window,
                text="Salary: ",
                pady=10,
                font=(
                    "sans-serif",
                    20,
                ),
            ).grid(row=4, column=0)
            salaryInput = CTkEntry(temp_window)
            salaryInput.grid(row=4, column=1)
            CTkLabel(
                temp_window,
                text="National ID: ",
                pady=10,
                font=(
                    "sans-serif",
                    20,
                ),
            ).grid(row=5, column=0)
            natIDInput = CTkEntry(temp_window)
            natIDInput.grid(row=5, column=1)
            CTkLabel(
                temp_window,
                text="Password: ",
                pady=10,
                font=(
                    "sans-serif",
                    20,
                ),
            ).grid(row=6, column=0)
            passwordInput = CTkEntry(temp_window, show="*")
            passwordInput.grid(row=6, column=1)
            CTkLabel(
                temp_window,
                text="Confirm: ",
                pady=10,
                font=(
                    "sans-serif",
                    20,
                ),
            ).grid(row=7, column=0)
            confirmPasswordInput = CTkEntry(temp_window, show="*")
            confirmPasswordInput.grid(row=7, column=1)
            CTkButton(temp_window, text="Create User", command=db_query).grid(
                row=8, column=0, columnspan=2, pady=(0, 20)
            )

        temp_window.wm_transient()

    def show_user():
        panel_manager = PanelManager(None)
        should_refresh = reinitialize_main_column2('users')
        if not should_refresh:
            return
        
        for index, val in enumerate(User.show_user()):
            # print(val[5])
            pass

        def edit_user(_):
            id = table.item(table.selection())["values"][0]
            user_arr = []
            selectedUser_arr = []
            for val in User.show_user():
                # print(val)
                if val[0] == loggedInUserID:
                    user_arr = val
                if val[0] == id:
                    selectedUser_arr = val

            pop_up = CTkToplevel()
            pop_up.title("Edit User")
            pop_up.attributes("-topmost", True)
            pop_up.minsize(600, 400)

            if "UI" == "UI":
                CTkLabel(
                    pop_up,
                    text="Edit User Details",
                    font=("sans-serif", 40, "bold"),
                    padx=100,
                    pady=50,
                ).grid(row=0, column=0, columnspan=2)

                CTkLabel(
                    pop_up, text="Employee ID:", pady=10, font=("sans-serif", 20)
                ).grid(row=1, column=0)
                empIDInput = CTkEntry(
                    pop_up, textvariable=StringVar(value=selectedUser_arr[1])
                )
                empIDInput.grid(row=1, column=1)

                CTkLabel(
                    pop_up, text="First name:", pady=10, font=("sans-serif", 20)
                ).grid(row=2, column=0)
                fnameInput = CTkEntry(
                    pop_up, textvariable=StringVar(value=selectedUser_arr[2])
                )
                fnameInput.grid(row=2, column=1)

                CTkLabel(
                    pop_up, text="Last name:", pady=10, font=("sans-serif", 20)
                ).grid(row=3, column=0)
                lnameInput = CTkEntry(
                    pop_up, textvariable=StringVar(value=selectedUser_arr[3])
                )
                lnameInput.grid(row=3, column=1)

                CTkLabel(pop_up, text="Salary:", pady=10, font=("sans-serif", 20)).grid(
                    row=4, column=0
                )
                salaryInput = CTkEntry(
                    pop_up, textvariable=StringVar(value=selectedUser_arr[4])
                )
                salaryInput.grid(row=4, column=1)

                CTkLabel(
                    pop_up, text="National ID:", pady=10, font=("sans-serif", 20)
                ).grid(row=5, column=0)
                natIDInput = CTkEntry(
                    pop_up, textvariable=StringVar(value=selectedUser_arr[5])
                )
                natIDInput.grid(row=5, column=1)

                CTkLabel(
                    pop_up,
                    text="*** Enter Admin password confirm details:",
                    pady=10,
                    font=("sans-serif", 20),
                ).grid(row=6, column=0)
                pwInput = CTkEntry(pop_up, show="*")
                pwInput.grid(row=6, column=1)

                CTkButton(pop_up, text="Update", command=update).grid(
                    row=7, column=0, columnspan=2, pady=(20, 20), padx=(10, 10)
                )

                pop_up.wm_transient()

        def delete_user():
            # print("here33", table.item(table.selection())["values"][0])
            id = table.item(table.selection())["values"][0]
            user_arr = []
            for val in User.show_user():
                # print(val, loggedInUserID)
                if val[0] == loggedInUserID:
                    user_arr = val

            def delete():
                pword = pwInput.get()
                # print(user_arr, 55586754)
                if pword == user_arr[5]:
                    User.delete_user(id)

                    ud = CTk()
                    ud.lift()
                    ud.title("User deleted")
                    ud.iconbitmap("./images/main/profit.ico")
                    ud.attributes("-topmost", True)
                    ud.bell()
                    if "UI" == "UI":
                        wp = CTkLabel(
                            mf,
                            text="User successfully deleted",
                            font=("sans-serif", 30, "bold"),
                            bg_color="red",
                        )
                        wp.pack(padx=10, pady=10)
                    mf.mainloop()

                else:

                    mf = CTk()
                    mf.lift()
                    mf.title("Wrong Password")
                    mf.iconbitmap("./images/main/profit.ico")
                    mf.attributes("-topmost", True)
                    mf.bell()
                    if "UI" == "UI":
                        wp = CTkLabel(
                            mf,
                            text="Wrong password entered!",
                            font=("sans-serif", 30, "bold"),
                            bg_color="red",
                        )
                        wp.pack(padx=10, pady=10)
                    mf.mainloop()

                return

            pop_up = CTk()
            pop_up.lift()
            pop_up.title("Delete User")
            pop_up.iconbitmap("./images/main/profit.ico")
            pop_up.attributes("-topmost", True)
            pop_up.bell()
            if "UI" == "UI":
                CTkLabel(
                    pop_up,
                    text="Enter Admin password to confirm deletion: ",
                    pady=10,
                    font=(
                        "sans-serif",
                        20,
                    ),
                ).grid(row=0, column=0)
                pwInput = CTkEntry(pop_up)
                pwInput.grid(row=0, column=1)
                CTkButton(pop_up, text="Delete", command=lambda: delete()).grid(
                    row=1, column=0, columnspan=2
                )

            pop_up.mainloop()

        if "UI" == "UI":
            user_screen = CTkFrame(master=main_column2, fg_color='transparent')
            user_screen.grid(row=0, column=0, sticky="nsew")

            user_screen.columnconfigure(0, weight=1)
            user_screen.rowconfigure(1, weight=1)

            top_bar = CTkFrame(master=user_screen, fg_color='transparent', height=60)
            top_bar.grid(row=0, column=0, sticky="ew", columnspan=2)

            top_bar.grid_propagate(False)

            # Configure the scrollable frame to expand
            scrollableFrame = CTkScrollableFrame(master=user_screen, fg_color="transparent", orientation=HORIZONTAL)
            scrollableFrame.grid(row=1, column=0, sticky="nsew", padx=0, pady=0)
            scrollableFrame.columnconfigure(0, weight=1)
            scrollableFrame.rowconfigure(0, weight=1)

            global selected_user
            selected_user = []

            def generate_table():
                # Create and configure the Treeview
                for widget in scrollableFrame.winfo_children():
                    widget.destroy()
 
                table = ttk.Treeview(
                    scrollableFrame,
                    columns=("ID", "Employee ID", "email", "First Name", "Last Name", "Salary", "National ID", "Password", "IsAdmin"),
                    show="headings",
                )

                # Define and configure each heading
                headings = ["ID", "Employee ID", "email", "First Name", "Last Name", "Salary", "National ID", "Password", "IsAdmin"]
                for heading in headings:
                    table.heading(heading, text=heading)
                    table.column(heading, anchor="center", stretch=True)  # Set width and allow stretching
                    table.tag_configure("oddrow", background="#f4fcff")
                    table.tag_configure("evenrow", background="#e1f8ff")

                # Grid the table with full stretch
                table.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")


                for index, val in enumerate(User.show_user()):
                    tag = "evenrow" if index % 2 == 0 else "oddrow"
                    table.insert(parent="", index=index, values=val, tags=tag)

                style = ttk.Style()
                style.configure(
                    "Treeview",
                        font=("Helvetica", 12),
                        rowheight=50,
                        background="#f8f9fa",  # Light grey background
                        foreground="#2b2b2b",
                )
                style.configure("Treeview.Heading", font=("Helvetica", 13, "bold"), foreground="grey", pady=20, background="#bde2ff", bg_color="#bde2ff")
                style.map(
                    "Treeview",
                    background=[("selected", "#2d598b")],
                    foreground=[("selected", "white")],
                )
                # Define the selection event callback
                def on_tree_select(event):
                    # Get the selected item ID
                    selected_item = table.selection()
                    
                    # Check if any item is selected
                    if selected_item:
                        # Fetch the selected row values
                        global selected_user 
                        selected_user = table.item(selected_item[0], "values")

                        select_panel(panel_manager.get_current_panel())
                        # Print or log the values as needed
                        
                # Bind the selection event to the table
                table.bind("<<TreeviewSelect>>", on_tree_select)

            generate_table()

            # table.bind("<Double-Button>", edit_user)
            # deletebtn = CTkButton(main_column2, text="delete", command=delete_user)
            # deletebtn.gird(row=1, column=0)

            top_bar.columnconfigure(0, weight=1)

            add_user_btn = CTkButton(
                master=top_bar,
                text="Add User",
                command=lambda: select_panel('add'),
                font=("sans-serif", 14, "bold"),
                corner_radius=6,
                hover_color="#bde2ff",
                bg_color='transparent',
                fg_color="#f5f3f3",
                text_color='grey',
                border_width=1,
                border_color="#eaeaea",
                height=40,
                anchor='w',
                image=CTkImage(
                    dark_image=Image.open("./images/main/add-male-user-color-icon.png"),
                    light_image=Image.open("./images/main/add-male-user-color-icon.png"),
                ),
            )
            add_user_btn.grid(
                row=0,
                column=1,
                pady=(10, 10),
                padx=10,
                sticky='e'
            )  # Adjust the second value for more or less margin

            edit_user_btn = CTkButton(
                master=top_bar,
                text="Edit User",
                command=lambda: select_panel('edit'),
                font=("sans-serif", 14, "bold"),
                corner_radius=6,
                hover_color="#bde2ff",
                bg_color='transparent',
                fg_color="#f5f3f3",
                text_color='grey',
                border_width=1,
                border_color="#eaeaea",
                height=40,
                anchor='w',
                image=CTkImage(
                    dark_image=Image.open("./images/main/edit-user-color-icon.png"),
                    light_image=Image.open("./images/main/edit-user-color-icon.png"),
                ),
            )
            edit_user_btn.grid(
                row=0,
                column=2,
                pady=(10, 10),
                padx=10,
                sticky='e'
            )  # Adjust the second value for more or less margin
            

            edit_add_box = CTkFrame(user_screen, width=270, height=600, fg_color="transparent")
            edit_add_box.grid(row=1, column=1, sticky='n')

            edit_add_box.columnconfigure(0, weight=1)
            edit_add_box.rowconfigure(0, weight=1)

            edit_add_box.grid_propagate(False)

            def select_panel(panel = 'edit'):
                panel_manager.set_current_panel(panel)
                for widget in edit_add_box.winfo_children():
                    widget.destroy()
                
                if panel == 'edit':
                    def update():
                        empID = selected_user[1]
                        User.update_user(
                            empID,
                            emailInput.get(),
                            fnameInput.get(),
                            lnameInput.get(),
                            salaryInput.get(),
                            natIDInput.get(),
                            pwInput.get()
                        )
                        generate_table()
                        desturi("User edited", "User successfully edited")
                    emailInput, fnameInput, lnameInput, salaryInput, natIDInput, pwInput = generate_panel(edit_add_box, panel, update, selected_user)

                elif panel == 'add':
                    def add():
                        isAdmin = 0
                        empID = generate(size=7)
                        user_obj = User(
                            empID,
                            emailInput.get(),
                            fnameInput.get(),
                            lnameInput.get(),
                            salaryInput.get(),
                            natIDInput.get(),
                            pwInput.get(),
                            isAdmin
                        )
                        user_obj.create_user()
                        generate_table()
                        desturi("Success!", "User Successfully Added")

                    emailInput, fnameInput, lnameInput, salaryInput, natIDInput, pwInput = generate_panel(edit_add_box, panel, add, selected_user=[])
                    
            select_panel()

    def create_product():
        # select file fix
        file_name = ""

        def select_file():
            global file_name
            # Bring the root window to the front
            temp_window.lift()  # Bring the window to the front
            temp_window.attributes("-topmost", True)  # Set the window to be topmost
            temp_window.attributes(
                "-topmost", False
            )  # Reset to allow it to lose focus later

            file_name = filedialog.askopenfilename(defaultextension="*.png")
            # print(file_name)  # Do something with the file name
            # print(file_name)

        def db_query():
            global file_name
            prodID = prodIDInput.get()
            name = nameInput.get()
            description = descriptionInput.get()
            quantity = quantityInput.get()
            price = priceInput.get()
            file_location = file_name
            # print(
            #     f"prodID: {prodID}, name: {name}, description: {description}, quantity: {quantity}, price: {price}, file_location: {file_location}"
            # )
            if (
                not prodID
                or not name
                or not description
                or not quantity
                or not price
                or not file_location
            ):
                desturi("Missing fields", "Please fill in all the fields")
                return

            try:
                product_obj = Product(
                    prodID, name, description, quantity, price, file_location
                )
                product_obj.create_product()
                desturi("Product Created", "Product Created Successfully")
            except Exception as e:
                desturi("ERROR", e)

        temp_window = CTkToplevel(window_obj)
        temp_window.title("Create a Product")
        temp_window.attributes("-topmost", True)

        if "UI" == "UI":
            CTkLabel(
                temp_window,
                text="Enter Product Details",
                font=("sans-serif", 40, "bold"),
                padx=100,
                pady=50,
            ).grid(row=0, column=0, columnspan=2)

            CTkLabel(
                temp_window,
                text="Product ID: ",
                pady=10,
                font=("sans-serif", 20),
            ).grid(row=1, column=0)
            prodIDInput = CTkEntry(temp_window)
            prodIDInput.grid(row=1, column=1)

            CTkLabel(
                temp_window,
                text="Product Name: ",
                pady=10,
                font=("sans-serif", 20),
            ).grid(row=2, column=0)
            nameInput = CTkEntry(temp_window)
            nameInput.grid(row=2, column=1)

            CTkLabel(
                temp_window,
                text="Description: ",
                pady=10,
                font=("sans-serif", 20),
            ).grid(row=3, column=0)
            descriptionInput = CTkEntry(temp_window)
            descriptionInput.grid(row=3, column=1)

            CTkLabel(
                temp_window,
                text="Quantity: ",
                pady=10,
                font=("sans-serif", 20),
            ).grid(row=4, column=0)
            quantityInput = CTkEntry(temp_window)
            quantityInput.grid(row=4, column=1)

            CTkLabel(
                temp_window,
                text="Price: ",
                pady=10,
                font=("sans-serif", 20),
            ).grid(row=5, column=0)
            priceInput = CTkEntry(temp_window)
            priceInput.grid(row=5, column=1)

            CTkButton(
                temp_window, text="Select Product Image", command=select_file
            ).grid(row=6, column=0, columnspan=2, pady=(20, 20))

            CTkButton(temp_window, text="Submit", command=db_query).grid(
                row=7, column=0, columnspan=2, pady=(20, 20)
            )

    def show_product():
        should_refresh = reinitialize_main_column2('products')
        if not should_refresh:
            return

        table = ttk.Treeview(
            main_column2,
            columns=(
                "ID",
                "Product ID",
                "Name",
                "Description",
                "Quantity",
                "Price",
                "Image",  # <-- NEW: Add this line for the image column
            ),
            show="headings",
        )

        headings = [
            "ID",
            "Product ID",
            "Name",
            "Description",
            "Quantity",
            "Price",
            "Image",
        ]  # <-- Modify this line
        for heading in headings:
            table.heading(heading, text=heading)
            table.column(heading, anchor="center")
            table.tag_configure("oddrow", background="white")
            table.tag_configure("evenrow", background="#e7e7e7")

        table.pack(fill="both", expand=True, padx=20, pady=20)

        for index, val in enumerate(Product.show_product()):
            tag = "evenrow" if index % 2 == 0 else "oddrow"
            image_display = "Show Image"  # <-- NEW: Add this line for the image link
            table.insert(
                parent="", index=index, values=(*val[:-1], image_display), tags=(tag,)
            )  # <-- Modify this line

        style = ttk.Style()
        style.configure(
            "Treeview",
                font=("Helvetica", 10),
                rowheight=30,
                background="#f8f9fa",  # Light grey background
                foreground="black",
        )
        style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"))
        style.map(
            "Treeview",
            background=[("selected", "#4A4A4A")],
            foreground=[("selected", "white")],
        )

        def show_image(event):
            image_path = val[
                -1
            ]  # <-- Get the image path from the selected item's values
            image_window = CTkToplevel()
            image_window.title("Product Image")
            image_window.attributes("-topmost", True)

            img = PhotoImage(
                file=f"./images/products/{image_path}"
            )  # Adjust the path as needed
            img_label = CTkLabel(image_window, image=img)
            img_label.image = img  # Keep a reference to avoid garbage collection
            img_label.pack()

        table.bind(
            "<F1>",
            lambda event: (
                show_image(event)
                if table.identify_region(event.x, event.y) == "cell"
                and "Image" in table["columns"]
                else None
            ),
        )

        def item_edit(event):
            selected_item = table.selection()[0]
            prod_arr = table.item(selected_item)["values"]

            def update():
                Product.update_product(
                    prod_arr[0],
                    prodIDInput.get(),
                    nameInput.get(),
                    descriptionInput.get(),
                    quantityInput.get(),
                    priceInput.get(),
                )

                desturi("Success", "Record successfully updated")

            pop_up = CTkToplevel()
            pop_up.attributes("-topmost", True)
            if "UI" == "UI":
                CTkLabel(
                    pop_up,
                    text="Enter the details of the product",
                    font=("sans-serif", 40, "bold"),
                    padx=100,
                    pady=50,
                ).grid(row=0, column=0, columnspan=2)

                CTkLabel(
                    pop_up,
                    text="Product ID: ",
                    pady=10,
                    font=("sans-serif", 20),
                ).grid(row=1, column=0)
                prodIDInput = CTkEntry(
                    pop_up, textvariable=StringVar(value=prod_arr[1])
                )
                prodIDInput.grid(row=1, column=1)

                CTkLabel(
                    pop_up,
                    text="Name: ",
                    pady=10,
                    font=("sans-serif", 20),
                ).grid(row=2, column=0)
                nameInput = CTkEntry(pop_up, textvariable=StringVar(value=prod_arr[2]))
                nameInput.grid(row=2, column=1)

                CTkLabel(
                    pop_up,
                    text="Description: ",
                    pady=10,
                    font=("sans-serif", 20),
                ).grid(row=3, column=0)
                descriptionInput = CTkEntry(
                    pop_up, textvariable=StringVar(value=prod_arr[3])
                )
                descriptionInput.grid(row=3, column=1)

                CTkLabel(
                    pop_up,
                    text="Quantity: ",
                    pady=10,
                    font=("sans-serif", 20),
                ).grid(row=4, column=0)
                quantityInput = CTkEntry(
                    pop_up, textvariable=StringVar(value=prod_arr[4])
                )
                quantityInput.grid(row=4, column=1)

                CTkLabel(
                    pop_up,
                    text="Price: ",
                    pady=10,
                    font=("sans-serif", 20),
                ).grid(row=5, column=0)
                priceInput = CTkEntry(pop_up, textvariable=StringVar(value=prod_arr[5]))
                priceInput.grid(row=5, column=1)

                CTkButton(
                    pop_up,
                    text="Update",
                    command=update,
                ).grid(row=6, column=0, columnspan=2, pady=(20, 20))

                pop_up.wm_transient()

        def delete_product():
            selected_item = table.selection()[0]
            id = table.item(selected_item)["values"][0]
            user_arr = []
            for val in User.show_user():
                # print(val)
                if val[0] == loggedInUserID:
                    user_arr = val

            def confirm_delete():
                pword = pwInput.get()
                # print(pword,user_arr[5])
                if pword == user_arr[5]:
                    Product.delete_product(id)
                    desturi("Product deleted", "Product deleted")
                else:
                    desturi("Wrong password", "Wrong password entered")
                return


            pop_up = CTkToplevel()
            pop_up.title("Enter password")
            pop_up.attributes("-topmost", True)
            CTkLabel(pop_up, text="Enter password to confirm deletion:").grid(
                row=1, column=0
            )
            pwInput = CTkEntry(pop_up, show="*")
            pwInput.grid(row=1, column=1)
            CTkButton(pop_up, text="Delete", command=confirm_delete).grid(
                row=2, column=0, columnspan=2
            )

        table.bind("<Double-Button>", item_edit)
        deletebtn = CTkButton(
            main_column2, text="Delete Selected Product", command=delete_product
        )
        deletebtn.pack(pady=10)

    def create_transaction():
        def db_query():
            if (
                prodIDLabel.get() == ""
                or quantityLabel.get() == ""
                or priceLabel.get() == ""
            ):
                desturi("Missing fields", "All fields must be filled!")
                return

            ProductNotAvailable = True
            for val in Product.show_product():
                # print(val[1], prodIDLabel.get())
                if val[1] == int(prodIDLabel.get()):
                    ProductNotAvailable = False
                    break
            if ProductNotAvailable:
                desturi("Unknown product", "No product with that ID")
                return

            try:
                transaction_obj = Transaction(
                    loggedInUserID,
                    prodIDLabel.get(),
                    quantityLabel.get(),
                    priceLabel.get(),
                    datetime.datetime.now().strftime("%Y %b %d %H:%M")
                )
                transaction_obj.create_transaction()
                desturi("Success", "Transaction Created Successfully")
            except Exception as e:
                desturi("ERROR", e)

        temp_window = CTkToplevel(window_obj)
        temp_window.title("Create a Transaction")
        temp_window.attributes("-topmost", True)

        CTkLabel(
            temp_window,
            text="Enter the details of the transaction",
            font=("sans-serif", 40, "bold"),
            padx=100,
            pady=50,
        ).grid(row=0, column=0, columnspan=2)

        CTkLabel(
            temp_window, text="Product ID:", pady=10, font=("sans-serif", 20)
        ).grid(row=1, column=0)
        prodIDLabel = CTkEntry(temp_window)
        prodIDLabel.grid(row=1, column=1)

        CTkLabel(temp_window, text="Quantity:", pady=10, font=("sans-serif", 20)).grid(
            row=2, column=0
        )
        quantityLabel = CTkEntry(temp_window)
        quantityLabel.grid(row=2, column=1)

        CTkLabel(temp_window, text="Price:", pady=10, font=("sans-serif", 20)).grid(
            row=3, column=0
        )
        priceLabel = CTkEntry(temp_window)
        priceLabel.grid(row=3, column=1)

        CTkButton(temp_window, text="Add", command=db_query).grid(
            row=5, column=0, columnspan=2
        )

        temp_window.wm_transient()

    def show_transaction():

        should_refresh = reinitialize_main_column2('transactions')
        if not should_refresh:
            return

        def item_edit(event):
            selected_item = table.selection()[0]
            id = table.item(selected_item)["values"][0]
            transaction_arr = []
            user_arr = []
            for val in User.show_user():
                # print(val, loggedInUserID)
                if val[0] == loggedInUserID:
                    user_arr = val
            for val in Transaction.show_transaction():
                if val[0] == id:
                    transaction_arr = val

            def update():
                pword = pwInput.get()
                # print(user_arr, 55586754)
                if pword == user_arr[5]:
                    Transaction.update_transaction(
                        id,
                        ReceiptIDInput.get(),
                        madeByEmpIDInput.get(),
                        prodIDInput.get(),
                        quantityInput.get(),
                        priceInput.get(),
                        datetime.datetime.now().isoformat(),
                    )

                    desturi("Transaction edited", "Transaction successfully deleted")
                else:
                    desturi("Wrong Password", "Wrong password entered!")

                # return

            pop_up = CTkToplevel()
            pop_up.title("Transaction Edit")
            pop_up.attributes("-topmost", True)
            if "UI" == "UI":
                CTkLabel(pop_up, text="Receipt ID: ").grid(row=1, column=0)
                ReceiptIDInput = CTkEntry(
                    pop_up,
                    textvariable=StringVar(value=transaction_arr[0]),
                    state=DISABLED,
                )
                ReceiptIDInput.grid(row=1, column=1)
                CTkLabel(pop_up, text="Made By Employee ID: ").grid(row=2, column=0)
                madeByEmpIDInput = CTkEntry(
                    pop_up,
                    textvariable=StringVar(value=transaction_arr[1]),
                    state=DISABLED,
                )
                madeByEmpIDInput.grid(row=2, column=1)
                CTkLabel(pop_up, text="Product ID: ").grid(row=3, column=0)
                prodIDInput = CTkEntry(
                    pop_up,
                    textvariable=StringVar(value=transaction_arr[2]),
                    state=DISABLED,
                )
                prodIDInput.grid(row=3, column=1)
                CTkLabel(pop_up, text="Quantity: ").grid(row=4, column=0)
                quantityInput = CTkEntry(
                    pop_up, textvariable=StringVar(value=transaction_arr[3])
                )
                quantityInput.grid(row=4, column=1)
                CTkLabel(pop_up, text="Price: ").grid(row=5, column=0)
                priceInput = CTkEntry(
                    pop_up, textvariable=StringVar(value=transaction_arr[4])
                )
                priceInput.grid(row=5, column=1)
                CTkLabel(pop_up, text="Time: ").grid(row=6, column=0)
                CTkLabel(
                    pop_up,
                    text="Enter Admin password to confirm deletion: ",
                    pady=10,
                    font=(
                        "sans-serif",
                        20,
                    ),
                ).grid(row=7, column=0)
                pwInput = CTkEntry(pop_up)
                pwInput.grid(row=7, column=1)
                CTkLabel(pop_up, text=transaction_arr[5]).grid(row=6, column=1)
                CTkButton(pop_up, text="Update", command=update).grid(
                    row=8, column=0, columnspan=2
                )

        def delete_transaction():
            id = table.item(table.selection())["values"][0]
            user_arr = []
            for val in User.show_user():
                # print(val, loggedInUserID)
                if val[0] == loggedInUserID:
                    user_arr = val

            def delete():
                pword = pwInput.get()
                # print(user_arr, 55586754)
                if pword == user_arr[5]:
                    Transaction.delete_transaction(id)
                    # table.delete(id)
                    desturi("Transaction deleted", "Transaction successfully deleted")
                else:
                    desturi("Wrong Password", "Wrong password entered!")

                return

            pop_up = CTkToplevel()
            pop_up.lift()
            pop_up.title("Delete Transaction")
            pop_up.iconbitmap("./images/main/profit.ico")
            pop_up.attributes("-topmost", True)
            pop_up.bell()
            if "UI" == "UI":
                CTkLabel(
                    pop_up,
                    text="Enter Admin password to confirm deletion: ",
                    pady=10,
                    font=(
                        "sans-serif",
                        20,
                    ),
                ).grid(row=0, column=0)
                pwInput = CTkEntry(pop_up)
                pwInput.grid(row=0, column=1)
                CTkButton(pop_up, text="Delete", command=lambda: delete()).grid(
                    row=1, column=0, columnspan=2
                )

            pop_up.mainloop()


        # Define the Treeview for displaying transaction records
        table = ttk.Treeview(
            main_column2,
            columns=(
                "Receipt ID",
                "Employee ID",
                "Product ID",
                "Quantity",
                "Price",
                "Time",
            ),
            show="headings",
        )

        # Set up headings and styles
        headings = [
            "Receipt ID",
            "Employee ID",
            "Product ID",
            "Quantity",
            "Price",
            "Time",
        ]
       
        for heading in headings:
            table.heading(heading, text=heading)
            table.column(heading, anchor="center")
            table.tag_configure("oddrow", background="white")
            table.tag_configure("evenrow", background="#e7e7e7")

        table.pack(fill="both", expand=True, padx=20, pady=20)

        # Insert transaction records into the Treeview
        for index, val in enumerate(Transaction.show_transaction()):
            tag = "evenrow" if index % 2 == 0 else "oddrow"
            table.insert(parent="", index=index, values=val, tags=(tag,))

        style = ttk.Style()
        style.configure(
            "Treeview",
                font=("Helvetica", 10),
                rowheight=30,
                background="#f8f9fa",  # Light grey background
                foreground="black",
        )
        style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"))
        style.map(
            "Treeview",
            background=[("selected", "#4A4A4A")],
            foreground=[("selected", "white")],
        )
        table.bind("<Double-Button>", item_edit)

        CTkButton(main_column2, text="Delete", command=delete_transaction).pack(pady=10)


    show_dashboard()       
        



def login_screen():  # returns user ID of the logged-in 
    

    login_screen_obj = CTk()
    login_screen_obj.title("Login")
    login_screen_obj.iconbitmap("./images/main/profit.ico")
    global userId
    userId = None

    def validate_login():
        global userId
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
            userId = user_data['empID']
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
    return userId




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

    user_id = login_screen()
    #'IYU2SF7'

    if user_id:
        main_screen(user_id)
    # User.show_user(35)

    # _DEBUG_()
