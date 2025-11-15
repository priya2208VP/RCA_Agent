import sqlite3
from faker import Faker
import random

fake = Faker()
conn = sqlite3.connect('sample_db/app_db.db')
c = conn.cursor()

c.execute('DROP TABLE IF EXISTS app_batches')
c.execute('''
CREATE TABLE app_batches (
    batch_number TEXT,
    material_code TEXT,
    quantity INTEGER,
    temperature REAL,
    production_date TEXT,
    reflect_time TEXT,
    status TEXT
)
''')

sample_data = []
for i in range(1, 21):
    batch_number = f'BATCH-{i:03d}'
    material_code = random.choice(['MAT-101', 'MAT-102', 'MAT-103', 'MAT-104'])
    quantity = random.randint(100, 500)
    temperature = round(random.uniform(5.0, 25.0), 2)
    production_date = fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S")
    reflect_time = fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S")
    status = random.choice(['Completed', 'Pending'])
    sample_data.append((batch_number, material_code, quantity, temperature, production_date, reflect_time, status))

c.executemany('INSERT INTO app_batches VALUES (?,?,?,?,?,?,?)', sample_data)
conn.commit()
conn.close()
print("Application DB created with sample batches")
