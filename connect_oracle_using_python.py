import cx_Oracle

# Connect to the database
conn = cx_Oracle.connect("user_name/password@host:port/service_name")

# Create a cursor
cursor = conn.cursor()

# Execute a query
query = "SELECT * FROM your_table"
cursor.execute(query)

# Fetch the results
results = cursor.fetchall()

# Loop through the results and print them
for result in results:
    print(result)

# Close the cursor and connection
cursor.close()
conn.close()
