import pandas as pd
import mysql.connector
import boto3
from io import StringIO
from datetime import datetime
import uuid

# S3 bucket details
s3_bucket = 'pizzamura-123'
from sqlalchemy import create_engine
import pandas as pd
import boto3
from io import StringIO

# MySQL connection details
MYSQL_USER = 'dewi'
MYSQL_PASSWORD = 'dewi'
MYSQL_HOST = '127.0.0.1'  # or the Docker container IP
MYSQL_PORT = '3306'
MYSQL_DATABASE = 'db'

# Create SQLAlchemy engine with allowPublicKeyRetrieval=true
jdbc_url = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"

engine = create_engine(jdbc_url)
table_name = "products"

# S3 connection details
S3_BUCKET = 'pizzamura-123'
S3_KEY = f'surabaya/{table_name}.csv'

# Connect to MySQL and execute query
try:
    with engine.connect() as connection:
        query = f"SELECT * FROM {table_name}"
        df = pd.read_sql(query, connection)
        print("Data retrieved successfully from MySQL", df)
except Exception as e:
    print(f"Error: {e}")
    exit(1)

# Convert DataFrame to CSV
csv_buffer = StringIO()
df.to_csv(csv_buffer, index=False)

# Upload CSV to S3
s3_client = boto3.client('s3')
s3_client.put_object(Bucket=S3_BUCKET, Key=S3_KEY, Body=csv_buffer.getvalue())

print(f"Data {table_name} uploaded to S3 successfully!")
