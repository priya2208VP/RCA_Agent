import sqlite3
from sample_db.pipeline_logs import pipeline_logs  # Import pipeline logs

# ---------------------------
# Fetch pipeline logs for a given batch
# ---------------------------
def get_pipeline_logs(batch_id):
    return [log for log in pipeline_logs if log["batch_id"] == batch_id]

# ---------------------------
# Run SQL query on Source DB
# ---------------------------
def run_source_query(query):
    conn = sqlite3.connect('sample_db/source_db.db')
    c = conn.cursor()
    c.execute(query)
    cols = [description[0] for description in c.description]
    rows = c.fetchall()
    conn.close()
    return [dict(zip(cols, row)) for row in rows]

# ---------------------------
# Run SQL query on Application DB
# ---------------------------
def run_app_query(query):
    conn = sqlite3.connect('sample_db/app_db.db')
    c = conn.cursor()
    c.execute(query)
    cols = [description[0] for description in c.description]
    rows = c.fetchall()
    conn.close()
    return [dict(zip(cols, row)) for row in rows]
