import csv
import requests

def audit_csv():
    file_path = 'Task 2 - Intern.csv'
    headers = {'User-Agent': 'Outreachy-Auditor/1.0'}
    
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            
            # FIX 1: SKIPPING THE HEADER:
            next(reader, None)
            
            for row in reader:
                url = row[0]
                try:
                    res = requests.get(url, headers=headers, timeout=5)
                    print(f"({res.status_code}) {url}")
                
                # FIX 2: NAMING THE EXCEPTIONS:
                except requests.exceptions.RequestException as e:
                    error_name = type(e).__name__ # Gets 'Timeout', 'ConnectionError', etc.
                    print(f"(FAILED: {error_name}) {url}")

    except FileNotFoundError:
        print("Error: Task 2 - Intern.csv not found in directory.")

if __name__ == "__main__":
    audit_csv()
