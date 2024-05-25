import psycopg2
import os 

S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')
IAM_ROLE_ARN = os.getenv('IAM_ROLE_ARN')

TABLE_NAMES = ['order_detail', 'orders', 'products', 'users']
SCHEMA_NAME = os.getenv('SCHEMA_NAME')

# Redshift settings
REDSHIFT_HOST = os.getenv('REDSHIFT_HOST')
REDSHIFT_PORT = os.getenv('REDSHIFT_PORT')
REDSHIFT_DBNAME = os.getenv('REDSHIFT_DBNAME')
REDSHIFT_USER = os.getenv('REDSHIFT_USER')
REDSHIFT_PASSWORD = os.getenv('REDSHIFT_PASSWORD')

# Establish a connection to Redshift
try:
    conn = psycopg2.connect(
        dbname=REDSHIFT_DBNAME,
        user=REDSHIFT_USER,
        password=REDSHIFT_PASSWORD,
        host=REDSHIFT_HOST,
        port=REDSHIFT_PORT
    )
    print('Connected to Redshift successfully!')
except psycopg2.Error as e:
    print('Error: Could not make connection to the Redshift cluster')
    print(e)

# Create a cursor object
cur = conn.cursor()

for table_name in TABLE_NAMES:

    REDSHIFT_TABLE = f'{SCHEMA_NAME}.{table_name}'
    S3_FILE_PATH = f'surabaya/{table_name}.csv'

    # Copy command
    copy_command = f'''
    COPY {REDSHIFT_TABLE}
    FROM 's3://{S3_BUCKET_NAME}/{S3_FILE_PATH}'
    IAM_ROLE '{IAM_ROLE_ARN}'
    CSV
    IGNOREHEADER 1
    '''

    # Execute the copy command
    try:
        cur.execute(copy_command)
        conn.commit()
        print(f'Data {table_name} copied successfully from S3 to Redshift {REDSHIFT_TABLE}!')
    except Exception as e:
        print(f'Error: Could not copy data {table_name} from S3 to Redshift {REDSHIFT_TABLE}')
        print(e)
        conn.rollback()

# Close the connection
cur.close()
conn.close()
