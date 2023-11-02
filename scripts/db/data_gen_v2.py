from faker import Faker
import random
import json
import uuid

fake = Faker()

# List of available tags
tags = ["finanzas", "tecnologia", "ropa", "apparel", "movilidad", "belleza", "hogar", "desportes", "educacion"]

print(f'/**Create stores table and add 100 rows of random data****/')
print(f'DROP TABLE IF EXISTS stores;')
print(f'CREATE TABLE stores(id VARCHAR,PRIMARY KEY(id),data JSON);')

for _ in range(200):
    store_id = str(uuid.uuid4())
    store_name = fake.company()
    selected_tags = random.sample(tags, 3)
    brand_owner = fake.name()
    discount = round(random.uniform(1.5, 99.9), 1)  
    min_amount = random.randint(0, 10)
    max_amount = random.randint(50, 100) 

    data = {
        "name": store_name,
        "tags": selected_tags,
        "brand_owner": brand_owner,
        "discount": discount,
        "maxAmount": max_amount,
        "minAmount": min_amount,
        "credentials": None
    }

    # Convert data dictionary to JSON string and print SQL INSERT statement
    print(f'INSERT INTO stores (id, data) VALUES (\'{store_id}\', \'{json.dumps(data)}\');')
