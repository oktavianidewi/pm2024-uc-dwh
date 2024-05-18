# initdb/generate_orders.py
import os
import csv
import dataclasses
import random
import json
import time


@dataclasses.dataclass
class Order:
    user_id: int

    items: str
    @staticmethod
    def create():
        # summary dari order_detail.csv
        header = ["order_id", "ordered_at", "user_id", "total"]
        order_detail, _ = Order.read_csv("order_detail.csv")
        orders: list = []
        total: dict = {}
        for order_detail in order_detail:
            order_id = order_detail[0]
            subtotal = order_detail[3]

            if order_id not in total: 
                total[order_id] = float(subtotal)
            else: 
                total[order_id] = float(total[order_id]) + float(subtotal)

            # print(f"isi total {total}")

            user_id = random.choices(range(1, 1000))[0]
            ordered_at = Order.generate_random_datetime_past_week()
            orders.append([order_id, ordered_at, user_id, total[order_id]])
        # print(orders)
        return orders, header
    


    def generate_random_datetime_past_week():
        import random
        import datetime
        
        # Current datetime
        now = datetime.datetime.now()
        
        # Datetime one week ago
        one_week_ago = now - datetime.timedelta(weeks=1)
        
        # Calculate the time difference in seconds
        time_difference = (now - one_week_ago).total_seconds()
        
        # Generate a random number of seconds within this time difference
        random_seconds = random.uniform(0, time_difference)
        
        # Add the random seconds to the one week ago datetime
        random_datetime = one_week_ago + datetime.timedelta(seconds=random_seconds)
        
        return random_datetime

    def write_csv(data: list, header: list, filename:str):
        with open(os.path.join(CURRENT_DIR, "dataset", filename), "w") as f:
            writer = csv.writer(f)
            writer.writerow(header)
            for datum in data:
                writer.writerow(datum)

    def read_csv(filename):
        rows: list = []
        with open(os.path.join(CURRENT_DIR, "dataset", filename), "r") as f:
            csvreader = csv.reader(f)
            header = next(csvreader)
            # header = ['name', 'description', 'price', 'category', 'image']
            for row in csvreader:
                rows.append(row)
            # print(rows)
            return rows, header

    def create_detail():
        product_id = random.randint(1, 82)
        header = ["order_id",  "product_id", "quantity", "price", "sub_total"]
        order_detail_ids = 80
        list_products, _ = Order.read_csv("products.csv")
        # print(list_products[0])
        order_detail: list = []
        for order_detail_id in range(1, order_detail_ids):
            order_id = random.randint(1, NUM_ORDERS)

            # print(f"order_id: {order_id}")
            
            for counter_product in range(0, random.randint(1, 3)):
                product_id = random.choices(range(1, 80))[0]
                product_detail = list_products[product_id]
                price = product_detail[2]
                quantity = random.randint(1, 2)
                sub_total = int(quantity) * float(price)
                order_detail.append([order_id, product_id, quantity, price, sub_total])

        return order_detail, header

if __name__ == "__main__":
    """
    Generate random orders given by the NUM_ORDERS environment variable.
        - orders.csv will be written to ./data folder
    
    Example:
        python generate_orders.py
        NUM_ORDERS=10000 python generate_orders.py
    """
    NUM_ORDERS = int(os.getenv("NUM_ORDERS", "100"))
    CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

    data, header = Order.create_detail()
    Order.write_csv(data, header, "order_detail.csv")

    time.sleep(1)
    
    data, header = Order.create()
    Order.write_csv(data, header, "orders.csv")