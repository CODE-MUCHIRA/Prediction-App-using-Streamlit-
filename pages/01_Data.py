import streamlit as st
import pandas as pd
from dotenv import dotenv_values
import pyodbc

st.set_page_config(
    page_title="Home",
    page_icon=":)",
    layout="wide"
)

st.title("DATA")

# Load environment variables from .env file into a dictionary
environment_variables = dotenv_values('.env')

# Get the values for the credentials you set in the '.env' file
database = environment_variables.get("DATABASE")
server = environment_variables.get("SERVER")
username = environment_variables.get("USERNAME")
password = environment_variables.get("PASSWORD")

connection_string = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"

# Use the connect method of the pyodbc library and pass in the connection string.
connection = pyodbc.connect(connection_string)

# Now the sql query to get the data is what what you see below.
# Note that you will not have permissions to insert delete or update this database table.
query = "Select * from dbo.LP2_Telco_churn_first_3000"

# Load data into DataFrame directly from the SQL query
df = pd.read_sql(query, connection)

# Close the connection
connection.close()

# Display DataFrame in Streamlit
st.dataframe(df)
