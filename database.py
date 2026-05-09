import sqlite3

def connect():
    return sqlite3.connect("expenses.db")

def create_table():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY,
            date TEXT,
            category TEXT,
            description TEXT,
            amount REAL
        )
    ''')
    conn.commit()
    conn.close()

def add_expense(date, category, description, amount):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO expenses (date, category, description, amount)
        VALUES (?, ?, ?, ?)
    ''', (date, category, description, amount))
    conn.commit()
    conn.close()

def get_all_expenses():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses ORDER BY date DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_expense(expense_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    conn.close()

def get_monthly_summary(month, year):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT category, SUM(amount) 
        FROM expenses
        WHERE strftime('%m', date) = ? AND strftime('%Y', date) = ?
        GROUP BY category
    ''', (month, year))
    rows = cursor.fetchall()
    conn.close()
    return rows