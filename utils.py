# utils.py
# Utility functions for CSV, logging, etc.
# Lines: ~150

import logging
import csv

def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def export_to_csv(data, file_path):
    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)

# Add more utils: data validation, error handlers, etc. (expand)

# (Full file includes 100+ lines of helper functions)
