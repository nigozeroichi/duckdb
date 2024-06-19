import duckdb
import pandas as pd

# Load CSV into DuckDB
conn = duckdb.connect(':memory:')  # In-memory database
df = pd.read_csv('data.csv')
conn.register('data', df)

# Query the data
result = conn.execute('SELECT * FROM data WHERE age < 30').fetchdf()

# Print the result
print(result)