# Import required modules
from sqlalchemy import create_engine, text
import pandas as pd

# Setup connection to the server
cnxn_string = (
"postgresql+psycopg2://{username}:{pswd}@{host}:{port}/{database}"
)
engine = create_engine(
    cnxn_string.format( 
        username="postgres", 
        pswd="my_password",
        host="localhost", 
        port=5432, 
        database="sqlda"
    )
)

# Fetch products table data
query = "SELECT * FROM products"
products_data = pd.read_sql_query(query, engine) 

# Confirm data is properly loaded
products_data.head(12)

# Filter products started in 2024
products_2024 = products_data[products_data['production_start_date'].dt.year == 2024]

# Confirm the data has been properly filtered
products_2024.head()

# Save the data to a products_2024 table
products_2024.to_sql(
    'products_2024', 
    engine, 
    if_exists='replace'
)

# SQL used for validating table creation in the database
'''
SELECT * FROM products_2024;
DROP TABLE products_2024;
'''
