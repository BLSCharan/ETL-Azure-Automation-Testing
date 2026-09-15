import pyodbc

try:
    # =========================================================
    # CONNECT TO SQL SERVER
    # =========================================================

    connection = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost\\SQLEXPRESS;"
        "DATABASE=ETL_DB;"
        "Trusted_Connection=yes;"
    )

    cursor = connection.cursor()

    print("Connected Successfully")


    # =========================================================
    # FIRST QUERY - SELECT ALL CUSTOMERS
    # =========================================================

    cursor.execute("SELECT * FROM dbo.customers")

    rows = cursor.fetchall()

    print("All Customers:")

    for row in rows:
        print(row)


    # =========================================================
    # SECOND QUERY - COUNT TOTAL RECORDS
    # =========================================================

    cursor.execute("SELECT COUNT(*) FROM dbo.customers")

    count = cursor.fetchone()

    print(count)
    print("Total Records:", count)


    # =========================================================
    # THIRD QUERY - PARAMETERIZED SELECT
    # =========================================================

    customer_id = 4

    cursor.execute(
        "SELECT * FROM dbo.customers WHERE id = ?",
        customer_id
    )

    result = cursor.fetchone()

    print("Customer with ID 1:", result)


    # =========================================================
    # INSERT A NEW CUSTOMER
    # =========================================================

    cursor.execute(
        "INSERT INTO customers VALUES (?, ?, ?, ?)",
        (10, 'cherry', 'mumbai', 22)
    )

    # Save the inserted record permanently
    connection.commit()

    print("Record Inserted Successfully")


    # =========================================================
    # VERIFY INSERT - SELECT ALL CUSTOMERS AGAIN
    # =========================================================

    cursor.execute("SELECT * FROM dbo.customers")

    rows = cursor.fetchall()

    print("All Customers:")

    for row in rows:
        print(row)


# =============================================================
# ERROR HANDLING
# =============================================================

except Exception as e:

    print("Error:", e)


# =============================================================
# CLOSE CONNECTION
# =============================================================

finally:

    cursor.close()
    connection.close()