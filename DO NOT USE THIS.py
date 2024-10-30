import sqlite3
import datetime
from tkinter import *
from tkinter import filedialog, messagebox, ttk
import shutil
import hashlib
import customtkinter as ctk
from customtkinter import *
from PIL import Image
import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import datetime
from tkinter import Toplevel, Label, Entry, Button, messagebox, StringVar, ttk

from customtkinter import CTk, CTkLabel, CTkEntry, CTkButton
from tkinter import PhotoImage


def main_screen(loggedInUserID):
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
                desturi("Missing fields","Please fill in all the fields")
                return

            if password != confirmPassword:

                desturi("Passwords not matching","The passwords do not match!")

                return
            isAdmin = False
            # print(empID, fname, lname, salary, natID, password, isAdmin)
            user_obj = User(empID, fname, lname, salary, natID, password, isAdmin)
            user_obj.create_user()

            desturi("User Created","User Created Successfully")

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
        
        def edit_user(_):
            id = table.item(table.selection())["values"][0]
            user_arr = []
            for val in User.show_user():
                # print(val)
                if val[0] == loggedInUserID:
                    user_arr = val

            def update():
                pword = pwInput.get()

                if pword == user_arr[5]:
                    User.update_user(
                        id,
                        empIDInput.get(),
                        fnameInput.get(),
                        lnameInput.get(),
                        salaryInput.get(),
                        natIDInput.get(),
                    )

                    pop_up = CTk()
                    pop_up.lift()
                    pop_up.title("User edited")
                    pop_up.iconbitmap("./images/main/profit.ico")
                    pop_up.attributes("-topmost", True)
                    pop_up.bell()
                    if "UI" == "UI":
                        wp = CTkLabel(
                            pop_up,
                            text="User successfully edited",
                            font=("sans-serif", 30, "bold"),
                            bg_color="red",
                        )
                        wp.pack(padx=10, pady=10)
                    pop_up.mainloop()
                else:
                    pop_up = CTk()
                    pop_up.lift()
                    pop_up.title("Wrong password")
                    pop_up.iconbitmap("./images/main/profit.ico")
                    pop_up.attributes("-topmost", True)
                    pop_up.bell()
                    if "UI" == "UI":
                        wp = CTkLabel(
                            pop_up,
                            text="Wrong password entered",
                            font=("sans-serif", 30, "bold"),
                            bg_color="red",
                        )
                        wp.pack(padx=10, pady=10)
                    pop_up.mainloop()
                return

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
                empIDInput = CTkEntry(pop_up, textvariable=StringVar(value=user_arr[0]))
                empIDInput.grid(row=1, column=1)

                CTkLabel(
                    pop_up, text="First name:", pady=10, font=("sans-serif", 20)
                ).grid(row=2, column=0)
                fnameInput = CTkEntry(pop_up, textvariable=StringVar(value=user_arr[1]))
                fnameInput.grid(row=2, column=1)

                CTkLabel(
                    pop_up, text="Last name:", pady=10, font=("sans-serif", 20)
                ).grid(row=3, column=0)
                lnameInput = CTkEntry(pop_up, textvariable=StringVar(value=user_arr[2]))
                lnameInput.grid(row=3, column=1)

                CTkLabel(pop_up, text="Salary:", pady=10, font=("sans-serif", 20)).grid(
                    row=4, column=0
                )
                salaryInput = CTkEntry(
                    pop_up, textvariable=StringVar(value=user_arr[3])
                )
                salaryInput.grid(row=4, column=1)

                CTkLabel(
                    pop_up, text="National ID:", pady=10, font=("sans-serif", 20)
                ).grid(row=5, column=0)
                natIDInput = CTkEntry(pop_up, textvariable=StringVar(value=user_arr[4]))
                natIDInput.grid(row=5, column=1)

                CTkLabel(
                    pop_up,
                    text="*** Enter this employee password confirm details:",
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

        
        temp_window = CTkToplevel(window_obj)
        temp_window.title("Users")
        temp_window.iconbitmap("./images/main/profit.ico")
        temp_window.attributes("-topmost", True)

        table = ttk.Treeview(
            temp_window,
            columns=("Employee ID", "First name", "Last name", "Salary", "National ID"),
            show="headings",
        )

        # Set up the headings
        for heading in table["columns"]:
            table.heading(heading, text=heading)
            table.column(heading, anchor="center")

        # Configure row colors
        table.tag_configure("oddrow", background="#3A3A3A")
        table.tag_configure("evenrow", background="#2E2E2E")

        table.pack(fill="both", expand=True, padx=20, pady=20)

        # Fetch and insert user data
        for index, val in enumerate(User.show_user()):
            tag = "evenrow" if index % 2 == 0 else "oddrow"
            # Only select the columns you want to display
            table.insert(parent="", index=index, values=(val[1], val[2], val[3], val[4], val[5]), tags=(tag,))

        # Style adjustments for the Treeview
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background="#2E2E2E", foreground="white", rowheight=25, fieldbackground="#2E2E2E")
        style.configure("Treeview.Heading", background="#3A3A3A", foreground="white")
        style.map("Treeview", background=[("selected", "#4A4A4A")], foreground=[("selected", "white")])

        table.bind("<Double-Button>", edit_user)
        deletebtn = CTkButton(temp_window, text="Delete", command=delete_user)
        deletebtn.pack(pady=10)

        temp_window.mainloop()

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
        temp_window = CTkToplevel()
        temp_window.title("Products")
        temp_window.attributes("-topmost", True)

        # 1. Update the Treeview to include an image column
        table = ttk.Treeview(
            temp_window,
            columns=(
                "Product ID",
                "Name",
                "Description",
                "Quantity",
                "Price",
                "Image",  # <-- NEW: Add this line for the image column
            ),
            show="headings",
        )

        # 2. Add 'Image' to the headings
        headings = [
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
            table.tag_configure("oddrow", background="#3A3A3A")
            table.tag_configure("evenrow", background="#2E2E2E")

        table.pack(fill="both", expand=True, padx=20, pady=20)

        for index, val in enumerate(Product.show_product()):
            tag = "evenrow" if index % 2 == 0 else "oddrow"
            image_display = "Show Image"  # <-- NEW: Add this line for the image link
            table.insert(
                parent="", index=index, values=(*val[:-1], image_display), tags=(tag,)
            )  # <-- Modify this line

        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "Treeview",
            background="#2E2E2E",
            foreground="white",
            rowheight=25,
            fieldbackground="#2E2E2E",
        )
        style.configure(
            "Treeview.Heading",
            background="#3A3A3A",
            foreground="white",
        )
        style.map(
            "Treeview",
            background=[("selected", "#4A4A4A")],
            foreground=[("selected", "white")],
        )

        # 3. Add the show_image function
        def show_image(event):
            image_path = val[
                -1
            ]  # <-- Get the image path from the selected item's values
            image_window = CTkToplevel()
            image_window.title("Product Image")

            img = PhotoImage(
                file=f"./images/products/{image_path}"
            )  # Adjust the path as needed
            img_label = CTkLabel(image_window, image=img)
            img_label.image = img  # Keep a reference to avoid garbage collection
            img_label.pack()

        # 4. Bind the show_image function to the left-click event
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

                temp_window.lift()
                temp_window.attributes("-topmost", True)
                temp_window.grab_set()
                messagebox.showinfo(
                    title="Success", message="Record successfully updated"
                )
                temp_window.grab_release()

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
                    pop_up, textvariable=StringVar(value=prod_arr[0])
                )
                prodIDInput.grid(row=1, column=1)

                CTkLabel(
                    pop_up,
                    text="Name: ",
                    pady=10,
                    font=("sans-serif", 20),
                ).grid(row=2, column=0)
                nameInput = CTkEntry(pop_up, textvariable=StringVar(value=prod_arr[1]))
                nameInput.grid(row=2, column=1)

                CTkLabel(
                    pop_up,
                    text="Description: ",
                    pady=10,
                    font=("sans-serif", 20),
                ).grid(row=3, column=0)
                descriptionInput = CTkEntry(
                    pop_up, textvariable=StringVar(value=prod_arr[2])
                )
                descriptionInput.grid(row=3, column=1)

                CTkLabel(
                    pop_up,
                    text="Quantity: ",
                    pady=10,
                    font=("sans-serif", 20),
                ).grid(row=4, column=0)
                quantityInput = CTkEntry(
                    pop_up, textvariable=StringVar(value=prod_arr[3])
                )
                quantityInput.grid(row=4, column=1)

                CTkLabel(
                    pop_up,
                    text="Price: ",
                    pady=10,
                    font=("sans-serif", 20),
                ).grid(row=5, column=0)
                priceInput = CTkEntry(pop_up, textvariable=StringVar(value=prod_arr[4]))
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

            def confirm_delete():
                Product.delete_product(id)

                temp_window.lift()
                temp_window.attributes("-topmost", True)
                temp_window.grab_set()
                messagebox.showinfo(
                    title="Success", message="Record successfully deleted"
                )
                temp_window.grab_release()

            pop_up = Toplevel()
            pop_up.attributes("-topmost", True)
            Label(pop_up, text="Enter password to confirm deletion:").grid(
                row=1, column=0
            )
            pwInput = Entry(pop_up, show="*")
            pwInput.grid(row=1, column=1)
            Button(pop_up, text="Delete", command=confirm_delete).grid(
                row=2, column=0, columnspan=2
            )

        table.bind("<Double-Button>", item_edit)
        deletebtn = CTkButton(
            temp_window, text="Delete Selected Product", command=delete_product
        )
        deletebtn.pack(pady=10)

        temp_window.mainloop()

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
                    datetime.datetime.now().isoformat(),
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
                    pop_up, textvariable=StringVar(value=transaction_arr[0]),state=DISABLED
                )
                ReceiptIDInput.grid(row=1, column=1)
                CTkLabel(pop_up, text="Made By Employee ID: ").grid(row=2, column=0)
                madeByEmpIDInput = CTkEntry(
                    pop_up, textvariable=StringVar(value=transaction_arr[1]),state=DISABLED
                )
                madeByEmpIDInput.grid(row=2, column=1)
                CTkLabel(pop_up, text="Product ID: ").grid(row=3, column=0)
                prodIDInput = CTkEntry(
                    pop_up, textvariable=StringVar(value=transaction_arr[2]),state=DISABLED
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
                Button(pop_up, text="Update", command=update).grid(
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

            pop_up = CTk()
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

        temp_window = CTkToplevel()
        temp_window.title("Transaction Records")
        temp_window.attributes("-topmost", True)

        # Define the Treeview for displaying transaction records
        table = ttk.Treeview(
            temp_window,
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
            table.tag_configure("oddrow", background="#3A3A3A")
            table.tag_configure("evenrow", background="#2E2E2E")

        table.pack(fill="both", expand=True, padx=20, pady=20)

        # Insert transaction records into the Treeview
        for index, val in enumerate(Transaction.show_transaction()):
            tag = "evenrow" if index % 2 == 0 else "oddrow"
            table.insert(parent="", index=index, values=val, tags=(tag,))

        # Style configuration
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "Treeview",
            background="#2E2E2E",
            foreground="white",
            rowheight=25,
            fieldbackground="#2E2E2E",
        )
        style.configure(
            "Treeview.Heading",
            background="#3A3A3A",
            foreground="white",
        )
        style.map(
            "Treeview",
            background=[("selected", "#4A4A4A")],
            foreground=[("selected", "white")],
        )
        table.bind("<Double-Button>", item_edit)

        Button(temp_window, text="Delete", command=delete_transaction).pack(pady=10)

        temp_window.mainloop()

    window_obj = CTk()
    window_obj.title("Profit Tracker")
    window_obj.iconbitmap("./images/main/profit.ico")
    set_default_color_theme("blue")
    window_obj.geometry("1280x720")
    window_obj.minsize(1280, 720)

    mainMenuBar = Menu(window_obj, tearoff=0)
    window_obj.config(menu=mainMenuBar)
    optionsMenu = Menu(mainMenuBar)
    mainMenuBar.add_cascade(label="options", menu=optionsMenu)
    mainMenuBar.add_cascade(label=f"logged in as: {User.show_user(loggedInUserID)}")
    optionsMenu.add_command(label="About us")
    optionsMenu.add_command(label="Exit")

    if "UI" == "UI":
        label = CTkLabel(
            window_obj,
            text="Welcome to Mr. Benson's Shop",
            font=("sans-serif", 40, "bold"),
        )
        label.pack()

        create_user_btn = CTkButton(
            master=window_obj,
            text="Create user",
            command=create_user,
            font=("sans-serif", 25, "bold"),
            corner_radius=32,
            hover_color="#4158D0",
            border_color="#FFCC70",
            border_width=2,
            image=CTkImage(
                dark_image=Image.open("./images/main/profit.png"),
                light_image=Image.open("./images/main/profit.png"),
            ),
        )
        create_user_btn.pack(
            pady=(20, 20)
        )  # Adjust the second value for more or less margin
        show_user_btn = CTkButton(
            master=window_obj,
            text="Show user",
            command=show_user,
            font=("sans-serif", 25, "bold"),
            corner_radius=32,
            hover_color="#4158D0",
            border_color="#FFCC70",
            border_width=2,
            image=CTkImage(
                dark_image=Image.open("./images/main/profit.png"),
                light_image=Image.open("./images/main/profit.png"),
            ),
        )
        show_user_btn.pack(pady=(20, 20))

        create_product_btn = CTkButton(
            master=window_obj,
            text="Create product",
            # command=create_product,
            font=("sans-serif", 25, "bold"),
            corner_radius=32,
            hover_color="#4158D0",
            border_color="#FFCC70",
            border_width=2,
            image=CTkImage(
                dark_image=Image.open("./images/main/profit.png"),
                light_image=Image.open("./images/main/profit.png"),
            ),
        )
        create_product_btn.pack(pady=(20, 20))
        show_product_btn = CTkButton(
            master=window_obj,
            text="Show product",
            command=show_product,
            font=("sans-serif", 25, "bold"),
            corner_radius=32,
            hover_color="#4158D0",
            border_color="#FFCC70",
            border_width=2,
            image=CTkImage(
                dark_image=Image.open("./images/main/profit.png"),
                light_image=Image.open("./images/main/profit.png"),
            ),
        )
        show_product_btn.pack(pady=(20, 20))

        create_transaction_btn = CTkButton(
            master=window_obj,
            text="Create transaction",
            command=create_transaction,
            font=("sans-serif", 25, "bold"),
            corner_radius=32,
            hover_color="#4158D0",
            border_color="#FFCC70",
            border_width=2,
            image=CTkImage(
                dark_image=Image.open("./images/main/profit.png"),
                light_image=Image.open("./images/main/profit.png"),
            ),
        )
        create_transaction_btn.pack(pady=(20, 20))
        show_transaction_btn = CTkButton(
            master=window_obj,
            text="Show transaction",
            command=show_transaction,
            font=("sans-serif", 25, "bold"),
            corner_radius=32,
            hover_color="#4158D0",
            border_color="#FFCC70",
            border_width=2,
            image=CTkImage(
                dark_image=Image.open("./images/main/profit.png"),
                light_image=Image.open("./images/main/profit.png"),
            ),
        )
        show_transaction_btn.pack(pady=(20, 20))

    window_obj.mainloop()


def login_screen():  # returns user ID of the logged-in user
    login_screen_obj = CTk()
    login_screen_obj.title("Login")
    login_screen_obj.iconbitmap("./images/main/profit.ico")
    global userId
    userId = None

    def validate_login():
        global userId
        empID = empIDInput.get()
        password = passwordInput.get()
        # print("here",User.show_user())
        for val in User.show_user():
            # print('fwfrw',val)
            if str(val[1]) == empID and val[5] == password:
                login_screen_obj.destroy()
                userId = val[1]
                return
            else:
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

    if "UI" == "UI":
        title_label = CTkLabel(
            login_screen_obj,
            text="Welcome to Mr. Benson's Shop",
            font=("sans-serif", 30, "bold"),
        )
        title_label.grid(row=0, column=0, columnspan=2, pady=20)

        CTkLabel(
            login_screen_obj, text="Enter Employee ID: ", font=("sans-serif", 15)
        ).grid(row=1, column=0, padx=10, pady=10)
        empIDInput = CTkEntry(login_screen_obj, font=("sans-serif", 15))
        empIDInput.grid(row=1, column=1, padx=10, pady=10)

        CTkLabel(
            login_screen_obj, text="Enter Password: ", font=("sans-serif", 15)
        ).grid(row=2, column=0, padx=10, pady=10)
        passwordInput = CTkEntry(login_screen_obj, show="*", font=("sans-serif", 15))
        passwordInput.grid(row=2, column=1, padx=10, pady=10)

        login_button = CTkButton(
            login_screen_obj,
            text="Login",
            command=validate_login,
            font=("sans-serif", 20, "bold"),
            hover_color="#4158D0",
            corner_radius=32,
        )
        login_button.grid(row=3, column=0, columnspan=2, pady=20)

    login_screen_obj.mainloop()
    return userId


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
            return curr.execute("SELECT * FROM users").fetchone()[2]
        else:
            with conn:
                return curr.execute("SELECT * FROM users").fetchall()

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
        ext = self.image.split("/")[5].split(".")[-1]

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

    def update_product(id, prodID, name, descripton, quantity, price, image):
        conn = sqlite3.connect("./databases/products.db")
        curr = conn.cursor()
        with conn:
            curr.execute(
                "UPDATE products SET prodID=:prodID,name=:name,descripton=:descripton,quantity=:quantity,price=:price,image=:image WHERE id=:id",
                {
                    "id": id,
                    "prodID": prodID,
                    "name": name,
                    "descripton": descripton,
                    "quantity": quantity,
                    "price": price,
                    "image": image,
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


def databases_initialisations():
    conn = sqlite3.connect("./databases/users.db")
    curr = conn.cursor()
    with conn:  # creating ADMIN account in the database
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
        if curr.execute("SELECT * FROM users").arraysize < 1:
            curr.execute(
                "INSERT INTO users(empID,fname,lname,salary,nationalID,isAdmin) VALUES(1,'admin','nistrator',1234,987456,True)"
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
    main_screen(login_screen())
    # User.show_user(35)

    # _DEBUG_()
