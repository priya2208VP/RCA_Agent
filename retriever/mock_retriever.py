import sqlite3
from datetime import datetime
import random
from sample_db.pipeline_logs import pipeline_logs  # existing pipeline logs

# ---------------------------
# Fetch pipeline logs for a given batch
# ---------------------------
def get_pipeline_logs(batch_id):
    # First check if batch exists in static logs
    existing_logs = [log for log in pipeline_logs if log["batch_id"] == batch_id]
    if existing_logs:
        return existing_logs

    # If batch not in logs, mock success/failure for testing
    if batch_id.endswith(("002", "004", "006")):  # simulate failures
        return [{
            "batch_id": batch_id,
            "status": "FAILED",
            "errors": [
                "Database connection timeout",
                "ETL script failed at step 3",
                "Missing input file in source directory"
            ],
            "start_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }]
    else:
        return [{
            "batch_id": batch_id,
            "status": "SUCCESS",
            "errors": ["Batch processed successfully"],
            "start_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }]

# ---------------------------
# Run SQL query on Source DB
# ---------------------------
def run_source_query(query):
    conn = sqlite3.connect('sample_db/source_db.db')
    c = conn.cursor()
    try:
        c.execute(query)
        cols = [description[0] for description in c.description]
        rows = c.fetchall()
        return [dict(zip(cols, row)) for row in rows]
    except Exception as e:
        return [{"error": str(e)}]
    finally:
        conn.close()

# ---------------------------
# Run SQL query on Application DB
# ---------------------------
def run_app_query(query):
    conn = sqlite3.connect('sample_db/app_db.db')
    c = conn.cursor()
    try:
        c.execute(query)
        cols = [description[0] for description in c.description]
        rows = c.fetchall()
        return [dict(zip(cols, row)) for row in rows]
    except Exception as e:
        return [{"error": str(e)}]
    finally:
        conn.close()

# ---------------------------
# Helper: Generate batches from range or comma-separated input
# ---------------------------
def parse_batch_input(batch_input):
    batch_input = batch_input.strip()
    batches = []

    # Comma-separated batches
    if "," in batch_input:
        for b in batch_input.split(","):
            b = b.strip()
            if b:
                batches.append(b)
    # Range of batches e.g., BATCH-001 to BATCH-007
    elif "to" in batch_input:
        start, end = [x.strip() for x in batch_input.split("to")]
        start_num = int(start.split("-")[1])
        end_num = int(end.split("-")[1])
        prefix = start.split("-")[0] + "-"
        for i in range(start_num, end_num + 1):
            batches.append(f"{prefix}{str(i).zfill(3)}")
    else:
        batches.append(batch_input)

    return batches
<<<<<<< HEAD
















# import sqlite3
# from datetime import datetime
# import random
# from sample_db.pipeline_logs import pipeline_logs  # existing pipeline logs

# # ---------------------------
# # Fetch pipeline logs for a given batch
# # ---------------------------
# def get_pipeline_logs(batch_id):
#     # First check if batch exists in static logs
#     existing_logs = [log for log in pipeline_logs if log["batch_id"] == batch_id]
#     if existing_logs:
#         return existing_logs

#     # If batch not in logs, mock success/failure for testing
#     if batch_id.endswith(("002", "004", "006")):  # simulate failures
#         return [{
#             "batch_id": batch_id,
#             "status": "FAILED",
#             "errors": [
#                 "Database connection timeout",
#                 "ETL script failed at step 3",
#                 "Missing input file in source directory"
#             ],
#             "start_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         }]
#     else:
#         return [{
#             "batch_id": batch_id,
#             "status": "SUCCESS",
#             "errors": ["Batch processed successfully"],
#             "start_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         }]

# # ---------------------------
# # Run SQL query on Source DB
# # ---------------------------
# def run_source_query(query):
#     conn = sqlite3.connect('sample_db/source_db.db')
#     c = conn.cursor()
#     try:
#         c.execute(query)
#         cols = [description[0] for description in c.description]
#         rows = c.fetchall()
#         return [dict(zip(cols, row)) for row in rows]
#     except Exception as e:
#         return [{"error": str(e)}]
#     finally:
#         conn.close()

# # ---------------------------
# # Run SQL query on Application DB
# # ---------------------------
# def run_app_query(query):
#     conn = sqlite3.connect('sample_db/app_db.db')
#     c = conn.cursor()
#     try:
#         c.execute(query)
#         cols = [description[0] for description in c.description]
#         rows = c.fetchall()
#         return [dict(zip(cols, row)) for row in rows]
#     except Exception as e:
#         return [{"error": str(e)}]
#     finally:
#         conn.close()

# # ---------------------------
# # Helper: Generate batches from range or comma-separated input
# # ---------------------------
# def parse_batch_input(batch_input):
#     batch_input = batch_input.strip()
#     batches = []

#     # Comma-separated batches
#     if "," in batch_input:
#         for b in batch_input.split(","):
#             b = b.strip()
#             if b:
#                 batches.append(b)
#     # Range of batches e.g., BATCH-001 to BATCH-007
#     elif "to" in batch_input:
#         start, end = [x.strip() for x in batch_input.split("to")]
#         start_num = int(start.split("-")[1])
#         end_num = int(end.split("-")[1])
#         prefix = start.split("-")[0] + "-"
#         for i in range(start_num, end_num + 1):
#             batches.append(f"{prefix}{str(i).zfill(3)}")
#     else:
#         batches.append(batch_input)

#     return batches


















# import json
# import re
# from datetime import datetime, timedelta
# import random

# # --- Mock Data Definitions ---

# MOCK_SOURCE_DATA = {
#     "BATCH-001": [
#         {"id": 1, "batch_number": "BATCH-001", "material_id": "MTRL-A", "quantity": 100, "cost": 500.00, "production_date": "2025-11-14T08:00:00Z"},
#         {"id": 2, "batch_number": "BATCH-001", "material_id": "MTRL-B", "quantity": 150, "cost": 750.00, "production_date": "2025-11-14T08:05:00Z"},
#         {"id": 3, "batch_number": "BATCH-001", "material_id": "MTRL-C", "quantity": 50, "cost": 250.00, "production_date": "2025-11-14T08:10:00Z"},
#     ],
#     "BATCH-002": [
#         {"id": 4, "batch_number": "BATCH-002", "material_id": "MTRL-D", "quantity": 200, "cost": 1000.00, "production_date": "2025-11-14T10:00:00Z"},
#     ],
#     "BATCH-003": [
#         {"id": 5, "batch_number": "BATCH-003", "material_id": "MTRL-E", "quantity": 50, "cost": 250.00, "production_date": "2025-11-14T12:00:00Z"},
#     ],
#     "BATCH-008": [ # Data Quality Failure
#         {"id": 10, "batch_number": "BATCH-008", "material_id": "MTRL-Z", "quantity": 50, "cost": 250.00, "production_date": "2025-11-15T09:00:00Z"},
#         {"id": 11, "batch_number": "BATCH-008", "material_id": "MTRL-Y", "quantity": 150, "cost": 750.00, "production_date": None}, # Missing timestamp
#     ],
# }

# MOCK_APP_DATA = {
#     "BATCH-001": [
#         {"id": 1, "batch_number": "BATCH-001", "material_id": "MTRL-A", "processed_quantity": 100, "calculated_cost": 500.00, "processed_date": "2025-11-14T09:00:00Z"},
#         {"id": 2, "batch_number": "BATCH-001", "material_id": "MTRL-B", "processed_quantity": 150, "calculated_cost": 750.00, "processed_date": "2025-11-14T09:05:00Z"},
#         # Record 3 is MISSING to simulate the count mismatch error
#     ],
#     "BATCH-002": [
#         {"id": 4, "batch_number": "BATCH-002", "material_id": "MTRL-D", "processed_quantity": 200, "calculated_cost": 1000.00, "processed_date": "2025-11-14T11:00:00Z"},
#     ],
#     # BATCH-003 is MISSING to simulate a complete load failure
#     # BATCH-008 is MISSING to simulate data quality failure rejection
# }

# MOCK_PIPELINE_LOGS = {
#     "BATCH-001": [ # Failure: Data Mismatch
#         {"step": "SOURCE_QUERY", "status": "SUCCESS", "message": "Queried 3 records from Source DB."},
#         {"step": "TRANSFORMATION", "status": "SUCCESS", "message": "Applied standard transformations."},
#         {"step": "APP_LOAD", "status": "FAILURE", "error": "Pre-Load Validation Failed: Record Count Mismatch. Expected 3, Loaded 2."},
#     ],
#     "BATCH-002": [ # Success
#         {"step": "SOURCE_QUERY", "status": "SUCCESS", "message": "Queried 2 records from Source DB."},
#         {"step": "TRANSFORMATION", "status": "SUCCESS", "message": "Applied standard transformations."},
#         {"step": "APP_LOAD", "status": "SUCCESS", "message": "Successfully loaded 2 records to App DB."},
#         {"step": "PIPELINE_END", "status": "SUCCESS", "message": "Batch processed successfully."},
#     ],
#     "BATCH-003": [ # Failure: Timeout
#         {"step": "SOURCE_QUERY", "status": "SUCCESS", "message": "Queried 10,000 records from Source DB (High Volume)."},
#         {"step": "TRANSFORMATION", "status": "RUNNING", "message": "Starting complex joins..."},
#         {"step": "TRANSFORMATION", "status": "FAILURE", "error": "Job Execution Timeout: Exceeded 15 minute limit."},
#     ],
#     "BATCH-007": [ # Failure: Logic Bug (Division by Zero)
#         {"step": "SOURCE_QUERY", "status": "SUCCESS", "message": "Queried 1 record."},
#         {"step": "TRANSFORMATION", "status": "FAILURE", "error": "Uncaught Exception: Division by zero in custom cost calculation script."},
#     ],
#     "BATCH-008": [ # Failure: Data Quality
#         {"step": "SOURCE_QUERY", "status": "SUCCESS", "message": "Queried 2 records."},
#         {"step": "DATA_VALIDATION", "status": "FAILURE", "error": "Data quality failure: Source timestamp data missing in 50% of records."},
#     ],
#     "BATCH-009": [ # Failure: Connection Failure
#         {"step": "SOURCE_QUERY", "status": "SUCCESS", "message": "Queried 1 record."},
#         {"step": "TRANSFORMATION", "status": "SUCCESS", "message": "Applied transformations."},
#         {"step": "APP_LOAD", "status": "FAILURE", "error": "Target DB Connection Failure: Auth token expired or Database offline."},
#     ],
# }

# MOCK_INCIDENT_SUMMARY = {
#     "BATCH-001": {"ticket_id": "INC-991", "application": "FinancialsReporting", "priority": "High", "timestamp": "2025-11-14T09:10:00Z", "incident_type": "DATA_MISMATCH"},
#     "BATCH-002": {"ticket_id": "INC-992", "application": "FinancialsReporting", "priority": "Low", "timestamp": "2025-11-14T11:00:00Z", "incident_type": "SUCCESS"},
#     "BATCH-003": {"ticket_id": "INC-993", "application": "InventoryProcessing", "priority": "Critical", "timestamp": "2025-11-14T12:30:00Z", "incident_type": "TIMEOUT"},
#     "BATCH-007": {"ticket_id": "INC-997", "application": "CostingEngine", "priority": "Critical", "timestamp": "2025-11-15T07:30:00Z", "incident_type": "LOGIC_BUG"},
#     "BATCH-008": {"ticket_id": "INC-998", "application": "FinancialsReporting", "priority": "High", "timestamp": "2025-11-15T09:05:00Z", "incident_type": "DATA_QUALITY"},
#     "BATCH-009": {"ticket_id": "INC-999", "application": "AssetTracking", "priority": "High", "timestamp": "2025-11-15T10:15:00Z", "incident_type": "CONNECTION_FAILURE"},
#     # Add a few more cases for a full range (not necessary to have logs/data for every one)
#     "BATCH-004": {"ticket_id": "INC-994", "application": "OrderProcessing", "priority": "Medium", "timestamp": "2025-11-14T13:00:00Z", "incident_type": "SUCCESS"},
#     "BATCH-005": {"ticket_id": "INC-995", "application": "SupplyChain", "priority": "Low", "timestamp": "2025-11-14T14:00:00Z", "incident_type": "REPORTING_ISSUE"},
#     "BATCH-006": {"ticket_id": "INC-996", "application": "DataLakeIngest", "priority": "Medium", "timestamp": "2025-11-14T15:00:00Z", "incident_type": "DATAFLOW_FAILURE"},
#     "BATCH-010": {"ticket_id": "INC-1000", "application": "FinancialsReporting", "priority": "Low", "timestamp": "2025-11-15T11:00:00Z", "incident_type": "SUCCESS"},
# }

# def get_pipeline_logs(batch_id):
#     """Retrieves pipeline execution logs for a specific batch ID."""
#     return MOCK_PIPELINE_LOGS.get(batch_id, [
#         {"step": "MOCK", "status": "ERROR", "error": f"Batch {batch_id} not found in log system."}
#     ])

# def run_source_query(batch_id):
#     """Retrieves raw data from the upstream Source DB."""
#     return MOCK_SOURCE_DATA.get(batch_id, [])

# def run_app_query(batch_id):
#     """Retrieves processed data from the Application DB."""
#     return MOCK_APP_DATA.get(batch_id, [])

# def get_incident_summary(batch_id):
#     """Retrieves key summary metadata for the incident."""
#     # Use incident_type from MOCK_INCIDENT_SUMMARY as part of the returned summary
#     summary = MOCK_INCIDENT_SUMMARY.get(batch_id, {
#         "ticket_id": f"TICKET-N/A", 
#         "application": "Unknown System", 
#         "priority": "Medium", 
#         "timestamp": datetime.now().isoformat() + 'Z',
#         "incident_type": "UNKNOWN_FAILURE"
#     })
#     return summary

# def parse_batch_input(raw_input):
#     """Parses input like 'BATCH-001, BATCH-003' or 'BATCH-001 to BATCH-005' into a list of valid batch IDs."""
#     batch_ids = []
#     input_upper = raw_input.strip().upper()
    
#     # 1. Handle range input: BATCH-X to BATCH-Y
#     if 'TO' in input_upper:
#         match = re.search(r'(BATCH-(\d+))\s+TO\s+(BATCH-(\d+))', input_upper, re.IGNORECASE)
#         if match:
#             start_num = int(match.group(2))
#             end_num = int(match.group(4))
#             for i in range(start_num, end_num + 1):
#                 batch_id = f"BATCH-{i:03d}"
#                 if batch_id in MOCK_INCIDENT_SUMMARY:
#                     batch_ids.append(batch_id)
#             return batch_ids

#     # 2. Handle comma-separated list
#     candidate_ids = [bid.strip() for bid in input_upper.split(',') if bid.strip()]
#     for bid in candidate_ids:
#         if bid in MOCK_INCIDENT_SUMMARY:
#             batch_ids.append(bid)
            
#     # 3. If no valid IDs were parsed, return a default known set for demonstration
#     if not batch_ids and input_upper:
#         return ["BATCH-001"] 
        
#     # Return unique valid IDs
#     return list(set(batch_ids))
=======
>>>>>>> 28f185771a8b69a047fc99d6c493633ac4f570d2
