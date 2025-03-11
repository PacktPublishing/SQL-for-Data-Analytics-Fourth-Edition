# # Data Management using Python
# ## Using Python with SQLAlchemy and pandas
from sqlalchemy import create_engine, text
import pandas as pd

%matplotlib inline

cnxn_string = (
    "postgresql+psycopg2://{username}:{pswd}@{host}:{port}/{database}"
) 
print(cnxn_string)

engine = create_engine(
    cnxn_string.format( 
        username="postgres", 
        pswd="my_password",
        host="localhost", 
        port=5432, 
        database="sqlda"
    )
)

with engine.connect() as conn:
  result = conn.execute(
    text("SELECT * FROM customers LIMIT 2")
  ).fetchall()
print(result)

# ## Reading and Writing to a Database with pandas
customers_data = pd.read_sql_table('customers', engine)

customers_data.head()






