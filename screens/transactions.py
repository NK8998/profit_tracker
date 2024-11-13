from customtkinter import *
from tkinter import *
from PIL import Image
from tkinter import ttk
from nanoid import generate
from datetime import datetime


# helpers
from helpers.image_widget import add_image_widget
from helpers.panel_generator import generate_panel
# helpers

# clases
from classes.classes import PanelManager, Transaction
# classes

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


def transaction_screen(reinitialize_main_column2, desturi, main_column2, user_data):
    should_refresh = reinitialize_main_column2('transactions')
    if not should_refresh:
        return

    # def item_edit(event):
    #     selected_item = table.selection()[0]
    #     id = table.item(selected_item)["values"][0]
    #     transaction_arr = []
    #     user_arr = []
    #     for val in User.show_user():
    #         # print(val, loggedInUserID)
    #         if val[0] == loggedInUserID:
    #             user_arr = val
    #     for val in Transaction.show_transaction():
    #         if val[0] == id:
    #             transaction_arr = val

    #     def update():
    #         pword = pwInput.get()
    #         # print(user_arr, 55586754)
    #         if pword == user_arr[5]:
    #             Transaction.update_transaction(
    #                 id,
    #                 ReceiptIDInput.get(),
    #                 madeByEmpIDInput.get(),
    #                 prodIDInput.get(),
    #                 quantityInput.get(),
    #                 priceInput.get(),
    #                 datetime.datetime.now().isoformat(),
    #             )

    #             desturi("Transaction edited", "Transaction successfully deleted")
    #         else:
    #             desturi("Wrong Password", "Wrong password entered!")

    #         # return

    #     pop_up = CTkToplevel()
    #     pop_up.title("Transaction Edit")
    #     pop_up.attributes("-topmost", True)
    #     if "UI" == "UI":
    #         CTkLabel(pop_up, text="Receipt ID: ").grid(row=1, column=0)
    #         ReceiptIDInput = CTkEntry(
    #             pop_up,
    #             textvariable=StringVar(value=transaction_arr[0]),
    #             state=DISABLED,
    #         )
    #         ReceiptIDInput.grid(row=1, column=1)
    #         CTkLabel(pop_up, text="Made By Employee ID: ").grid(row=2, column=0)
    #         madeByEmpIDInput = CTkEntry(
    #             pop_up,
    #             textvariable=StringVar(value=transaction_arr[1]),
    #             state=DISABLED,
    #         )
    #         madeByEmpIDInput.grid(row=2, column=1)
    #         CTkLabel(pop_up, text="Product ID: ").grid(row=3, column=0)
    #         prodIDInput = CTkEntry(
    #             pop_up,
    #             textvariable=StringVar(value=transaction_arr[2]),
    #             state=DISABLED,
    #         )
    #         prodIDInput.grid(row=3, column=1)
    #         CTkLabel(pop_up, text="Quantity: ").grid(row=4, column=0)
    #         quantityInput = CTkEntry(
    #             pop_up, textvariable=StringVar(value=transaction_arr[3])
    #         )
    #         quantityInput.grid(row=4, column=1)
    #         CTkLabel(pop_up, text="Price: ").grid(row=5, column=0)
    #         priceInput = CTkEntry(
    #             pop_up, textvariable=StringVar(value=transaction_arr[4])
    #         )
    #         priceInput.grid(row=5, column=1)
    #         CTkLabel(pop_up, text="Time: ").grid(row=6, column=0)
    #         CTkLabel(
    #             pop_up,
    #             text="Enter Admin password to confirm deletion: ",
    #             pady=10,
    #             font=(
    #                 "sans-serif",
    #                 20,
    #             ),
    #         ).grid(row=7, column=0)
    #         pwInput = CTkEntry(pop_up)
    #         pwInput.grid(row=7, column=1)
    #         CTkLabel(pop_up, text=transaction_arr[5]).grid(row=6, column=1)
    #         CTkButton(pop_up, text="Update", command=update).grid(
    #             row=8, column=0, columnspan=2
    #         )

    # def delete_transaction():
    #     id = table.item(table.selection())["values"][0]
    #     user_arr = []
    #     for val in User.show_user():
    #         # print(val, loggedInUserID)
    #         if val[0] == loggedInUserID:
    #             user_arr = val

    #     def delete():
    #         pword = pwInput.get()
    #         # print(user_arr, 55586754)
    #         if pword == user_arr[5]:
    #             Transaction.delete_transaction(id)
    #             # table.delete(id)
    #             desturi("Transaction deleted", "Transaction successfully deleted")
    #         else:
    #             desturi("Wrong Password", "Wrong password entered!")

    #         return

    #     pop_up = CTkToplevel()
    #     pop_up.lift()
    #     pop_up.title("Delete Transaction")
    #     pop_up.iconbitmap("./images/main/profit.ico")
    #     pop_up.attributes("-topmost", True)
    #     pop_up.bell()
    #     if "UI" == "UI":
    #         CTkLabel(
    #             pop_up,
    #             text="Enter Admin password to confirm deletion: ",
    #             pady=10,
    #             font=(
    #                 "sans-serif",
    #                 20,
    #             ),
    #         ).grid(row=0, column=0)
    #         pwInput = CTkEntry(pop_up)
    #         pwInput.grid(row=0, column=1)
    #         CTkButton(pop_up, text="Delete", command=lambda: delete()).grid(
    #             row=1, column=0, columnspan=2
    #         )

    #     pop_up.mainloop()

    panel_manager = PanelManager()

    transaction_screen = CTkFrame(master=main_column2, fg_color='transparent')
    transaction_screen.grid(row=0, column=0, sticky="nsew")

    transaction_screen.columnconfigure(0, weight=1)
    transaction_screen.rowconfigure(1, weight=1)

    top_bar = CTkFrame(master=transaction_screen, fg_color='transparent', height=60)
    top_bar.grid(row=0, column=0, sticky="ew", columnspan=2)

    top_bar.grid_propagate(False)

    # Configure the scrollable frame to expand
    scrollableFrame = CTkScrollableFrame(master=transaction_screen, fg_color="transparent", orientation=HORIZONTAL)
    scrollableFrame.grid(row=1, column=0, sticky="nsew", padx=0, pady=0)
    scrollableFrame.columnconfigure(0, weight=1)
    scrollableFrame.rowconfigure(0, weight=1)

    # scrollableFrame.grid_propagate(False)

    global selected_row
    selected_row = []

                    # Define and configure each heading
    # Set up headings and styles
    headings = [
        "ID",
        "Transaction ID",
        "Employee ID",
        "Product ID",
        "Quantity",
        "Price",
        "Time",
    ]

    def generate_table():
        # Create and configure the Treeview
        for widget in scrollableFrame.winfo_children():
            widget.destroy()

        table = ttk.Treeview(
            scrollableFrame,
            columns=(
                    "ID",
                    "Transaction ID",
                    "Employee ID",
                    "Product ID",
                    "Quantity",
                    "Price",
                    "Time",
            ),
            show="headings",
        )


        for heading in headings:
            table.heading(heading, text=heading)
            table.column(heading, anchor="center", stretch=True)  # Set width and allow stretching
            table.tag_configure("oddrow", background="#f4fcff")
            table.tag_configure("evenrow", background="#e1f8ff")

        # Grid the table with full stretch
        table.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")
        # table.pack(fill="both", expand=True)

        print(Transaction.show_transaction())


        for index, val in enumerate(Transaction.show_transaction()):
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
                global selected_row 
                selected_row = table.item(selected_item[0], "values")

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
        text="Add Transaction",
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
        text="Edit Transaction",
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
    

    edit_add_box = CTkFrame(transaction_screen, width=270, height=600, fg_color="transparent")
    edit_add_box.grid(row=1, column=1, sticky='n', padx=(20, 40), pady=20)

    edit_add_box.columnconfigure(0, weight=1)
    edit_add_box.rowconfigure(0, weight=1)

    # edit_add_box.grid_propagate(False)


    def select_panel(panel = 'edit'):

        entity = 'Transaction'
        
        panel_manager.set_current_panel(panel)
        for widget in edit_add_box.winfo_children():
            widget.destroy()
        
        if panel == 'edit':
            # Set up headings and styles
            columns = [
                "Quantity",
                "Price",
                "Time",
            ]
            def update():
                if len(selected_row) == 0:
                    return
                transactionID = selected_row[0] 
                Transaction.update_transaction(
                    transactionID,
                    quantityInput.get(),
                    priceInput.get(),
                    timeInput.get(),
                )
                generate_table()
                desturi("Product edited", "Product successfully edited")
            quantityInput, priceInput, timeInput = generate_panel(edit_add_box, panel, update, columns, entity, selected_row)

        elif panel == 'add':
            # Set up headings and styles
            columns = [
                "Product ID",
                "Quantity",
                "Price",
                "Discount"
            ]
            def add():

                loggedInUserID = user_data['empID']
                
                transactionID = generate(size=12)
                # Get the current date and time
                current_time = datetime.now()
                # Format the date and time in a readable format
                formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
                transaction_obj = Transaction(
                    transactionID,
                    loggedInUserID,
                    productIDInput.get(),
                    quantityInput.get(),
                    priceInput.get(),
                    discountInput.get(),
                    formatted_time
                )
                transaction_obj.create_transaction()
                generate_table()
                desturi("Success!", "Product Successfully Added")

            productIDInput, quantityInput, discountInput, priceInput = generate_panel(edit_add_box, panel, add, columns, entity, selected_row=[])
            
    select_panel()