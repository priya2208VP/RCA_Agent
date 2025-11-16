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














# import json
# # CORRECTED IMPORT: Use get_incident_summary to match the definition in mock_retriever.py
# from retriever.mock_retriever import get_incident_summary 

# # --- AGENT LOGIC ---

# def analyze_data_findings(batch_id, source_data, app_data):
#     """Simulates the LLM Agent performing data comparison."""
#     data_findings = {}
    
#     # Data Discrepancy Check (Simulated)
#     if batch_id == "BATCH-007": # Logic Bug/Division by Zero Case
#         data_findings['discrepancies'] = {
#             "total_cost": {
#                 "source_value": "Calculated (10.00 / 0)", 
#                 "app_value": "NaN",
#                 "note": "Transformation output resulted in NaN due to division by zero, causing load failure."
#             }
#         }
#     elif batch_id == "BATCH-008": # Type Mismatch Case
#         # BATCH-008 source had "TBD" for inventory_count, App DB is empty
#         source_rec = source_data.get(batch_id, {})
#         app_rec = app_data.get(batch_id, {})
        
#         if source_rec and not app_rec:
#              data_findings['discrepancies'] = {
#                 "inventory_count": {
#                     "source_value": source_rec.get("inventory_count", "N/A"), 
#                     "app_value": "Missing",
#                     "note": "Source field contained non-numeric value ('TBD') leading to load process abortion."
#                 }
#             }
            
#     # Missing Critical Field Check (Simulated)
#     if batch_id == "BATCH-004": # Missing Material ID Case
#         data_findings['missing_source_fields'] = ['material_id']
#         data_findings['missing_app_fields'] = ['material_id', 'processed_date']
    
#     return data_findings

# def determine_rca_output(incident_type, data_findings):
#     """Determines RCA elements and team based on incident type."""
    
#     # Default output for success cases
#     if incident_type == "SUCCESS":
#         return {
#             "root_cause_analysis": {
#                 "what_happened": "No issue detected. Batch successfully processed.",
#                 "when_happened": "N/A",
#                 "where_happened": "ETL Pipeline / Application DB",
#                 "why_happened": "No issue detected. Batch successfully processed.",
#                 "how_happened": "Normal data ingestion and transformation.",
#                 "who_involved": "No action required."
#             },
#             "redirect_team": "Monitoring/Triage",
#             "immediate_action": "None - Batch successful."
#         }
        
#     # --- Failure Cases ---
    
#     if incident_type == "TIMEOUT":
#         return {
#             "root_cause_analysis": {
#                 "what_happened": "Pipeline Failure: ETL process timed out during heavy load execution.",
#                 "when_happened": "End of ETL execution phase.",
#                 "where_happened": "Compute Cluster / ETL Engine",
#                 "why_happened": "Insufficient compute resources or overly long execution window.",
#                 "how_happened": "Job killed by orchestrator after exceeding max runtime.",
#                 "who_involved": "DevOps / Data Engineering"
#             },
#             "redirect_team": "DevOps / Data Engineering",
#             "immediate_action": "Increase the time-out setting for this specific pipeline (e.g., from 120min to 180min) and analyze job execution plan for optimization opportunities."
#         }
        
#     if incident_type == "MISSING_FIELD":
#         field = data_findings.get('missing_source_fields', ['a critical field'])[0]
#         return {
#             "root_cause_analysis": {
#                 "what_happened": f"Source Data Quality: Critical field '{field}' was missing (NULL) in source records.",
#                 "when_happened": "Ingestion stage, validation step.",
#                 "where_happened": "Source Database / Data Validation Layer",
#                 "why_happened": "Upstream system failed to populate mandatory field. This is a source data contract issue.",
#                 "how_happened": "Validation rule failure resulted in batch rejection.",
#                 "who_involved": "Source Data Quality Team"
#             },
#             "redirect_team": "Source Data Quality Team",
#             "immediate_action": f"Contact upstream owners to verify data population for '{field}'. Rerun the batch after source data fix."
#         }
        
#     if incident_type == "SAP_DELAY":
#         return {
#             "root_cause_analysis": {
#                 "what_happened": "Source data was unavailable: The staging database was empty due to upstream delay from the SAP system.",
#                 "when_happened": "Start of ETL execution.",
#                 "where_happened": "Source System Staging DB",
#                 "why_happened": "SAP system batch job delay or failure to complete data push before ETL window.",
#                 "how_happened": "Ingestion process found 0 records and aborted, classified as high priority failure.",
#                 "who_involved": "SAP Operations Team"
#             },
#             "redirect_team": "SAP Operations Team",
#             "immediate_action": "Verify SAP job schedule and status. Once SAP data is confirmed in staging, manually trigger a re-run of the ETL pipeline."
#         }

#     if incident_type == "LOGIC_BUG":
#         return {
#             "root_cause_analysis": {
#                 "what_happened": "Pipeline Failure: Bug in custom transformation logic (e.g., Division by Zero) caused load failure.",
#                 "when_happened": "Transformation stage.",
#                 "where_happened": "ETL Transformation Code",
#                 "why_happened": "Inadequate handling of edge case (zero-value) in custom calculation code.",
#                 "how_happened": "Uncaught exception halted the load process.",
#                 "who_involved": "Development Team"
#             },
#             "redirect_team": "Development Team",
#             "immediate_action": "Dev team to patch the transformation code to safely handle zero or null inputs (e.g., use coalesce or try-catch block). Redeploy and reprocess."
#         }
        
#     if incident_type == "TYPE_MISMATCH":
#         return {
#             "root_cause_analysis": {
#                 "what_happened": "Data Type Mismatch: Non-numeric data entered a field expecting an integer, causing conversion failure.",
#                 "when_happened": "Data Type casting during transformation.",
#                 "where_happened": "Data Validation/Casting Layer",
#                 "why_happened": "Source system allowed invalid data ('TBD') into a key numeric field.",
#                 "how_happened": "Job failed schema validation/type enforcement.",
#                 "who_involved": "Source Data Quality Team"
#             },
#             "redirect_team": "Source Data Quality Team",
#             "immediate_action": "Data team to manually correct 'TBD' values in source DB and adjust source schema to enforce numeric input."
#         }

#     # Default fallback
#     return {
#         "root_cause_analysis": "Root cause unknown. Needs manual investigation.",
#         "redirect_team": "Triage Lead",
#         "immediate_action": "Escalate to Triage Lead for manual investigation."
#     }


# def generate_rca(batch_id, source_data, app_data, pipeline_logs):
#     """
#     Simulates the full LLM RCA generation process.
    
#     Note: We are pulling from the mock_retriever data to simulate the context 
#     the LLM would use to generate its structured JSON output.
#     """
    
#     # Use the correct function from the imported retriever module
#     incident_data = get_incident_summary(batch_id) # CORRECTED FUNCTION CALL
#     incident_type = incident_data.get('incident_type', 'UNKNOWN_FAILURE') # Safely extract type
    
#     # 1. Simulate data validation and comparison
#     data_findings = analyze_data_findings(batch_id, source_data, app_data)
    
#     # 2. Simulate LLM generating RCA based on context
#     rca_outputs = determine_rca_output(incident_type, data_findings)
    
#     # 3. Assemble the final report structure
#     rca_report = {
#         "incident_summary": {
#             "ticket_id": incident_data.get('ticket_id', f"TICKET-{batch_id}"),
#             "application": incident_data.get('application', 'Unknown'),
#             "priority": incident_data.get('priority', 'Medium'),
#             "timestamp": incident_data.get('timestamp', 'N/A'),
#         },
#         "pipeline_logs": pipeline_logs,
#         "data_findings": data_findings if data_findings else None,
#         "root_cause_analysis": rca_outputs['root_cause_analysis'],
#         # These are the top-level fields that are sometimes missed by the LLM
#         "redirect_team": rca_outputs.get('redirect_team'), 
#         "immediate_action": rca_outputs.get('immediate_action'),
        
#         # Internal flag used by the mock system for success/failure grouping
#         "_is_success": incident_type == "SUCCESS"
#     }
    
#     return rca_report