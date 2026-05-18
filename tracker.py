from datetime import datetime
from database import *

def add_new_expense():
    print("\n--- Add Expense ---")
    date = input("Date (DD-MM-YYYY) or press Enter for today: ")
    if date == ""or"/"in date:
        date = datetime.today().strftime('%d-%m-%y')
    
    print("Categories: Food, Transport, Shopping, Bills, Health, Other")
    category = input("Category: ").capitalize()
    description = input("Description: ")
    
    try:
        amount = float(input("Amount (₹): "))
    except ValueError:
        print("Invalid amount!")
        return
    
    add_expense(date, category, description, amount)
    print("Expense added successfully!")

def view_expenses():
    print("\n--- All Expenses ---")
    expenses = get_all_expenses()
    
    if not expenses:
        print("No expenses found.")
        return
    
    print(f" {'Date':<12} {'Category':<12} {'Description':<20} {'Amount':>10}")
    print("-" * 65)
    
    total = 0
    for exp in expenses:
        print(f" {exp[1]:<12} {exp[2]:<12} {exp[3]:<20} ₹{exp[4]:>9.2f}")
        total += exp[4]
    
    print("-" * 65)
    print(f"{'Total':<49} ₹{total:>9.2f}")

def delete_an_expense():
    view_expenses()
    try:
        exp_id = int(input("\nEnter ID to delete: "))
        delete_expense(exp_id)
        print("Expense deleted!")
    except ValueError:
        print("Invalid ID!")

def monthly_summary():
    print("\n--- Monthly Summary ---")
    month = input("Enter Month (01-12): ")
    year = input("Enter Year (YYYY): ")
    
    summary = get_monthly_summary(month, year)
    
    if not summary:
        print("No data found for this month.")
        return
    
    print(f"\n{'Category':<15} {'Total Amount':>15}")
    print("-" * 32)
    
    grand_total = 0
    for row in summary:
        print(f"{row[0]:<15} ₹{row[1]:>14.2f}")
        grand_total += row[1]
    
    print("-" * 32)
    print(f"{'Grand Total':<15} ₹{grand_total:>14.2f}")
