# utils.py

import os
from datetime import datetime

def read_log_file(file_path):
    """
    Read the entire log file and return its lines.

    :param file_path: str, path to the log file
    :return: list of str, lines of the log file
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return lines


def parse_timestamp(line):
    """
    Extract and parse the datetime object from a log line if it exists.

    :param line: str, a line from the log file
    :return: datetime or None, datetime object if found, otherwise None
    """
    # Typical format in the given logs: "2024-12-08 00:00:28.907"
    # We'll try to match the first occurrence of this pattern.
    # The example format: YYYY-MM-DD HH:MM:SS.mmm
    # We assume the line starts with a timestamp.
    try:
        # Split the line by space and take first two parts: "YYYY-MM-DD" and "HH:MM:SS.mmm"
        parts = line.split()
        if len(parts) > 1:
            date_part, time_part = parts[0], parts[1]
            dt_str = f"{date_part} {time_part}"
            dt_format = "%Y-%m-%d %H:%M:%S.%f"
            dt = datetime.strptime(dt_str, dt_format)
            return dt
    except Exception:
        pass
    return None
