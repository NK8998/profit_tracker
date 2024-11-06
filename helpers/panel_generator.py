from customtkinter import CTk, CTkLabel, CTkEntry, CTkButton
from tkinter import Toplevel, Label, Entry, Button, messagebox, StringVar, ttk


def generate_panel(parent, type, command, selected_user=[]):

    CTkLabel(
        parent, 
        text="Add User" if type == "add" else "Edit User", 
        font=("sans-serif", 26, "bold"), 
        padx=10, 
        pady=10, 
        anchor='w', 
        text_color='#515151'
    ).grid(row=0, column=0, columnspan=2)

    CTkLabel(
        parent, 
        text="Email:", 
        font=("sans-serif", 13, 'bold'), 
        anchor='w', 
        text_color='#515151'
    ).grid(row=1, column=0, sticky='w', pady=(10, 0), padx=10)
    empIDInput = CTkEntry(
        parent, 
        textvariable=StringVar(value=selected_user[2] if len(selected_user) > 1 else ''), 
        width=250, 
        height=35, 
        border_width=1, 
        border_color="#e9e9e9", 
        bg_color='transparent', 
        fg_color='#F1F5FF', 
        text_color="#393939"
    )
    empIDInput.grid(row=2, column=0)

    CTkLabel(
        parent, 
        text="First name:", 
        font=("sans-serif", 13, 'bold'), 
        anchor='w', 
        text_color='#515151'
    ).grid(row=3, column=0, sticky='w', pady=(10, 0), padx=10)
    fnameInput = CTkEntry(
        parent, 
        textvariable=StringVar(value=selected_user[3] if len(selected_user) > 1 else ''), 
        width=250, 
        height=35, 
        border_width=1, 
        border_color="#e9e9e9", 
        bg_color='transparent', 
        fg_color='#F1F5FF', 
        text_color="#393939"
    )
    fnameInput.grid(row=4, column=0)

    CTkLabel(
        parent, 
        text="Last name:",         
        font=("sans-serif", 13, 'bold'), 
        anchor='w', 
        text_color='#515151'
    ).grid(row=5, column=0, sticky='w', pady=(10, 0), padx=10)
    lnameInput = CTkEntry(
        parent, 
        textvariable=StringVar(value=selected_user[4] if len(selected_user) > 1 else ''),         
        width=250, 
        height=35, 
        border_width=1, 
        border_color="#e9e9e9", 
        bg_color='transparent', 
        fg_color='#F1F5FF', 
        text_color="#393939"
    )
    lnameInput.grid(row=6, column=0)

    CTkLabel(
        parent, 
        text="Salary:",         
        font=("sans-serif", 13, 'bold'), 
        anchor='w', 
        text_color='#515151'
    ).grid(row=7, column=0, sticky='w', pady=(10, 0), padx=10)
    salaryInput = CTkEntry(
        parent, 
        textvariable=StringVar(value=selected_user[5] if len(selected_user) > 1 else ''),         
        width=250, 
        height=35, 
        border_width=1, 
        border_color="#e9e9e9", 
        bg_color='transparent', 
        fg_color='#F1F5FF', 
        text_color="#393939"
    )
    salaryInput.grid(row=8, column=0)

    CTkLabel(
        parent, 
        text="National ID:",         
        font=("sans-serif", 13, 'bold'), 
        anchor='w', 
        text_color='#515151'
    ).grid(row=9, column=0, sticky='w', pady=(10, 0), padx=10)
    natIDInput = CTkEntry(
        parent, 
        textvariable=StringVar(value=selected_user[6] if len(selected_user) > 1 else ''),         
        width=250, 
        height=35, 
        border_width=1, 
        border_color="#e9e9e9", 
        bg_color='transparent', 
        fg_color='#F1F5FF', 
        text_color="#393939"
    )
    natIDInput.grid(row=10, column=0)

    CTkLabel(
        parent, 
        text="Password:",         
        font=("sans-serif", 13, 'bold'), 
        anchor='w', 
        text_color='#515151'
    ).grid(row=11, column=0, sticky='w', pady=(10, 0), padx=10)
    pwInput = CTkEntry(
        parent, 
        show="", 
        textvariable=StringVar(value=selected_user[7] if len(selected_user) > 1 else ''),         
        width=250, 
        height=35, 
        border_width=1, 
        border_color="#e9e9e9", 
        bg_color='transparent', 
        fg_color='#F1F5FF', 
        text_color="#393939"
    )
    pwInput.grid(row=12, column=0)
    

    CTkButton(parent, text="Update" if type=='edit' else 'Add', command=command, corner_radius=1000, height=40).grid(
        row=13, column=0, columnspan=2, pady=(20, 20), padx=(15, 15)
    )

    return empIDInput, fnameInput, lnameInput, salaryInput, natIDInput, pwInput