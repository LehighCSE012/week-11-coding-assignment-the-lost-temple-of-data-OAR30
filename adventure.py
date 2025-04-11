'''
Week 11 Coding Assignment
'''
import pandas as pd
import re

def load_artifact_data(excel_filepath):
    '''
    Read artifact data from a specific Excel file,
    skipping the first 3 rows
    '''
    df = pd.read_excel(excel_filepath, sheet_name='Main Chamber', skiprows=3)
    return df

def load_location_notes(tsv_filepath):
    """
    Reads location data from a TSV file
    """
    df = pd.read_csv(tsv_filepath, sep='\t')
    return df

def extract_journal_dates(journal_text):
    """
    Exctracts all dates in MM/DD/YYYY format
    """
    pattern = r"\b(0[1-9]|1[0-2])/\d{2}\d{2}/\d{4}\b"
    return re.findall(pattern, journal_text)

def extract_secret_codes(journal_text):
    """
    Extracts all secret codes from journal text
    """
    pattern = r"\bAZMAR-\d{3}\b"
    return re.findall(pattern, journal_text)
