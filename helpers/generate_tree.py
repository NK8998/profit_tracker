from ..classes.classes import User
from tkinter import Toplevel, Label, Entry, Button, messagebox, StringVar, ttk

def generate_tree(parent, columns):
                # Create and configure the Treeview
        table = ttk.Treeview(
            parent,
            columns=tuple(columns),
            show="headings",
        )

        # Define and configure each heading
        headings = columns
        for heading in headings:
            table.heading(heading, text=heading)
            table.column(heading, anchor="center", stretch=True)  # Set width and allow stretching
            table.tag_configure("oddrow", background="white")
            table.tag_configure("evenrow", background="#e7e7e7")

        # Grid the table with full stretch
        table.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")


        for index, val in enumerate(User.show_user()):
            tag = "evenrow" if index % 2 == 0 else "oddrow"
            table.insert(parent="", index=index, values=val, tags=tag)

        style = ttk.Style()
        style.configure(
            "Treeview",
                font=("Helvetica", 10),
                rowheight=50,
                background="#f8f9fa",  # Light grey background
                foreground="black",
        )
        style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"))
        style.map(
            "Treeview",
            background=[("selected", "#4A4A4A")],
            foreground=[("selected", "white")],
        )

        return table
