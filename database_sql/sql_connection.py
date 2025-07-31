import pymysql

# connecting the python to sql database
connection = pymysql.connect(
    host="",
    user="root",
    password="",
    database="startersql",
    port=1234
)

#creating the cursor
cursor = connection.cursor()

# Example query
# cursor.execute("SELECT * FROM users")
cursor.execute("select users.name,addresses.city,addresses.id as aadress_id,users.id,addresses.pincode from users inner join addresses on users.id = addresses.user_id")

# Fetch results
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close connection
cursor.close()
connection.close()