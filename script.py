import csv
import requests

def audit_csv():
    # Using the exact filename
    file_path = 'Task 2 - Intern.csv'
    
    # Adding contact info to User-Agent is a Wikimedia best practice
    headers = {
        'User-Agent': 'Outreachy-Auditor/1.0 (shehrbanoali2230@gmail.com)'
    }
    
    print(f"--- Starting Audit on {file_path} ---")
    
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            
            # FIX 1: SKIPPING THE HEADER
            # The None ensures it won't crash even if the file is empty
            next(reader, None) 
            
            for row in reader:
                # Skips empty rows to prevent index errors
                if not row:
                    continue
                    
                url = row[0].strip() # strip() removes accidental spaces
                
                try:
                    # Timeout is crucial for large-scale audits
                    res = requests.get(url, headers=headers, timeout=5)
                    print(f"[{res.status_code}] {url}")
                
                # FIX 2: PRINTING THE SPECIFIC EXCEPTION NAME
                except requests.exceptions.RequestException as e:
                    # Extracts name like 'ConnectionError' or 'ReadTimeout'
                    error_name = type(e).__name__ 
                    print(f"[FAILED: {error_name}] {url}")

    except FileNotFoundError:
        print(f"Error: {file_path} not found. Please check the file name.")
    
    print("--- Audit Complete ---")

if __name__ == "__main__":
    audit_csv()
