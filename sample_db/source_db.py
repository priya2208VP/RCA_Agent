<<<<<<< HEAD
# import sqlite3
# from faker import Faker
# import random

# fake = Faker()
# conn = sqlite3.connect('sample_db/source_db.db')
# c = conn.cursor()

# c.execute('DROP TABLE IF EXISTS batches')
# c.execute('''
# CREATE TABLE batches (
#     batch_number TEXT,
#     material_code TEXT,
#     quantity INTEGER,
#     temperature REAL,
#     production_date TEXT,
#     status TEXT
# )
# ''')

# sample_data = []
# for i in range(1, 21):
#     batch_number = f'BATCH-{i:03d}'
#     material_code = random.choice(['MAT-101', 'MAT-102', 'MAT-103', 'MAT-104'])
#     quantity = random.randint(100, 500)
#     temperature = round(random.uniform(5.0, 25.0), 2)
#     production_date = fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S")
#     status = random.choice(['Completed', 'Pending'])
#     sample_data.append((batch_number, material_code, quantity, temperature, production_date, status))

# c.executemany('INSERT INTO batches VALUES (?,?,?,?,?,?)', sample_data)
# conn.commit()
# conn.close()
# print("Source DB created with sample batches")





=======
>>>>>>> 28f185771a8b69a047fc99d6c493633ac4f570d2
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
<<<<<<< HEAD




















#new

# import sqlite3
# from faker import Faker
# import random
# from datetime import datetime, timedelta

# fake = Faker()
# conn = sqlite3.connect('source_db.db')
# c = conn.cursor()

# c.execute('DROP TABLE IF EXISTS batches')

# c.execute('''
# CREATE TABLE batches (
#     batch_number TEXT,
#     material_code TEXT,
#     product_name TEXT,
#     produced_qty INTEGER,
#     target_qty INTEGER,
#     batch_start_time TEXT,
#     batch_end_time TEXT,
#     processing_duration TEXT,
#     site_name TEXT,
#     line_id TEXT,
#     shift TEXT,
#     operator TEXT,
#     status TEXT,
#     error_messages TEXT,
#     root_cause_category TEXT,
#     corrective_action TEXT,
#     preventive_actions TEXT,
#     quality_status TEXT,
#     remarks TEXT,
#     rca_ticket_id TEXT
# )
# ''')

# sample_data = []
# for i in range(1, 51):
#     batch_number = f'BATCH-{i:03d}'
    
#     # Existing MISMATCH SIMULATIONS
#     if i in [1, 2, 3]:
#         material_code = '101-RAW' 
#     elif i in [4, 5]:
#         material_code = '102-BASE'
#     else:
#         material_code = random.choice(['MAT-101', 'MAT-102', 'MAT-103', 'MAT-104'])
    
#     product_name = random.choice(['Tablet A', 'Tablet B', 'Syrup X', 'Capsule Y'])
#     produced_qty = random.randint(100, 500)
    
#     if i == 5:
#         produced_qty = 95 
        
#     target_qty = produced_qty + random.randint(-20, 20)
    
#     # 🚨 NEW CONDITION: Empty data in a few columns
#     batch_start_time = fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S")
#     batch_end_time = fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S")
    
#     # Simulate missing timestamp (BATCH-008, which has the "Source timestamp data missing" error in logs)
#     if i == 8:
#         batch_end_time = None
        
#     # Simulate missing Line ID for BATCH-011
#     line_id = random.choice(['Line A', 'Line B', 'Line C'])
#     if i == 11:
#         line_id = None 

#     processing_duration = str(random.randint(30, 180)) + " mins"
#     site_name = random.choice(['Plant 1', 'Plant 2', 'Plant 3'])
#     shift = random.choice(['Morning', 'Evening', 'Night'])
#     operator = fake.name()
    
#     if i in [1, 2, 3]:
#         status = 'Raw_Pending' 
#     else:
#         status = random.choice(['Completed', 'Pending', 'Failed']) 
    
#     error_messages = random.choice(['None', 'Temperature high', 'Material shortage', 'Machine error'])
#     root_cause_category = random.choice(['Equipment', 'Material', 'Human Error', 'Process'])
#     corrective_action = random.choice(['Reprocess batch', 'Check equipment', 'Adjust recipe', 'No action'])
#     preventive_actions = random.choice(['Add alerts', 'Schedule maintenance', 'Training', 'Review SOP'])
#     quality_status = random.choice(['Pass', 'Fail', 'Hold'])
#     remarks = fake.sentence(nb_words=6)
#     rca_ticket_id = f"TICKET-{batch_number}"

#     sample_data.append((
#         batch_number, material_code, product_name, produced_qty, target_qty, batch_start_time, batch_end_time,
#         processing_duration, site_name, line_id, shift, operator, status, error_messages, root_cause_category,
#         corrective_action, preventive_actions, quality_status, remarks, rca_ticket_id
#     ))

# c.executemany('INSERT INTO batches VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', sample_data)
# conn.commit()
# conn.close()

# print("Source DB created with new partial empty column simulations.")
=======
>>>>>>> 28f185771a8b69a047fc99d6c493633ac4f570d2
