from database import create_table
from tracker import *

def main():
    create_table() # DB initialize
    
    while True:
        print("\n====== Expense Tracker ======")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Delete Expense")
        print("4. Monthly Summary")
        print("5. Exit")
        print("=============================")
        
        choice = input("Enter choice (1-5): ")
        
        if choice == "1":
            add_new_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_an_expense()
        elif choice == "4":
            monthly_summary()
        elif choice == "5":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()