from customtkinter import CTkLabel, CTkEntry, CTkButton, CTkFrame
from tkinter import StringVar


def generate_panel(parent, type, command, columns, entity, delete_command, selected_row=[]):
    CTkLabel(
        parent, 
        text=f"Add {entity}" if type == "add" else f"Edit {entity}", 
        font=("sans-serif", 26, "bold"), 
        padx=10, 
        pady=10, 
        anchor='w', 
        text_color='#515151'
    ).grid(row=0, column=0, columnspan=2)

    input_fields = {}

    row_index = 0
    for index, val in enumerate(columns):
        label = CTkLabel(
                master=parent, 
                text=f"{val}: ", 
                font=("sans-serif", 13, 'bold'), 
                anchor='w', 
                text_color='#515151',
            )
        label.grid(row=row_index + 1, column=0, sticky='w', pady=(10, 0), padx=10)
        input_field = CTkEntry(
                parent, 
                textvariable=StringVar(value=selected_row[index] if len(selected_row) > 0 else ''), 
                width=250, 
                height=35, 
                border_width=1, 
                border_color="#e9e9e9", 
                bg_color='transparent', 
                fg_color='#F1F5FF', 
                text_color="#393939"
            )
        input_field.grid(row=row_index + 2, column=0, sticky='w')
        # Store the input field in the dictionary with a descriptive key
        input_fields[val] = input_field
        row_index += 2  

    frame = CTkFrame(parent, fg_color='transparent')  # Create a frame within the parent
    frame.grid(row=(len(columns) * 2) + 1, column=0, columnspan=2, pady=(20, 20), padx=(10, 10))

    # Add the "Update" or "Add" button to the frame
    CTkButton(
        frame,
        text="Update" if type == 'edit' else 'Add',
        command=command,
        corner_radius=8,
        height=30,
        width=100,
    ).grid(row=0, column=0, padx=(5, 5))  # Use grid within the frame

    CTkButton(
        frame,
        text="Delete",
        command=delete_command,  # Replace with the appropriate delete command function
        corner_radius=8,
        height=30,
        width=100,
        fg_color='white',  # Default background color
        text_color='grey',  # Default text color
    ).grid(row=0, column=1, padx=(5, 5))  # Adjust padding for spacing

    return tuple(input_fields.get(field) for field in columns if field != None)
