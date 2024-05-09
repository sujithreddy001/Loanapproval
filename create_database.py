import psycopg2

# Connect to the default "postgres" database
conn = psycopg2.connect(
    dbname="postgres",
    user="loan",
    password="password",
    host="localhost"
)

# Create a new database named "loanapplication"
with conn.cursor() as cursor:
    cursor.execute("CREATE DATABASE loanapplication")

# Close the connection
conn.close()

