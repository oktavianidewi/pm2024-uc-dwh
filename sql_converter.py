import csv
import argparse

def csv_to_sql_insert(file_path, table_name):
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  # Get the column headers
        columns = ', '.join(headers)

        insert_queries = []
        for row in reader:
            values = ', '.join(f"'{value}'" if value != '' else 'NULL' for value in row)
            insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({values});"
            insert_queries.append(insert_query)

    return insert_queries


def main():
    # Example usage

    parser = argparse.ArgumentParser(description='Convert CSV to SQL INSERT statements.')
    parser.add_argument('file_path', type=str, help='Path to the CSV file')
    parser.add_argument('table_name', type=str, help='Name of the database table')
    args = parser.parse_args()

    file_path = args.file_path
    table_name = args.table_name

    insert_queries = csv_to_sql_insert(file_path, table_name)
    for query in insert_queries:
        print(query)

if __name__ == '__main__':
    main()