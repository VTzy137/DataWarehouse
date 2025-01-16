import pandas as pd
from sqlalchemy import create_engine

# Define the PostgreSQL database credentials
username = 'pastgres'
password = 'Truong123'
host = 'your_host'
port = '5432'  # Default PostgreSQL port
database = 'newdatabase'

# Create a database connection
engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}')

# Define the SQL query
query = "SELECT * FROM sales_fact"  # Modify table name to match your data warehouse

# Load data into a Pandas DataFrame
df = pd.read_sql(query, engine)

# Now you can analyze the data with Pandas
print(df.head())  # Display the first few rows
