

        # row_3 = tk.Frame(window_obj, bg="white")
        # row_3.pack(side="top", fill='both', expand=True)

        # separator_thickness = 1
        # debounce_delay = 20  # Delay in milliseconds

        # labels_arr = []

        # def generate_row(arr, type):
        #     new_row = tk.Frame(row_3, bg=("#3a3f52" if type == 'heading' else 'white'))
        #     new_row.pack(side='top', fill='x', padx=20)
        #     if type == 'tb_row':
        #         underline = tk.Frame(row_3, bg="#e6e6e6", width=separator_thickness)
        #         underline.pack(side='top', fill='x', padx=20)

        #     for index, value in enumerate(arr):
        #         label = CTkLabel(
        #             new_row, 
        #             text=value, 
        #             font=("sans-serif", 13, 'normal'),
        #             text_color="#f7f7f7" if type == 'heading' else 'black',
        #         )
        #         label.pack(side="left", fill='x') 
        #         labels_arr.append(label)
        #         if index < len(arr) - 1:       # Border frame for the image
        #             border_frame = tk.Frame(new_row, bg="#e6e6e6", width=separator_thickness)  # Border width and color
        #             border_frame.pack(side='left', fill='y')




        # headings = ['Receipt ID', 'Employee ID', 'Product ID', 'Quantity', 'Price', 'Discount', 'Time']
        # generate_row(headings, 'heading')

        # transactions = Transaction.show_transaction()

        # for transaction in transactions:
        #     generate_row(transaction, 'tb_row')

        # def recalculate_width(event):

        #     row_3.after(debounce_delay, update_label_width)
        # def update_label_width():            
        #     total_width = row_3.winfo_width()
        #     separator_space = (len(headings) - 1) * separator_thickness
        #     new_width = (total_width - separator_space) /( len(headings) + 2)          
        #     for label in labels_arr:
        #         label.configure(width=new_width)

        
        # window_obj.bind("<Configure>", recalculate_width)