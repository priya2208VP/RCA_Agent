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



# #new
# import random
# from datetime import datetime, timedelta

# pipeline_logs = []

# for i in range(1, 21):  # 20 sample batches
#     batch_id = f'BATCH-{i:03d}'
    
#     # Hardcode failures to test specific RCA paths
#     if i in [2, 5, 8, 11, 14, 17]:
#         status = 'FAILED'
#     else:
#         status = 'SUCCESS'
        
#     # Hardcode specific errors for the RCA agent to analyze
#     if i == 2:
#         error = "ETL timeout"
#     elif i == 5:
#         error = "Transformation error"
#     elif i == 8:
#         error = "Source timestamp data missing" # New specific error for partial empty columns
#     elif i == 11:
#         error = "App DB connection failure bug" # New specific error for DEV team redirect
#     elif i == 14:
#         error = "Power BI refresh issue" # New specific error for Power BI team redirect
#     elif i == 17:
#         error = "Dataflow transformation failed" # New specific error for DF team redirect
#     elif status == 'FAILED':
#         error = random.choice([
#             "ETL timeout",
#             "Missing source data",
#             "Transformation error"
#         ])
#     else:
#         error = None
        
#     start_time = datetime(2025, 11, 10, 8, 0) + timedelta(minutes=i*10)
#     end_time = start_time + timedelta(minutes=5)
    
#     log_entry = {
#         "job_id": f"ETL-{i:03d}",
#         "batch_id": batch_id,
#         "status": status,
#         "start_time": start_time.strftime("%Y-%m-%d %H:%M"),
#         "end_time": end_time.strftime("%Y-%m-%d %H:%M"),
#         "error": error
#     }
#     pipeline_logs.append(log_entry)

# # Ensure BATCH-001 (for data quality mismatch) is SUCCESS in logs so the agent proceeds to data quality check
# # Since BATCH-001 is SUCCESS here, the agent will move to the data quality check where it will find a mismatch
