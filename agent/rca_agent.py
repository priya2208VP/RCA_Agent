def generate_rca(batch_id, source_data, app_data, pipeline_logs):
    source_batches = {d['batch_number']: d for d in source_data}
    app_batches = {d['batch_number']: d for d in app_data}
    missing_in_app = [b for b in source_batches if b not in app_batches]
    failed_pipeline = [log for log in pipeline_logs if log['status'] != 'SUCCESS']

    rca_json = {
        "incident_summary": {
            "title": f"RCA for Batch {batch_id}",
            "ticket_id": f"TICKET-{batch_id}",
            "timestamp": "2025-11-15T10:00:00Z",
            "application": "FactoryApp",
            "location": "Plant 2",
            "priority": "High" if missing_in_app or failed_pipeline else "Medium"
        },
        "root_cause_analysis": {
            "what_happened": "Batch missing in App DB" if missing_in_app else "Batch processed successfully",
            "when_happened": source_batches.get(batch_id, {}).get('production_date', 'N/A'),
            "where_happened": "Application DB" if missing_in_app else "Pipeline/DB",
            "why_happened": "Pipeline failed or data not ingested" if failed_pipeline or missing_in_app else "No issue",
            "how_happened": "ETL pipeline did not insert batch" if missing_in_app else "N/A",
            "who_involved": "Ops team"
        },
        "steps_to_reproduce": [
            f"Query source DB for batch {batch_id}",
            f"Query app DB for batch {batch_id}",
            f"Check pipeline logs for batch {batch_id}"
        ],
        "pipeline_analysis": failed_pipeline if failed_pipeline else pipeline_logs,
        "analysis_steps_done": ["Checked source DB", "Checked App DB", "Checked ETL logs"],
        "corrective_actions": [f"Rerun ETL pipeline for batch {batch_id}" if missing_in_app else "No action needed"],
        "preventive_actions": ["Add pipeline alerts", "Schedule batch verification"],
        "escalation_recommendation": {
            "next_owner": "Ops Lead" if missing_in_app else "Monitor",
            "urgency": "High" if missing_in_app else "Low",
            "notes": "Escalate if batch missing again"
        },
        "confidence_score": 0.95,
        "audit_metadata": {
            "generated_by": "Mock RCA Agent",
            "reviewed_by": "Pending",
            "timestamp": "2025-11-15T10:05:00Z"
        }
    }
    return rca_json
