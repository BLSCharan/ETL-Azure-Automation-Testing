# import urllib.parse
# from sqlalchemy import create_engine
#
#
# # =========================================================
# # AZURE SQL DATABASE CONFIGURATION
# # =========================================================
#
# AZURE_SERVER = "********"
# AZURE_DATABASE = "********"
# AZURE_USERNAME = "********"
# AZURE_PASSWORD = "********"
#
#
# # =========================================================
# # GET AZURE SQL ENGINE
# # =========================================================
#
# def get_azure_sql_engine():
#
#     connection_string = (
#         "DRIVER={ODBC Driver 18 for SQL Server};"
#         f"SERVER={AZURE_SERVER};"
#         f"DATABASE={AZURE_DATABASE};"
#         f"UID={AZURE_USERNAME};"
#         f"PWD={AZURE_PASSWORD};"
#         "Encrypt=yes;"
#         "TrustServerCertificate=no;"
#         "Connection Timeout=30;"
#     )
#     print(connection_string)
#
#     params = urllib.parse.quote_plus(connection_string)
#     print(params)
#
#     engine = create_engine(
#         f"mssql+pyodbc:///?odbc_connect={params}"
#     )
#     print(engine)
#
#     return engine
#
# get_azure_sql_engine()


import pyodbc

# =========================================================
# CONNECT TO AZURE SQL
# =========================================================

try:

    connection = pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};"
        "SERVER=********;"
        "DATABASE=********;"
        "UID=********;"
        "PWD=********;"
        "Encrypt=yes;"
        "TrustServerCertificate=no;"
        "Connection Timeout=30;"
    )

    cursor = connection.cursor()

    print("Connected Successfully")


    # =====================================================
    # FIRST QUERY - GET ALL CUSTOMERS
    # =====================================================

    cursor.execute("SELECT * FROM dbo.customers")

    rows = cursor.fetchall()

    print("All Customers:")

    for row in rows:
        print(row)


    # =====================================================
    # SECOND QUERY - COUNT RECORDS
    # =====================================================

    cursor.execute("SELECT COUNT(*) FROM dbo.customers")

    count = cursor.fetchone()[0]

    print("Total Records:", count)


    # =====================================================
    # THIRD QUERY - PARAMETERIZED SELECT
    # =====================================================

    customer_id = 1

    cursor.execute(
        "SELECT * FROM dbo.customers WHERE id = ?",
        customer_id
    )

    result = cursor.fetchone()

    print("Customer with ID 1:", result)


    # =====================================================
    # INSERT RECORD
    # =====================================================

    cursor.execute(
        "INSERT INTO dbo.customers VALUES (?, ?, ?, ?)",
        (8, "param", "mumbai", 22)
    )

    connection.commit()

    print("Record Inserted Successfully")


    # =====================================================
    # VERIFY INSERT
    # =====================================================

    cursor.execute("SELECT * FROM dbo.customers")

    rows = cursor.fetchall()

    print("All Customers After Insert:")

    for row in rows:
        print(row)


except Exception as e:

    print("Azure SQL Error:", e)


finally:

    if 'cursor' in locals():
        cursor.close()

    if 'connection' in locals():
        connection.close()

    print("Connection Closed")
