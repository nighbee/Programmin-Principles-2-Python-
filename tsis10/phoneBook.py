import csv
import psycopg2

# Connect to the database
conn = psycopg2.connect(database="phonebook", user="postgres", password="72zv5u3xp")
cur = conn.cursor()

# # Create the contacts table
# cur.execute("CREATE TABLE contacts (id SERIAL PRIMARY KEY, first_name VARCHAR(50) NOT NULL, last_name VARCHAR(50) NOT NULL, phone_number VARCHAR(20) NOT NULL)")

# # Insert data from CSV file
# with open('phonebook.csv', 'r') as f:
#     reader = csv.reader(f)
#     next(reader)  # skip header row
#     for row in reader:
#         first_name = row[0]
#         last_name = row[1]
#         phone_number = row[2]
#         cur.execute("INSERT INTO contacts (first_name, last_name, phone_number) VALUES (%s, %s, %s)", (first_name, last_name, phone_number))

# Insert data from console
while True:
    first_name = input("Enter first name (or leave blank to exit): ")
    if not first_name:
        break
    last_name = input("Enter last name: ")
    phone_number = input("Enter phone number: ")
    cur.execute("INSERT INTO contacts (first_name, last_name, phone_number) VALUES (%s, %s, %s)", (first_name, last_name, phone_number))

# Update data
id = input("Enter contact ID to update: ")
new_first_name = input("Enter new first name (or leave blank to skip): ")
new_last_name = input("Enter new last name (or leave blank to skip): ")
new_phone_number = input("Enter new phone number (or leave blank to skip): ")
if new_first_name:
    cur.execute("UPDATE contacts SET first_name = %s WHERE id = %s", (new_first_name, id))
if new_last_name:
    cur.execute("UPDATE contacts SET last_name = %s WHERE id = %s", (new_last_name, id))
if new_phone_number:
    cur.execute("UPDATE contacts SET phone_number = %s WHERE id = %s", (new_phone_number, id))

# Query data
cur.execute("SELECT * FROM contacts")
rows = cur.fetchall()
for row in rows:
    print(f"{row[0]} - {row[1]} {row[2]}: {row[3]}")

# Delete data
delete_by = input("Enter 'name' to delete by name, 'phone' to delete by phone number: ")
if delete_by == "name":
    name = input("Enter name to delete: ")
    cur.execute("DELETE FROM contacts WHERE first_name = %s OR last_name = %s", (name, name))
elif delete_by == "phone":
    phone_number = input("Enter phone number to delete: ")
    cur.execute("DELETE FROM contacts WHERE phone_number = %s", (phone_number,))

# Commit changes and close connection
conn.commit()
cur.close()
conn.close()
