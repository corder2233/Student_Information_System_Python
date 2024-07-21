import sqlite3

# Path to your SQLite database
db_path = r'C:\Users\ACER\Documents\my_project\Python_Project_college\Python Project\demo.db'
conn = sqlite3.connect(db_path)

# Get the list of all tables in the database
tables_query = "SELECT name FROM sqlite_master WHERE type='table';"
cursor = conn.cursor()
cursor.execute(tables_query)
tables = cursor.fetchall()

# Extract table names from the query result
table_names = [table[0] for table in tables]
print("Tables in the database:", table_names)

# Delete all data from each table
for table in table_names:
    delete_query = f"DELETE FROM {table};"
    cursor.execute(delete_query)
    conn.commit()

print("All data deleted from all tables.")

# (Optional) Verify deletion
for table in table_names:
    count_query = f"SELECT COUNT(*) FROM {table};"
    cursor.execute(count_query)
    row_count = cursor.fetchone()[0]
    print(f"Table {table} has {row_count} rows.")

# Close the database connection
conn.close()

