import sys
import os

# Add RCA_Agent folder to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import streamlit as st
from retriever import mock_retriever
import pandas as pd
from datetime import datetime

import streamlit as st
from retriever import mock_retriever
import pandas as pd
from datetime import datetime
from io import BytesIO
from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.oxml import OxmlElement

# ---------------------------
# Streamlit config
# ---------------------------
st.set_page_config(page_title="Pharma RCA Agent", layout="wide")
st.title("💊 Pharma Manufacturing RCA AI Agent")

# ---------------------------
# Input
# ---------------------------
batch_input = st.text_input(
    "Enter Batch Number(s) (comma-separated, e.g., BATCH-002,BATCH-007)"
)
batch_ids = [b.strip() for b in batch_input.split(",") if b.strip()]

# ---------------------------
# Process each batch
# ---------------------------
for batch_id in batch_ids:
    st.header(f"Batch: {batch_id}")

    # Pipeline Logs
    pipeline_logs_data = mock_retriever.get_pipeline_logs(batch_id)
    status = pipeline_logs_data[0]['status'] if pipeline_logs_data else "N/A"
    error = pipeline_logs_data[0]['error'] if pipeline_logs_data and status=="FAILED" else None
    start_time = pipeline_logs_data[0]['start_time'] if pipeline_logs_data else "N/A"

    # Source DB
    source_query = f"SELECT * FROM batches WHERE batch_number='{batch_id}'"
    source_data = mock_retriever.run_source_query(source_query)
    st.subheader("Source DB Data")
    st.dataframe(pd.DataFrame(source_data))

    # App DB
    app_query = f"SELECT * FROM app_batches WHERE batch_number='{batch_id}'"
    app_data = mock_retriever.run_app_query(app_query)
    st.subheader("Application DB Data")
    st.dataframe(pd.DataFrame(app_data))

    # ---------------------------
    # Generate Word Document
    # ---------------------------
    doc = Document()

    # Heading
    doc.add_heading(f"RCA Report - Batch {batch_id}", level=0).alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

    # Incident Summary
    doc.add_heading("Incident Summary", level=1)
    doc.add_paragraph(f"Title: RCA for Batch {batch_id}")
    doc.add_paragraph(f"Ticket ID: TICKET-{batch_id}")
    doc.add_paragraph(f"Timestamp: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}")
    doc.add_paragraph("Application: FactoryApp")
    doc.add_paragraph("Location: Plant 2")
    doc.add_paragraph("Priority: Medium")

    # Root Cause Analysis
    doc.add_heading("Root Cause Analysis", level=1)
    rca_para = doc.add_paragraph()
    rca_para.add_run("What Happened: ").bold = True
    rca_para.add_run('Batch processed successfully' if status=='SUCCESS' else 'Batch failed during processing')
    rca_para = doc.add_paragraph()
    rca_para.add_run("When Happened: ").bold = True
    rca_para.add_run(start_time)
    rca_para = doc.add_paragraph()
    rca_para.add_run("Where Happened: ").bold = True
    rca_para.add_run("Pipeline/DB")
    rca_para = doc.add_paragraph()
    rca_para.add_run("Why Happened: ").bold = True
    rca_para.add_run('No issue' if status=='SUCCESS' else error)
    rca_para = doc.add_paragraph()
    rca_para.add_run("How Happened: ").bold = True
    rca_para.add_run("Automated ETL pipeline")
    rca_para = doc.add_paragraph()
    rca_para.add_run("Who Involved: ").bold = True
    rca_para.add_run("Ops team")

    # Steps to Reproduce
    doc.add_heading("Steps to Reproduce", level=1)
    steps = [
        f"Query source DB for batch {batch_id}",
        f"Query app DB for batch {batch_id}",
        f"Check pipeline logs for batch {batch_id}"
    ]
    for i, step in enumerate(steps, 1):
        doc.add_paragraph(f"{i}. {step}")

    # Pipeline Analysis Table
    doc.add_heading("Pipeline Analysis", level=1)
    if pipeline_logs_data:
        table = doc.add_table(rows=1, cols=len(pipeline_logs_data[0]))
        table.style = 'Light List Accent 1'
        hdr_cells = table.rows[0].cells
        for idx, key in enumerate(pipeline_logs_data[0].keys()):
            hdr_cells[idx].text = key
        for log in pipeline_logs_data:
            row_cells = table.add_row().cells
            for idx, val in enumerate(log.values()):
                row_cells[idx].text = str(val)
    else:
        doc.add_paragraph("No pipeline logs found.")

    # Analysis Steps Done
    doc.add_heading("Analysis Steps Done", level=1)
    steps_done = ["Checked source DB", "Checked App DB", "Checked ETL logs"]
    for i, step in enumerate(steps_done, 1):
        doc.add_paragraph(f"{i}. {step}")

    # Corrective & Preventive Actions
    doc.add_heading("Corrective Actions", level=1)
    doc.add_paragraph('No action needed' if status=='SUCCESS' else 'Investigate pipeline failure')
    doc.add_heading("Preventive Actions", level=1)
    doc.add_paragraph("- Add pipeline alerts")
    doc.add_paragraph("- Schedule batch verification")

    # Escalation Recommendation
    doc.add_heading("Escalation Recommendation", level=1)
    doc.add_paragraph("Next Owner: Monitor")
    doc.add_paragraph(f"Urgency: {'Low' if status=='SUCCESS' else 'High'}")
    doc.add_paragraph("Notes: Escalate if batch missing or failed again")

    # Confidence & Audit
    doc.add_heading("Confidence & Audit", level=1)
    doc.add_paragraph("Confidence Score: 95%")
    doc.add_paragraph("Generated By: Mock RCA Agent")
    doc.add_paragraph("Reviewed By: Pending")

    # Save to BytesIO for Streamlit download
    file_stream = BytesIO()
    doc.save(file_stream)
    file_stream.seek(0)

    # Display Download Button
    st.download_button(
        label="📥 Download RCA Report (.docx)",
        data=file_stream,
        file_name=f"RCA_{batch_id}.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
