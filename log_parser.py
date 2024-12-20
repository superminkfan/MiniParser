# log_parser.py

import re
from utils import parse_timestamp


def parse_log_lines(lines):
    """
    Parse the log lines to extract metrics at each recorded event.

    """

    cpu_pattern = re.compile(r"CPU \[CPUs=\d+, curLoad=([\d\.]+)%, avgLoad=([\d\.]+)%, GC=[\d\.]+%\]")
    heap_pattern = re.compile(r"Heap \[used=(\d+)MB, free=([\d\.]+)%, comm=\d+MB\]")
    default_region_pattern = re.compile(
        r"default region \[.*?usedRam=(\d+)MB, freeRam=([\d\.]+)%, allocRam=.*?\]"
    )

    results = []
    current_record = None
    collecting = False

    line_for_ts = None;

    for line in lines:
        # Check if the line starts a new metrics block
        if "Metrics for local node" in line:
            # If we were previously collecting a record and it has data, store it
            if collecting and current_record and current_record["curLoad"] is not None:
                results.append(current_record)

            # Parse timestamp from the current line
            ts = parse_timestamp(line_for_ts)
            # Start a new record
            current_record = {
                "timestamp": ts,
                "curLoad": None,
                "avgLoad": None,
                "heapUsed": None,
                "heapFree": None,
                "defaultUsedRam": None,
                "defaultFreeRam": None
            }
            collecting = True
            continue
        else:
            line_for_ts = line

        # If we are currently collecting data for a record:
        if collecting and current_record:
            # Match CPU line
            cpu_match = cpu_pattern.search(line)
            if cpu_match:
                current_record["curLoad"] = cpu_match.group(1)
                current_record["avgLoad"] = cpu_match.group(2)

            # Match Heap line
            heap_match = heap_pattern.search(line)
            if heap_match:
                current_record["heapUsed"] = heap_match.group(1)
                current_record["heapFree"] = heap_match.group(2)

            # Match default region line
            default_match = default_region_pattern.search(line)
            if default_match:
                current_record["defaultUsedRam"] = default_match.group(1)
                current_record["defaultFreeRam"] = default_match.group(2)

    # After the loop, if we were in the middle of collecting a record, append it
    if collecting and current_record and current_record["curLoad"] is not None:
        results.append(current_record)

    return results
