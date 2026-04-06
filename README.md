# Shehrbano Ali - Outreachy Task 2 Submission

**Contributor:** Shehrbano Ali  
**Email:** shehrbanoali2230@gmail.com  
**Github:** [Shehrbaano-Ali](https://github.com/Shehrbaano-Ali)  
**Program:** Outreachy May 2026 Cohort  
**Project:** Addressing the lusophone technological wishlist proposals  
**Date:** April 6, 2026  
**Task:** [Task 2 - Create a Python script to audit URL status codes](https://phabricator.wikimedia.org/T418284)

---

## 🔗 LINKS

### 🌐 [Click here to view the LIVE Production Prototype](https://shehrbanoali.pythonanywhere.com/)
*(Note: This Link is running in 'PythonAnywhere')*


---

## 📸 Visual Overview

### 1. Operational Logic & Documentation
Identifying the technical methodology and explaining HTTP status codes to the user via interactive briefings.

![Operational Briefing](01-briefing-modal.png)

### 2. Live Audit Terminal
Real-time output of the 171 URL dataset, displaying clear status verification for each URL.

![Audit Results](02-audit-results.png)

---

# Table of Contents
* [Introduction](#introduction)
* [Objectives](#objectives)
* [Implementation Details](#implementation-details)
* [Verification Logic & Error Handling](#verification-logic--error-handling)
* [Beyond the Task: Project Prototype](#beyond-the-task-project-prototype)
* [Key Findings](#key-findings)
* [Repository Structure](#repository-structure)
* [AI Usage](#ai-usage)

---

## Introduction
This repository contains my submission for **Task 2** of the Outreachy 2026 contribution period for Wikimedia. This task is part of **T418284: Addressing the lusophone technological wishlist proposals**.

The core requirement involved developing a Python script to parse a `.csv` dataset of Wikimedia-related URLs and retrieve their live HTTP status codes. To demonstrate the practical application of this logic, I extended the script into a web-based dashboard that automates the audit of these links, serving as a functional prototype for improving metadata reliability.

---
## Objectives
* **Parse CSV Data:** Implement Python logic to extract URLs from `Task 2 - Intern.csv`.
* **Automated Auditing:** Utilize the `requests` library to fetch real-time HTTP status codes.
* **Format Output:** Print results in the mentor-specified format: `(STATUS CODE) URL`.
* **Cloud Integration:** Deploy the operational script to PythonAnywhere for community access.
* **Document Findings:** Provide a technical breakdown of the audit process.

---
## Implementation Details
This project provides two ways to audit the Wikimedia dataset:
1.  **CLI Script (`script.py`):** A lightweight Python script that reads directly from `Task 2 - Intern.csv` and prints status codes to the terminal as requested.
2.  **Web Dashboard (`app.py`):** A Flask-based prototype that visualizes the audit process and calculates "Wikiscores" for Wikidata entities.

---
## Verification Logic & Error Handling
During development, I focused on ensuring the script remains stable even when encountering broken or restricted links.
* **The Challenge:** Many URLs in the dataset may point to dead servers or have restricted access, which can cause a standard script to crash.
* **The Solution:** I implemented a robust `try-except` block within the audit loop. This ensures that even if a URL fails to connect (due to DNS or SSL issues), the script catches the error and reports it as **FAILED** instead of stopping the entire execution.

---
```python
# Implementation of error-resistant auditing
try:
    res = requests.get(url, headers=HEADERS, timeout=5)
    return jsonify({'status': res.status_code})
except:
    return jsonify({'status': 'FAILED'})
```
---
## Beyond the Task: Project Prototype
While the primary task was a script-based check, I developed a web-based **Status Auditor** prototype to show the application of this logic to **Wishlist Proposal #8**:

* **Proposal #8 Relevance:** This demonstrates how a maintainer could use an automated auditor to ensure cross-project links between Wikidata and Commons remain active, preventing "dead-end" navigation for users.

---

## Key Findings
* **Resilience:** Handling network exceptions is as important as the core logic when dealing with large, diverse datasets of external URLs.
* **Server-Side Versatility:** Python provides a robust environment for network tasks that can eventually be integrated into larger Wikimedia tools like Pywikibot.

---
## Repository Structure
```text
Outreachy-Wikimedia-Task-2-Python-Script/
│
├── templates/
│   └── index.html        # UI for the Web Terminal prototype
├── 01-briefing-modal.png # Screenshot: Prototype UI
├── 02-audit-results.png  # Screenshot: Audit results
├── LICENSE               # MIT License
├── README.md             # Analytical documentation
├── Task 2 - Intern.csv   # The source dataset
├── app.py                # Flask-based Web Terminal logic
├── requirements.txt      # Dependencies (Flask, Requests)
└── script.py             # Official CSV parsing script (Task Requirement)
```

---
## AI Usage
I utilized ChatGPT for:

Documentation Structure: Organizing this README to reflect systematic open-source analysis.

Infrastructure Troubleshooting: Assisting in the migration from Render to PythonAnywhere during deployment.

All code and logic were manually verified and implemented by me. The AI served as a guide to accelerate understanding of cloud deployment configurations.

---
📝 Read my Blog post for this task  
This work is submitted for the Outreachy May 2026 internship application for the Wikimedia Project.

*~Shehrbano Ali*
