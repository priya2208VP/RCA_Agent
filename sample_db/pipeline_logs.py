import random
from datetime import datetime, timedelta

pipeline_logs = []

for i in range(1, 21):  # 20 sample batches
    batch_id = f'BATCH-{i:03d}'
    status = random.choice(['SUCCESS', 'FAILED'])
    error = None if status == 'SUCCESS' else random.choice([
        "ETL timeout",
        "Missing source data",
        "Transformation error"
    ])
    start_time = datetime(2025, 11, 10, 8, 0) + timedelta(minutes=i*10)
    end_time = start_time + timedelta(minutes=5)
    
    log_entry = {
        "job_id": f"ETL-{i:03d}",
        "batch_id": batch_id,
        "status": status,
        "start_time": start_time.strftime("%Y-%m-%d %H:%M"),
        "end_time": end_time.strftime("%Y-%m-%d %H:%M"),
        "error": error
    }
    pipeline_logs.append(log_entry)
