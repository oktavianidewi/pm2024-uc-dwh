import pandas as pd
import boto3
from io import StringIO
from sqlalchemy import create_engine
import pandas as pd
import boto3
from io import StringIO
import os

# MySQL connection details
MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_HOST = os.getenv('MYSQL_HOST')  # or the Docker container IP
MYSQL_PORT = os.getenv('MYSQL_PORT')
MYSQL_DATABASE = os.getenv('MYSQL_DATABASE')

# Create SQLAlchemy engine with allowPublicKeyRetrieval=true
JDBC_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"

engine = create_engine(JDBC_URL)
TABLE_NAMES = ["order_detail", "orders", "products", "users"]

# S3 connection details
S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')

for table_name in TABLE_NAMES:
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
    s3_client.put_object(Bucket=S3_BUCKET_NAME, Key=S3_KEY, Body=csv_buffer.getvalue())

    print(f"Data {table_name} uploaded to S3 successfully!")
