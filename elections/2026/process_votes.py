#!/usr/bin/env python3
"""
Process election votes by matching email addresses with contributor information.

Expected input files:
- CONTRIBUTOR_LIST_FILE: CSV with columns: Names (github), Email, Company, Name. 
  This file is exported from our active member spreadsheet.
  
- RAW_VOTES_FILE: Text file with candidate names header, then email,vote1,vote2,...vote12 per line. 
  This file comes from copy/pasting the individual ballots from the https://civs1.civs.us/ poll results.

Output: unified-vote-people.py with Python array format. This output can be copied and pasted
into the Jupyter Notebook that process the votes to derive the final results.
"""
import csv
import sys

# Input file paths, to be updated each year with the actual files.
CONTRIBUTOR_LIST_FILE = '/Users/alexe/Data/Studies/DLC/ONNX SC/election2026-2027/ONNX-contributor-list-2026-main-page.csv'
RAW_VOTES_FILE = '/Users/alexe/Data/Studies/DLC/ONNX SC/election2026-2027/raw-votes'
OUTPUT_FILE = '/Users/alexe/Data/Studies/DLC/ONNX SC/election2026-2027/unified-vote-people.py'

def process_votes():
    # Read the contributor list into a dictionary keyed by email.
    contributors = {}
    with open(CONTRIBUTOR_LIST_FILE, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            email = row['Email'].strip().lower()
            contributors[email] = row
    
    # Read the raw votes file.
    votes_data = []
    with open(RAW_VOTES_FILE, 'r') as f:
        lines = f.readlines()
    
    # First line is the header with candidate names.
    candidate_header = lines[0].strip()
    
    # Process each vote line (starting from line 2, index 1).
    for line in lines[1:]:
        parts = [p.strip() for p in line.split(',')]
        if len(parts) < 2:
            continue
        
        email = parts[0].lower()
        votes = parts[1:]
        
        # Match with contributor data.
        if email in contributors:
            contributor = contributors[email]
            votes_data.append({
                'email': parts[0],  # Keep original case
                'company': contributor['Company'],
                'name': contributor['Name'],
                'votes': votes
            })
        else:
            # Email not found in contributor list.
            votes_data.append({
                'email': parts[0],
                'company': 'NOT FOUND',
                'name': 'NOT FOUND',
                'votes': votes
            })
    
    # Write the unified Python array file.
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        # First array: with email
        f.write('votes_data = [\n')
        
        # Write header as first array element.
        header = ['Email', 'Company', 'Name'] + [f'Vote_{i+1}' for i in range(12)]
        header_str = '    [' + ','.join(f'"{col}"' for col in header) + '],\n'
        f.write(header_str)
        
        # Write data rows.
        for data in votes_data:
            # Build row with strings quoted and numbers unquoted.
            row_elements = [
                f'"{data["email"]}"',
                f'"{data["company"]}"',
                f'"{data["name"]}"'
            ] + data['votes']  # Votes are already strings from CSV parsing.
            
            row_str = '    [' + ','.join(row_elements) + '],\n'
            f.write(row_str)
        
        f.write(']\n\n')
        
        # Second array: without email.
        f.write('votes_data_no_email = [\n')
        
        # Write header without email.
        header_no_email = ['Company', 'Name'] + [f'Vote_{i+1}' for i in range(12)]
        header_str = '    [' + ','.join(f'"{col}"' for col in header_no_email) + '],\n'
        f.write(header_str)
        
        # Write data rows without email.
        for data in votes_data:
            row_elements = [
                f'"{data["company"]}"',
                f'"{data["name"]}"'
            ] + data['votes']
            
            row_str = '    [' + ','.join(row_elements) + '],\n'
            f.write(row_str)
        
        f.write(']\n')
    
    print(f"Processed {len(votes_data)} votes")
    print(f"Output written to: {OUTPUT_FILE}")
    
    # Report any unmatched emails.
    unmatched = [d for d in votes_data if d['name'] == 'NOT FOUND']
    if unmatched:
        print(f"\nWarning: {len(unmatched)} email(s) not found in contributor list:")
        for u in unmatched:
            print(f"  - {u['email']}")

if __name__ == '__main__':
    process_votes()
