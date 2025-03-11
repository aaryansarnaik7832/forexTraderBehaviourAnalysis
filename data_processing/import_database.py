import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Radium@614",
    database="stockdatadb"
)

cursor = connection.cursor()

with open("sql_files/exchangerate.sql", "r") as file:
    sql_statements = file.read()

statements = sql_statements.split(";")

try:
    for index, statement in enumerate(statements, start=1):
        if statement.strip():
            try:
                cursor.execute(statement)
                print(f"Executed statement {index}: {statement}")
            except mysql.connector.Error as error:
                if error.errno == 1064:
                    print(f"Skipping statement {index} due to syntax error: {error}")
                else:
                    raise

    connection.commit()
    print("Changes committed successfully.")

except mysql.connector.Error as error:
    print(f"Error executing SQL statement: {error}")
    connection.rollback()

finally:
    cursor.close()
    connection.close()
