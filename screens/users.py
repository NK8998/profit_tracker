from customtkinter import *
from tkinter import *
from tkinter import ttk
from nanoid import generate
from PIL import Image

# helpers
from helpers.panel_generator import generate_panel
# helpers

# clases
from classes.classes import PanelManager, User
# classes


def user_screen(reinitialize_main_column2, desturi, main_column2):
    panel_manager = PanelManager(None)
    should_refresh = reinitialize_main_column2('users')
    if not should_refresh:
        return
    
    for index, val in enumerate(User.show_user()):
        # print(val[5])
        pass

    # def edit_user(_):
    #     id = table.item(table.selection())["values"][0]
    #     user_arr = []
    #     selectedUser_arr = []
    #     for val in User.show_user():
    #         # print(val)
    #         if val[0] == loggedInUserID:
    #             user_arr = val
    #         if val[0] == id:
    #             selectedUser_arr = val

    #     pop_up = CTkToplevel()
    #     pop_up.title("Edit User")
    #     pop_up.attributes("-topmost", True)
    #     pop_up.minsize(600, 400)

    #     if "UI" == "UI":
    #         CTkLabel(
    #             pop_up,
    #             text="Edit User Details",
    #             font=("sans-serif", 40, "bold"),
    #             padx=100,
    #             pady=50,
    #         ).grid(row=0, column=0, columnspan=2)

    #         CTkLabel(
    #             pop_up, text="Employee ID:", pady=10, font=("sans-serif", 20)
    #         ).grid(row=1, column=0)
    #         empIDInput = CTkEntry(
    #             pop_up, textvariable=StringVar(value=selectedUser_arr[1])
    #         )
    #         empIDInput.grid(row=1, column=1)

    #         CTkLabel(
    #             pop_up, text="First name:", pady=10, font=("sans-serif", 20)
    #         ).grid(row=2, column=0)
    #         fnameInput = CTkEntry(
    #             pop_up, textvariable=StringVar(value=selectedUser_arr[2])
    #         )
    #         fnameInput.grid(row=2, column=1)

    #         CTkLabel(
    #             pop_up, text="Last name:", pady=10, font=("sans-serif", 20)
    #         ).grid(row=3, column=0)
    #         lnameInput = CTkEntry(
    #             pop_up, textvariable=StringVar(value=selectedUser_arr[3])
    #         )
    #         lnameInput.grid(row=3, column=1)

    #         CTkLabel(pop_up, text="Salary:", pady=10, font=("sans-serif", 20)).grid(
    #             row=4, column=0
    #         )
    #         salaryInput = CTkEntry(
    #             pop_up, textvariable=StringVar(value=selectedUser_arr[4])
    #         )
    #         salaryInput.grid(row=4, column=1)

    #         CTkLabel(
    #             pop_up, text="National ID:", pady=10, font=("sans-serif", 20)
    #         ).grid(row=5, column=0)
    #         natIDInput = CTkEntry(
    #             pop_up, textvariable=StringVar(value=selectedUser_arr[5])
    #         )
    #         natIDInput.grid(row=5, column=1)

    #         CTkLabel(
    #             pop_up,
    #             text="*** Enter Admin password confirm details:",
    #             pady=10,
    #             font=("sans-serif", 20),
    #         ).grid(row=6, column=0)
    #         pwInput = CTkEntry(pop_up, show="*")
    #         pwInput.grid(row=6, column=1)

    #         CTkButton(pop_up, text="Update", command=update).grid(
    #             row=7, column=0, columnspan=2, pady=(20, 20), padx=(10, 10)
    #         )

    #         pop_up.wm_transient()

    # def delete_user():
    #     # print("here33", table.item(table.selection())["values"][0])
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
    #             User.delete_user(id)

    #             ud = CTk()
    #             ud.lift()
    #             ud.title("User deleted")
    #             ud.iconbitmap("./images/main/profit.ico")
    #             ud.attributes("-topmost", True)
    #             ud.bell()
    #             if "UI" == "UI":
    #                 wp = CTkLabel(
    #                     mf,
    #                     text="User successfully deleted",
    #                     font=("sans-serif", 30, "bold"),
    #                     bg_color="red",
    #                 )
    #                 wp.pack(padx=10, pady=10)
    #             mf.mainloop()

    #         else:

    #             mf = CTk()
    #             mf.lift()
    #             mf.title("Wrong Password")
    #             mf.iconbitmap("./images/main/profit.ico")
    #             mf.attributes("-topmost", True)
    #             mf.bell()
    #             if "UI" == "UI":
    #                 wp = CTkLabel(
    #                     mf,
    #                     text="Wrong password entered!",
    #                     font=("sans-serif", 30, "bold"),
    #                     bg_color="red",
    #                 )
    #                 wp.pack(padx=10, pady=10)
    #             mf.mainloop()

    #         return

    #     pop_up = CTk()
    #     pop_up.lift()
    #     pop_up.title("Delete User")
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

        global selected_row
        selected_row = []

        headings = ["ID", "Employee ID", "email", "First Name", "Last Name", "Salary", "National ID", "Password", "IsAdmin"]

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

        def delete_user():
            if len(selected_row) == 0:
                desturi("...", "Please select a user first")
                return
            user_id = selected_row[1]
            User.delete_user(user_id)
            generate_table()
            desturi("Success", "User successfully deleted")


        def select_panel(panel = 'edit'):
            
            entity = 'User'
            columns = ["email", "First Name", "Last Name", "Salary", "National ID", "Password"]
            panel_manager.set_current_panel(panel)
            for widget in edit_add_box.winfo_children():
                widget.destroy()
            
            
            if panel == 'edit':
                adjusted_selected_row = selected_row[2:]

                def update():
                    if len(selected_row) == 0:
                        desturi("Error", "No user selected for editing!")
                        return

                    # Check for missing fields
                    if not emailInput.get().strip():
                        desturi("Error", "Email field is required!")
                        return
                    if not fnameInput.get().strip():
                        desturi("Error", "First Name field is required!")
                        return
                    if not lnameInput.get().strip():
                        desturi("Error", "Last Name field is required!")
                        return
                    if not salaryInput.get().strip():
                        desturi("Error", "Salary field is required!")
                        return
                    if not natIDInput.get().strip():
                        desturi("Error", "National ID field is required!")
                        return
                    if not pwInput.get().strip():
                        desturi("Error", "Password field is required!")
                        return

                    # Proceed with updating the user
                    empID = selected_row[1]
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
                    desturi("User Edited", "User successfully edited")

                emailInput, fnameInput, lnameInput, salaryInput, natIDInput, pwInput = generate_panel(
                    edit_add_box, panel, update, columns, entity, delete_user, adjusted_selected_row
                )


            elif panel == 'add':
                def add():
                    # Check for missing fields
                    if not emailInput.get().strip():
                        desturi("Error", "Email field is required!")
                        return
                    if not fnameInput.get().strip():
                        desturi("Error", "First Name field is required!")
                        return
                    if not lnameInput.get().strip():
                        desturi("Error", "Last Name field is required!")
                        return
                    if not salaryInput.get().strip():
                        desturi("Error", "Salary field is required!")
                        return
                    if not natIDInput.get().strip():
                        desturi("Error", "National ID field is required!")
                        return
                    if not pwInput.get().strip():
                        desturi("Error", "Password field is required!")
                        return

                    # Proceed if all fields are valid
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

                emailInput, fnameInput, lnameInput, salaryInput, natIDInput, pwInput = generate_panel(
                    edit_add_box, panel, add, columns, entity, delete_user, selected_row=[]
                )

                
        select_panel()