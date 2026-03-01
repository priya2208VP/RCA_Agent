# Pharma Manufacturing RCA AI Agent

[![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.51.0-red?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Pandas-2.3.3-lightblue?style=for-the-badge&logo=pandas&logoColor=black)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-2.3.4-orange?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.10.7-yellow?style=for-the-badge&logo=matplotlib&logoColor=black)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-0.13.2-blueviolet?style=for-the-badge&logo=seaborn&logoColor=white)](https://seaborn.pydata.org/)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-black?style=for-the-badge&logo=github&logoColor=white)](https://github.com/priya2208VP/RCA_Agent)

---

### 🛠 Tech Used in This Project
[![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![SQL](https://img.shields.io/badge/SQL-MySQL-lightblue?style=for-the-badge&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![YAML](https://img.shields.io/badge/YAML-1.2-orange?style=for-the-badge&logo=yaml&logoColor=white)](https://yaml.org/)

[![Visitor Count](https://visitor-badge.laobi.icu/badge?page_id=priya2208VP)](https://github.com/priya2208VP)

---

**Pharma Manufacturing RCA AI Agent** is an advanced, user-friendly web application built with **Streamlit** that automates the **Root Cause Analysis (RCA)** of batch processes in pharmaceutical manufacturing. It allows engineers and operations teams to quickly visualize batch statuses, access logs, download detailed RCA reports, and improve operational efficiency.  

🔗 [Live Demo](https://rca-agent.streamlit.app/)

---

## Table of Contents
- [Project Overview](#project-overview)  
- [Key Features](#key-features)  
- [UI Components & Interactions](#ui-components--interactions)  
- [Use Cases](#use-cases)  
- [Technologies Used](#technologies-used)  
- [Installation & Setup](#installation--setup)  

---

## Project Overview
This tool automates the **RCA process** for batch production in pharma plants, helping teams detect failed batches, track pipeline issues, and implement preventive measures. The system generates **well-structured RCA reports in Word format** and displays detailed pipeline, source, and app database logs.

---

## Key Features
- ✅ **Batch Input & Filters**: Enter single, multiple, or range of batch numbers with status filters (Success/Failed).  
- ✅ **Dynamic Batch Analysis**: Separate views for successful and failed batches.  
- ✅ **Interactive Tabs**: View pipeline logs, source DB, app DB, and download RCA reports.  
- ✅ **Automated RCA Report Generation**: DOCX reports with incident summary, root cause, corrective/preventive actions, and confidence scores.  
- ✅ **Responsive UI**: Modern card-based design with collapsible sections for clean visualization.  
- ✅ **Detailed Pipeline Metrics**: Logs include `job_id`, `batch_id`, `status`, `start_time`, `end_time`, and `error`.  
- ✅ **Multiple Batch Support**: Supports batch ranges like `BATCH-001 to BATCH-005` or comma-separated batches.  

---

## UI Components & Interactions
- **Batch Input Field** – compact text input for entering batch IDs.  
- **Filters** – select “All,” “Success,” or “Failed” batches.  
- **Result Cards** – collapsible, color-coded cards:  
  - **Red**: Failed batches  
  - **Green**: Successful batches  
- **Tabs inside cards**:
  1. **Pipeline Logs** – shows ETL job logs.  
  2. **Source DB** – displays the batch data from source DB.  
  3. **App DB** – displays batch data from application DB.  
  4. **Download RCA** – download ready-to-use Word report.  

---

## Use Cases
1. **Operations Monitoring** – Track which batches failed and why.  
2. **Audit & Compliance** – Maintain structured RCA reports for regulatory compliance.  
3. **ETL Pipeline Verification** – Detect ETL or data pipeline issues quickly.  
4. **Decision Support** – Helps managers decide preventive actions based on confidence scores and logs.  
5. **Batch Trend Analysis** – Analyze batch failures over time for predictive maintenance.  

---

## Technologies Used
| Category | Technology |
|----------|------------|
| Programming Language | Python 3.12 |
| Web Framework | Streamlit 1.51.0 |
| Data Analysis | Pandas 2.3.3, NumPy 2.3.4 |
| Report Generation | python-docx 1.2.0 |
| Visualization | Matplotlib 3.10.7, Seaborn 0.13.2 |
| Version Control | Git & GitHub |
| Testing & Mock Data | Custom `mock_retriever` module |

---

## Installation & Setup

1. **Clone the repository**:
```bash
git clone https://github.com/priya2208VP/RCA_Agent.git
cd RCA_Agent
