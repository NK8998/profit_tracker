from customtkinter import *
import tkinter as tk
from tkinter import *
from collections import defaultdict
from datetime import datetime, timedelta


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
# from mock_data import profits_per_week, profit_per_Product
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

        def process_transactions(transactions):
            profits_by_week = defaultdict(float)

            for transaction in transactions:
                # Parse the time string into a datetime object
                transaction_time = datetime.strptime(transaction['time'], "%Y-%m-%d %H:%M:%S")
                
                # Calculate the start of the week (Monday)
                week_start = transaction_time - timedelta(days=transaction_time.weekday())
                week_end = week_start + timedelta(days=6)

                # Format as "Jan 1 - Jan 7"
                week_range = f"{week_start.strftime('%b %d')} - {week_end.strftime('%b %d')}"
                
                # Calculating the profit
                profit = (transaction['selling_price'] - transaction['buying_price']) * transaction['quantity']
                profits_by_week[week_range] += profit

            # Sort the weeks based on their start date
            sorted_profits_by_week = dict(
                sorted(profits_by_week.items(), key=lambda item: datetime.strptime(item[0].split(" - ")[0], "%b %d"))
            )

            return sorted_profits_by_week

        # Example usage
        transactions = Transaction.get_transcations_as_Dict()

        # Group transactions by week and calculate profits
        profits_per_week = process_transactions(transactions)


        plt.rcParams["axes.prop_cycle"] = plt.cycler(
            color=["#44BEE3", "#4E63E5", "#679EE0", "#3DB5E0", "#2274E6"])
        
        # BAR_CHART
        # Create the bar chart figure
        fig = Figure(figsize=(9, 3), dpi=100)
        ax = fig.add_subplot(111)
        ax.bar(profits_per_week.keys(), profits_per_week.values())
        ax.set_title("Profit per Week")
        ax.set_xlabel("Week")
        ax.set_ylabel("Profits")

        # Embed the figure into the Tkinter frame
        canvas = FigureCanvasTkAgg(fig, master=chart_row_frame)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0, padx=10, pady=10, sticky='nse')


        profit_per_Product = Transaction.get_top_5_products_based_on_transactions()

        # Create the pie chart figure
        fig2 = Figure(figsize=(6, 4), dpi=100)
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

        stats_row_frame = CTkScrollableFrame(main_page_frame, height= 400, orientation='horizontal', fg_color='#eeeeee')
        stats_row_frame.grid(row=3, column=0, padx=20, pady=(10, 20), sticky=NSEW)   

        stats_row_frame.rowconfigure(0, weight=1)
        # stats_row_frame.columnconfigure(1, weight=1)
        # stats_row_frame.grid_propagate(False)




        def calculate_stats():
            # Total inventory cost (expenditure)
            products = Product.get_products_as_Dict()
            total_inventory_cost = 0
            for p in products:
                total_inventory_cost += p['buying_price'] * p['quantity']
            
            # Total sales (gross income)
            transactions = Transaction.get_transcations_as_Dict()
            total_sales = 0
            for t in transactions:
                total_sales += t['selling_price'] * t['quantity']

            # Total cost of sold products (cost of goods sold)
            total_inventory_cost_sold = 0
            for t in transactions:
                total_inventory_cost_sold += t['buying_price'] * t['quantity']

            # Net revenue (profit from sales)
            net_revenue = total_sales - total_inventory_cost_sold

            return net_revenue, total_inventory_cost, total_sales, total_inventory_cost_sold

        # Calling the function
        net_revenue, total_inventory_cost, total_sales, total_inventory_cost_sold = calculate_stats()

        box_1 = CTkFrame(stats_row_frame, bg_color='transparent', fg_color="#d8d8d8", width=350, height=300)
        box_1.grid(row=0, column=0, padx=20, pady=20)

        box_1.grid_propagate(False)
        box_1.columnconfigure(0, weight=1)
        box_1.columnconfigure(1, weight=0)  # Column 1 for the image

        # Title and icon at the top
        CTkLabel(
            master=box_1,
            text="Earnings so far:",
            font=("sans-serif", 20, 'bold'), 
            anchor='nw',
            text_color="white",
        ).grid(row=0, column=0, pady=(20, 10), padx=20, sticky='w')

        box_1_image = add_image_widget(box_1, './images/main/profits.png', width=60, height=60, background='#d8d8d8')
        box_1_image.grid(row=0, column=1, sticky='ne', padx=20)

        # Create a separator line for visual clarity
        separator = CTkFrame(master=box_1, height=2, fg_color="white")
        separator.grid(row=1, column=0, columnspan=2, pady=10, sticky='ew')

        # Stats Labels with styling
        stats_font = ("sans-serif", 14)
        stats_color = "black"
        highlight_color = "#003366"  # Darker blue for emphasis

        # Total inventory cost
        CTkLabel(
            master=box_1,
            text=f"Total Inventory Cost: Kes.{total_inventory_cost}",
            font=stats_font,
            anchor='w',
            text_color=stats_color
        ).grid(row=2, column=0, pady=(10, 5), padx=20, sticky='w')

        # Total sales
        CTkLabel(
            master=box_1,
            text=f"Total Sales: Kes.{total_sales}",
            font=stats_font,
            anchor='w',
            text_color=stats_color
        ).grid(row=3, column=0, pady=(10, 5), padx=20, sticky='w')

        # Total inventory cost of sold products
        CTkLabel(
            master=box_1,
            text=f"Total Inventory Cost Sold: Kes.{total_inventory_cost_sold}",
            font=stats_font,
            anchor='w',
            text_color=stats_color
        ).grid(row=4, column=0, pady=(10, 5), padx=20, sticky='w')

        # Net Revenue (highlighted with a different color)
        CTkLabel(
            master=box_1,
            text=f"Net Revenue: Kes.{net_revenue}",
            font=("sans-serif", 16, 'bold'),
            anchor='w',
            text_color=highlight_color
        ).grid(row=5, column=0, pady=(15, 5), padx=20, sticky='w')

        # Optional separator for balance or future stats
        separator_2 = CTkFrame(master=box_1, height=2, fg_color="white")
        separator_2.grid(row=6, column=0, columnspan=2, pady=10, sticky='ew')

        
        box_2 = CTkFrame(stats_row_frame, bg_color='transparent', fg_color="#d8d8d8", width=350, height=300)
        box_2.grid(row=0, column=2, padx=(50, 20), pady=20, sticky='e')

        box_2.grid_propagate(False)
        box_2.columnconfigure(0, weight=1)
        box_2.columnconfigure(1, weight=0)  # Column 1 for the image

        # Title and icon at the top
        CTkLabel(
            master=box_2,
            text="Total Employees:",
            font=("sans-serif", 20, 'bold'), 
            anchor='nw',
            text_color="white",
        ).grid(row=0, column=0, pady=(20, 10), padx=20, sticky='w')

        box_2_image = add_image_widget(box_2, './images/main/user-group.png', width=60, height=60, background='#d8d8d8')
        box_2_image.grid(row=0, column=1, sticky='ne', padx=20, pady=10)

        # Create a separator line for visual clarity
        separator = CTkFrame(master=box_2, height=2, fg_color="white")
        separator.grid(row=1, column=0, columnspan=2, pady=10, sticky='ew')

        # Display total employees with styling
        total_users = User.get_total_users() - 1  # Excluding the admin

        CTkLabel(
            master=box_2,
            text=f"{total_users}",
            font=("sans-serif", 30, 'bold'), 
            anchor='center',
            text_color="black"
        ).grid(row=2, column=0, pady=(40, 40), columnspan=2)

        # Optional separator for balance or future stats (if needed)
        separator_2 = CTkFrame(master=box_2, height=2, fg_color="white")
        separator_2.grid(row=3, column=0, columnspan=2, pady=10, sticky='ew')
