import pandas as pd

from sql_server import get_sql_server_engine
from ETL_AT_SSMS_AZURE.azure_connect import get_azure_sql_engine


# ---------------------------------
# EXTRACT FROM LOCAL SQL SERVER
# ---------------------------------

def extract_data():

    engine = get_sql_server_engine()

    data = pd.read_sql(
        "SELECT * FROM dbo.superstore_raw",
        engine
    )

    print(f"Extracted {len(data)} rows from SQL Server")

    return data


# ---------------------------------
# LOAD TO AZURE SQL
# ---------------------------------

def load_raw_to_azure(data):

    # Convert column names to uppercase
    data.columns = data.columns.str.upper()

    engine = get_azure_sql_engine()

    data.to_sql(
        name="SUPERSTORE",
        schema="dbo",
        con=engine,
        if_exists="append",
        index=False,
        chunksize=500
    )

    print("Data loaded successfully into Azure SQL 🚀")


# ---------------------------------
# MAIN
# ---------------------------------

if __name__ == "__main__":

    dataset = extract_data()

    load_raw_to_azure(dataset)

    print("RAW LOAD TO AZURE COMPLETED ✅")