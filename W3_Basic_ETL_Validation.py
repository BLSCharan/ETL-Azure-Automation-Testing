import pyodbc
import snowflake.connector
import pandas as pd
import logging
from datetime import datetime

#Logging Configuration

log_file = f"etl_validation_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("ETL Validation Process Started")


#SQL SERVER CONNECTION
try:
    sql_connection = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost\\SQLEXPRESS;"
        "DATABASE=ETL_DB;"
        "Trusted_Connection=yes;"
    )
    logging.info("Connected to SQL Server Successfully")

except Exception as e:
    logging.error(f"SQL Server Connection Error: {e}")
    raise


#AZURE CONNECTION

try:
    az_connection = pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};"
        "SERVER=charan-etl-sql-2026.database.windows.net;"
        "DATABASE=ETL_DB;"
        "UID=azureadmin;"
        "PWD=06082004@As;"
        "Encrypt=yes;"
        "TrustServerCertificate=no;"
        "Connection Timeout=30;"
    )

    print("Azure SQL connection established")

except Exception as e:
    print(f"Azure SQL Connection Error: {e}")
    raise


#LOAD DATA INTO PANDAS DATAFRAMES

source_query = "SELECT * FROM dbo.customers"
target_query = "SELECT * FROM customers"

try:
    df_source = pd.read_sql(source_query, sql_connection)
    df_target = pd.read_sql(target_query, az_connection)
    print("df_source",df_source)
    print("df_target",df_target)

    logging.info("Data loaded into Pandas DataFrames successfully")

except Exception as e:
    logging.error(f"Error loading data into Pandas: {e}")
    raise