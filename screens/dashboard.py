from customtkinter import *
import tkinter as tk
from tkinter import *

# matplotlib
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#matplotlib

# helpers
from helpers.image_widget import add_image_widget
# helpers

# clases
from classes.classes import User, Transaction, Product
# classes

# 
from mock_data import profits_per_week, profit_per_Product
# 


def dashboard_screen(
            reinitialize_main_column2, 
            main_column2, 
            user_data):
        loggedInUserID = user_data['empID']
        should_refresh = reinitialize_main_column2('dashboard')
        if not should_refresh:
            return
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
        ax2.pie(profit_per_Product.values(), labels=profit_per_Product.keys(), autopct='%1.1f%%', startangle=140)
        ax2.set_title("Profit per Product")

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