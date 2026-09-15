# =========================================
# ENVIRONMENT
# =========================================

ENVIRONMENT = "DEV"

# =========================================
# CONFIGURATION
# =========================================

CONFIG = {

    "DEV": {

        # ================================
        # SQL SERVER CONNECTION
        # ================================
        "sql_server": {
            "driver": "ODBC Driver 17 for SQL Server",
            "server": "LENOVO\\SQLEXPRESS",
            "database": "ETL_SUPERSTORE"
        },

        # ================================
        # AZURE CONNECTION
        # ================================

"azure": {
            "DRIVER": "ODBC Driver 18 for SQL Server",
            "SERVER": "charan-etl-sql-2026.database.windows.net",
            "DATABASE": "ETL_DB",
            "UID": "azureadmin",
            "PWD": "06082004@As",
            "Encrypt": "yes",
            "TrustServerCertificate": "no",
            "Connection Timeout": "30"
        },

        # ================================
        # TABLE CONFIGS
        # ================================
        "tables": [

            # --------------------------------
            # SUPERSTORE TABLE (DB: ETL_SUPERSTORE)
            # --------------------------------
            {
                "name": "SUPERSTORE",


                "source_table": "ETL_SUPERSTORE.dbo.superstore_raw",
                "target_table": "SUPERSTORE_TRANSFORMED",

                "primary_key_source": "Row_ID",
                "primary_key_target": "ROW_ID",

                "filters": {
                    "Sales": ">100"
                },

                "string_rules": {
                    "Customer_Name": "upper",
                    "Category": "strip",
                    "Ship_Mode": "replace_space",
                    "City": "title"
                },

                "regex_column": "Product_Name",
                "date_column": "Order_Date"
            },

            # --------------------------------
            # CUSTOMERS TABLE (DB: ETL_DB)
            # --------------------------------
            {
                "name": "CUSTOMERS",

                # Different database
                "source_table": "ETL_DB.dbo.customers",
                "target_table": "CUSTOMERS",

                "primary_key_source": "id",
                "primary_key_target": "ID",

                "filters": {
                    "AGE": ">18"
                },

                "string_rules": {
                    "NAME": "upper",
                    "CITY": "title"
                }

            }

        ]
    }
}