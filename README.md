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

## Project Overview: Lusophone Railway Terminal
This project is an automated data integrity pipeline designed to audit a dataset of 171 URLs. It serves as a functional prototype for **[Proposal #8](https://meta.wikimedia.org/wiki/Lista_de_desejos_tecnol%C3%B3gicos_da_lusofonia/2025/Propostas/Ferramenta_de_pontua%C3%A7%C3%A3o_para_edi%C3%A7%C3%B5es_no_Wikidata)**: The Wikidata Quality Scorer.

###  Key Features
* **Station 1 (Compliance):** Batch verification of URL connectivity in the required `(STATUS) URL` format.
* **Station 2 (Innovation):** A metadata assessment engine that calculates a "Wikiscore" based on the completeness of Wikidata entities.
* **Technical Stack:** Python (Flask), JavaScript (Asynchronous Fetch), and the Wikidata API.



---

## 💻 Technical Setup
To run the terminal locally and access the link above:

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
