import sqlite3
from faker import Faker
import random

fake = Faker()
conn = sqlite3.connect('sample_db/source_db.db')
c = conn.cursor()

c.execute('DROP TABLE IF EXISTS batches')
c.execute('''
CREATE TABLE batches (
    batch_number TEXT,
    material_code TEXT,
    quantity INTEGER,
    temperature REAL,
    production_date TEXT,
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
    status = random.choice(['Completed', 'Pending'])
    sample_data.append((batch_number, material_code, quantity, temperature, production_date, status))

c.executemany('INSERT INTO batches VALUES (?,?,?,?,?,?)', sample_data)
conn.commit()
conn.close()
print("Source DB created with sample batches")
