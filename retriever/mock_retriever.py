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
