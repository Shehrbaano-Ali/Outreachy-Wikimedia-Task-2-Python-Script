import csv
import requests

def audit_csv():
    file_path = 'Task 2 - Intern.csv'
    headers = {'User-Agent': 'Outreachy-Auditor/1.0'}
    
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            # using csv.reader(file)
            reader = csv.reader(file)
            for row in reader:
                url = row[0] # Takes the first column
                try:
                    res = requests.get(url, headers=headers, timeout=5)
                    print(f"({res.status_code}) {url}")
                except:
                    print(f"(FAILED) {url}")
    except FileNotFoundError:
        print("Error: Task 2 - Intern.csv not found in directory.")

if __name__ == "__main__":
    audit_csv()
