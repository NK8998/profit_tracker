from customtkinter import *
from tkinter import *
from PIL import Image
from tkinter import ttk
from nanoid import generate


# helpers
from helpers.image_widget import add_image_widget
from helpers.panel_generator import generate_panel
# helpers

# clases
from classes.classes import PanelManager, Product
# classes

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

# table.bind("<Double-Button>", item_edit)
# deletebtn = CTkButton(
#     main_column2, text="Delete Selected Product", command=delete_product
# )
# deletebtn.pack(pady=10)

def product_screen(reinitialize_main_column2, desturi, main_column2):
    should_refresh = reinitialize_main_column2('products')
    if not should_refresh:
        return

    panel_manager = PanelManager()

    if 'UI' == 'UI':
        product_screen = CTkFrame(master=main_column2, fg_color='transparent')
        product_screen.grid(row=0, column=0, sticky="nsew")

        product_screen.columnconfigure(0, weight=1)
        product_screen.rowconfigure(1, weight=1)

        top_bar = CTkFrame(master=product_screen, fg_color='transparent', height=60)
        top_bar.grid(row=0, column=0, sticky="ew", columnspan=2)

        top_bar.grid_propagate(False)

        # Configure the scrollable frame to expand
        scrollableFrame = CTkScrollableFrame(master=product_screen, fg_color="transparent", orientation=HORIZONTAL)
        scrollableFrame.grid(row=1, column=0, sticky="nsew", padx=0, pady=0)
        scrollableFrame.columnconfigure(0, weight=1)
        scrollableFrame.rowconfigure(0, weight=1)

        # scrollableFrame.grid_propagate(False)

        global selected_row
        selected_row = []

                        # Define and configure each heading
        headings = ["ID",
                    "Product ID",
                    "Name",
                    "Description",
                    "Quantity",
                    "Price",
                    # "Image",
                    ]

        def generate_table():
            # Create and configure the Treeview
            for widget in scrollableFrame.winfo_children():
                widget.destroy()

            table = ttk.Treeview(
                scrollableFrame,
                columns=(
                        "ID",
                        "Product ID",
                        "Name",
                        "Description",
                        "Quantity",
                        "Price",
                        # "Image",
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

            print(Product.show_product())


            for index, val in enumerate(Product.show_product()):
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
            text="Add Product",
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
            text="Edit Product",
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
        

        edit_add_box = CTkFrame(product_screen, width=270, height=600, fg_color="transparent")
        edit_add_box.grid(row=1, column=1, sticky='n', padx=20, pady=20)

        edit_add_box.columnconfigure(0, weight=1)
        edit_add_box.rowconfigure(0, weight=1)

        # edit_add_box.grid_propagate(False)


        def select_panel(panel = 'edit'):

            entity = 'Product'
            
            panel_manager.set_current_panel(panel)
            for widget in edit_add_box.winfo_children():
                widget.destroy()

        
            
            if panel == 'edit':
                columns = [
                "Name",
                "Description",
                "Quantity",
                "Price",
                ] 
                def update():
                    if len(selected_row) == 0:
                        return
                    prodID = selected_row[1] 
                    Product.update_product(
                        prodID,
                        nameInput.get(),
                        descInput.get(),
                        quantityInput.get(),
                        priceInput.get(),
                    )
                    generate_table()
                    desturi("Product edited", "Product successfully edited")
                nameInput, descInput, quantityInput, priceInput = generate_panel(edit_add_box, panel, update, columns, entity, selected_row)

            elif panel == 'add':
                columns = [
                "Name",
                "Description",
                "Quantity",
                "Price",
                # "Image"
                ] 
                def add():
                    prodID = generate(size=7)
                    product_obj = Product(
                        prodID,
                        nameInput.get(),
                        descInput.get(),
                        quantityInput.get(),
                        priceInput.get(),
                        # imageInput.get()
                    )
                    product_obj.create_product()
                    generate_table()
                    desturi("Success!", "Product Successfully Added")

                nameInput, descInput, quantityInput, priceInput = generate_panel(edit_add_box, panel, add, columns, entity, selected_row=[])
                
        select_panel()