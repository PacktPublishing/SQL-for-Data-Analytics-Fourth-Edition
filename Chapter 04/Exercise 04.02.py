# Step 2
from sqlalchemy import create_engine, text
import pandas as pd

# Step 3
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

query = "SELECT * FROM customers"
customer_data = pd.read_sql_query(query, engine) 
customer_data.head()

# Step 4
customer_per_state = \
  customer_data[['state', 'customer_id']] \
    .groupby('state').count()
customer_per_state.head(3)

# Step 5
%matplotlib inline

# Step 6
import matplotlib.pyplot as plt
customer_per_state.plot(kind='bar')
plt.show()

# Step 7
customer_per_state.to_sql(
    'customer_per_state', 
    engine, 
    if_exists='replace'
)

# Step 8: SQL scripts to be run in psql
'''
SELECT * FROM customer_per_state LIMIT 5;
DROP TABLE customer_per_state;
'''



